---
type: feynman-note
stage: "[[F1_5_continuous_distributions]]"
id: F1.5
---

# Continuous Distributions
`F1.5` · **Started:** ____ · **Completed:** ____
**Time spent:** __h · **Source(s):** Ross 6th ed. Ch. 5, pp. ____

> This note is **yours** — what you understood. What to *do* (checklist, problems, code,
> deliverables) lives in `stage_maps/F1_5_continuous_distributions.md`.

## Review log
- [ ] +1 week (2026-08-08): reproduce the three-row summary table cold → pass/fail
- [ ] +1 month (2026-08-31): re-derive `E[Exp(λ)]` via the tail formula → pass/fail
- [ ] +3 months (2026-10-31): re-take I.3 → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

<!-- Explain to a smart 15-year-old. Four things:
     (a) Uniform + inverse transform — how does U(0,1) become ANY distribution you want?
     (b) Exponential — E[X] = 1/λ, Var = 1/λ². What does memorylessness actually mean to
         someone waiting for a bus?
     (c) Normal — why does standardisation Z = (X−μ)/σ reduce every question to one table?
     (d) The Poisson–exponential bridge: same process, two descriptions. Which is which?
     No jargon shortcuts. If you use a term, define it in the same paragraph. -->

1. Uniform distribution gives even probability of events over a range. Can think of as a box, where width (b-a) is range of x, and height 1/(b-a) is PDF, so total area is 1. Inverse transform is a process where given probability we work out distribution of random variable. And here the generator of probability, we use U which is a random variable for probability with uniform distribution. Then we plug it in to expression of other distribution and get expression for X
2. memoryless, means the incremental probability from change in x is independent from existing value for x. think this as, you have a curve representing PDF, and integral of it is F(x). When you cut the curve from say t=2, to make the remaining curve still have integral of 1, you apply a linear scaler and will find that the shape is exactly the same as the old curve. And that probability change of every incremental change in x is the same
3. normal distribution has the mu and sigma as parameters describing the curve, with z-transform, we can map it back to exactly the unit normal distribution ,then calculate the value phi using the table of x vs F(x)
4. Binomial is sequence of events, each with a binary results so a Bernoulli, modelling for total number of successes given n and p; Poission is binomial for large n and small p; exponential is for measuring continuous of variable passage until the first occurance of a event; 

## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Watch for: writing the MGF of Exp(λ) as λ/(λ−t) without stating t < λ. The existence
     range is not a technicality — it is the whole content. -->

1. didn't know about inverse transformation
2. is it saying F(1) = F(3)-F(2)?
3. for number 4, is this bridge true? also binomial a bit rusty already even from last week..

## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist. -->
1. uniform distribution givens even probability to every value in a continuous range. we can use inverse transformation to get the variable distribution
2. normal distribution is very common in nature, and for many distributions when n is large eought the shape resembles normals' bell shape
3. exponential measures time passage until event. this adds up to gamma; this is like geometric adds up to binomial


## 4. Where I'd actually meet this

<!-- One line each. Technical is fine — this replaced "Analogy" on 2026-08-04 because a
     supplied analogy is just another sentence to memorise, while "where does this show up"
     is a real interview question. Your R.linalg answers (PCA factors, portfolio covariance)
     were the model. Concrete beats clever. -->

1. normal distribution used for measuring daily stock return, then used for computing VaR
2. exponential measure arrival rate and constant hazard rate, used for order filling in market making

## 5. THE SUMMARY TABLE — this is the deliverable

<!-- Fill from memory first, THEN check. Sits directly under yesterday's discrete table. -->

|                  | PDF        | CDF         | E[X]    | Var(X)     | MGF | The one fact |
| ---------------- | ---------- | ----------- | ------- | ---------- | --- | ------------ |
| **Uniform(a,b)** | 1/(b-a)    | (x-a)/(b-a) | (b+a)/2 | (b-a)^2/12 | x   |              |
| **Exp(λ)**       | k*exp(-kx) | 1-exp(-kx)  | k       | k^2        | x   |              |
| **N(μ,σ²)**      |            |             |         |            |     |              |

**Numerical anchors (from memory):** `P(|Z|>2) = __0.05__` · one-tail 95% z = 1.645____ · two-tail 95% z = 2____

**Poisson ↔ Exponential:** <!-- one line -->

## 6. Where this breaks

<!-- ≥2 items. Candidates you will meet in the problems:
     - MGF of Exp exists only for t < λ; heavy tails have NO MGF near 0 (A3)
     - memorylessness is wrong for wear-out (physical parts) — hazard rises, use Weibull (B3)
     - normal approx to binomial needs large n AND p not near 0/1 — else use Poisson (B5)
     - E[Exp] = SD[Exp] = 1/λ: "average wait 5 min" says much less than people assume (A2) -->



## 7. Links

- **Problems solved:** F1.5-A1…A5, B__ (from `stage_maps/F1_5_continuous_distributions.md`)
- **Prereqs:** `F1.4` (geometric memorylessness — the discrete twin of B1; Poisson for B2) ·
  R.calculus (integration by parts, `e^x`)
- **Unlocks:** S1.6 joint/MVN · S4.1 Brownian motion · S6 Black-Scholes (log-normal) ·
  S9.2 hypothesis testing (χ²) · S25 correlated MC
- **Baseline questions this closes:** **I.3 (E/Var of Exp(λ)) — the mandatory-deep item** ·
  partial I.4 (normal sums)
- **Deliberately deferred:** log-normal → S6 · χ² → S9.2 · Gamma/Beta → later ·
  CLT *proof* → S1.8 · bivariate normal → S1.6

---

*Completion checklist lives in the stage map (§Deliverables), not here.*
