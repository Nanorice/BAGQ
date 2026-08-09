# BAGQ — Agent Context

> Auto-loaded each session. If you are picking this repo up cold, this file is enough.
> A human on a fresh machine (or a non-Claude agent) should be handed `../AGENT_CONTEXT.md`,
> which points here.

**Last updated:** 2026-07-30 (Sprint 15, Day 11)

---

## 1. The user in one paragraph

Aeronautical-engineering background, ~10 years out from serious math. Currently in a working
role (working language: Slang; transitioning to Python). Aiming for **buy-side QR / systematic
PM (primary) + HFT / market-making (secondary)** interviews starting **2027-01-15**. Runs a
parallel personal "quantamental" project (agent-driven vibe coding, capped at 6 h/week).
Prefers agile — plans life in 2-week sprints.

Committed **~11 h/week prime + ~3 h/week scrap** (from a 36.5-hour discretionary pool). Full
time audit and circuit breakers in `05_commitment_contract.md`.

---

## 2. The plan in one paragraph

25 weeks = **13 two-week sprints (S15 → S27)**. S15 = setup + baseline + T0 refreshers.
S16 onward = content. Target is buy-side QR + HFT, so probability + stats + algos are pulled
forward; exotic derivatives + measure theory deferred. Full calendar in
`03_gated_progression.md`. Two capstones (P1 Options Pricer, P16 HMM Regime Detection) plus
4 mock interviews in S26–27.

---

## 3. Baseline diagnostic (completed 2026-07-23/24)

**Combined mean: 0.88 across 13 sections** (rubric 0–5). No section > 1.5.

Per-question detail in `progress/baseline_scores.md`. Key findings:

- **Reasoning ≥ formalism** — genuine quant instinct (III.3, VI.3, II.4 landed) but missing
  named machinery (tower property, MLE, BFS all scored 0). This is a vocabulary problem, not
  an ability problem.
- **Critical-path lows:** IX stats (1.00) and X algos (1.20) — both essential for target roles.
- **Red flags:** VIII.1 (`dy/dx = y` answered as a sqrt formula) — **closed by R.calculus** ·
  X.4 (BFS unknown, HFT-screen blocker) — open, S10.3 in S19 ·
  VII.1/VII.2 (eigenvalues, PSD) — **closed by R.linalg** · I.3 (E/Var of Exp) — open, `F1.5`.
- 11 baseline-driven adjustments applied, documented at the bottom of `03_gated_progression.md`.

---

## 4. Design decisions (do NOT re-open unless the user asks)

| Decision | Rationale | Documented |
|---|---|---|
| 25-week runway to Q1-2027 | User's target date | `05_commitment_contract.md` §B |
| Buy-side QR + HFT dual target | User's stated preference | `05_commitment_contract.md` §B |
| Quantamental capped 6h/week, scrap mode | Time-shape principle | `05_commitment_contract.md` §A.0 |
| S1.7 tower property pulled to S17 | Scored 0; blocks S3 + S9 | Adjustment #1 |
| Every solver needs a complexity docstring | Baseline X.1: right answer, wrong Big-O | Adjustment #9 |
| No new textbooks | Has Ross, Green Book, Hull, CLM. Over-collecting = procrastination | Chat 07-24 |
| `topics/` is the scope inventory, NOT the curriculum | 911 problems written far above baseline. Per-stage sets live in `stage_maps/` | Chat 07-25 |
| Problem sets written just-in-time | Retiering all 13 sections now = speculative work for December stages | Chat 07-25 |
| **One source per stage, named chapter + page range** | 7 sources across 3 media cost R.calculus more time choosing than studying. Video only as a single named fallback, never in the main path | Chat 07-29 |
| **Plain-English stage names lead, IDs subscript** | Write the name first, ID as subscript. See §6 + `03_gated_progression.md` for the `R`/`F`/`D` scheme adopted 08-04 | Chat 07-29, revised 08-04 |
| `T1.X` split into Discrete `F1.4` + Continuous `F1.5` | 9 distributions ≈ 8h — Tier-1 sized wearing a Tier-0 label. Log-normal → S6, χ² → S9.2 | Chat 07-29 |
| **Size stages by type: refresher ×1.2, new material ×2.0** | Measured over S15's three stages. The one-source 40-min cap fixed *fragmentation*, not *depth* — it was calibrated on a refresher | S15 retro §2 |
| **New material gets two input passes on separate days** | One pass doesn't install machinery never held. `F1.4`'s second pass happened anyway — unplanned, unbudgeted, spread over 3 days | Adj #12 |
| **Every stage set names the "hard → drifting" move** | Log the `⚠️ GAP`, switch to Tier A on paper. Drift = input exhausted with no next action; the fix is structural, not motivational | Adj #13 |

