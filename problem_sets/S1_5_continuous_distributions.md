# Continuous Distributions — Problem Set
`stage: S1.5` · **Sprint 16, Days 3–4 + 6 (Wed 08-05, Thu 08-06, Sat 08-08)** · **Budget: 6h, two passes**

> **Re-planned 2026-08-03.** Originally a 3h single-day stage; carried over from S15 unstarted.
> `S1.3` ran 6h against a 3h budget on the same one-source design — the finding was that
> **new probability material needs two passes, not one**. This stage is now sized at 2× and the
> second pass is scheduled, not improvised. See the S15 retro.

**Why this stage exists:** baseline I.3 asked for `E[X]` and `Var(X)` of `Exp(λ)` and got `e^λ`
and `0`. Correct: `1/λ` and `1/λ²`. This is the **mandatory-deep** item of the pair — the
exponential is the waiting time between Poisson arrivals (you built that bridge in S1.3-B3), the
building block of the Poisson process, and the first hitting-time distribution you meet in S4.
The normal is downstream of everything: CLT, Black-Scholes, MVN, every regression residual.

**Scope — three distributions:**
1. **Uniform** — the atom, and the inverse-transform engine for simulation
2. **Exponential** — memorylessness, hazard rate, the Poisson link
3. **Normal** — standardisation, the 68/95/99.7 anchors, why it is everywhere

For each: **PDF · CDF · E[X] · Var(X) · MGF · one classic problem.**

Out of scope: log-normal (S6, with Black-Scholes), χ² (S9.2, with hypothesis testing), Gamma
and Beta beyond a mention, and the *proof* of the CLT (S1.8). Joint/bivariate normal is S1.6 —
today is one variable at a time.

---

## Source — one book, one sitting

| Source | Covers | Time |
|---|---|---|
| **Ross, *A First Course in Probability* 6th ed. — Ch. 5** | All three, plus the normal approximation | **40 min, hard stop** |

Navigate by heading. Ross does uniform, then normal, then exponential. **Skip the Gamma, Beta,
Cauchy, and Weibull subsections** — same chapter, not this stage. Do read the
normal-approximation-to-binomial passage; it connects straight back to yesterday.

**If the normal's `E[X²]` integral is the sticking point,** the single named fallback is
**3Blue1Brown, "Why π is there and why it's squared (Gaussian integral)", 12 min**. That is the
*only* video in this stage.

**Input cap: 40 min.**

---

## The two-pass shape

Three distributions across two study days, split by *difficulty*, not by page count. Uniform and
exponential are Pass 1 because they are where baseline I.3 lives; the normal is harder and gets
its own pass with a fresh head.

| Pass | When | Scope | Do | Out |
|---|---|---|---|---|
| **1** | **Wed 08-05, 2.5h** | **Uniform + Exponential** | Read Ch.5 uniform + exponential subsections (40 min cap) → close book → §1 teach-back for those two → A1, A2 on paper | §1(a)(b) drafted · A1–A2 done |
| **2** | **Thu 08-06, 2.5h** | **Normal** + re-read | **Start by re-reading only what Pass 1 didn't stick** (≤20 min, look at your `⚠️ GAP` list first) → normal subsection (40 min cap) → §1(c) → A3, A4, A5 | §1 complete · A3–A5 done |
| **3** | **Sat 08-08, 3h** | close | Gap-hunt §1 · Tier B (≥3) · §3–§6 · summary table · MC verifier · unlock test I.3 | Note closed |

Note skeleton: `progress/feynman_notes/S1_5_continuous_distributions.md`

**When it gets hard and you start drifting** — that is the S1.3 failure mode, and it has a move
now: **stop reading, write the sentence you can't finish into §2 as a `⚠️ GAP`, and switch to
Tier A on paper.** Paper problems survive low focus; re-reading the same paragraph does not.
Drifting means input is exhausted for this sitting, not that you need more discipline.

