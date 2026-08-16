"""Regenerate BACKLOG.md - every topic, its status, estimate, and which roles it pays into.

    python vault/build_backlog.py

Sources, in priority order:
  vault/topics/*.md   the 59 topics: id, name, coverage, concepts
  stage_maps/*.md     est_h / actual_h / status where a map exists
  vault/concepts/*.md concept -> application -> role, for the "pays into" column

Estimates for topics with no stage map come from ESTIMATES below - deliberate guesses,
replaced by the real est_h the moment a stage map is written. Prereqs come from PREREQS,
transcribed from the DAG in vault/method/progression.md, which owns sequencing.

Stdlib only.
"""

import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "BACKLOG.md"

# Rough hours for topics with no stage map yet. Replaced by est_h once one exists.
# Scale: a refresher of held machinery ~2h, a new install ~5h, a wide new section ~8h.
ESTIMATES = {
    "I.1": 6.5, "I.2": 2, "I.3": 7, "I.4": 6, "I.5": 5, "I.6": 6, "I.7": 8.5, "I.8": 5,
    "II.1": 3, "II.2": 3, "II.3": 3, "II.4": 3, "II.5": 3,
    "III.1": 6, "III.2": 6, "III.3": 4, "III.4": 6, "III.5": 5,
    "IV.1": 6, "IV.2": 6, "IV.3": 8, "IV.4": 5, "IV.5": 5,
    "V.1": 5, "V.2": 5, "V.3": 6,
    "VI.1": 4, "VI.2": 8, "VI.3": 6, "VI.4": 5, "VI.5": 5, "VI.6": 5,
    "VII.1": 3.5, "VII.2": 5,
    "VIII.1": 5, "VIII.2": 6, "VIII.3": 5,
    "IX.1": 7, "IX.2": 6, "IX.3": 8, "IX.4": 5,
    "X.1": 5, "X.2": 7, "X.3": 6, "X.4": 5, "X.5": 3,
    "XI.1": 3, "XI.2": 3, "XI.3": 3, "XI.4": 4,
    "XII.1": 3, "XII.2": 3, "XII.3": 3, "XII.4": 3,
    "XIII.1": 5, "XIII.2": 6, "XIII.3": 6, "XIII.4": 5, "XIII.5": 5,
}

# Prerequisites, transcribed from the DAG. Topic id -> topic ids that must come first.
PREREQS = {
    "I.3": ["I.1"], "I.4": ["I.3"], "I.5": ["I.4", "VIII.1"], "I.6": ["I.5", "VII.1"],
    "I.7": ["I.6"], "I.8": ["I.7"],
    "II.1": ["I.1", "I.7"], "II.2": ["I.1", "I.7"], "II.3": ["I.1", "I.7"],
    "II.4": ["I.1", "I.7"], "II.5": ["I.1", "I.7"],
    "III.1": ["I.4", "I.7"], "III.2": ["III.1"], "III.3": ["III.2"],
    "III.4": ["III.1", "IX.1"], "III.5": ["III.1"],
    "IV.1": ["I.5", "I.8"], "IV.2": ["IV.1"], "IV.3": ["IV.2"], "IV.5": ["IV.3"],
    "IV.4": ["I.5"],
    "V.1": ["III.2"], "V.2": ["V.1"], "V.3": ["IV.3"],
    "VI.2": ["IV.3", "VI.1", "VIII.2"], "VI.3": ["VI.2", "IV.5"], "VI.5": ["VI.2"],
    "VIII.2": ["VIII.1"],
    "IX.1": ["I.7"], "IX.2": ["IX.1"], "IX.3": ["IX.2", "I.6"], "IX.4": ["IX.3"],
    "X.2": ["X.1"], "X.3": ["X.1"], "X.4": ["VI.5", "I.5"],
    "XI.4": ["I.7"],
    "XIII.3": ["IV.3"],
}

SECTIONS = {
    "I": "Probability and combinatorics", "II": "Classical puzzles",
    "III": "Markov chains", "IV": "Stochastic processes", "V": "Stochastic control",
    "VI": "Derivatives pricing", "VII": "Linear algebra", "VIII": "Calculus and ODEs",
    "IX": "Statistics and inference", "X": "Algorithms and computation",
    "XI": "Information theory", "XII": "Game theory", "XIII": "Measure theory",
}

ROMAN = list(SECTIONS)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(path):
    text = io.open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    out = {}
    for line in text.split("---", 2)[1].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "#")):
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        found = WIKILINK.findall(v)
        out[k.strip()] = found if found else v.strip('"')
    return out


def load(subdir):
    return {p.stem: frontmatter(p) for p in sorted((ROOT / subdir).glob("*.md"))
            if p.name != "HOME.md"}


def role_map(concepts, apps):
    """concept slug -> sorted role names it eventually pays into."""
    out = {}
    for cslug, c in concepts.items():
        roles = set()
        for a in c.get("applications", []):
            roles |= set(apps.get(a, {}).get("roles", []))
        out[cslug] = roles
    return out


