# BAGQ — Be A Good Quant

A self-directed 25-week curriculum toward buy-side QR / HFT quant interviews.
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
| A new AI agent picking this up cold | **[AGENT_CONTEXT.md](AGENT_CONTEXT.md)** — full state in ~5 min |
| Me, on a given morning | **[progress/sprints/S16.md](progress/sprints/S16.md)** — active sprint: schedule + actuals |
| Curious what the whole plan is | [SYLLABUS.md](SYLLABUS.md) — one page, 13 sprints |
| Wondering *why* a stage matters | [CAPABILITY_MAP.md](CAPABILITY_MAP.md) — top-down: stages → the 6 things a quant does |

---

## Layout

```
├── 00_README.md              method overview
├── AGENT_CONTEXT.md          portable brain-dump: state, decisions, conventions
├── SYLLABUS.md               25 weeks on one page
├── 01_baseline_assessment.md the diagnostic
├── 02_feynman_protocol.md    the 4-step study method  ← the theory of change
├── 03_gated_progression.md   skill-tree DAG + 13-sprint traversal
├── 04_deliverables_spec.md   what "done" means
├── 05_commitment_contract.md time audit, cadence, circuit breakers
├── stage_maps/             per-stage problems, written at study level
├── vault/topics/              stage ↔ topics/ section mapping: what's in scope, what's deferred
├── CAPABILITY_MAP.md         top-down: which capabilities each stage builds (reference, not a plan)
├── topics/                   13-section topic inventory (911 problems, full scope)
└── progress/
    ├── sprints/              one file per sprint — plan, actuals, retro
    ├── baseline_scores.md    graded diagnostic + red flags
    ├── sprints/              per-sprint plan + retro
    ├── feynman_notes/        the core output — one per stage
    ├── weekly_reviews/       Sunday 30-min logs
    └── mocks/                interview transcripts (from S26)
```

**`stage_maps/` vs `topics/`** — `topics/` is an inherited inventory written for
someone who already has the material (Riccati equations, Carr-Madan FFT). It is kept
for scope, not used as the curriculum. `stage_maps/` holds the actual study-level
problems, written per stage as it comes up.

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
