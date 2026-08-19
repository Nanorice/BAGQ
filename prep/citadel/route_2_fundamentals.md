---
type: prep-route
name: Route 2 — Fundamentals
status: active
opened: 2026-08-19
blocks: [A, C, D, E, F]
---

# Route 2 — Fundamentals

**Mode: prime only.** This is the route that wins the technical rounds, and it is the only one of
the three that needs an uninterrupted 60+ minute block with paper. When time is short, this is
what you protect.

**Standard: rebuild, not recognise.** The test for every unit below is the same — *blank paper,
derive it, no source*. You could already pass a recognition test on most of A. That is the gap
you named, and recognition is what fails in front of an ex-GS-Market-Risk interviewer.

**Format per unit:** each is a curriculum-style stage — source, checklist, problems, and a
teach-back. **You write the teach-back, I check it.** Working mode does not change for this prep.

---

## Sources — fixed, do not go shopping

| Block | Source | Why |
|---|---|---|
| A. VaR | **Hull, *Risk Management and Financial Institutions*** — VaR + volatility + correlation chapters. If you only have *Options, Futures & Other Derivatives*, its VaR chapter covers A1–A3 | Owned. No new books (`CLAUDE.md` §4) |
| A3 extension | Paleologo §3.5 + §11.1.5 (Route 1, P1/P4) | Marginal contribution, the same machinery |
| C1–C2 | Ross, *A First Course in Probability* — estimation + hypothesis testing chapters | Owned, and it is the curriculum's own source |
| C3 | **Written inline below** — no book you own does Kupiec/Christoffersen | Named gap, resolved per `done.md` §D2 |
| C4 | Isichenko Ch.7 (Route 1, I2) | Best treatment you have |
| C5 | Baseline IX.3/IX.4 + Hull volatility chapter (EWMA/GARCH) | Closes two baseline lows |
| D | **Written inline below** + your own CCAR/ICAAP experience | You have run these; the gap is the build side |
| E | Paleologo Ch.7 + Isichenko §6.1/§6.9 | Route 1 does the reading; this route does the derivation |

---

## Unit A — VaR, rebuilt ⭐⭐ THE MAIN UNIT

> Est. 12–15h. Three passes on separate days (curriculum rule: new machinery needs two+ passes).
> **This is the unit the technical rounds are about.**

### A-i. The three estimators (~3h)
- [ ] Parametric: derive `VaR_α = −(μ + z_α σ)·V` from the normal quantile. Know `z` for 95/99
- [ ] Historical: the empirical quantile, the window-is-the-assumption problem, ghosting
- [ ] Monte Carlo: when it is the only option; the variance of the VaR estimate itself
- [ ] **On paper:** same portfolio, all three methods, and explain every difference
- [ ] Scaling: `√T` rule, and precisely when it is invalid (autocorrelation, non-iid, fat tails)

### A-ii. Portfolio VaR and non-linearity (~2h)
- [ ] `σ_p² = wᵀΣw` expanded by hand for 2 assets — cold, no prompt
- [ ] Derive why the 2-asset VaR surface is **curved** in `(x, y)`. One sentence, then the algebra
- [ ] Diversification benefit `Σ VaR_i − VaR_p`; when it goes to zero
- [ ] Subadditivity, and construct the counterexample where VaR fails it *(two defaultable bonds —
      the standard one; be able to build it, not just cite it)*

### A-iii. Decomposition — marginal, component, incremental (~4h) ⭐⭐
> **The core of the whole prep.** This is what a central risk desk does all day, and it is the
> named machinery behind the tool you already built.
- [ ] Derive `MVaR_i = ∂VaR/∂w_i = VaR · (Σw)_i / (wᵀΣw)`. Do the differentiation, do not cite it
- [ ] `CVaR_i = w_i · MVaR_i`, and **prove `Σ_i CVaR_i = VaR`** via Euler's theorem on
      homogeneous-degree-1 functions. *Know that the proof depends on homogeneity — that is the
      follow-up question*
- [ ] Incremental VaR: full recomputation, and why it differs from `MVaR × Δw` for non-small `Δw`
      **— this difference is exactly why your surface needed to be a surface**
- [ ] Show a position with negative component VaR, i.e. risk-*reducing*. Say what its correlation
      with the rest of the book must be
- [ ] **The entity question:** same asset, risk-adding in entity 1, risk-reducing in entity 2.
      Write it as two different `Σw` products. This is your story with the algebra attached
- [ ] Beta representation: `MVaR_i = VaR · β_{i,p}` — connect risk decomposition to CAPM beta

