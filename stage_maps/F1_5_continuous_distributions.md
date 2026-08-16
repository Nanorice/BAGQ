---
type: stage
id: F1.5
name: Continuous Distributions
topic: "[[I-5-continuous-random-variables-and-distributions]]"
concepts: ["[[memorylessness]]", "[[standardisation]]", "[[change-of-variables]]", "[[poisson-exponential-duality]]"]
roles: ["[[market-making]]", "[[risk-management]]", "[[options-pricing]]"]
sprint: S16
status: ready-for-test
est_h: 6
actual_h: 5.0
---

# Continuous Distributions

**Source:** Ross, *A First Course in Probability* 6th ed. — Ch. 5, §5.1–§5.7.

**Estimated: 6h.** *(Sized at 2× from the start, after discrete distributions ran 6h against a 3h
budget on the same one-source design. The finding was that new probability material needs two
passes, not one — so the second pass is scheduled here rather than improvised.)*

---

## What this covers

Three distributions, and the machinery that connects them to everything downstream.

1. **Uniform** — the atom, and the inverse-transform engine for simulation
2. **Exponential** — memorylessness, hazard rate, the Poisson link
3. **Normal** — standardisation, the 68/95/99.7 anchors, and why it is everywhere

For each: PDF, CDF, `E[X]`, `Var(X)`, one classic problem.

The exponential is the waiting time between Poisson arrivals — the bridge built in discrete
distributions — the building block of the Poisson process, and the first hitting-time
distribution you will meet in stochastic processes. The normal is downstream of everything: the
central limit theorem, Black-Scholes, every regression residual.

**Not here:** the log-normal (arrives with Black-Scholes), chi-squared (with hypothesis testing),
Gamma and Beta beyond a mention, and the *proof* of the central limit theorem. Bivariate normal
comes with joint distributions — this is one variable at a time.

---

## Knowledge checklist — tick when you can produce it cold

Built from Ross Ch.5's real section headings, verified against the book. Tick during the close
block, not while reading. **Anything still unticked at close is what the unlock test targets.**

**§5.1–5.2 Density and expectation**
- [x] Density: `P(a≤X≤b) = ∫f`, and why `P(X=a) = 0`
- [x] `E[X] = ∫xf(x)dx` · `Var(X) = E[X²] − E[X]²`
- [ ] **Tail formula `E[X] = ∫₀^∞ P(X>x)dx`** — *Lemma 2.1*. Works for any non-negative RV,
      and it beats by-parts under pressure. Discrete twin: `E[X] = Σ P(X≥k)`.

**§5.3 Uniform**
- [x] PDF · CDF on `[a,b]`
- [x] `E[X] = (a+b)/2` · `Var(X) = (b−a)²/12`

**§5.4 Normal**
- [ ] PDF, and where the `1/√(2π)` comes from
- [x] `E[Z]=0` by symmetry · `Var(Z)=1` by parts
- [x] Standardisation `Z = (X−μ)/σ` — reduces every normal question to one table
- [ ] 68 / 95 / 99.7
- [x] **1.645 one-tail vs 1.96 two-tail** (the VaR-bug pair)
- [x] **§5.4.1** Normal approximation to the binomial (de Moivre–Laplace) + continuity correction
- [x] …and when Poisson is the right limit instead (`p→0`, `np` fixed) vs Normal (`p` fixed)

**§5.5 Exponential**
- [x] PDF · CDF · tail `P(X>x) = e^{−λx}`
- [x] `E[X] = 1/λ` · `Var(X) = 1/λ²` ← **baseline I.3, the reason this stage is mandatory-deep**
- [ ] `SD = mean` — why "average wait 5 min" says less than people assume
- [x] **Memorylessness** `P(X>s+t | X>s) = P(X>t)`, + that exponential is the *only* continuous one
- [x] **§5.5.1** Hazard rate `h(x) = f(x)/(1−F(x))`; constant hazard ⟺ memoryless ⟺ exponential

**§5.7 Function of a random variable**
- [x] Change-of-variables rule for `Y = g(X)`
- [ ] **Inverse transform**: `F⁻¹(U) ~ F`, and the one-line proof
- [ ] `F⁻¹` for the exponential → `X = −ln(U)/λ` *(this is what makes the sampling solver possible)*

**Cross-cutting**
- [x] Geometric → exponential is the discrete → continuous memoryless pair
- [x] Poisson counts ↔ exponential gaps — same process, two descriptions

