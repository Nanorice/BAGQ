# BAGQ — Agent Context

> Auto-loaded each session. If you are picking this repo up cold, this file is enough.
> A human on a fresh machine (or a non-Claude agent) should be handed `AGENT_CONTEXT.md`
> (repo root), which points here. For the operating procedure, `MANUAL.md`.

**Last updated:** 2026-08-09 (Sprint 16, Week 1 end)

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

## 5. Current status — Sprint 16, Week 1 end (2026-08-09)

> Live numbers are in `progress/sprints/S16.md` (Dataview). This section is the narrative.

**Four stages exist. All four are `ready-for-test`. ZERO have been tested.**

| Stage | Closed | Hours | State |
|---|---|---:|---|
| Calculus `R.calculus` | 07-29 | 5.0 | `ready-for-test` |
| Linear Algebra `R.linalg` | 07-30 | 3.5 | `ready-for-test` — closes VII.1 + VII.2 |
| Discrete Distributions `F1.4` | 08-02 | 6.0 | `ready-for-test`, **PARTIAL** — table in handnote |
| Continuous Distributions `F1.5` | — | — | in flight, Sprint 16 |

**This is the open risk in the whole system.** The write side works (the `R.linalg` note struck a
stalled derivation and rebuilt it correctly). The **retrieval** side has never run.
**Sat 08-15 carries all four D4 tests** — first real evidence on whether the notes produce
retention or just produce notes. `vault/HOME.md` surfaces this permanently.

**S15 closed at 14.5h / 18h = 81%.** Sizing constants, measured — use these, not the 81%:
**refresher ≈ 1.2× budget · new material ≈ 2.0×.** The 40-min one-source cap was calibrated on a
*refresher*; applied to *new* material (`F1.4`, 3h budgeted → 6h) it overran 2×, because one pass
does not install machinery never held. Hence Adj #12 (two passes, separate days) and Adj #13
(named drift move). Drift was exhausted input with no next action, not low effort — contact was
10/11 days.