### A-iv. Expected Shortfall (~2h)
- [ ] `ES_α = E[L | L > VaR_α]`; derive the closed form under normality `= σ·φ(z_α)/(1−α)`
- [ ] The four coherence axioms; which one VaR fails and why ES does not
- [ ] FRTB's move from 99% VaR to 97.5% ES — and why *97.5*, not 99
- [ ] ES is not elicitable, so backtesting it is hard — one sentence, high signal

### A-v. The covariance matrix (~2h)
- [ ] EWMA: `σ²_t = λσ²_{t−1} + (1−λ)r²_{t−1}`; why RiskMetrics chose `λ = 0.94`; effective window
- [ ] GARCH(1,1) and its relation to EWMA *(EWMA is GARCH with `ω=0`, `α+β=1` — the connection
      closes baseline IX.4)*
- [ ] `Σ` PSD, and what breaks otherwise *(already closed — `R.linalg` B1/B4, cash it in)*
- [ ] `N(N+1)/2` parameters; why sample `Σ` is unusable when `T ≈ N`
- [ ] Shrinkage and factor models as the two fixes — one sentence each

**Code (→ `code/codify.ipynb`, `# Citadel VaR`):** parametric/historical/MC VaR on one series,
asserted against each other · component VaR summing to total · the 2-asset VaR surface itself,
rebuilt in Python. *Rebuilding your own tool in the language they use is the single best-value
code artifact in this prep.*

---

## Unit C — Statistics and backtesting ⚠️ WEAKEST SECTION

> Est. 10h. Baseline Section IX = **1.00**. `IX.1` MLE = **0**. This is where a technical round
> with an academic interviewer will find you, and it is on the DAG anyway — pull-forward, not detour.

### C-i. Estimation (~3h) — closes baseline IX.1
- [ ] MLE by hand: likelihood → log → differentiate → solve. **Exponential** (`λ̂ = 1/x̄`, the
      baseline zero) and **Normal** (`μ̂ = x̄`, `σ̂² = Σ(x−x̄)²/n`)
- [ ] Why the MLE of `σ²` is biased and where the `n−1` comes from
- [ ] Bias / variance / MSE, and the decomposition `MSE = bias² + var`
- [ ] Consistency vs unbiasedness — not the same thing; have an example
- [ ] SE of the mean `σ/√n`; why `√T` runs through all of risk

### C-ii. Hypothesis testing (~2h) — closes baseline IX.2/IX.3
- [ ] Type I, Type II, and **power** stated precisely *(the exact half-mark you lost)*
- [ ] p-value in one correct sentence. Then say the three wrong versions and why they are wrong
- [ ] Likelihood ratio tests; `−2 log Λ → χ²`, with degrees of freedom — **needed for C-iii**
- [ ] OLS assumptions, all of them, with what breaks when each fails *(baseline IX.3 = 1)*
- [ ] Multiple testing: Bonferroni, FDR, and why it is *the* backtesting problem