### Stretch — not in Ross Ch.5

*A stretch item is never left as a bare pointer. It is written inline below, given a named chapter
in a book you own, or deferred with the reason.*

- [ ] **Competing risks** — `min(X,Y) ~ Exp(λ₁+λ₂)` and `P(X<Y) = λ₁/(λ₁+λ₂)`
      → **written inline below.** Five lines, needs only independence, and it is first-to-fill,
      first-to-default, first-to-arrive. Too useful to defer.
- [ ] **MGF of `Exp(λ)`** = `λ/(λ−t)`, existing only for `t < λ`
      → **deferred**, because *using* MGFs needs convolution machinery this stage does not build.
      The definition is below so the term is not foreign when it lands.
- [ ] **Gaussian integral** `∫e^{−x²/2}dx = √(2π)` by polar coordinates
      → **Tier C, optional.** Ross states the constant; the derivation is the stretch.

---

## Stretch notes

Short by design — these exist so a stretch item is learnable *in this stage* rather than becoming
a to-do that resolves three months out.

### Competing risks (inline — do this in the Saturday close block)

Two independent exponential clocks, `X ~ Exp(λ₁)` and `Y ~ Exp(λ₂)`. Which rings first, and when?

**When:** the minimum is exponential with the rates *added*.
```
P(min(X,Y) > t) = P(X>t)·P(Y>t)        ← independence, and only here
                = e^{−λ₁t}·e^{−λ₂t}
                = e^{−(λ₁+λ₂)t}         ← survival function of Exp(λ₁+λ₂)
```
Generalises directly: `n` independent clocks → first to ring is `Exp(Σλᵢ)`. **Rates add.**

**Which:** condition on when `X` fires and ask that `Y` hasn't yet.
```
P(X<Y) = ∫₀^∞ P(Y>x)·λ₁e^{−λ₁x}dx = ∫₀^∞ λ₁e^{−(λ₁+λ₂)x}dx = λ₁/(λ₁+λ₂)
```
The faster clock wins in proportion to its rate — and notice the answer doesn't depend on `t` at
all. *Why it matters:* first-to-fill across venues, first-to-default in a basket, next-arrival
among order types. Both results are short enough to memorise and are asked directly.

### MGF — the definition only (so the term isn't cold in the generating-functions stage)

`M(t) = E[e^{tX}]`. It is a **transform**: one function that encodes every moment, because
`M'(0) = E[X]`, `M''(0) = E[X²]`, and so on. The reason it earns its keep is that the MGF of a
sum of independents is the *product* of their MGFs — it turns convolution (hard) into
multiplication (easy). For `Exp(λ)` it is `λ/(λ−t)` and it **only exists for `t < λ`**; beyond
that the integral diverges. That existence range is the fingerprint of exponential tails, and its
absence is why MGF arguments fail on heavy-tailed distributions.

**Do not derive anything from this today.** It is here so the word is familiar. the generating-functions stage is where it
does work.

---

## Problems

### Tier A — the floor. All five, unhinted, on paper.

**A1.** `X ~ Uniform(a,b)`. Write the PDF and CDF. Derive `E[X] = (a+b)/2` and
`Var(X) = (b−a)²/12`. Then: **inverse transform** — show that if `U ~ Uniform(0,1)` and `F` is a
continuous strictly-increasing CDF, then `F⁻¹(U)` has CDF `F`.
*That last part is how every Monte Carlo sampler you will ever write gets started, including
tonight's verifier.*

**A2.** `X ~ Exp(λ)`, PDF `f(x) = λe^{−λx}` for `x ≥ 0`. Derive the CDF, then
`E[X] = 1/λ` and `Var(X) = 1/λ²`. Do `E[X]` by parts, then again via the tail formula
`E[X] = ∫₀^∞ P(X > x)dx` — and say which you would rather do under interview pressure.
*This is baseline I.3, scored 1. It is the reason this stage is mandatory-deep.*

**A3.** *(§5.7)* `X ~ Exp(λ)`. Derive the distribution of `Y = √X` by the
change-of-variables rule: write `F_Y(y) = P(Y≤y) = P(X≤y²)`, then differentiate.
Then state the general rule for `Y = g(X)` with `g` monotone, and say **why the `|dx/dy|` factor
has to be there** — what would go wrong without it.
*§5.7 is the engine behind both the inverse transform (A1) and the normal's `X = μ+σZ` (A4).
Doing it once explicitly means those two stop being separate tricks.*

