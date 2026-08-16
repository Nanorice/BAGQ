"""Regenerate CAPABILITY_MAP.md's mermaid diagram + status counts from frontmatter.

Reads stage_maps/*.md and vault/{concepts,applications,roles}/*.md, follows
stage -> concept -> application -> role, and rewrites the two generated blocks
in CAPABILITY_MAP.md in place. Everything outside those blocks is left alone.

Run at each sprint retro, or after writing a stage map:
    python vault/build_capability_map.py

Stdlib only, no YAML dependency - the frontmatter here is flat key: value with
JSON-ish lists, so a line parser is enough and correct for this repo's shape.
"""

import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAP = ROOT / "CAPABILITY_MAP.md"
BEGIN, END = "<!-- BEGIN GENERATED:{} -->", "<!-- END GENERATED:{} -->"

WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(path):
    """Flat key -> str|list from a --- delimited YAML header. Nested keys are ignored."""
    text = io.open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    body = text.split("---", 2)[1]
    out = {}
    for line in body.splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")) or ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        out[key.strip()] = WIKILINK.findall(value) if value.startswith("[") else value.strip('"')
    return out


def load(subdir):
    d = ROOT / subdir
    return {p.stem: frontmatter(p) for p in sorted(d.glob("*.md")) if p.name != "HOME.md"}


def node_id(prefix, slug):
    return prefix + re.sub(r"[^A-Za-z0-9]", "", slug.title())[:24]


def mermaid(stages, concepts, apps, roles):
    """stage -> concept -> application -> role, plus direct stage -> application edges."""
    lines = [
        "graph LR",
        "    classDef stage fill:#f5f5f5,stroke:#666,stroke-width:1px",
        "    classDef concept fill:#fffbe6,stroke:#b8860b,stroke-width:1.5px,stroke-dasharray:4 3",
        "    classDef app fill:#dae8fc,stroke:#6c8ebf,stroke-width:1.5px",
        "    classDef role fill:#e1d5e7,stroke:#9673a6,stroke-width:3px",
        "",
    ]
    mark = {"closed": " ✅", "ready-for-test": " ✅", "partial": " ~", "in-progress": " ~"}

    for slug, fm in stages.items():
        label = fm.get("name", slug) + mark.get(fm.get("status", ""), "")
        lines.append(f'    {node_id("S", slug)}["{label}"]:::stage')
    for slug, fm in concepts.items():
        lines.append(f'    {node_id("C", slug)}("{fm.get("name", slug)}"):::concept')
    for slug, fm in apps.items():
        lines.append(f'    {node_id("A", slug)}["{fm.get("name", slug)}"]:::app')
    for slug, fm in roles.items():
        lines.append(f'    {node_id("R", slug)}(["{fm.get("name", slug).upper()}"]):::role')

    edges = []
    for slug, fm in stages.items():
        src = node_id("S", slug)
        for c in fm.get("concepts", []):
            if c in concepts:
                edges.append(f"    {src} --> {node_id('C', c)}")
        # A stage naming a role with no concept in between still needs to reach it.
        for r in fm.get("roles", []):
            if r in roles and not any(c in concepts for c in fm.get("concepts", [])):
                edges.append(f"    {src} --> {node_id('R', r)}")
    for slug, fm in concepts.items():
        for a in fm.get("applications", []):
            if a in apps:
                edges.append(f"    {node_id('C', slug)} --> {node_id('A', a)}")
    for slug, fm in apps.items():
        for r in fm.get("roles", []):
            if r in roles:
                edges.append(f"    {node_id('A', slug)} --> {node_id('R', r)}")
        for a in fm.get("feeds", []):
            if a in apps:
                edges.append(f"    {node_id('A', slug)} --> {node_id('A', a)}")

    lines.append("")
    lines += sorted(set(edges))
    return "```mermaid\n" + "\n".join(lines) + "\n```"


def status_table(stages, roles):
    """Per role: stages closed / stages that reach it, via concepts or directly."""
    reach = {r: set() for r in roles}
    for slug, fm in stages.items():
        targets = set(fm.get("roles", []))
        for r in targets & set(roles):
            reach[r].add(slug)

    rows = ["| Role | Stages closed | Stages mapped | Applications |", "|---|---:|---:|---|"]
    for r, fm in sorted(roles.items(), key=lambda kv: kv[1].get("name", kv[0])):
        mapped = reach[r]
        closed = sum(1 for s in mapped if stages[s].get("status") in ("closed", "ready-for-test"))
        apps = [k for k, a in load("vault/applications").items() if r in a.get("roles", [])]
        rows.append(
            f'| **{fm.get("name", r)}** | {closed} | {len(mapped)} | '
            + " · ".join(f"[[{a}]]" for a in sorted(apps))
            + " |"
        )
    return "\n".join(rows)


def splice(text, name, payload):
    begin, end = BEGIN.format(name), END.format(name)
    if begin not in text or end not in text:
        sys.exit(f"CAPABILITY_MAP.md is missing the {name} markers - add {begin} / {end}")
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    return f"{head}{begin}\n{payload}\n{end}{tail}"


def main():
    stages = load("stage_maps")
    concepts, apps, roles = load("vault/concepts"), load("vault/applications"), load("vault/roles")

    dangling = set()
    for src in (stages, concepts, apps):
        for slug, fm in src.items():
            for key, target in (("concepts", concepts), ("applications", apps), ("roles", roles)):
                dangling |= {f"{slug} -> {x}" for x in fm.get(key, []) if x not in target}

    text = io.open(MAP, encoding="utf-8").read()
    text = splice(text, "diagram", mermaid(stages, concepts, apps, roles))
    text = splice(text, "status", status_table(stages, roles))
    io.open(MAP, "w", encoding="utf-8", newline="\n").write(text)

    print(f"{len(stages)} stages · {len(concepts)} concepts · {len(apps)} applications · {len(roles)} roles")
    for d in sorted(dangling):
        print(f"  dangling link: {d}")


def demo():
    """Self-check: the parser and edge-walk on a known shape."""
    fm = frontmatter(ROOT / "vault/applications/arrival-modelling.md")
    assert fm["type"] == "application", fm
    assert fm["concepts"] == ["poisson-exponential-duality"], fm
    assert fm["roles"] == ["market-making"], fm

    stages = {"f1_5": {"name": "X", "status": "closed", "concepts": ["memorylessness"], "roles": []}}
    out = mermaid(stages, {"memorylessness": {"name": "memorylessness", "applications": ["time-to-fill"]}},
                  {"time-to-fill": {"name": "Time to fill", "roles": ["market-making"]}},
                  {"market-making": {"name": "Market making"}})
    assert "SF15 --> CMemorylessness" in out, out
    assert "CMemorylessness --> ATimeToFill" in out, out
    assert "ATimeToFill --> RMarketMaking" in out, out
    assert '"X ✅"' in out, out
    print("ok")


if __name__ == "__main__":
    demo() if "--demo" in sys.argv else main()
