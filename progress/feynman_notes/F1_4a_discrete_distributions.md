# Discrete Distributions
`stage: `F1.4a` · **Started:** 2026-07-31 · **Completed:** 2026-08-02 (partial — see checklist)
**Time spent:** 6.0h (Fri 1.0 · Sat 3.0 · Sun 2.0) · **Source(s):** Ross 6th ed. Ch. 4

> **Closed as PARTIAL.** Summary table lives in the handnote, not here. Solver deferred to S16
> alongside `F1.4b`. Everything else landed. The +1wk review on 08-08 is the real test.

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

(a) in binmial, each trial is a bernoulli random variable as it has constant praameter p a,d number of trial is 1. when computing E(x), due to linearity of expectation, we can simply get n*p, which is total number of trials times Expectation of each trial (irrelevant to independence)
(b) counting the number of trials until first success. expectation of 2nd trial is no different than what we get for 1st trial, as they aer independent events. so the equality exists, where E(x) = 1 + (1-p)*E(x), meaning, besides the first trial which must exist to have a result, the failure probability should weight the same Expected value.
(c) when total number of trial is large and p reasonably small, such that np is moderate. lambda is np, effectively expected number of successes in this population. lambda is the rate parameter, measured per window, can be scaled. 
(d) deferred, this is not in the book chapter 4.

## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Watch for: "variance adds" stated without saying that this needs independence, when
     the expectation step one line earlier did not. That asymmetry is the thing. -->
1. derivation of E(x^k) for binomial, plus how we assigned a new random variable, why it is Y+1 not Y
2. derivation of E(x^2) for Poisson
3. derivation of Geometric E(x) using Gambler's Ruin approach
4. MGF, deferred — **not a gap.** Confirmed 08-09: MGFs are Ross Ch.7, outside this stage's
   source. Formally moved to S1.8; the definition is in `F1.4b`'s §Stretch notes.


## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist. -->
Bernoulli, atomic event where for a single event we can express a success with probability of p and fail as 1-p
Binomial, a series of bernoulli, counting for number of successes, independent to each other, expressed in n,p
Poisson, approximation of binomial for large population and low probability
Geometric, counting number of trials until first success


## 4. Analogy (non-mathematical)

<!-- One per distribution. Non-mathematical — "some rearrangement of a formula" is not an
     analogy. Geometric has a good one about waiting. Poisson has one about rare events in
     a big crowd. -->
POisson: number of typos in a page


## 5. THE SUMMARY TABLE — this is the deliverable

<!-- Fill from memory first, THEN check. This is what you recall in a year. -->

| | PMF | E[X] | Var(X) | MGF |
|---|---|---|---|---|
| **Bernoulli(p)** | | | | |
| **Binomial(n,p)** | | | | |
| **Geometric(p)** | | | | |
| **Poisson(λ)** | | | | |

written in handnote

**Poisson as limit of Binomial:** <!-- one line: which limit, and what it means practically -->
n large, p small amd np moderate
## 6. Where this breaks

<!-- ≥2 items. Candidates you will meet in the problems:
     - variance adds only under independence; expectation always adds (A1 vs A2)
     - Poisson needs p → 0 with np fixed; p fixed gives a NORMAL limit, not Poisson (B5 tomorrow)
     - real arrival data is overdispersed — Var > E breaks the Poisson fit (C2)
     - geometric memorylessness is exactly the gambler's fallacy people get wrong (B2) -->

geometric memorylessness is exactly the gambler's fallacy people get wrong;
linearity of expectation, and derivatives

## 7. Links

- **Problems solved:** F1.4a-A1…A5, B__ (from `stage_maps/F1_4a_discrete_distributions.md`)
- **Prereqs:** R.calculus (Taylor series for `e^λ`, the `(1+dx)^{1/dx}` limit)
- **Unlocks:** `F1.4b` continuous (tomorrow — geometric→exponential) · S1.4 discrete RVs ·
  S1.8 MGF · S2.1 puzzles · S3 Markov (first-step analysis is A3(ii))
- **Baseline questions this closes:** II.1 (E[flips for HH]) · II.3 (coupon collector, Tier C) ·
  partial I.3 (the discrete half of the named-distribution gap)
- **Deliberately deferred:** negative binomial, hypergeometric, multinomial → later.
  Using MGFs for sums → S1.8. Poisson *process* → S4.4 (deferred).

---

## Completion checklist (all must pass)

- [x] All 6 template sections have real content
- [x] Zero remaining ⚠️ GAP markers *(MGF is a deliberate defer to S1.8, not a gap)*
- [ ] Summary table filled from memory, then verified — **in handnote, not in repo**
- [x] Napkin ≤200 words AND said out loud once
- [x] Analogy is non-mathematical
- [x] "Where this breaks" lists ≥2 items
- [x] Tier-A problems A1–A4 solved unhinted — **A5 formally withdrawn 08-09** (MGF is Ross Ch.7,
      not Ch.4; the map was wrong, not the study). Tier A for this stage is A1–A4.
- [ ] ≥3 of 5 Tier-B solved
- [ ] `src/solvers/s1_probability/discrete_verify.py` — **deferred to S16 with `F1.4b`**
- [ ] Unlock test: II.1 re-answered cold, fully correct — **do at the 08-08 +1wk review**