*Replaced the original A3 (derive the MGF of `Exp(λ)`) on 2026-08-09: MGFs are Ross **Ch.7**, not
Ch.5 — the same out-of-chapter mismatch that made `F1.4`-A5 unanswerable. The MGF definition is
in the stretch notes; deriving anything from it belongs to the generating-functions stage.*

**A4.** `Z ~ N(0,1)`. Write the PDF. Show `E[Z] = 0` by symmetry, and derive
`Var(Z) = E[Z²] = 1` by parts. Then: `X = μ + σZ` — derive the PDF of `X` by the
change-of-variables rule and confirm `E[X] = μ`, `Var(X) = σ²`.
*Standardisation `Z = (X−μ)/σ` is the move that reduces every normal question to a table lookup.
Do it in this direction once and it stops being magic.*

**A5.** State the 68/95/99.7 rule. Then compute `P(|Z| > 2)` and `P(Z > 1.645)` from
memory, and say what the second number is used for.
*Numerical anchors you should be able to produce cold. `1.645` is the 95% one-tail critical
value; `1.96` is the 95% two-tail. Mixing them up is a classic interview stumble and a classic
production bug in a VaR calculation.*

---

### Tier B — the target. At least three.

**B1.** Prove the exponential is **memoryless**: `P(X > s+t | X > s) = P(X > t)`. Then
prove the converse *(sketch is fine)*: the exponential is the **only** continuous distribution
with this property.
*Compare line by line with the geometric memorylessness proof. Same theorem,
continuous setting. Then say what memorylessness implies for a component that has already
survived 5 years — and why that is a bad model for most physical parts and a decent one for
"time until the next trade".*

**B2.** Complete the Poisson–exponential bridge: if arrivals follow a Poisson
process with rate `λ`, show the waiting time to the first arrival is `Exp(λ)`.
*One line: `P(T > t) = P(no arrivals in [0,t]) = e^{−λt}`. Then say what the gap between the
`k`-th and `(k+1)`-th arrival is distributed as, and why the answer needs memorylessness.*

**B3.** The **hazard rate** `h(x) = f(x)/(1−F(x))` is the instantaneous failure rate given
survival to `x`. Compute it for `Exp(λ)`. What is special about the answer, and how does it
relate to B1?
*Constant hazard ↔ memoryless ↔ exponential — three names for one fact. Hazard rates are the
native language of credit default modelling and of survival analysis.*

**B4.** ⚡ *stretch — not in Ch.5; material is in §Stretch notes above.*
`X ~ Exp(λ₁)` and `Y ~ Exp(λ₂)` independent. Show `min(X,Y) ~ Exp(λ₁+λ₂)`, and compute `P(X<Y)`.
**Attempt it cold first** — you have every tool needed (the tail `e^{−λt}` and independence).
Read the stretch note only after you've tried, or when you're stuck.
*Competing risks: which of two events happens first — first to fill, first to default, first to
arrive. Both answers are one line and both get asked directly.*

**B5.** Use the normal approximation to the binomial: 10,000 fair coin flips, estimate
`P(more than 5,100 heads)`. State the mean and SD of the binomial first, then standardise.
*Connects straight to yesterday's A1/A2. Also note the continuity correction and say whether it
matters at this scale.*

---

### Tier C — only if A and B ran short.

**C1.** `X ~ Exp(λ)`. Derive the distribution of `Y = ⌈X⌉` (round up to the next integer).
*It is geometric. Yesterday's distribution falls out of today's — the two memoryless
distributions are the same object at two resolutions.*

**C2.** Derive the Gaussian integral `∫_{−∞}^{∞} e^{−x²/2}dx = √(2π)` via the polar-
coordinate trick. *This is where the `1/√(2π)` in the normal PDF comes from.*

---

---

## Code problems

Both live in `code/codify.ipynb` under `# Distributions`, shared with discrete distributions.
Standard library only, no test framework.

### 1 · Sampling an exponential by inverse transform

Draw from `Exp(λ)` using only `random.random()` — no `numpy.random.exponential`.

> **Input:** rate `λ > 0`, number of samples
> **Output:** draws from `Exp(λ)`
> **Method:** if `U ~ Uniform(0,1)` then `X = −ln(U)/λ ~ Exp(λ)`. Invert the CDF yourself.
> **Verify:** sample mean ≈ `1/λ` and sample variance ≈ `1/λ²`, within tolerance.

