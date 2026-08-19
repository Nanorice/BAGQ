---
type: prep-map
name: Citadel Central Risk — Knowledge Map
role: "[[portfolio-construction]]"
process: hackerrank → HR → coderpad → onsite (2 tech, 1 sysdes, 1 behavioural)
status: active
opened: 2026-08-19
---

# Citadel — Central Risk / Portfolio Construction

**Fork, not interrupt.** Curriculum continues at reduced hours; this runs alongside.
Rounds map to blocks: HackerRank/CoderPad ← **B**, technicals ← **A + C**, system design ← **D**,
behavioural ← **E**.

**Ranked by expected damage, not by discomfort.** Python is first because it is a *gate* — it
fails you before anyone hears the VaR surface story.

---

## A. VaR — rebuild, not read

> The gap you named: *"I understand how VaR works, but could I rebuild the model?"*
> The ceiling here is lower than you fear. You do not need a firmwide engine. You need to derive
> it on a whiteboard. Ex-GS-Market-Risk hiring manager means this is where the technicals go.

**A1. The three estimators, and when each breaks**
- [ ] Parametric / variance-covariance: `VaR_α = −(μ + z_α σ)·V`, the normality assumption, why it
      understates tails
- [ ] Historical simulation: no distributional assumption, but the window *is* the assumption;
      ghosting when a shock drops out of the window
- [ ] Monte Carlo: when it is the only option (non-linear payoffs, path dependence), and its cost
- [ ] Which one a central risk desk actually runs, and why

**A2. Portfolio VaR and why it is not linear in weights** ⭐
- [ ] `σ_p² = wᵀΣw` — expand for two assets by hand, unprompted
- [ ] **This is your VaR surface.** The tool you built is the answer to "why can't we just add
      the VaRs" — write down why the surface is curved, in one sentence
- [ ] Subadditivity: `VaR(A+B) ≤ VaR(A)+VaR(B)` *usually*, and the counterexample where it fails
- [ ] Diversification benefit as `ΣVaR_i − VaR_p`

**A3. Risk decomposition — the central-risk core** ⭐⭐
- [ ] **Marginal VaR**: `∂VaR/∂w_i`, and its closed form `= VaR · (Σw)_i / (wᵀΣw)`
- [ ] **Component VaR**: `w_i · MVaR_i`, and why the components sum to total VaR (Euler theorem,
      homogeneity of degree 1). *This is the mathematical fact that makes central risk possible.*
- [ ] **Incremental VaR**: the full what-if of adding a position — the exact quantity your surface
      tabulated. Name the difference between incremental and marginal out loud.
- [ ] Why an asset can be risk-*adding* in one entity and risk-*reducing* in another
      *(your own example — it is a correlation-sign story, say it in 20 seconds)*

**A4. Expected Shortfall, and why the regulator moved**
- [ ] `ES_α = E[L | L > VaR_α]`, closed form under normality
- [ ] Coherence: the four axioms; VaR fails subadditivity, ES does not
- [ ] FRTB moved from VaR to ES — say why in one sentence
- [ ] Backtesting ES is harder than VaR (not elicitable) — knowing this is a strong signal

**A5. The covariance matrix is the whole model**
- [ ] EWMA vs sample covariance; the RiskMetrics `λ = 0.94` and what it buys
- [ ] Why `Σ` must be PSD, and what breaks when it is not *(closed — `R.linalg` B1, B4)*
- [ ] Estimation error: `N` assets means `N(N+1)/2` parameters; why sample `Σ` is garbage when
      `T ≈ N`
- [ ] Shrinkage (Ledoit–Wolf), factor models as the alternative — one sentence each, no more

---

## B. Python — the gate ⚠️ FIRST

> Highest risk, cheapest fix. Volume, not insight. Drill list in `leetcode_list.md`.

- [ ] Idioms cold: comprehensions, `dict`/`set` as the default reach, `collections.Counter`,
      `defaultdict`, `heapq`, `bisect`, `itertools`
- [ ] Slicing, unpacking, `enumerate`, `zip`, `sorted(key=)` — no hesitation
- [ ] numpy: vectorised ops, broadcasting, `@`, `np.linalg.{cholesky,eig,inv}`, axis semantics
- [ ] pandas: `groupby`, `rolling`, `merge`, `pct_change`, resampling, `shift` for lookahead safety
- [ ] Typing a working solution in **under 20 minutes** without an interpreter to lean on
- [ ] Saying the complexity out loud before writing *(baseline X.1: right answer, wrong Big-O)*

---

## C. Statistics & backtesting — the grilling ⚠️

> Baseline Section IX = **1.00**, your weakest section, and exactly where a Citadel technical
> round with an academic interviewer will go. `IX.1` MLE scored **0**.

**C1. Estimation**
- [ ] MLE: write the likelihood, log it, differentiate, solve. Exponential and Normal by hand.
      *(Baseline IX.1 — closes a zero)*
- [ ] Bias, variance, MSE, consistency; the bias–variance decomposition
- [ ] Standard error of the mean; why `√T` scaling shows up everywhere in risk

**C2. Hypothesis testing**
- [ ] Type I / II, **power** *(baseline IX.2 lost the mark on power specifically)*
- [ ] p-value stated correctly — the sentence that trips most candidates
- [ ] Multiple testing: Bonferroni, FDR, and why it is *the* backtesting problem

