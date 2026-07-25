# Agent Context — For a New AI Session or a New Machine

> **Purpose:** if you (a new AI agent, or the user on a fresh device) are opening this folder cold, read this file end-to-end. In ~5 minutes you will have all the context needed to help without re-litigating design decisions.

**Last updated:** 2026-07-25
**Current sprint:** 15 (2026-07-20 → 08-02) — Day 6 of 14

---

## 1. The user in one paragraph

Aeronautical-engineering background, ~10 years out from serious math. Currently in a working role (working language: Slang; transitioning to Python). Aiming for **buy-side QR / systematic PM (primary) + HFT / market-making (secondary)** interviews starting **2027-01-15**. Runs a parallel personal "quantamental" project (agent-driven vibe coding, capped at 6 h/week). Prefers agile — plans life in 2-week sprints.

Committed **~11 h/week of prime-time learning + ~3 h/week scrap** (from a 36.5-hour discretionary pool). Full time audit and circuit breakers in `05_commitment_contract.md`.

---

## 2. The plan in one paragraph

25 weeks = **13 two-week sprints (Sprint 15 → Sprint 27)**, aligned to the user's existing agile cadence. Sprint 15 = setup (baseline done). Sprint 16 onward = content. Traversal targets buy-side QR + HFT, so probability + stats + algos are pulled forward; exotic derivatives + measure theory are deferred. Full 13-sprint table in `03_gated_progression.md`. Two capstones (P1 Options Pricer, P16 HMM Regime Detection) plus 4 mock interviews in Sprints 26–27.

---

## 3. Baseline diagnostic (already completed 2026-07-23/24)

**Combined mean: 0.88 across 13 sections** (rubric 0–5). No section > 1.5; no auto-credit anywhere.

Per-section scores in `progress/baseline_scores.md`. Key findings:

- **Reasoning ≥ formalism** — user has genuine quant instinct (III.3, VI.3, II.4 landed) but lacks named machinery (tower property, MLE, BFS all scored 0)
- **Critical-path lows:** Section IX (stats, 1.00) and Section X (algos, 1.20) both essential for target roles
- **Red flags:** VIII.1 (dy/dx=y answered as sqrt formula — canonical ODE unknown) and X.4 (BFS unknown — HFT-screen blocker)
- **11 baseline-driven adjustments** applied to the plan (documented in `03_gated_progression.md` bottom section)

---

## 4. Design decisions (do NOT re-open unless user asks)

| Decision | Rationale | Where documented |
|---|---|---|
| 25-week runway to Q1-2027, not a full year | User's target date | `05_commitment_contract.md` §B |
| Buy-side QR + HFT dual target (not sell-side desk strat) | User's stated preference | `05_commitment_contract.md` §B |
| Quantamental capped at 6h/week, agent-driven scrap mode | Time-shape principle (deep vs. shallow) | `05_commitment_contract.md` §A.0, §A.1a |
| Entertainment tracked as 7h floor, flagged if >10h | Elastic-bucket monitoring | `05_commitment_contract.md` §D question 6 |
| S1.7 (tower property) pulled forward to Sprint 17 | Baseline showed it scored 0; blocks S3 + S9 | `03_gated_progression.md` adjustment #1 |
| Named Distributions added as Tier-0 mini-stage | Cheapest single-point improvement | Adjustment #2 |
| STS projects P2–P4, P6–P20 deferred | Built for sell-side desk-strat, not target roles | `03_gated_progression.md` deferrals list |
| Every solver requires docstring with time + space complexity | Baseline X.1: correct answer, wrong complexity | Adjustment #9 |
| No new textbooks needed (has Ross, Green Book, Hull, CLM) | Over-collecting = procrastination | Chat 2026-07-24 |
| `archive/` is an advanced backlog, NOT the curriculum | Written for someone who already has the material (Riccati/CIR bond pricing, Carr-Madan FFT, brachistochrone). Far above baseline 0.88. Left intact; per-stage problem sets written at study level in `problem_sets/` instead. | Chat 2026-07-25 |
| Per-stage problem sets written just-in-time, not upfront | Retiering all 13 archive sections now = speculative work for stages not touched until December | Chat 2026-07-25 |

---