---

## 5. Current status — Sprint 16, Day 1 (2026-08-03)

**S15 closed at 14.5h / 18h = 81%.** Retro held 08-03 (one day late), full detail in
`progress/sprints/S15.md`.

**Closed:** baseline · 6 system files · radar chart · T0.A env · T0.B git ·
**Calculus `R.calculus`** (5.0h, 07-29) · **Linear Algebra `R.linalg`** (3.5h, 07-30 — closes VII.1 + VII.2) ·
**Discrete Distributions `F1.4`** (6.0h, 08-02, **PARTIAL** — table lives in the handnote, solver
deferred; the 08-08 +1wk review is the real pass/fail and carries the II.1 unlock test).

**The S15 finding — use this to size, not the 81%:**
**refresher stage ≈ 1.2× budget · new material ≈ 2.0× budget.** The 40-min one-source input cap
was calibrated on a *refresher* (R.linalg, landed on budget). Applied to *new* material (`F1.4`) it
overran 2×, because one pass does not install machinery never held. Two consequences, both now
structural: new-material stages get **two input passes on separate days** (Adj #12), and the
"hard → drifting" state gets a **named move** — log the `⚠️ GAP`, switch to Tier A on paper
(Adj #13). Drift was a symptom of exhausted input with no next action, not of low effort.

**Sprint 16 (08-03 → 08-16), ~21h, two new-material stages — not three:**
- **Week 1:** S15 retro (Mon) · **`F1.5` Continuous Distributions** Pass 1 Wed / Pass 2 Thu /
  close Sat — carryover, still holds baseline I.3 open, **not cuttable** (it was the designated
  cut in S15 and got cut) · `src/solvers/` created Sat with one shared verifier covering `F1.4` +
  `F1.5` · `F1.4` +1wk review Sat
- **Week 2:** **`F1.1` Combinatorics** split into three day-stages (a counting rules /
  b stars-and-bars / c inclusion–exclusion + derangements). Sets written Sun 08-09, just-in-time.
- **Dropped to S17:** `S1.2` Bayes (Adj #14) — three new stages at a 2× multiplier was fiction.

---

## 6. Working conventions

- **Stage IDs — `<TYPE><section>.<sub><split>`** (adopted 08-04, full spec in `03_gated_progression.md`).
  `R` refresher (×1.2) · `F` foundation (×2.0) · `D` deepen. **Type first because it is the cost
  driver.** Section number indexes `topics/` 1:1 (1 = `section_I`, 7 = `section_VII`, …); the sub
  number is the `##` heading *inside* that file — **check it before assigning, the old scheme
  drifted because nobody did.** Split letters (`F1.4`/`F1.5`) = one subsection over two days.
  Refreshers are `R.<name>` (they cut across sections). **Plain name first, ID as subscript.**
- **Two files per stage, and only two:**
  - `stage_maps/<id>_<slug>.md` — **what to do.** Knowledge checklist · source · schedule ·
    problems A/B/C · code problems · deliverables · answer key. Written before the block.
  - `progress/feynman_notes/<id>_<slug>.md` — **what you understood.** Teach-back, gaps, napkin,
    summary table, where-it-breaks. The user writes this; never draft it.
- **Stage-map shape that works** (R.linalg landed on budget with it): one source + 40-min hard stop ·
  5 Tier A, 5 Tier B, 2 Tier C · a named **collapse subset** ("if the day collapses: A1, A5, B1") ·
  the named **drift move** · new material gets **two passes on separate days**.
- **Note §4 is "Where I'd actually meet this"**, not "Analogy" (changed 08-04 — a supplied
  analogy is just another sentence to memorise; "where does this show up" is a real interview
  question, and the user's own PCA/portfolio answers were better than any analogy).
- **D4 unlock test runs at the +1 week review**, not at stage close. Between the two the stage is
  `READY_FOR_TEST` — a real state. Sprint retro reviews *process*; D4 tests *knowledge*.
- **No `tracker.md`** (deleted 08-04). Schedule + actuals + invariants live in
  `progress/sprints/S<NN>.md`, one file per sprint.
- **Solvers:** `src/solvers/<section>/<snake_case>.py` — (a) analytical fn if closed-form exists,
  (b) Monte Carlo verifier, (c) docstring with time + space complexity.
- **Tests:** `tests/solvers/<section>/test_<name>.py`, pytest, analytical ≈ MC within tolerance.
- **Dates:** ISO 8601. **Time-shape:** learning = prime (≥60 min); quantamental = scrap (15 min).

---

## 7. How to help well

- **Do NOT re-derive the plan.** It exists and is tuned to baseline data. Edit in place.
- **Do NOT recommend new textbooks.** Known procrastination trap.
- **Do NOT write the teach-back.** Working mode is **"I study, you check"** — the user reads the
  source and writes §1 from memory; your job is Feynman Step 3 (hunt gaps ruthlessly) and
  grading against the 6-item checklist. Drafting the note destroys the theory of change.
- **When the user says a check is unnecessary, take it.** On 07-30 they declined a numerical
  anchor as redundant and were right — the work was already in the note. That is a judgment
  call about their own recall, not a corner cut. Don't re-litigate it.
- **Review means: find the actual error, then the unfilled checklist items.** Sign slips and
  notation collisions in a *summary* section matter most — the napkin is what gets recalled cold.
- **Do bias toward action.** Draft the scaffolding (problem sets, note skeletons, tooling); let
  the user supply the thinking.
- **Do prepare materials fully before a study block.** Stated need: "everything ready, so I have
  a concrete time of study, nothing interrupting."
- **Do track velocity honestly**, and read it for *cause*, not just magnitude. Days 1–7 ran
  0.7h/day; Day 11 ran 3.5h and hit its allocation. The variable that changed was stage design
  (one source, three blocks), not effort. Size S16 off the new shape, not the old average.

---

## 8. What to open next

0. `MANUAL.md` — **the operating procedure**: how a day/stage/sprint runs, and the rules that were
   paid for. Read this first if picking the repo up cold.
1. `progress/sprints/S<NN>.md` — active sprint: schedule, actuals, retro (there is no tracker.md)
2. `SYLLABUS.md` — one-page overview of everything ahead
3. `progress/sprints/S15.md` — active sprint plan
4. `progress/baseline_scores.md` — starting point + red flags
5. `03_gated_progression.md` — the 13-sprint calendar
6. `vault/topics/` — stage ↔ `topics/` mapping: what each stage closed, what it deferred, why
7. `CAPABILITY_MAP.md` — top-down: stages → competencies → the 6 capabilities a quant is hired
   for. **Reference only, never a planning input** — the DAG owns sequencing. Update status
   counts at each retro; the structure should stay near-static.
7. `stage_maps/` — per-stage problems at study level

---

*Keep §5 current — it is the only section that goes stale. Everything else is evergreen.*
