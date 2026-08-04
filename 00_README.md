# Learning System — START HERE

> **If you (or a new AI agent) are picking this up cold, read `AGENT_CONTEXT.md` first**, then this file.

---

## What this folder is

A **self-contained, portable learning system** for one person's 5-month push toward buy-side QR / HFT quant interviews (target: 2027-01-15).

It has two layers:

- **Root files (`00`–`05`, `SYLLABUS`, `AGENT_CONTEXT`) + `progress/`** = the *method*: how to learn, what "done" means, sprint mechanics, progress log.
- **`topics/` + `stage_maps/`** = the *content*: `topics/section_*.md` is the 13-section inventory (911 problems, full scope, above current level); `stage_maps/` holds the study-level problems written per stage. [TOPIC_MAP.md](TOPIC_MAP.md) maps stages onto `topics/` sections and records what each stage deferred.

Portable design: every file uses relative paths only. Clone the repo → open `AGENT_CONTEXT.md` → any new agent has full context in ~5 minutes.

---

## The five governing files (read in this order)

| # | File | Purpose | When to touch |
|---|---|---|---|
| 01 | `01_baseline_assessment.md` | The diagnostic test | Once at start, then quarterly |
| 02 | `02_feynman_protocol.md` | The 4-step study method | Read once, apply every stage |
| 03 | `03_gated_progression.md` | Skill-tree DAG + 13-sprint traversal | Refer weekly |
| 04 | `04_deliverables_spec.md` | Definition of "done" per stage | Refer at each stage's unlock test |
| 05 | `05_commitment_contract.md` | Time audit, goals, sprint cadence, circuit breakers | Fill week 1, renegotiate monthly |

Plus the operational layer:

| File | Purpose |
|---|---|
| `AGENT_CONTEXT.md` | Portable brain-dump for a new agent (state, decisions, current sprint) |
| `SYLLABUS.md` | The end-to-end curriculum in one page |
| `progress/sprints/S<NN>.md` | Active sprint — schedule, actuals log, retro. The one you open every morning |
| `progress/baseline_scores.md` | Baseline test results (radar chart in `radar_*.png`) |
| `progress/sprints/S<NN>.md` | Per-sprint plan + retro |
| `progress/feynman_notes/*.md` | The core learning output (one per stage) |
| `progress/weekly_reviews/YYYY-WW.md` | Sunday 30-min review log |
| `progress/mocks/YYYY-MM-DD_*.md` | Mock interview transcripts (from Sprint 26) |

---

## The one-sentence loop

> **Pick the next unlocked node in the DAG → Learn it → Write the Feynman note → Solve the problems → Code the solvers → Pass the unlock test → Mark node complete → Loop.**

Everything else in this folder is scaffolding for that loop.

---

## Non-negotiables (the anti-drift rules)

1. **No stage is "complete" without a Feynman note that passes the 6-item checklist** (see `02_feynman_protocol.md`). Reading ≠ knowing.
2. **Every probability problem with a numerical answer gets a Monte Carlo verifier.** Simulation is the truth serum.
3. **Every solver has a docstring with time + space complexity.** Interviewers grade Big-O explicitly.
4. **Slack ≥ 20% of committed hours.** If you plan 15h/week, expect 12h. You will get sick / tired / interrupted.
5. **Weekly 30-min review, Sunday evening.** What unlocked? What stalled? Log it.
6. **Quarterly re-baseline.** Regression on any section = schedule a Feynman refresh; it's data, not failure.

---

## Directory map

```
learning_system/
├── 00_README.md                     ← YOU ARE HERE
├── AGENT_CONTEXT.md                 ← read this first if new agent
├── SYLLABUS.md                      ← one-page curriculum
├── 01_baseline_assessment.md
├── 02_feynman_protocol.md
├── 03_gated_progression.md
├── 04_deliverables_spec.md
├── 05_commitment_contract.md
└── progress/
    ├── sprints/S16.md               ← daily driver (active sprint)
    ├── baseline_scores.md
    ├── radar_chart.py
    ├── radar_2026-07-24_baseline.png
    ├── sprints/
    │   ├── S15.md
    │   ├── S16.md
    │   └── S<NN>.md ...
    ├── feynman_notes/               ← the core learning output
    │   └── <stage_id>_<slug>.md
    ├── problem_solutions/           ← per-stage worked problems
    ├── unlock_tests/                ← per-stage rubrics + attempts
    ├── weekly_reviews/              ← Sunday 30-min reviews
    ├── mocks/                       ← mock interview logs (Sprint 26+)
    └── contracts/                   ← monthly-signed contract snapshots

src/solvers/                         ← code twin (parent repo)
tests/solvers/                       ← unit tests for solvers
```

---

## For a new AI agent picking this up

Read `AGENT_CONTEXT.md` — it has current state, all decisions made, sprint status, target scores, and how to help without re-litigating design choices.

---

*Version: 1.0 | Created: 2026-07-24*

