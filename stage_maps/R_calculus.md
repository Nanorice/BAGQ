---
type: stage
id: R.calculus
name: Calculus Refresher
topic: "[[VIII-1-ordinary-differential-equations]]"
concepts: ["[[itos-lemma]]"]
roles: ["[[options-pricing]]"]
sprint: S15
status: ready-for-test
est_h: 4
actual_h: 5.0
---

# Calculus Refresher

**Source:** Green Book (Zhou) §2.2 "Calculus" — the ODE subsection — and §2.3 "Optimization" for
the worked Lagrange examples.

**If a concept will not land from the page:** 3Blue1Brown *Essence of Calculus* Ch. 5
("What's so special about Euler's number e?") is literally `dy/dx = y` drawn out. One video, as a
fallback, not as part of the main path.

**Estimated: 4h.**

> This stage originally listed seven sources across three media, and choosing between them cost
> more time than studying did. One source, one fallback — that change is why the next refresher
> landed in a single day.

---

## What this covers

Four things, and the first one gates everything downstream — geometric Brownian motion, mean
reversion, discounting, Feynman-Kac all reduce to `dy/dx ∝ y`.

1. **Separable ODEs** — including `dy/dx = y`, the most canonical ODE there is
2. **Linear first-order ODEs** via integrating factor
3. **Chain rule and implicit differentiation**
4. **Lagrange multipliers** — and the shadow-price reading of `λ`, which is how mean-variance
   optimisation is actually derived

**Not here:** PDEs, Riccati equations, Carr-Madan, Euler-Lagrange, KKT conditions. They are in the
full inventory but not in this refresher, and each returns with the stage that needs it.

---

## Knowledge checklist — tick when you can produce it cold

**Separable equations**
- [x] `dy/dx = y` → `y = Ae^x`, and why the integration constant becomes multiplicative
- [x] `dy/dx = ky` → `y = y₀e^{kx}`, and what that means for continuous compounding
- [x] The mean-reverting form `dx/dt = κ(θ−x)` and its solution `θ + (x₀−θ)e^{−κt}`
- [x] Why it converges to `θ` for any `κ>0`, regardless of the starting point

**Linear first-order**
- [x] The integrating factor `μ(x) = e^{∫p dx}`, and **what multiplying by it does** — it collapses
      the left side into a single product-rule derivative
- [x] Time-varying rates: `dV/dt = r(t)V` → `V₀exp(∫r)`, which is the discount factor

**Chain rule and implicit differentiation**
- [x] Differentiating composed exponentials and logs, naming the rule at each step
- [x] Implicit differentiation on a constraint curve, and checking the result geometrically

**Lagrange multipliers**
- [x] Setting up `L = f − λ(g − c)` and solving the stationarity conditions
- [x] **`λ` is the shadow price** — the rate at which the optimum improves as the constraint
      relaxes, to first order
- [x] Why `∇f` and `∇g` must be parallel at a constrained optimum

---

## Problems

### Tier A — the floor. All six, unhinted, on paper.

**A1.** Solve `dy/dx = y` with `y(0) = 1`. Show every step of the separation, including where the
constant of integration goes and why it becomes a multiplicative constant.

**A2.** Solve `dy/dx = ky` with `y(0) = y₀`, for constant `k`. Then state in one sentence what this
means when `y` is a bank balance and `k` is a continuously-compounded interest rate.

**A3.** Solve `dy/dx = xy` with `y(0) = 1`. Note where the answer differs in *shape* from A1 and
say why the `x` on the right changes the exponent.

**A4.** Differentiate `f(x) = e^{3x²}`, then `g(x) = ln(cos x)`. Name which rule you used at each
step.

**A5.** Minimise `f(x,y) = x² + y²` subject to `x + y = 1` using Lagrange multipliers. Give `x*`,
`y*`, the minimum value, and `λ`.

**A6.** Solve the mean-reverting ODE `dx/dt = κ(θ − x)` with `x(0) = x₀`. Show that `x(t) → θ` as
`t → ∞` regardless of `x₀`, provided `κ > 0`.

*The deterministic skeleton of Ornstein-Uhlenbeck. You will meet it again in every mean-reversion
strategy you ever backtest.*

### Tier B — the target. At least four.

**B1.** Solve `y' + 2y = e^{-x}` with `y(0) = 0` using an integrating factor. State the factor
explicitly and say why `μ(x) = e^{∫p dx}` is the right choice — **what does multiplying by it do**
to the left-hand side?

**B2.** Solve `y' + (1/x)y = x` for `x > 0`, with `y(1) = 1/3`.

**B3.** A perpetuity pays continuously at rate `c`, growing at `g`, discounted at `r > g`. Its
present value satisfies `rV − gV = c`. Derive `V = c/(r−g)`. Then explain in one sentence what
happens as `g → r`, and why that is financially sensible rather than a mathematical accident.

**B4.** Given `x² + y² = 25`, find `dy/dx` at `(3, 4)` by implicit differentiation. Verify
geometrically — the tangent to a circle is perpendicular to the radius, so the slopes multiply
to `−1`.

**B5.** Maximise `f(x,y) = xy` subject to `x + y = 10`. State the general result this special case
illustrates about rectangles of fixed perimeter.

**B6.** In A5 you found `λ`. Change the constraint to `x + y = 1.1` and re-solve. Compare the
change in the minimum to `λ × 0.1`. **Write one sentence on what the shadow price means to a
portfolio manager.**

**B7.** Solve `dV/dt = r(t)V` with `V(0) = V₀` for a *time-varying* rate. Show
`V(t) = V₀ exp(∫₀ᵗ r(s)ds)`, and say why this justifies the discount factor `exp(−∫r)` that
appears throughout fixed income.

### Tier C — only if A and B ran short.

**C1.** Solve the logistic ODE `dN/dt = rN(1 − N/K)` with `N(0) = N₀`. *(Separable, then partial
fractions.)* Sketch the S-curve.

**C2.** *Two-asset minimum variance.* Minimise `½wᵀΣw` subject to `wᵀ1 = 1` for
`Σ = [[0.04, 0.01], [0.01, 0.09]]`. Set up the Lagrangian, solve for `w*`, confirm the weights sum
to one.
*The single most-asked Lagrange application in a quant interview.*

---

## Code problems

**None this stage.** One numerical check belongs inline in the note rather than in a file: solve
A1 by hand, then verify with a three-line Euler scheme that it lands on `e¹ ≈ 2.71828` at `x = 1`.

---

## Deliverables

**Feynman note** — `progress/feynman_notes/R_calculus.md`
- [ ] Teach-back for all four topics, source closed
- [ ] The numerical check above, worked into the note
- [ ] Any `⚠️ GAP` logged

**Problems**
- [ ] A1–A6 unhinted, on paper
- [ ] At least four from Tier B
- [ ] Log which needed hints

**Unlock test** — one week after close.

---

**When it gets hard and you start drifting:** stop reading, write the sentence you can't finish
into the note as a `⚠️ GAP`, and switch to Tier A on paper. **For ODEs specifically, separate the
variables and integrate before you understand why** — the mechanics land first and the meaning
follows, not the other way round.

**If the day collapses, do A1 and A5.** A1 is the exponential ODE that gates everything
downstream; A5 is Lagrange, which is how portfolio optimisation is derived.

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
