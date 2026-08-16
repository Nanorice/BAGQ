---
type: feynman-note
stage: "[[F1_7a_expectation_tower_property]] / [[F1_7b_moment_inequalities_mgf]]"
id: F1.7
---

# Expectation, Variance & Moments
`F1.7` (a+b) · Completed:
**Time spent:** __h · **Source(s):** `topics/section_I` §7

> This note is **shared across `F1.7a` and `F1.7b`** — one note, two sub-stages, same as
> `F1.1`'s pattern. Write §1(a) after `F1.7a` (Thu/Fri), §1(b) after `F1.7b` (Sat), close
> §2–§6 at the end of `F1.7b`. What to *do* lives in the two stage maps.

## Review log
- [ ] +1 week (2026-08-30): reproduce the concept table cold → pass/fail
- [ ] +1 month (2026-09-30): re-derive Chebyshev from Markov from scratch → pass/fail
- [ ] +3 months (2026-11-30): re-take one D4 question → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

### 1(a) — Linearity, LOTUS, Tower Property, Eve's Law (after `F1.7a`)

<!-- Explain to a smart 15-year-old. Four things:
     (a) Linearity of expectation — why does it need zero assumptions about dependence?
     (b) LOTUS — when does it save you work vs. deriving g(X)'s distribution first?
     (c) Tower property — what IS E[X|Y], and why is first-step conditioning the same move
         as Bayes' law of total probability from F1.2?
     (d) Eve's Law — what do the two terms mean physically (within-group vs between-group)?
     No jargon shortcuts. -->

### 1(b) — Moment Inequalities & MGF (after `F1.7b`)

<!-- Explain to a smart 15-year-old:
     (a) Markov → Chebyshev — why is Chebyshev just Markov applied to a squared variable?
     (b) Jensen — the chord/curve picture, and why Jensen applied to x² IS "variance ≥ 0"
     (c) MGF — what is M_X(t), why do derivatives at 0 give you moments, and what does it
         mean for an MGF to "not exist" for some t? -->

## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     F1.7b's Pass opens on whatever is logged here from F1.7a. -->

## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist.
     Cover tower property + Eve's Law at minimum — those are the baseline-critical items. -->

## 4. Where I'd actually meet this

<!-- One line each. Technical is fine.
     Tower property → S3 first-passage / gambler's ruin is the obvious one; find your own too. -->

## 5. THE SUMMARY TABLE — this is the deliverable

<!-- Fill from memory first, THEN check. One row per named result, not a distribution table. -->

| Result | Formula | The one fact / failure mode |
| ------ | ------- | ---------------------------- |
| **Linearity** |  |  |
| **LOTUS** |  |  |
| **Tower property** |  |  |
| **Eve's Law** |  |  |
| **Markov** |  |  |
| **Chebyshev** |  |  |
| **Jensen** |  |  |
| **MGF** |  |  |

## 6. Where this breaks

<!-- ≥2 items. Candidates: E[XY]=E[X]E[Y] needs independence, linearity doesn't · Chebyshev is
     loose because it's distribution-free · MGF doesn't exist for heavy-tailed distributions. -->

## 7. Links

- **Problems solved:** F1.7a-A1…A5, B__ · F1.7b-A1…A4, B__ (from the two stage maps)
- **Prereqs:** `F1.2` (tower property is the continuous analogue of law of total probability) ·
  `F1.4`/`F1.5` (named distributions the MGF examples draw on)
- **Unlocks:** `S1.8` MGF/PGF full treatment (convolution, uniqueness) · `S3` Markov chains
  (first-step conditioning) · `S9.1` MLE (previewed in `F1.7b`-B4)
- **Baseline questions this closes:** tower property was scored 0 on the diagnostic
  (Adjustment #1) — this stage is the fix
- **Deliberately deferred:** MGF uniqueness · convolution via MGF product · characteristic
  functions · PGF — all `S1.8`

---

*Completion checklist lives in the stage maps (§Deliverables), not here.*
