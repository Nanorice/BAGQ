# Discrete Distributions
`stage: S1.3` · **Started:** ____ · **Completed:** ____
**Time spent:** __h · **Source(s):** Ross 6th ed. Ch. 4, pp. ____

## Review log
- [ ] +1 week (2026-08-08): reproduce the four-row summary table cold → pass/fail
- [ ] +1 month (2026-08-31): re-derive `E[Geometric] = 1/p` by conditioning → pass/fail
- [ ] +3 months (2026-10-31): re-take I.3 + II.1 → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

<!-- Explain to a smart 15-year-old. Four things:
     (a) Bernoulli → Binomial: why is a binomial just a pile of Bernoullis, and what does
         that buy you when computing E[X]?
     (b) Geometric — what is it counting, and why is E[X] = 1/p almost obvious once you
         condition on the first trial?
     (c) Poisson — what situation produces it, and what does λ mean?
     (d) MGF — what is it FOR? (not "what is the formula")
     No jargon shortcuts. If you use a term, define it in the same paragraph. -->



## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Watch for: "variance adds" stated without saying that this needs independence, when
     the expectation step one line earlier did not. That asymmetry is the thing. -->



## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist. -->



## 4. Analogy (non-mathematical)

<!-- One per distribution. Non-mathematical — "some rearrangement of a formula" is not an
     analogy. Geometric has a good one about waiting. Poisson has one about rare events in
     a big crowd. -->



## 5. THE SUMMARY TABLE — this is the deliverable

<!-- Fill from memory first, THEN check. This is what you recall in a year. -->

| | PMF | E[X] | Var(X) | MGF |
|---|---|---|---|---|
| **Bernoulli(p)** | | | | |
| **Binomial(n,p)** | | | | |
| **Geometric(p)** | | | | |
| **Poisson(λ)** | | | | |

**Poisson as limit of Binomial:** <!-- one line: which limit, and what it means practically -->

## 6. Where this breaks

<!-- ≥2 items. Candidates you will meet in the problems:
     - variance adds only under independence; expectation always adds (A1 vs A2)
     - Poisson needs p → 0 with np fixed; p fixed gives a NORMAL limit, not Poisson (B5 tomorrow)
     - real arrival data is overdispersed — Var > E breaks the Poisson fit (C2)
     - geometric memorylessness is exactly the gambler's fallacy people get wrong (B2) -->



## 7. Links

- **Problems solved:** S1.3-A1…A5, B__ (from `problem_sets/S1_3_discrete_distributions.md`)
- **Prereqs:** T0.C (Taylor series for `e^λ`, the `(1+dx)^{1/dx}` limit)
- **Unlocks:** S1.5 continuous (tomorrow — geometric→exponential) · S1.4 discrete RVs ·
  S1.8 MGF · S2.1 puzzles · S3 Markov (first-step analysis is A3(ii))
- **Baseline questions this closes:** II.1 (E[flips for HH]) · II.3 (coupon collector, Tier C) ·
  partial I.3 (the discrete half of the named-distribution gap)
- **Deliberately deferred:** negative binomial, hypergeometric, multinomial → later.
  Using MGFs for sums → S1.8. Poisson *process* → S4.4 (deferred).

---

## Completion checklist (all must pass)

- [ ] All 6 template sections have real content
- [ ] Zero remaining ⚠️ GAP markers
- [ ] Summary table filled from memory, then verified
- [ ] Napkin ≤200 words AND said out loud once
- [ ] Analogy is non-mathematical
- [ ] "Where this breaks" lists ≥2 items
- [ ] Tier-A problems A1–A5 all solved unhinted
- [ ] ≥3 of 5 Tier-B solved
- [ ] `src/solvers/s1_probability/discrete_verify.py` runs and confirms E[Geom]=1/p and E[HH]=6
- [ ] Unlock test: II.1 re-answered cold, fully correct