def main():
    topics, stages = load("vault/topics"), load("stage_maps")
    concepts, apps, roles = load("vault/concepts"), load("vault/applications"), load("vault/roles")
    c2r = role_map(concepts, apps)
    short = {r: fm.get("name", r).split(" and ")[0] for r, fm in roles.items()}

    # topic id -> the stage map covering it, if any
    by_topic = {}
    for slug, fm in stages.items():
        t = fm.get("topic")
        key = t[0] if isinstance(t, list) else t
        if key:
            by_topic.setdefault(key, []).append((slug, fm))

    rows, done_h, todo_h = {}, 0.0, 0.0
    for tslug, fm in topics.items():
        tid = fm.get("id", "?")
        maps = by_topic.get(tslug, [])
        statuses = {m.get("status", "") for _, m in maps}
        if not maps:
            tick, state = "[ ]", "not started"
        elif statuses & {"closed"}:
            tick, state = "[x]", "closed"
        elif statuses & {"ready-for-test"}:
            tick, state = "[~]", "awaiting test"
        else:
            tick, state = "[ ]", "in progress"

        est = next((float(m["est_h"]) for _, m in maps if m.get("est_h")), None)
        est = est if est is not None else ESTIMATES.get(tid)
        actual = sum(float(m["actual_h"]) for _, m in maps if m.get("actual_h"))
        if tick == "[x]":
            done_h += actual or est or 0
        else:
            todo_h += est or 0

        paying = sorted({short[r] for c in fm.get("concepts", []) for r in c2r.get(c, ())})
        blocked = [p for p in PREREQS.get(tid, []) if p not in
                   {t.get("id") for s, t in topics.items()
                    if by_topic.get(s) and {m.get("status") for _, m in by_topic[s]} & {"closed"}}]

        link = f"[[{maps[0][0]}]]" if maps else f"[[{tslug}]]"
        rows.setdefault(fm.get("section", "?"), []).append(
            (tid, tick, fm.get("name", tslug), link, est, actual, state,
             " · ".join(paying) or "—", ", ".join(blocked) or "—"))

    lines = [
        "# Backlog — every topic, one line each",
        "",
        "> **Generated** by `vault/build_backlog.py` from `vault/topics/`, `stage_maps/`, and the",
        "> concept→application→role wiring. Run it after closing a stage or writing a stage map.",
        "> Hand edits between the markers are overwritten; change the source files instead.",
        "",
        "`[x]` closed · `[~]` studied, awaiting its unlock test · `[ ]` not started",
        "",
        "**Est** is the stage map's `est_h` where one exists, otherwise a rough guess that gets",
        "replaced the moment a map is written. **Blocked by** comes from the DAG in",
        "`vault/method/progression.md`, which owns sequencing — a topic with entries there is not ready",
        "to pick. **Pays into** is why the topic is on the list at all.",
        "",
        "<!-- BEGIN GENERATED:backlog -->",
        "",
        f"**{sum(1 for s in rows.values() for r in s if r[1] == '[x]')} closed · "
        f"{sum(1 for s in rows.values() for r in s if r[1] == '[~]')} awaiting test · "
        f"{sum(1 for s in rows.values() for r in s if r[1] == '[ ]')} not started · "
        f"~{todo_h:.0f}h remaining**",
        "",
    ]
    for sec in ROMAN:
        if sec not in rows:
            continue
        lines += [f"## {sec} — {SECTIONS[sec]}", "",
                  "| | Topic | Est | Actual | Status | Pays into | Blocked by |",
                  "|---|---|--:|--:|---|---|---|"]
        for tid, tick, name, link, est, actual, state, paying, blocked in rows[sec]:
            e = f"{est:g}h" if est else "—"
            a = f"{actual:g}h" if actual else "—"
            lines.append(f"| {tick} | {link} {name} | {e} | {a} | {state} | {paying} | {blocked} |")
        lines.append("")
    lines.append("<!-- END GENERATED:backlog -->")

    io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print(f"{sum(len(v) for v in rows.values())} topics · ~{todo_h:.0f}h remaining · wrote {OUT.name}")


def demo():
    """Self-check: parsing, role rollup, and that estimates cover every topic."""
    topics = load("vault/topics")
    missing = [fm.get("id") for fm in topics.values() if fm.get("id") not in ESTIMATES]
    assert not missing, f"no estimate for {missing}"
    c2r = role_map({"memorylessness": {"applications": ["time-to-fill"]}},
                   {"time-to-fill": {"roles": ["market-making"]}})
    assert c2r["memorylessness"] == {"market-making"}, c2r
    assert PREREQS["I.5"] == ["I.4", "VIII.1"], "continuous dists needs discrete + calculus"
    print("ok")


if __name__ == "__main__":
    demo() if "--demo" in sys.argv else main()