**Sprint 16 (08-03 → 08-16), ~21h.** Week 1: `F1.5` Pass 1 Wed / Pass 2 Thu / close Sat, plus
`src/solvers/` with one shared verifier covering `F1.4` + `F1.5`. Week 2: `F1.1` Combinatorics as
three day-stages, maps written 08-09 just-in-time. `S1.2` Bayes dropped to S17 (Adj #14).

**Schedule reality:** Week 1 ran ~6h against 11h planned, and `F1.5` had not started as of 08-09.
Read the actuals table before assuming any row happened.

---

## 6. Working conventions

- **Stage IDs — `<TYPE><section>.<sub><split>`** (adopted 08-04, full spec in `03_gated_progression.md`).
  `R` refresher (×1.2) · `F` foundation (×2.0) · `D` deepen. **Type first because it is the cost
  driver.** Section number indexes `topics/` 1:1 (1 = `section_I`, 7 = `section_VII`, …); the sub
  number is the `##` heading *inside* that file. **Open the file and read the heading before
  assigning — this has been got wrong twice** (`S1.3`→`F1.4`, then `F1.4a`/`F1.4b`→`F1.4`/`F1.5`,
  because §4 is Discrete RVs and §5 is Continuous — different subsections).
  Split letters (`a`/`b`/`c`) **only** when one genuine subsection spans multiple days
  (`F1.1a/b/c`). Refreshers are `R.<name>`. **Plain name first, ID as subscript.**
- **Two files per stage, and only two:**
  - `stage_maps/<id>_<slug>.md` — **what to do.** Frontmatter · knowledge checklist · source ·
    schedule · problems A/B/C · code problems · deliverables · answer key. Written before the block.
  - `progress/feynman_notes/<id>_<slug>.md` — **what you understood.** Teach-back, gaps, napkin,
    summary table, where-it-breaks. The user writes this; never draft it.
- **Obsidian vault (added 08-09).** Repo root is a vault; `topics/`, `src/`, `tests/`,
  `pine_scripts/`, `.claude/` are excluded via `.obsidianignore`. Chain:
  `stage → topic → concept → application → role`, all in `vault/`. **91 stubs exist already —
  do not create more without asking.** `vault/HOME.md` is the Dataview dashboard.
  `TOPIC_MAP.md` and `tracker.md` are both **deleted**; their content lives in topic-note
  frontmatter and the sprint files respectively.
- **Knowledge checklists are built from the source's real `##` headings**, with section numbers
  attached — never from what interviews tend to ask. Anything interview-critical but outside the
  chapter is **stretch**, and every stretch item resolves one of three ways: written inline,
  a named chapter in a book already owned, or deferred **with the reason**. Full rule in
  `04_deliverables_spec.md` §D2.
- **Dataview inline fields are parsed anywhere in a file** — blockquotes and prose included.
  Never write a live `[field:: value]` in guidance text; put examples in fenced code blocks.
  Never put `|` in a table cell (aliased wikilinks, `|x|`) — it splits the row.
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
  **`src/` does not exist yet** — it gets created by `F1.5`'s close block, one shared verifier
  covering `F1.4` + `F1.5`. Do not scaffold it early.
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
### Reviewing a Feynman note — the protocol

This is the most common task. Read the stage map's **knowledge checklist** first, then the note.
Report in this order:

1. **Actual errors, hardest first.** Wrong claims, sign slips, notation collisions. Say what is
   wrong and what it should be, in one or two sentences. **Errors in §3 (napkin) and §5 (summary
   table) outrank everything** — those are what gets recalled cold in an interview.
   *Look specifically for a right answer with wrong justification* — e.g. `E[X]=np` attributed to
   independence when it is linearity. That reads as correct and is the kind of thing an
   interviewer probes.
2. **Checklist items not covered**, against the stage map, not against your own sense of the topic.
3. **What is genuinely good**, briefly and only if true. The user's `R.linalg` note struck out a
   stalled derivation and rebuilt it; that deserved saying and nothing else did.

**Do not:** rewrite their prose, add material they did not ask for, or pad with encouragement.
**Do:** take their call when they say a check is redundant — on 07-30 they declined a numerical
anchor and were right.

**Grade honestly, including "this is not finished."** `F1.4` closed as PARTIAL with 6 of 10 boxes
failing, and saying so plainly was more useful than a pass.
- **Do bias toward action.** Draft the scaffolding (problem sets, note skeletons, tooling); let
  the user supply the thinking.
- **Do prepare materials fully before a study block.** Stated need: "everything ready, so I have
  a concrete time of study, nothing interrupting."
- **Do track velocity honestly**, and read it for *cause*, not just magnitude. Days 1–7 ran
  0.7h/day; Day 11 ran 3.5h and hit its allocation. The variable that changed was stage design
  (one source, three blocks), not effort. Size S16 off the new shape, not the old average.

---

## 8. What to open next

1. **`MANUAL.md`** — the operating procedure: day / stage / sprint, and §6 "the rules that were
   paid for" with what each one cost. **Read this first if picking the repo up cold.**
2. `progress/sprints/S16.md` — active sprint: schedule, actuals log, retro
3. `stage_maps/<id>_<slug>.md` — the active stage: checklist, source, problems, deliverables
4. `progress/feynman_notes/<id>_<slug>.md` — what the user has written
5. `progress/baseline_scores.md` — starting point + the red flags stages are built to close
6. `04_deliverables_spec.md` — D1–D4, the stretch-item rule, definition of done
7. `03_gated_progression.md` — **owns study order.** DAG is current; the 13-sprint traversal
   table is marked stale, rewrite scheduled for the S16 retro (08-16)
8. `vault/HOME.md` — Dataview dashboard; `vault/topics/` holds coverage + deferrals
9. `CAPABILITY_MAP.md` — top-down, why a stage matters. **Reference only, never a planning
   input** — the DAG owns sequencing
10. `SYLLABUS.md` — one-page overview *(overlaps the sprint files; treat as stale if they disagree)*

---

*Keep §5 current — it is the only section that goes stale. Everything else is evergreen.*
