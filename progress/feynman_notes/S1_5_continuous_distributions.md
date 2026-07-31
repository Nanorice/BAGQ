# Continuous Distributions
`stage: S1.5` · **Started:** ____ · **Completed:** ____
**Time spent:** __h · **Source(s):** Ross 6th ed. Ch. 5, pp. ____

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



## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Watch for: writing the MGF of Exp(λ) as λ/(λ−t) without stating t < λ. The existence
     range is not a technicality — it is the whole content. -->



## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist. -->



## 4. Analogy (non-mathematical)

<!-- One per distribution. Non-mathematical. Memorylessness has a very good one about
     waiting for a bus that never gets more likely to arrive. -->



## 5. THE SUMMARY TABLE — this is the deliverable

<!-- Fill from memory first, THEN check. Sits directly under yesterday's discrete table. -->

| | PDF | CDF | E[X] | Var(X) | MGF | The one fact |
|---|---|---|---|---|---|---|
| **Uniform(a,b)** | | | | | | |
| **Exp(λ)** | | | | | | |
| **N(μ,σ²)** | | | | | | |

**Numerical anchors (from memory):** `P(|Z|>2) = ____` · one-tail 95% z = ____ · two-tail 95% z = ____

**Poisson ↔ Exponential:** <!-- one line -->

## 6. Where this breaks

<!-- ≥2 items. Candidates you will meet in the problems:
     - MGF of Exp exists only for t < λ; heavy tails have NO MGF near 0 (A3)
     - memorylessness is wrong for wear-out (physical parts) — hazard rises, use Weibull (B3)
     - normal approx to binomial needs large n AND p not near 0/1 — else use Poisson (B5)
     - E[Exp] = SD[Exp] = 1/λ: "average wait 5 min" says much less than people assume (A2) -->



## 7. Links

- **Problems solved:** S1.5-A1…A5, B__ (from `problem_sets/S1_5_continuous_distributions.md`)
- **Prereqs:** S1.3 (geometric memorylessness — the discrete twin of B1; Poisson for B2) ·
  T0.C (integration by parts, `e^x`)
- **Unlocks:** S1.6 joint/MVN · S4.1 Brownian motion · S6 Black-Scholes (log-normal) ·
  S9.2 hypothesis testing (χ²) · S25 correlated MC
- **Baseline questions this closes:** **I.3 (E/Var of Exp(λ)) — the mandatory-deep item** ·
  partial I.4 (normal sums)
- **Deliberately deferred:** log-normal → S6 · χ² → S9.2 · Gamma/Beta → later ·
  CLT *proof* → S1.8 · bivariate normal → S1.6

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
- [ ] `src/solvers/s1_probability/distributions_verify.py` runs — inverse-transform Exp sampler
      confirms mean `1/λ`, var `1/λ²`
- [ ] **Unlock test: I.3 re-answered cold, fully correct** (`1/λ`, `1/λ²`)
