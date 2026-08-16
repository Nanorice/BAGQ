# BAGQ — Be A Good Quant

A self-directed 25-week curriculum toward a better quant.
Target: first interview **2027-01-15**. Baseline taken 2026-07-24 at **0.88 / 5**.

Not a course. A closed loop with a measurement at both ends: a graded diagnostic
defines the starting point, and every stage ships a Feynman note, worked problems,
and code before it counts as done.

---

## The loop

> Pick the next unlocked node in the DAG → Learn it → Write the Feynman note →
> Solve the problems → Code the solvers → Pass the unlock test → Mark complete → Loop.

Everything in this repo is scaffolding for that sentence.

---

## Start here

| If you are… | Read |
|---|---|
| **How do I actually run this?** | **[MANUAL.md](MANUAL.md)** — the operating procedure. Start here after a gap. |
| An agent picking this up cold | [.claude/CLAUDE.md](.claude/CLAUDE.md) — full state in ~5 min, auto-loaded in Claude Code |
| Me, on a given morning | [progress/sprints/S16.md](progress/sprints/S16.md) — active sprint: log + retro |
| Curious what the whole plan is | [vault/method/syllabus.md](vault/method/syllabus.md) — one page, 13 sprints |
| Wondering *why* a topic matters | [CAPABILITY_MAP.md](CAPABILITY_MAP.md) — top-down: topics → the 6 things a quant does |

---

## Layout

```
├── MANUAL.md              the operating procedure — day, stage, sprint
├── BACKLOG.md             every topic, ranked        (generated)
├── CAPABILITY_MAP.md      topics → what a quant does (generated)
├── inventory/             13-section problem inventory, 911 problems, full scope
├── stage_maps/            what to do, per topic — source, checklist, tiered problems
├── progress/
│   ├── sprints/           one file per sprint — log + retro
│   ├── feynman_notes/     the core output — what was understood, one per topic
│   └── baseline_scores.md graded diagnostic + red flags
└── vault/                 the Obsidian graph
    ├── HOME.md            Dataview dashboard
    ├── method/            how the system works — baseline, feynman, progression, done, contract
    ├── topics/            59 stubs indexing inventory/ 1:1
    ├── concepts/          the ideas topics carry
    ├── applications/      where a concept gets used
    └── roles/             the 6 quant roles the whole thing points at
```

**`stage_maps/` vs `inventory/`** — `inventory/` is inherited, written for someone who already
has the material (Riccati equations, Carr-Madan FFT). Kept for scope, never used as the
curriculum. `stage_maps/` holds the study-level problems, written per topic as it comes up.

---

## Non-negotiables

1. No stage is complete without a Feynman note passing the 6-item checklist. Reading ≠ knowing.
2. Every probability problem with a numerical answer gets a Monte Carlo verifier. Simulation is the truth serum.
3. Every solver carries a docstring with time + space complexity. Interviewers grade Big-O explicitly.
4. Slack ≥ 20% of committed hours. You will get sick, tired, interrupted.
5. Weekly 30-min review, Sunday. Quarterly re-baseline. Regression is data, not failure.

---

## Status

- **Sprint 15** (2026-07-20 → 08-02) — T0 refreshers; knowingly over-committed, tracking actuals
- **Baseline:** 0.88 combined. Diagnosis: *reasoning ≥ formalism* — the instinct is
  there, the named machinery isn't. A vocabulary problem, not an ability problem.