### C-iii. VaR backtesting (~3h) ⭐⭐ — no source, written inline
> **The intersection of your weakest section and the role's core.** Also the most likely single
> technical question given the hiring manager's background.
- [ ] Exceptions are Bernoulli(`1−α`); the count is Binomial(`T`, `1−α`) under the null
- [ ] **Kupiec POF (unconditional coverage):**
      `LR_uc = −2 log[ ((1−p)^{T−N} p^N) / ((1−N/T)^{T−N} (N/T)^N ) ] ~ χ²(1)`
      — derive it as a likelihood ratio (this is why C-ii's LR item comes first)
- [ ] **Christoffersen independence:** a 2-state Markov chain on exception/no-exception;
      `LR_ind ~ χ²(1)`. Combined `LR_cc = LR_uc + LR_ind ~ χ²(2)`
- [ ] **Why independence matters more than the count** — 10 exceptions spread out is a fine model;
      10 clustered in one week is a broken one. *Say this out loud; it is the insight the test exists for*
- [ ] Basel traffic light: green ≤4, amber 5–9, red ≥10 at 99%/250d, and the capital multiplier
- [ ] Power: at 99% over 250 days you expect 2.5 exceptions — compute how bad a model has to be
      before you can reject it. **The answer is depressing and knowing it is a strong signal**

**Code (`# Citadel Backtest`):** exception counter + Kupiec LR + χ² p-value on a simulated series;
verify by simulating a *deliberately* bad VaR model and checking the test catches it.

### C-iv. Strategy backtesting (~2h)
- [ ] Sharpe, annualisation, and `SE(Ŝ) ≈ √((1+S²/2)/T)` — then compute how many years of data a
      Sharpe of 1.0 needs to be 2-sigma from zero. **Memorise that number**
- [ ] In-sample / out-of-sample / walk-forward; deflated Sharpe and why it exists
- [ ] Look-ahead, survivorship, point-in-time data
- [ ] Turnover, capacity, transaction costs
> Source: Isichenko Ch.7 + §2.4.2 (Route 1, I2).

### C-v. Time series, light (~1h)
- [ ] Stationarity; returns not prices; unit roots at concept level
- [ ] Autocorrelation, Ljung–Box
- [ ] GARCH(1,1) equation and persistence `α+β` *(closes baseline IX.4)*

---

## Unit D — Stress testing (~4h)

> Your gap: *"I analysed the results, I did not build the scenarios."* Smaller than it feels —
> it is a taxonomy plus one genuine modelling problem (propagation).

- [ ] Historical / hypothetical / reverse stress testing — and when each is used
- [ ] **Scenario construction:** choose shocked factors, then propagate to everything else.
      *The propagation is the modelling.* Two approaches: conditional historical means, or a
      factor model with the shock applied to factor returns
- [ ] Your own example, built properly: eq spot −20%. What must vol do, and *where does that number
      come from*? (Historical conditional distribution of vol given a −20% equity move.) **Answering
      this converts your stated gap into a strength**
- [ ] Sensitivity-based (Greeks) vs full revaluation; when the Taylor approximation breaks —
      large shocks, convexity/gamma, path dependence
- [ ] CCAR/ICAAP structure — *frame as experience, not gap; you ran these*
- [ ] Stress testing vs VaR: VaR says nothing beyond the quantile, and nothing about *why*
- [ ] Reverse stress testing: "what breaks us?" — the question a central risk team actually asks

---

## Unit E — Portfolio construction (~6h)

> Route 1 supplies the reading (Paleologo Ch.7, Isichenko Ch.6); this unit does the derivation.
> Least covered by your GS experience.

- [ ] Derive `w* ∝ Σ⁻¹μ` from `max wᵀμ − (λ/2)wᵀΣw`. Do the calculus
- [ ] Why `Σ⁻¹` is unstable and what that does to the weights; the shrinkage/factor-model fix
- [ ] Efficient frontier, tangency portfolio, the Sharpe-maximising portfolio
- [ ] Risk parity / equal risk contribution — **and derive it as the portfolio where all component
      VaRs are equal.** *This is Unit A-iii again; make the connection explicit, it is a strong
      interview move*
- [ ] Constraints: long-only, leverage, factor neutrality, turnover
- [ ] Factor model `r = Bf + ε`, so `Σ = BΩBᵀ + D`; factor vs idiosyncratic risk
- [ ] **Central risk book:** netting internal exposures across PMs, internalising before hedging
      externally. *This is the actual seat — be able to describe the workflow*

---

## Unit F — The story (~2h) ⭐ DO THIS EARLY, IT IS CHEAP

> Needed before the HR call. Written once, told identically five times.

- [ ] The problem, in two sentences: portfolio risk is not linear in weights, so a table of
      standalone VaRs cannot answer "how much of A and B can I add"
- [ ] The tool: matrix, cell `(x,y)` = what-if VaR impact of adding `x` of A, `y` of B
- [ ] The finding: same asset, risk-adding in one entity, risk-reducing in another
- [ ] **The bridge:** this is incremental VaR, and the curvature is why marginal VaR alone is
      not enough. *Attach Unit A-iii's algebra to the story you already own*
- [ ] Scale, users, what decisions changed
- [ ] What you would do differently now (a factor model instead of raw `Σ`? more assets? live?)
- [ ] **Also prepped:** the full-stack VaR decomposition infra as the **system design** answer —
      Slang/SQL/APIs/Tableau, real-time, to desks. You have been undercounting this
- [ ] PD/LGD + CECL/IFRS9 as the rebuttal to "have you built models from scratch?" — you have

---

## Order and pacing

**F → A-iii → A-i/ii → C-iii → C-i/ii → A-iv/v → D → C-iv/v → E**

F first (cheap, needed for the HR call). **A-iii before A-i** — decomposition is the role and the
story; the estimator taxonomy is easier and can wait a week. C-iii early because it is the
likeliest hard question and it needs C-ii's likelihood-ratio machinery, so do C-ii's LR item
alongside it.

**Two passes, separate days, for A-iii and C-iii.** Those two are new machinery, and the
curriculum's own measurement (Adj #12) says one pass does not install it.

**If everything collapses: A-iii and F.**