**C3. VaR backtesting** ⭐ *the intersection of the role and your weakest section*
- [ ] Exception counting; exceptions are Bernoulli, so the count is Binomial under the null
- [ ] **Kupiec POF test** — unconditional coverage, the LR statistic, χ²(1)
- [ ] **Christoffersen test** — independence of exceptions; why clustering matters more than count
- [ ] Basel traffic light (green/amber/red zones) — you have seen this from the results side
- [ ] Why 250 days gives so little power to reject a bad 99% model

**C4. Strategy backtesting**
- [ ] Sharpe, and its standard error `≈ √((1+S²/2)/T)` — why short backtests prove nothing
- [ ] Overfitting: in/out-of-sample, walk-forward, deflated Sharpe
- [ ] Look-ahead bias, survivorship bias, transaction costs
- [ ] Max drawdown, turnover, capacity

**C5. Time series (light)**
- [ ] Stationarity; why returns not prices
- [ ] Autocorrelation, Ljung–Box
- [ ] Vol clustering leads to GARCH(1,1): `σ²_t = ω + αε²_{t−1} + βσ²_{t−1}`, persistence `α+β`
      *(baseline IX.4 knew the shape, not the equation)*
- [ ] OLS assumptions, properly *(baseline IX.3 = 1: recognised acronym, no content)*

---

## D. Stress testing

> Your stated gap: *"I analysed results, e.g. eq spot −20%, vol up xx — I did not build the
> scenarios."* The build side is smaller than it looks: mostly a taxonomy plus a consistency
> problem.

- [ ] Historical scenarios (2008, 2020-03, 1987) vs hypothetical vs reverse stress testing
- [ ] **How a scenario is built**: pick shocked factors, then propagate to unshocked ones — the
      propagation is the actual modelling work
- [ ] Conditional/coherent scenarios: shock eq spot −20%, and vol *must* move with it. Where does
      the co-movement come from — historical conditional means, or a factor model?
- [ ] CCAR/ICAAP structure *(you have run these — frame as experience, not gap)*
- [ ] Sensitivity vs full revaluation; when Greeks-based approximation breaks (large shocks,
      convexity, path dependence)
- [ ] Stress testing as the answer to the VaR blind spot: VaR says nothing beyond the quantile

---

## E. Portfolio construction

> The forward-looking half of the role. Least covered by your GS experience, so most likely to
> find you out — but it is mostly one optimisation.

- [ ] Mean-variance: `max wᵀμ − (λ/2) wᵀΣw`, solve it, `w* ∝ Σ⁻¹μ`
- [ ] Why `Σ⁻¹` makes it unstable, and what practitioners do about it
- [ ] Efficient frontier, tangency portfolio, Sharpe maximisation
- [ ] Constraints: long-only, leverage, sector/factor neutrality, turnover
- [ ] Risk parity, equal risk contribution — and the link back to **component VaR** (A3)
- [ ] Factor models: `r = Bf + ε`, risk split into factor + idiosyncratic
- [ ] Central risk book: netting internal exposures, internalising flow before hedging externally
- [ ] Transaction costs and the optimisation-vs-turnover tradeoff

---

## F. The story ⭐ tell it identically in all five rounds

**The VaR surface tool.** Written up properly, once, then reused.

- [ ] The problem: 2-asset portfolio risk is not linear in component weights, so "how much of A
      and B can I add" cannot be answered from a table of standalone VaRs
- [ ] What you built: a matrix, cell `(x,y)` = what-if VaR impact of adding `x` of A and `y` of B
- [ ] The insight it surfaced: the same asset is risk-adding in one entity and risk-reducing in
      another, via diversification
- [ ] Why that is exactly a **component/incremental VaR** problem (A3) — connect the tool to the
      named machinery. The machinery is what you were missing, not the idea.
- [ ] Scale, users, decisions it changed
- [ ] What you would do differently now

**Also ready:** the full-stack VaR decomposition infra (Slang/SQL/APIs/Tableau, real-time, to
desks) — this is your **system design** answer, and you have not been counting it as an asset.
PD/LGD + CECL/IFRS9 is the counterexample to gap (a): you *have* built models end to end, just
not VaR ones.

---

## Sequencing

| # | Block | Why here | Rough |
|---|---|---|---:|
| 1 | **B** Python | Gate. Fails you before anything else is heard | ongoing, daily |
| 2 | **F** The story | Cheap, reused in all 5 rounds, needed before the HR call | 2h |
| 3 | **A** VaR rebuild | Highest ceiling; the ex-GS-MR manager goes here | 12–15h |
| 4 | **C** Backtesting + stats | Weakest section, and C3 sits inside the role | 10h |
| 5 | **D** Stress testing | Half-known already; taxonomy + propagation | 4h |
| 6 | **E** Portfolio construction | Least covered; mostly one optimisation | 6h |

**Overlap with the DAG, so this is pull-forward, not detour:** C1 ↔ `IX-1-estimation-theory` ·
C2 ↔ `IX-2` · C5 ↔ `IX-3` · A5/E ↔ `VII-2-applications-in-quant-finance` · B ↔ all of section X.

**If everything collapses: A3 and F.** Component VaR is the role; the story is the interview.
