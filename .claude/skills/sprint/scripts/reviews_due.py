"""Which topics are due for review in a given sprint, per the spaced-retrieval ladder.

    python .claude/skills/sprint/scripts/reviews_due.py S18 2026-09-14

Ladder: R1 +1 week, R2 +1 month, R3 +3 months, then interview prep. A failed review
(<80%) resets the topic to R1 - record that by setting `review: R1` and a fresh
`reviewed:` date in the stage map, and the next sprint picks it up again.

Reads stage_maps/*.md frontmatter:
    sprint:    which sprint the topic was studied in
    status:    closed | ready-for-test | in-progress | unlocked
    reviewed:  ISO date of the last review that PASSED (absent = never reviewed)
    review:    the rung last completed - R1 | R2 | R3 (absent = none)

Stdlib only.
"""

import datetime as dt
import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
GAPS = {None: 7, "R1": 30, "R2": 90, "R3": None}  # days until the next rung
NEXT = {None: "R1", "R1": "R2", "R2": "R3", "R3": "interview prep"}


def frontmatter(path):
    text = io.open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    out = {}
    for line in text.split("---", 2)[1].splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"')
    return out


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sprint, end = sys.argv[1], dt.date.fromisoformat(sys.argv[2])

    overdue, due, waiting = [], [], []
    for p in sorted((ROOT / "stage_maps").glob("*.md")):
        fm = frontmatter(p)
        if fm.get("status") not in ("closed", "ready-for-test"):
            continue
        if fm.get("sprint") == sprint:
            continue  # studied this sprint; its R1 lands next sprint

        rung = fm.get("review") or None
        name = fm.get("name", p.stem)
        gap = GAPS.get(rung)
        if gap is None:
            continue  # past R3 - carried by interview prep, not a sprint review

        last = fm.get("reviewed")
        if not last:
            # Never reviewed. ready-for-test means the R1 was scheduled and missed.
            overdue.append((name, p.stem, NEXT[rung], "never tested"))
            continue

        when = dt.date.fromisoformat(last) + dt.timedelta(days=gap)
        row = (name, p.stem, NEXT[rung], when.isoformat())
        (due if when <= end else waiting).append(row)

    def show(title, rows):
        print(f"\n{title} ({len(rows)})")
        for name, slug, rung, note in rows:
            print(f"  {rung:<4} {name:<34} {note}   [{slug}]")

    show("OVERDUE - no retrieval evidence", overdue)
    show(f"DUE by {end}", due)
    show("Not yet due", waiting)
    print(f"\nWrite unlock tests for OVERDUE + DUE. R1 = 5Q/45min; R2 and R3 = 3Q/15min.")


def demo():
    """Self-check the ladder arithmetic on synthetic frontmatter."""
    assert GAPS[None] == 7 and NEXT[None] == "R1"
    assert GAPS["R1"] == 30 and NEXT["R1"] == "R2"
    assert GAPS["R2"] == 90 and NEXT["R2"] == "R3"
    assert GAPS["R3"] is None, "R3 has no further rung; interview prep carries it"
    d = dt.date.fromisoformat("2026-08-09") + dt.timedelta(days=GAPS["R1"])
    assert d.isoformat() == "2026-09-08", d
    assert frontmatter(ROOT / "stage_maps/R_calculus.md").get("type") == "stage"
    print("ok")


if __name__ == "__main__":
    demo() if "--demo" in sys.argv else main()