**If a pass collapses: A2, A3, B1 only.** A2/A3 are baseline I.3 itself. B1 (memorylessness) is
the interview one-liner and the direct continuation of S1.3-B2.

**This stage is not cuttable.** It was the designated cut in S15 and it got cut — which is why
baseline I.3 is still open eight days later. It is one of two red-flag items in the whole
probability block.

---

## Tier A — the floor (all five, unhinted, on paper)

**S1.5-A1.** `X ~ Uniform(a,b)`. Write the PDF and CDF. Derive `E[X] = (a+b)/2` and
`Var(X) = (b−a)²/12`. Then: **inverse transform** — show that if `U ~ Uniform(0,1)` and `F` is a
continuous strictly-increasing CDF, then `F⁻¹(U)` has CDF `F`.
*That last part is how every Monte Carlo sampler you will ever write gets started, including
tonight's verifier.*

**S1.5-A2.** `X ~ Exp(λ)`, PDF `f(x) = λe^{−λx}` for `x ≥ 0`. Derive the CDF, then
`E[X] = 1/λ` and `Var(X) = 1/λ²`. Do `E[X]` by parts, then again via the tail formula
`E[X] = ∫₀^∞ P(X > x)dx` — and say which you would rather do under interview pressure.
*This is baseline I.3, scored 1. It is the reason this stage is mandatory-deep.*

**S1.5-A3.** Derive the MGF of `Exp(λ)`. State the `t` range where it exists and say what goes
wrong outside it. Recover `E[X]` and `Var(X)` from it and check against A2.
*The existence condition `t < λ` is not a technicality — it is the fingerprint of a distribution
with exponential tails, and it is why the MGF approach fails for heavy-tailed things you will
meet in risk work.*

**S1.5-A4.** `Z ~ N(0,1)`. Write the PDF. Show `E[Z] = 0` by symmetry, and derive
`Var(Z) = E[Z²] = 1` by parts. Then: `X = μ + σZ` — derive the PDF of `X` by the
change-of-variables rule and confirm `E[X] = μ`, `Var(X) = σ²`.
*Standardisation `Z = (X−μ)/σ` is the move that reduces every normal question to a table lookup.
Do it in this direction once and it stops being magic.*

**S1.5-A5.** State the 68/95/99.7 rule. Then compute `P(|Z| > 2)` and `P(Z > 1.645)` from
memory, and say what the second number is used for.
*Numerical anchors you should be able to produce cold. `1.645` is the 95% one-tail critical
value; `1.96` is the 95% two-tail. Mixing them up is a classic interview stumble and a classic
production bug in a VaR calculation.*

---

## Tier B — the target (≥3 of 5)

**S1.5-B1.** Prove the exponential is **memoryless**: `P(X > s+t | X > s) = P(X > t)`. Then
prove the converse *(sketch is fine)*: the exponential is the **only** continuous distribution
with this property.
*Compare line by line with S1.3-B2, which you did yesterday for the geometric. Same theorem,
continuous setting. Then say what memorylessness implies for a component that has already
survived 5 years — and why that is a bad model for most physical parts and a decent one for
"time until the next trade".*

**S1.5-B2.** Complete the Poisson–exponential bridge from S1.3-B3: if arrivals follow a Poisson
process with rate `λ`, show the waiting time to the first arrival is `Exp(λ)`.
*One line: `P(T > t) = P(no arrivals in [0,t]) = e^{−λt}`. Then say what the gap between the
`k`-th and `(k+1)`-th arrival is distributed as, and why the answer needs memorylessness.*

**S1.5-B3.** The **hazard rate** `h(x) = f(x)/(1−F(x))` is the instantaneous failure rate given
survival to `x`. Compute it for `Exp(λ)`. What is special about the answer, and how does it
relate to B1?
*Constant hazard ↔ memoryless ↔ exponential — three names for one fact. Hazard rates are the
native language of credit default modelling and of survival analysis.*

