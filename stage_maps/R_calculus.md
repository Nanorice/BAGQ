---
type: stage
id: R.calculus
name: Calculus Refresher
kind: refresher
multiplier: 1.2
topic: "[[VIII-1-ordinary-differential-equations]]"
concepts: ["[[itos-lemma]]"]
roles: ["[[options-pricing]]"]
sprint: S15
status: ready-for-test
budget_h: 4
actual_h: 5.0
d4_due: 2026-08-15
baseline_closes: [VIII.1, VIII.3]
---

# R.calculus — Calculus & ODE Refresher · Problem Set

**Stage:** R.calculus · **Sprint:** 15 (Days 6–7, 2026-07-25 → 07-26) · **Budget:** ~105 min input+teach-back, ~60 min problems

**Why this stage exists:** baseline VIII.1 asked `dy/dx = y, y(0)=1` and got `sqrt(2/(x-2))`. The answer is `eˣ`. That is the single most canonical ODE in existence and it gates everything downstream — GBM, OU mean reversion, discounting, Feynman-Kac. VIII.3 (Lagrange) was also fuzzy, and Lagrange is how Markowitz optimization is derived. This stage is mandatory-deep, not a skim (`baseline_scores.md` adjustment #6).

**Scope — four things only:**
1. Separable ODEs
2. Linear first-order ODEs (integrating factor)
3. Chain rule / implicit differentiation
4. Lagrange multipliers

Everything else in `topics/section_VIII_calculus_des.md` (PDEs, Riccati, Carr-Madan, Euler-Lagrange, KKT) is **out of scope** — that file is the full inventory, not this stage. See [vault/topics/](../vault/topics/) for what this stage closed vs deferred.

---

## Sources — read in this order, stop when the concept clicks

| # | Source | Covers | Time | Have it? |
|---|---|---|---|---|
| S1 | 3Blue1Brown, *Essence of Calculus* **Ch. 4** ("Visualizing the chain rule and product rule") | Topic 3 | 12 min | free, YouTube |
| S2 | 3Blue1Brown, *Essence of Calculus* **Ch. 5** ("What's so special about Euler's number e?") | Topic 1 — this is literally `dy/dx = y` | 14 min | free, YouTube |
| S3 | 3Blue1Brown, *Essence of Calculus* **Ch. 6** ("Implicit differentiation, what's going on here?") | Topic 3 | 15 min | free, YouTube |
| S4 | Khan Academy, "Lagrange multipliers, introduction" + "Interpretation of Lagrange multipliers" | Topic 4 | 20 min | free |
| S5 | **Green Book (Zhou), §2.2 "Calculus"** — the ODE subsection | Topics 1–2, in interview register | 20 min | ✅ on hand |
| S6 | **Green Book, §2.3 "Optimization"** — Lagrange worked examples | Topic 4 | 15 min | ✅ on hand |
| S7 | **Ross, Appendix / Ch.5 §5.5** — exponential distribution derivation | Optional: sanity-check that `e^{-λx}` is a separable-ODE solution | 10 min | ✅ on hand |

**Input time-box: 45 min.** Feynman protocol Step 1 caps input at ≤40% of stage time. Do not watch all seven. Pick what closes your gap; S2 and S5 are the non-negotiables.

---

## How to use this set

Problems are tiered. **Tier A is the floor — all six must be done unhinted.** Tier B is the target. Tier C only if Tier A+B took under 45 min.

Work them on paper, closed-book, *after* the teach-back draft. Answer keys are at the bottom — do not scroll early; a peeked problem is a `⚠️ GAP` you'll never find.

Cite these IDs in your Feynman note §7 ("Problems solved") and in the unlock test.

---

## Tier A — the floor (must pass unhinted)

**R.calculus-A1.** Solve `dy/dx = y` with `y(0) = 1`. Show every step of the separation, including where the constant of integration goes and why it becomes a multiplicative constant.
*This is baseline VIII.1. If you cannot do this one cold, the stage is not complete.*

**R.calculus-A2.** Solve `dy/dx = ky` with `y(0) = y₀`, for constant `k`. Then state in one sentence what this means when `y` is a bank balance and `k` is a continuously-compounded interest rate.

**R.calculus-A3.** Solve `dy/dx = xy` with `y(0) = 1`. Note where the answer differs in *shape* from A1 and say why the `x` on the right changes the exponent.

**R.calculus-A4.** Differentiate `f(x) = e^{3x²}` with respect to `x`. Then differentiate `g(x) = ln(cos x)`. Name which rule you used at each step.

**R.calculus-A5.** Minimize `f(x,y) = x² + y²` subject to `x + y = 1` using Lagrange multipliers. Give `x*`, `y*`, the minimum value, and `λ`.
*This is baseline VIII.3. Answer: x=y=1/2, min=1/2.*

**R.calculus-A6.** Solve the mean-reverting ODE `dx/dt = κ(θ − x)` with `x(0) = x₀`. Show that `x(t) → θ` as `t → ∞` regardless of `x₀`, provided `κ > 0`.
*This is the deterministic skeleton of Ornstein-Uhlenbeck. You will meet it again in S4 and in every mean-reversion strategy you ever backtest.*

---

## Tier B — the target

**R_calculus-B1.** Solve the linear first-order ODE `y' + 2y = e^{-x}` with `y(0) = 0`, using an integrating factor. State the integrating factor explicitly and why `μ(x) = e^{∫p dx}` is the right choice — what does multiplying by it *do* to the left-hand side?

**R_calculus-B2.** Solve `y' + (1/x)y = x` for `x > 0`, with `y(1) = 1/3`.

**R_calculus-B3.** A perpetuity pays continuously at rate `c`, growing at rate `g`, discounted at `r > g`. Its present value `V` satisfies `rV − gV = c`. Derive `V = c/(r−g)`. Then explain in one sentence what happens as `g → r` and why that is financially sensible rather than a mathematical accident.

**R_calculus-B4.** Given `x² + y² = 25`, find `dy/dx` at the point `(3, 4)` by implicit differentiation. Verify geometrically (the tangent to a circle is perpendicular to the radius — check the slopes multiply to −1).

**R_calculus-B5.** Maximize `f(x,y) = xy` subject to `x + y = 10`. Then state the general result this special case illustrates about the rectangle of fixed perimeter and maximum area.

**R_calculus-B6.** In A5 you found `λ`. Now change the constraint to `x + y = 1.1` and re-solve. Compare the change in the minimum value to `λ × 0.1`. This is why `λ` is called the **shadow price** of the constraint — write one sentence explaining what that means to a portfolio manager.

**R_calculus-B7.** Solve `dV/dt = r(t)V` with `V(0) = V₀` for a *time-varying* rate `r(t)`. Show `V(t) = V₀ exp(∫₀ᵗ r(s)ds)`. Say why this justifies the discount factor `exp(−∫r)` you see everywhere in fixed income.

---

## Tier C — stretch (only if A+B ran short)

**R_calculus-C1.** Solve the logistic ODE `dN/dt = rN(1 − N/K)` with `N(0) = N₀`. (Hint: separable, then partial fractions.) Sketch the S-curve.

**R_calculus-C2.** *Markowitz, two assets.* Minimize `½wᵀΣw` subject to `wᵀ1 = 1` for `Σ = [[0.04, 0.01], [0.01, 0.09]]`. Set up the Lagrangian, solve for `w*`, and confirm the weights sum to 1. This is the minimum-variance portfolio — the single most-asked Lagrange application in a QR interview.

**R_calculus-C3.** Green Book has a class of problems asking for `max`/`min` of a function on a constrained region. Find two in §2.3 and do them.

---

## Deliverables for this stage

Per `04_deliverables_spec.md` and `02_feynman_protocol.md`:

- [ ] `progress/feynman_notes/R_calculus.md` — all 6 template sections, zero remaining `⚠️ GAP`, napkin version ≤200 words said out loud once
- [ ] All 6 Tier-A problems solved unhinted, worked on paper, answers logged
- [ ] ≥4 of 7 Tier-B solved
- [ ] Numerical anchor in the note: solve A1 by hand, then verify with `scipy.integrate.solve_ivp` or a 3-line Euler scheme, and confirm it lands on `e¹ ≈ 2.71828` at `x=1`
- [ ] Unlock test: re-answer baseline VIII.1 and VIII.3 cold. Both must be fully correct.

**No solver files this stage.** `src/solvers/` gets created at T1.X (Day 11) when the Monte Carlo verifiers actually need it. The one numerical check above can live inline in the Feynman note.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** `dy/y = dx` → `ln|y| = x + C` → `y = Ae^x` where `A = e^C`. The constant becomes multiplicative because it was additive *inside a log*. `y(0)=1` → `A=1` → **`y = eˣ`**. The defining property: this is the unique function that is its own derivative.

**A2.** `y = y₀e^{kx}`. A balance growing at continuously-compounded rate `k` multiplies by `e^k` each unit time — not `1+k`. The gap between them is the whole point of continuous compounding.

**A3.** `dy/y = x dx` → `ln|y| = x²/2 + C` → **`y = e^{x²/2}`**. The `x` on the right integrates to `x²/2`, so growth is super-exponential — the exponent itself grows. A1 has a constant growth *rate*; A3's rate rises with `x`.

**A4.** `f'(x) = 6x·e^{3x²}` (chain rule: outer `e^u`, inner `3x²` with derivative `6x`).
`g'(x) = −tan x` (chain rule: `(1/cos x)·(−sin x)`).

**A5.** `L = x² + y² − λ(x + y − 1)`. `∂L/∂x: 2x = λ`, `∂L/∂y: 2y = λ` → `x = y`. Constraint → `x = y = 1/2`. **Min = 1/2, λ = 1.**

**A6.** Separable: `dx/(θ−x) = κ dt` → `−ln|θ−x| = κt + C` → `θ − x = Ae^{−κt}`. With `x(0)=x₀`: `A = θ − x₀`. **`x(t) = θ + (x₀ − θ)e^{−κt}`.** As `t→∞`, `e^{−κt}→0` for `κ>0`, so `x→θ`. The deviation from the mean decays exponentially at rate `κ`; half-life is `ln2/κ`.

</details>

<details>
<summary>Tier B</summary>

**B1.** `μ = e^{∫2dx} = e^{2x}`. Multiplying through: `e^{2x}y' + 2e^{2x}y = e^{x}`, and the left side is exactly `d/dx(e^{2x}y)` — *that* is what the integrating factor buys you, it collapses two terms into one product-rule derivative. Integrate: `e^{2x}y = e^x + C` → `y = e^{-x} + Ce^{-2x}`. With `y(0)=0`: `C = −1`. **`y = e^{-x} − e^{-2x}`.**

**B2.** `μ = e^{∫(1/x)dx} = x`. → `(xy)' = x²` → `xy = x³/3 + C` → `y = x²/3 + C/x`. With `y(1)=1/3`: `C=0`. **`y = x²/3`.**

**B3.** `V(r − g) = c` → **`V = c/(r−g)`**. As `g→r` the value diverges: a cashflow growing as fast as you discount it never shrinks in present-value terms, so the infinite sum doesn't converge. Financially sensible — and it is exactly why the Gordon growth model breaks when analysts assume perpetual growth near the discount rate.

**B4.** `2x + 2y·(dy/dx) = 0` → `dy/dx = −x/y` = **`−3/4`** at (3,4). Radius slope is `4/3`; `(−3/4)(4/3) = −1`. ✓

**B5.** `L = xy − λ(x+y−10)` → `y = λ`, `x = λ` → `x = y = 5`, **max = 25**. General result: among rectangles of fixed perimeter, the square has maximum area.

**B6.** New constraint `x+y=1.1` → `x=y=0.55` → min `= 2(0.55²) = 0.605`. Change `= 0.605 − 0.5 = 0.105 ≈ λ × 0.1 = 0.1`. (Not exact — `λ` is the *instantaneous* rate of change, so it's first-order accurate; the 0.005 is the quadratic term.) **Shadow price:** `λ` tells you how much the objective worsens per unit of constraint tightening — to a PM, "how many bps of variance does one more unit of required return cost me."

**B7.** `dV/V = r(t)dt` → `ln V = ∫₀ᵗ r(s)ds + C` → **`V(t) = V₀exp(∫₀ᵗ r(s)ds)`**. Inverting gives the discount factor `exp(−∫r)`. Constant `r` collapses it to `e^{rt}` — the familiar case is just the special case.

</details>

<details>
<summary>Tier C</summary>

**C1.** `N(t) = K / (1 + (K/N₀ − 1)e^{−rt})`. S-shaped: near-exponential at small `N`, inflection at `N = K/2`, saturating at `K`.

**C2.** `L = ½wᵀΣw − λ(wᵀ1 − 1)` → `Σw = λ1` → `w = λΣ⁻¹1`, and `λ = 1/(1ᵀΣ⁻¹1)` from the constraint. So **`w* = Σ⁻¹1 / (1ᵀΣ⁻¹1)`**. For the given `Σ`: `Σ⁻¹1 ∝ [0.08, 0.03]/0.0035`, normalizing → **`w* ≈ [0.727, 0.273]`**. Sanity check: the lower-variance asset (0.04 vs 0.09) gets the larger weight. ✓

**C3.** Varies by which you pick — log your two in the Feynman note.

</details>