*The inverse-CDF derivation is what makes the sampler exist. Calling a library sampler proves
nothing about whether you can derive one.*

### 2 · The normal's 68/95/99.7 anchors

> **Input:** number of samples
> **Output:** the empirical fraction of `N(0,1)` draws within `±1σ`, `±2σ`, `±3σ`
> **Verify:** those fractions are `≈ 0.68`, `0.95`, `0.997`.

*The cheapest possible check that the anchors you recite are real numbers and not memorised
noise.*

**Tolerance:** pick the sample count so the standard error is comfortably under the assert
threshold, and say in a comment what you chose and why. A flaky assert is worse than none.

---

## Deliverables

**Feynman note** — `progress/feynman_notes/F1_5_continuous_distributions.md`
- [ ] Teach-back for all three distributions, source closed
- [ ] Summary table: one row per distribution — PDF, CDF, `E[X]`, `Var(X)`, and the classic problem
- [ ] Any `⚠️ GAP` logged

**Problems**
- [ ] A1–A5 unhinted, on paper
- [ ] At least three from Tier B
- [ ] Log which needed hints

**Code** — both problems asserting, with complexity docstrings.

**Unlock test** — one week after close.

---

**When it gets hard and you start drifting:** stop reading, write the sentence you can't finish
into the note as a `⚠️ GAP`, and switch to Tier A on paper. **For these three specifically, sketch
the density and shade the probability you are being asked for** — most continuous-distribution
confusion is about which region the integral covers, and a shaded sketch settles it faster than
re-reading the formula.

**If the day collapses, do A1 and A3.** A1 is the tail formula, which shortcuts half the
expectation questions you will meet; A3 is the exponential's mean and variance.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** PDF `f(x) = 1/(b−a)` on `[a,b]`. CDF `F(x) = (x−a)/(b−a)` on `[a,b]`, 0 below, 1 above.
`E[X] = ∫ₐᵇ x/(b−a)dx = (b²−a²)/(2(b−a)) = **(a+b)/2**`.
`E[X²] = (b³−a³)/(3(b−a)) = (a²+ab+b²)/3`, so
`Var = (a²+ab+b²)/3 − (a+b)²/4 = **(b−a)²/12**`.

*Inverse transform:* let `Y = F⁻¹(U)`. Then
`P(Y ≤ y) = P(F⁻¹(U) ≤ y) = P(U ≤ F(y)) = F(y)`, the last step because `U` is uniform on `[0,1]`
and `F(y) ∈ [0,1]`. So `Y` has CDF `F`. ∎
**This is the entire foundation of sampling by inversion.** For `Exp(λ)`:
`F(x) = 1−e^{−λx}`, so `F⁻¹(u) = −ln(1−u)/λ`, and since `1−U` is also uniform,
`X = −ln(U)/λ`. That one line is tonight's verifier.

**A2.** CDF: `F(x) = ∫₀ˣ λe^{−λs}ds = **1 − e^{−λx}**` for `x ≥ 0`. Tail: `P(X > x) = e^{−λx}`.

*By parts:* `E[X] = ∫₀^∞ xλe^{−λx}dx`; take `u = x`, `dv = λe^{−λx}dx`:
`= [−xe^{−λx}]₀^∞ + ∫₀^∞ e^{−λx}dx = 0 + 1/λ = **1/λ**`.

*Tail formula:* `E[X] = ∫₀^∞ P(X > x)dx = ∫₀^∞ e^{−λx}dx = **1/λ**`. One line, no parts.
**Take the tail formula under pressure** — it works for any non-negative RV and it is the same
trick as the discrete `E[X] = Σ P(X ≥ k)`.

`E[X²] = ∫₀^∞ x²λe^{−λx}dx = 2/λ²` (parts twice, or `Γ(3)/λ²`), so
`Var = 2/λ² − 1/λ² = **1/λ²**`.
*Note `SD = 1/λ = E[X]`: the exponential's standard deviation equals its mean. A high-variance
distribution, which is why "average wait 5 minutes" tells you much less than people assume.*
**(Baseline I.3: `1/λ` and `1/λ²`. You wrote `e^λ` and `0`.)**

**A3.** *(§5.7 — change of variables.)* Go through the **CDF**, never the density directly.