**S1.5-B4.** `X ~ Exp(λ₁)` and `Y ~ Exp(λ₂)` independent. Show `min(X,Y) ~ Exp(λ₁+λ₂)`, and
compute `P(X < Y)`.
*The competing-risks result. It is how you model "which of these two events happens first" —
first to fill, first to default, first to arrive. Both answers are short and worth memorising.*

**S1.5-B5.** Use the normal approximation to the binomial: 10,000 fair coin flips, estimate
`P(more than 5,100 heads)`. State the mean and SD of the binomial first, then standardise.
*Connects straight to yesterday's A1/A2. Also note the continuity correction and say whether it
matters at this scale.*

---

## Tier C — only if A+B ran short

**S1.5-C1.** `X ~ Exp(λ)`. Derive the distribution of `Y = ⌈X⌉` (round up to the next integer).
*It is geometric. Yesterday's distribution falls out of today's — the two memoryless
distributions are the same object at two resolutions.*

**S1.5-C2.** Derive the Gaussian integral `∫_{−∞}^{∞} e^{−x²/2}dx = √(2π)` via the polar-
coordinate trick. *This is where the `1/√(2π)` in the normal PDF comes from.*

---

## Deliverables

- [ ] `progress/feynman_notes/S1_5_continuous_distributions.md` — all 6 sections real, zero
      `⚠️ GAP`, napkin ≤200 words **said out loud once**
- [ ] Tier A A1–A5 unhinted, on paper
- [ ] ≥3 of 5 Tier B
- [ ] **Summary table in the note** — three rows × six columns (PDF, CDF, E[X], Var, MGF,
      the one fact that matters). Sits directly under yesterday's discrete table.
- [ ] **MC verifier — ONE file covering S1.3 + S1.5** (S1.3's was deferred here):
      `src/solvers/s1_probability/distributions_verify.py`, ~30 lines. Creates `src/solvers/`.
      - S1.3: geometric `E[X] = 1/p` · two-heads-in-a-row `E = 6` (baseline II.1)
      - S1.5: sample `Exp(λ)` via **inverse transform** (A1) — *not* `np.random.exponential`,
        the point is to use A1 — check mean/var against `1/λ`, `1/λ²`
      - S1.5: normal check against the 68/95/99.7 rule
      - Docstring with time + space complexity, per baseline adjustment #9. One `assert`-based
        `__main__` self-check; no test framework yet.
- [ ] **Unlock test:** re-answer baseline I.3 cold (`E` and `Var` of `Exp(λ)`), fully correct.

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

**A3.** `M(t) = E[e^{tX}] = ∫₀^∞ e^{tx}λe^{−λx}dx = λ∫₀^∞ e^{−(λ−t)x}dx = **λ/(λ−t)**, for `t < λ`.

Outside that range the integral **diverges** — the integrand `e^{(t−λ)x}` grows without bound.
The MGF simply does not exist for `t ≥ λ`. This is the fingerprint of exponential tails: the MGF
exists in a neighbourhood of 0 but not everywhere. **Heavy-tailed distributions (log-normal,
Cauchy, power-law) have no MGF on any interval around 0** — which is exactly why MGF-based
arguments quietly fail in risk work, and why you reach for characteristic functions instead.

`M'(t) = λ/(λ−t)²` → `M'(0) = **1/λ**` ✓
`M''(t) = 2λ/(λ−t)³` → `M''(0) = 2/λ² = E[X²]` → `Var = 2/λ² − 1/λ² = **1/λ²**` ✓

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
exactly the structure you saw in T0.C when `dy/dx = y` forced the exponential.)*

*Meaning:* a component that has survived 5 years has the **same** remaining-life distribution as
a new one. For physical parts that is wrong — they wear out, hazard increases, and you want a
Weibull. For "time until the next trade arrives" in a liquid book it is a reasonable first
model, because arrivals are driven by a fresh stream of independent decisions rather than by
accumulated fatigue. Compare S1.3-B2: **geometric is memoryless in discrete time, exponential in
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
