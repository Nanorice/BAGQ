# Sprint 16-C — Citadel prep (interrupt)

**Dates:** 2026-08-19 → 2026-08-30
**Supersedes:** the remainder of [[S16]]. Curriculum is **paused**, not cancelled.

> **Why an interrupt and not a fork.** A live process at the target shop outranks a January-optimal
> sequence. Most of what this sprint covers — MLE, hypothesis testing, GARCH, section X algorithms
> — is *on the DAG already*. This is pull-forward, not detour.

---

## What is paused

| Was | State | Resumes |
|---|---|---|
| `F1.1` Combinatorics (a/b/c) | maps written, note not closed | after the process resolves |
| Four D4 unlock tests (`R.calculus`, `R.linalg`, `F1.4`, `F1.5`) | never run | **see below** |
| `F1.2` Bayes, `F1.7` expectation | backlog | S17+ |

> **The D4 backlog does not pause.** It is 4 tests × 25–40 min and it is the only evidence in the
> system that the notes produce retention. Run them in scrap slots across this sprint — a stats
> interview will ask distribution questions and `F1.5` is exactly that material. **They are now
> prep, not curriculum.**

---

## Three routes, in parallel

| Route | File | Mode | Target |
|---|---|---|---|
| 1. Books | [[route_1_books]] | scrap + overflow | background, ~100 pp starred |
| 2. Fundamentals | [[route_2_fundamentals]] | **prime, protected** | the technical rounds |
| 3. Coding | [[route_3_coding]] | scrap (HR) + prime (CoderPad) | the two gates |

**Priority when they conflict: 3 > 2 > 1.** Route 3's gates come first in the process and a gate
failure ends everything behind it. Route 1 is the one that yields.

**Route 2 is the only one needing a protected 60+ min block.** Routes 1 and 3A survive on 30-min
scraps; 3B needs privacy to talk out loud, not length.

---

## This sprint's targets

**Route 3 (highest priority — the gates come first)**
- [ ] Tier 0 — all six. **Closes baseline X.1, X.3, X.4** *(BFS is flagged in `CLAUDE.md` as a
      screen blocker)*
- [ ] Tier 1 — at least six of ten
- [ ] **Two narrated CoderPad sessions**, one recorded and watched back
- [ ] Three problems typed in a plain editor, no autocomplete

**Route 2 (the main line)**
- [ ] **Unit F — the story.** Written, 2h, before anything else. Needed for the HR call
- [ ] **Unit A-iii — marginal/component/incremental VaR.** Two passes, separate days
- [ ] Unit A-i/ii — three estimators + `wᵀΣw` non-linearity
- [ ] Unit C-iii — Kupiec + Christoffersen *(with C-ii's likelihood-ratio item first)*

**Route 1 (background)**
- [ ] P1 — Paleologo Ch.3, pp. 22–41. Read §3.5 against your own VaR surface
- [ ] I1 — Isichenko Ch.4, pp. 190–207. §4.7 crowding twice
- [ ] Three-line artifact per starred section in `route_1_notes.md`

**Code (`code/codify.ipynb` — `# Citadel`)**
- [ ] Parametric / historical / MC VaR on one series, asserted against each other
- [ ] Component VaR summing to total VaR — the verifier *is* Euler's theorem
- [ ] **The VaR surface, rebuilt in Python** ⭐ the single best artifact in this prep
- [ ] Kupiec test, verified by simulating a deliberately bad VaR model

---

## Log

| Date | Hrs | Route | What I did / what blocked |
| --------- | ----------- | --- | --- |
| Tue 08-19 | [hours:: 0] | | prep scoped, three route files written |
| Wed 08-20 | [hours:: 0] | | |
| Thu 08-21 | [hours:: 0] | | |
| Fri 08-22 | [hours:: 0] | | |
| Sat 08-23 | [hours:: 0] | | |
| Sun 08-24 | [hours:: 0] | | |
| Mon 08-25 | [hours:: 0] | | |
| Tue 08-26 | [hours:: 0] | | |
| Wed 08-27 | [hours:: 0] | | |
| Thu 08-28 | [hours:: 0] | | |
| Fri 08-29 | [hours:: 0] | | |
| Sat 08-30 | [hours:: 0] | | |

```dataview
TABLE WITHOUT ID
  sum(rows.h) AS "Hours logged",
  length(filter(rows.h, (x) => x > 0)) AS "Contact days"
FROM "progress/sprints" WHERE file.name = "S16_CITADEL"
FLATTEN number(hours) AS h
WHERE h != null
GROUP BY true
```

---

## Invariants

- **Sizing constants still apply.** New material ×2.0, refresher ×1.2. Unit A is new material:
  the 12–15h estimate is already doubled — do not re-double it, and do not believe it if you
  find yourself planning 6h
- **Two passes on separate days** for A-iii and C-iii. Both are machinery you have never held
- **Working mode unchanged:** you study, I check. I do not write the teach-backs
- **Drift move:** input exhausted with no next action → switch to Route 3 Tier 0 on the keyboard.
  There is always a LeetCode problem available, and it is never wasted
- **Complexity stated before writing**, every code problem. Baseline X.1 is a speech habit gap

---

## Open, awaiting information

- [ ] **Hiring manager background** — ex-GS Market Risk strats. Once details arrive, re-weight
      Unit A. Strats background means VaR internals, not brainteasers
- [ ] **Timeline** — no dates yet. If HackerRank lands inside 10 days, Route 3 Tier 0+1 becomes
      the *only* thing that matters and Routes 1–2 stop
- [ ] Recruiter's read on the team's actual mandate — central risk book vs risk reporting vs
      portfolio construction proper. Changes the Unit E weighting

---

## Retro — 08-30

*(knowledge, not process — what can you now rebuild that you could not on 08-19?)*