`F_Y(y) = P(Y ≤ y) = P(√X ≤ y) = P(X ≤ y²) = F_X(y²) = 1 − e^{−λy²}` for `y ≥ 0`.
Differentiate: `f_Y(y) = **2λy·e^{−λy²}**` for `y ≥ 0`. *(That is a Rayleigh distribution.)*

*General rule*, `g` monotone with inverse `g⁻¹`:
`f_Y(y) = f_X(g⁻¹(y))·|d/dy g⁻¹(y)|`

**Why the `|dx/dy|` factor must be there:** a density is probability *per unit length*, not
probability. When `g` stretches an interval, the same probability mass is spread over a longer
interval, so the density must fall — the Jacobian is exactly that bookkeeping. Drop it and
`f_Y` won't integrate to 1. The absolute value is because a decreasing `g` flips the limits of
integration; density can't be negative.

**Where you have already used this without naming it:** the inverse transform (A1) is this rule
with `g = F⁻¹`, and `X = μ + σZ` (A4) is this rule with `g` affine — which is why the normal PDF
picks up its `1/σ`.

**A4.** `φ(z) = (1/√(2π))e^{−z²/2}`.
`E[Z] = 0`: the integrand `zφ(z)` is odd and the integral converges absolutely, so it vanishes.
*(Both conditions matter — the Cauchy has an odd integrand too, and no mean at all.)*

`E[Z²] = ∫z²φ(z)dz`. By parts with `u = z`, `dv = zφ(z)dz` (note `dv = −dφ`, since `φ'(z) = −zφ(z)`):
`= [−zφ(z)]_{−∞}^{∞} + ∫φ(z)dz = 0 + 1 = **1**`. So `Var(Z) = 1 − 0 = 1`.

*Change of variables:* `X = μ + σZ` → `z = (x−μ)/σ`, `dz/dx = 1/σ`, so
`f_X(x) = φ((x−μ)/σ)·(1/σ) = **(1/(σ√(2π)))e^{−(x−μ)²/(2σ²)}**`.
`E[X] = μ + σE[Z] = μ` ✓ `Var(X) = σ²Var(Z) = σ²` ✓ *(variance scales by the square — the
`σ²` in `Var`, `σ` in `SD`, and the reason vol scales with `√t` and not `t`.)*

**A5.** 68% within `±1σ`, 95% within `±2σ`, 99.7% within `±3σ`.
`P(|Z| > 2) = 1 − 0.9545 ≈ **0.0455**` (≈ 4.6%, the "1 in 22" tail).
`P(Z > 1.645) = **0.05**` — the **95% one-tailed** critical value.
Keep both straight: **1.645 one-tail, 1.96 two-tail**, both at 95%. `2.326` is one-tail 99%,
`2.576` two-tail 99%. A 99% one-day VaR uses `2.326`, and using `2.576` there overstates the
number by ~11%.

</details>

<details>
<summary>Tier B</summary>

**B1.** `P(X > t) = e^{−λt}`. Then
`P(X > s+t | X > s) = P(X > s+t)/P(X > s) = e^{−λ(s+t)}/e^{−λs} = e^{−λt} = P(X > t)` ∎

*Converse (sketch):* let `G(t) = P(X > t)`. Memorylessness says `G(s+t) = G(s)G(t)` for all
`s,t ≥ 0` — the **Cauchy functional equation** in multiplicative form. With `G` right-continuous,
monotone, and `G(0)=1`, the only solutions are `G(t) = e^{−λt}`. *(The proof runs: the relation
forces `G(n) = G(1)^n`, then rationals by the same argument, then all reals by continuity —
exactly the structure behind `dy/dx = y` forcing the exponential.)*

*Meaning:* a component that has survived 5 years has the **same** remaining-life distribution as
a new one. For physical parts that is wrong — they wear out, hazard increases, and you want a
Weibull. For "time until the next trade arrives" in a liquid book it is a reasonable first
model, because arrivals are driven by a fresh stream of independent decisions rather than by
accumulated fatigue. **Geometric is memoryless in discrete time, exponential in
continuous time, and they are the only two.**

**B2.** `P(T > t) = P(zero arrivals in [0,t])`. For a Poisson process with rate `λ`, the count in
a window of length `t` is `Poisson(λt)`, so `P(N(t)=0) = e^{−λt}(λt)⁰/0! = e^{−λt}`.
Hence `F_T(t) = 1 − e^{−λt}` — **`T ~ Exp(λ)`** ∎