## 5. Current status (2026-07-25, Day 6 of Sprint 15)

**Sprint 15 remaining tasks (deadline Sun Aug 2):**
- [x] Baseline diagnostic complete (both sittings graded)
- [x] All 6 learning-system files scaffolded
- [x] Radar chart script + PNG generated
- [x] Sprint 16 plan drafted
- [x] T0.A Python env verified
- [x] T0.B Git hygiene done
- [ ] **T0.C Calculus refresher** — Days 6–7. Problem set ready at `problem_sets/T0C_calculus.md`; note skeleton at `progress/feynman_notes/T0C_calculus_refresher.md`
- [ ] **T0.D Linear algebra refresher** — Days 8–9. Problem set not yet written (write at start of Day 8).
- [ ] **T1.X Named Distributions** — Days 11–14. Needs `src/solvers/` created (deferred until then by design).
- [ ] Sprint 15 retro Sun 08-02

**Sprint 16 (Aug 3–16) — revised scope:**
Starts with T1.X Named Distributions carryover + S1.1 Combinatorics (T0.C/T0.D now happen in Sprint 15 tail).

---

## 6. Working conventions

- **Stage IDs:** `S<section>.<sub>-<slug>` e.g., `S1.7-expectation-variance`. Tier-0 stages use `T0.<letter>`. Mini-stages use `T1.X` etc.
- **Feynman notes:** `progress/feynman_notes/<stage_id>_<slug>.md` — always follow the template in `02_feynman_protocol.md`.
- **Problem sets:** `problem_sets/<stage_id>_<slug>.md` — tiered A/B/C, problems numbered `<STAGE>-<TIER><N>` (e.g. `T0C-A1`), answer key hidden in a collapsed `<details>` block at the bottom. Written at the start of each stage, not upfront.
- **Solvers:** `src/solvers/<section>/<snake_case_name>.py` — every solver has (a) analytical function if closed-form exists, (b) Monte Carlo verifier, (c) docstring with time+space complexity. **Directory does not exist yet — created at T1.X (Day 11) when first needed.**
- **Tests:** `tests/solvers/<section>/test_<name>.py` — pytest style, asserts analytical ≈ MC within tolerance.
- **Dates:** ISO 8601 (YYYY-MM-DD).
- **Time-shape:** learning = prime (≥60 min blocks); quantamental = scrap (15-min slots).

---

## 7. How to help the user well (if you are a new agent)

- **Do NOT re-derive the plan.** It exists, it's tuned to baseline data. If the user asks to change something, edit in place.
- **Do NOT recommend new textbooks.** User has enough. Over-collection is a known procrastination trap flagged in prior sessions.
- **Do NOT write the teach-back for the user.** The user's chosen working mode is *"I study, you check"* — they read the source and write §1 from memory; the agent's job is Step 3 (hunt gaps ruthlessly) and grading against the 6-item checklist. Drafting the note for them destroys the theory of change.
- **Do NOT skip Feynman step 3 (gap-finding).** This is the entire theory of change of the system.
- **Do enforce the completion checklist** in `02_feynman_protocol.md` before marking any stage complete.
- **Do bias toward action.** User prefers agents that DO rather than ask. When in doubt, draft the *scaffolding* (problem sets, note skeletons, tooling) and let the user supply the thinking.
- **Do prepare materials fully before a study block.** User's stated need: "everything ready, so I have a concrete time of study, nothing interrupting." Sources listed with time-boxes, problems numbered, answer keys hidden behind `<details>`.
- **Do track velocity honestly.** If a sprint underruns, adjust the next sprint's scope in the retro — don't just push everything right.

---

## 8. What to open next (as a new agent)

1. `SYLLABUS.md` — one-page overview of everything ahead
2. `progress/tracker.md` — today's / this-week's action items
3. `progress/sprints/S15.md` (or current sprint) — active plan
4. `progress/baseline_scores.md` — user's starting point + red flags
5. `03_gated_progression.md` — the 13-sprint calendar
6. `problem_sets/` — per-stage problems at study level (`archive/` is the advanced backlog, not this)

That's enough to be useful. The rest is depth-when-needed.

---

*If this file goes stale, update the "Current status" section (§5) and the "Last updated" line at top. Everything else should be evergreen.*