The gap between the `k`-th and `(k+1)`-th arrival is **also `Exp(λ)`, and independent of all
previous gaps**. This needs memorylessness: at the moment of the `k`-th arrival the process
restarts with no memory of elapsed time, so the next gap is distributed exactly like the first.
**Poisson counts and exponential gaps are one process seen two ways** — counts in a window, gaps
between events. Mean gap `1/λ` and mean count `λt` are consistent: `λt` arrivals in time `t`
means one every `1/λ`.

**B3.** `h(x) = f(x)/(1−F(x)) = λe^{−λx}/e^{−λx} = **λ**`. **Constant** — independent of `x`.

The instantaneous failure rate never changes; surviving longer does not make you more or less
likely to fail next instant. That *is* memorylessness (B1) restated in rate form, and the
equivalence is exact: **constant hazard ⟺ memoryless ⟺ exponential**. Increasing hazard (wear-out)
→ Weibull with shape > 1; decreasing hazard (infant mortality) → shape < 1.
In credit, `λ` is the default intensity and `P(survive to t) = e^{−∫₀ᵗ h(s)ds}` — the general
form, which reduces to `e^{−λt}` when `h` is constant. That integral is the whole of
reduced-form default modelling.

**B4.** `P(min(X,Y) > t) = P(X > t)P(Y > t) = e^{−λ₁t}e^{−λ₂t} = e^{−(λ₁+λ₂)t}` — which is the
survival function of `**Exp(λ₁+λ₂)**` ∎ *(independence used in the first equality.)*
**Rates add.** `n` independent exponential clocks → the first to ring is `Exp(Σλᵢ)`.

`P(X < Y) = ∫₀^∞ P(Y > x)λ₁e^{−λ₁x}dx = ∫₀^∞ e^{−λ₂x}λ₁e^{−λ₁x}dx = λ₁/(λ₁+λ₂)`.
**`P(X < Y) = λ₁/(λ₁+λ₂)`** — the faster clock wins in proportion to its rate. Both results are
worth memorising: they are the arithmetic of competing risks, of which-venue-fills-first, and of
first-to-default baskets.

**B5.** `X ~ Bin(10000, 0.5)`: `μ = np = **5000**`, `σ = √(np(1−p)) = √2500 = **50**`.

`P(X > 5100) ≈ P(Z > (5100−5000)/50) = P(Z > 2) ≈ **0.0228**` (about 2.3%).

*Continuity correction:* use `5100.5`, giving `z = 2.01` and `P ≈ 0.0222`. The difference is
~0.0006 — **immaterial at this scale**, because the correction is worth roughly `0.5/σ = 0.01`
standard deviations. It matters when `σ` is small (small `n`, or `p` near 0 or 1), not here.
*This is de Moivre–Laplace, the CLT's first special case, and the reason a binomial with large
`n` is safe to treat as normal. It is also the sanity check on yesterday's B1: with `p = 0.5`
fixed, `n → ∞` gives you a normal, not a Poisson. Poisson needs `p → 0` with `np` held fixed.
Same limit, two different regimes — knowing which one you are in is the actual skill.*

</details>

<details>
<summary>Tier C</summary>

**C1.** `P(Y > k) = P(X > k) = e^{−λk}` for integer `k`, so
`P(Y = k) = P(X > k−1) − P(X > k) = e^{−λ(k−1)} − e^{−λk} = e^{−λ(k−1)}(1 − e^{−λ})`.
Writing `p = 1 − e^{−λ}`: `P(Y = k) = (1−p)^{k−1}p` — **`Y ~ Geometric(p)`** ∎
Yesterday's distribution is today's, sampled at integer times. Both memoryless, and the
discretisation preserves it exactly — which it would not for any other continuous distribution.

**C2.** Let `I = ∫_{−∞}^{∞}e^{−x²/2}dx`. Then
`I² = ∫∫e^{−(x²+y²)/2}dxdy`. Switch to polar: `x²+y² = r²`, `dxdy = r·drdθ`:
`I² = ∫₀^{2π}∫₀^∞ e^{−r²/2}r·drdθ = 2π·[−e^{−r²/2}]₀^∞ = 2π·1 = 2π`
So `I = **√(2π)**` ∎
The `r` from the Jacobian is what makes it integrable — the trick works in 2D and nowhere else,
which is why this identity feels like a magic trick even after you have seen it. The `1/√(2π)`
in the normal PDF is exactly the constant that makes it integrate to 1.

</details>