---
type: stage
id: F1.7
name: Expectation, Variance and Moments
topic: "[[I-7-expectation-variance-and-moments]]"
concepts: ["[[linearity-of-expectation]]", "[[tower-property]]", "[[first-step-conditioning]]", "[[jensen-inequality]]", "[[moment-generating-function]]"]
roles: ["[[signal-research]]", "[[market-making]]"]
sprint: S17
status: unlocked
est_h: 8.5
actual_h:
---

# Expectation, Variance and Moments

**Source:** `topics/section_I_probability_combinatorics.md` §7 — Core Concepts and problems 1–9.

**Backup, only if something doesn't click:** Ross, *A First Course in Probability* 6th ed.
Ch. 7 — §7.1–§7.4 and §7.7.1 for conditional expectation, §7.7 for the inequalities and the MGF
definition. Reach for it when a derivation won't land from the topic file, not by default.

**Estimated: 8.5h** — roughly 5h for parts 1–2, 3.5h for part 3.

---

## What this covers

Everything here is one idea used repeatedly: **an expectation is a weighted average, and you can
compute it by splitting the weights however is convenient.** Linearity splits over a sum, the
tower property splits over a conditioning variable, and the inequalities bound what a weighted
average can do when you only know part of the picture.

**Three natural pauses.** Stop at a part boundary if the session ends; don't stop mid-part.

**Part 1 — Linearity and LOTUS.** `E[aX+bY] = aE[X]+bE[Y]` is true whether or not `X` and `Y`
are dependent, and knowing *why* is what separates knowing the formula from knowing the fact.
LOTUS computes `E[g(X)]` directly from `X`'s distribution without ever deriving the distribution
of `g(X)` — almost always the shorter route when you only need a number.

**Part 2 — The tower property and Eve's law.** `E[X] = E[E[X|Y]]`, the general form of the law of
total probability, with expectations in place of probabilities. `E[X|Y]` is a **random variable**,
a function of `Y`, not a number — that is the sentence people cannot produce under pressure. Its
mechanical form is **first-step conditioning**: partition on the first random event, write the
conditional expectation on each branch, weight and sum. That structure is identical in every
gambler's-ruin and Markov first-passage problem you will meet later. Eve's law does the same
split for variance: within-group spread plus between-group spread of the group means.

**Part 3 — Inequalities and the MGF.** Markov, Chebyshev and Jensen are three bounds using
different amounts of information — mean only, mean and variance, convexity. Chebyshev is not a
separate result to memorise; it is Markov applied to `(X−μ)²`. Jensen applied to `x²` *is* the
statement that variance is non-negative. The MGF section is deliberately thin: the definition,
moment extraction by differentiation, and the existence caveat.

**Parts 2 and 3 meet at Eve's law and Jensen** — both say a spread term is non-negative, and both
are the same observation from different directions.

**Not here:** MGF uniqueness, convolution via the MGF product, characteristic functions,
probability generating functions. Those need the convolution theorem, which is a topic of its own.
This stage installs what an MGF *is* and how to read moments off it — enough to use one, not
enough to prove things with one.

---

## Knowledge checklist — tick when you can produce it cold

Tick at the close of a block, not while reading.

### Part 1 — Linearity and LOTUS

- [ ] `E[aX+bY] = aE[X]+bE[Y]` holds **even when `X,Y` are dependent** — say why the proof never
      uses independence (it is a property of the sum, not of the joint distribution)
- [ ] The indicator trick: write a count as a sum of `0/1` indicators, apply linearity
      term-by-term, never touch their joint distribution
- [ ] `E[g(X)] = Σ g(x)p(x)` or `∫g(x)f(x)dx` — compute on `X`'s own distribution
- [ ] When to reach for LOTUS versus deriving the distribution of `Y=g(X)` first

### Part 2 — Tower property and Eve's law

- [ ] `E[X] = E[E[X|Y]]` — state it, and say what `E[X|Y]` is: **a random variable, a function of
      `Y`**, not a number
- [ ] **First-step conditioning** — partition on the first event, write
      `E[X] = Σᵧ E[X|Y=y]P(Y=y)`, solve for the unknown
- [ ] That the tower property is the general form of the law of total probability — same
      partition-and-weight shape, expectations instead of probabilities
- [ ] `Var(X) = E[Var(X|Y)] + Var(E[X|Y])` — Eve's law
- [ ] One sentence on what each Eve's-law term means physically: within-group spread, plus
      between-group spread of the group means

### Part 3 — Inequalities and the MGF

- [ ] **Markov:** `P(X≥a) ≤ E[X]/a` for `X≥0`, `a>0` — derive it, don't quote it
- [ ] **Chebyshev:** `P(|X−μ|≥kσ) ≤ 1/k²` — derive it **from Markov**, applied to `(X−μ)²`
- [ ] **Jensen:** `E[g(X)] ≥ g(E[X])` for convex `g`, flipped for concave — with the geometric
      reason (a chord lies above the graph)
- [ ] Rank the three by how much they assume: Markov (mean only) → Chebyshev (mean and variance)
      → Jensen (convexity, no spread parameter) — and what each buys in exchange
- [ ] `M_X(t) = E[e^{tX}]`
- [ ] `M_X'(0)=E[X]`, `M_X''(0)=E[X²]`, generally `M_X^{(n)}(0)=E[X^n]` — and why
- [ ] **An MGF only exists on an interval of `t` around 0** — the exponential's `λ/(λ−t)` for
      `t<λ` as the concrete case, and what a non-existent MGF says about the tail
- [ ] Identify a distribution from its MGF by pattern-matching a known form

---

## Problems

### Tier A — the floor. All nine, unhinted, on paper.

**A1.** Prove linearity of expectation for the discrete case:
`E[X+Y] = ΣΣ(x+y)p(x,y) = Σx·p_X(x) + Σy·p_Y(y) = E[X]+E[Y]`. **State explicitly which line
would break if you tried to prove `E[XY]=E[X]E[Y]` the same way**, and why that one genuinely
needs independence while linearity does not.

*The single most commonly mis-attributed fact in probability interviews: `E[X+Y]=E[X]+E[Y]` gets
explained via independence when the real reason is that summation is linear. Pointing at exactly
which step needs independence is what separates knowing the formula from knowing why.*

**A2.** State when LOTUS saves work versus needing the full distribution of `Y=g(X)`. Compute
`E[X²]` for `X ~ Uniform(0,1)` via LOTUS directly, **and** by deriving the distribution of
`Y=X²` first and integrating `y·f_Y(y)dy`. Confirm they agree.

*Both give `1/3`. The point is feeling, once, how much extra work the second route costs — that
felt difference is why LOTUS is a reflex rather than a special-case trick.*

**A3.** Expected number of inversions in a random permutation of `{1,…,n}`. Set up the indicator
decomposition explicitly (`I_{ij} = 1` if positions `i<j` are inverted), state `P(I_{ij}=1)`, and
apply linearity. **Do not** attempt to find the distribution of the total.

*The cleanest demonstration that linearity needs zero independence and zero knowledge of the joint
distribution — the indicators are wildly dependent and it does not matter at all.*

**A4. Screaming baby.** A baby cries with probability `p` if hungry, `q` if not, and is hungry
with probability `r`. Set up — not necessarily solve — `E[time to stop crying | crying now]` as a
tower-property computation: define the partition, write the conditional expectations at each
branch, and show the equation you would solve.

*The setup is the skill, not the algebra. Partition, weights, conditional expectation per branch,
weighted sum — that structure is identical in every first-step-conditioning problem you will ever
see.*

**A5. Eve's law, worked.** Roll a fair die to get `N ∈ {1,…,6}`, then flip `N` fair coins. Find
`E[heads]` and `Var(heads)` using the tower property and Eve's law.

*Run both terms of Eve's law end to end. Quoting the formula is not the exercise.*

**A6.** Derive Markov's inequality: for `X≥0`, `a>0`, `E[X] ≥ a·P(X≥a)`, hence
`P(X≥a) ≤ E[X]/a`. Then derive Chebyshev **from Markov**, applying it to `(X−μ)²` with threshold
`k²σ²`.

*Chebyshev is not a separate inequality to memorise. If you can produce it from Markov in under a
minute, you have the one fact that matters — the two formulas are one idea used twice.*

**A7.** State Jensen's inequality for convex `g` with the geometric intuition in one sentence.
Apply it to `g(x)=x²`: what does Jensen say about `E[X²]` versus `(E[X])²`, and what familiar
quantity is the gap?

*The gap is exactly `Var(X) ≥ 0`. Jensen applied to `x²` **is** the statement that variance is
non-negative — worth seeing once, because it makes Jensen a generalisation of something you
already believe rather than a new tool.*

**A8.** Write `M_X(t)=E[e^{tX}]` for a Bernoulli(`p`) and for an Exponential(`λ`). For the
exponential, state the range of `t` where the MGF exists and **show where the integral fails to
converge** outside it.

*The existence range is not a technicality. A distribution with no MGF near 0 is a real and
interview-relevant failure mode, and you cannot say anything sensible about it without having
derived a case where the range is finite.*

**A9.** Differentiate `M_X(t)=E[e^{tX}]` once and evaluate at `t=0` to show `M_X'(0)=E[X]`. State
the general pattern. Then: given `M_X(t)=e^{3t+2t²}`, identify the distribution family and its
parameters by pattern-matching.

*Pattern-matching an MGF to a table is a real interview move — you do not re-derive the table
under time pressure, you recognise the shape.*

### Tier B — the target. At least five.

**B1. Expected max of uniforms.** `E[max(X₁,…,X_n)]` for i.i.d. `Uniform(0,1)`.
*Via order statistics, or via `E[M] = ∫₀¹ P(M>t)dt`. Either route, and note the behaviour as
`n→∞`.*

**B2. Variance of correlated assets.** Derive `Var(aX+bY) = a²σ_X² + b²σ_Y² + 2abρσ_Xσ_Y`, then
find the fully-invested two-asset weights that minimise portfolio variance.
*This is the two-asset minimum-variance portfolio — say that connection out loud. Differentiate,
set to zero, solve.*

**B3. Jensen and option value.** Explain why `E[max(S−K,0)] ≥ max(E[S]−K,0)`, and say what it
implies about an option's price versus its intrinsic value at the forward.
*The payoff is convex in `S`, so Jensen gives it directly. The implication: time value is
non-negative **because** of that convexity — a mathematical consequence, not a market quirk.*

**B4. Chebyshev on returns.** A stock's daily return has mean 0.1%, standard deviation 2%. Bound
`P(daily loss > 5%)`.
*State the bound and say explicitly that Chebyshev is distribution-free and therefore
conservative. That looseness is the price of not assuming normality.*

**B5.** Prove `Var(X) ≥ 0` always, and identify the one case where Eve's law's `Var(E[X|Y])` term
is zero. What does that case mean in words?

**B6.** Rank Markov, Chebyshev and Jensen by how much you need to know about `X`, and
correspondingly by how tight the bound tends to be. One sentence on why more assumptions buy
tightness.

**B7.** Use Markov to bound `P(X ≥ 2E[X])` for any non-negative `X`. Say why the bound does not
depend on the distribution, then **construct a distribution where it is nearly tight** — showing
the bound is achievable rather than merely safe.

**B8.** Given the MGF `M(t)=(pe^t/(1−qe^t))^r` for `t < −ln q`, identify the distribution.
*A9's skill on a less obvious case.*

**B9. Estimation preview.** You observe 7 heads in 10 flips of a coin with unknown `p`. What value
of `p` maximises the probability of seeing exactly this data? Answer and one line of reasoning, no
formal calculus needed.
*Recognising "maximise the probability of the data" as a concept before the machinery arrives.*

### Tier C — only if A and B ran short.

**C1.** Prove the tower property for the discrete case:
`E[E[X|Y]] = Σᵧ E[X|Y=y]P(Y=y) = ΣᵧΣₓ x·P(X=x,Y=y) = Σₓ x P(X=x) = E[X]`.
*Worth doing once so the formula stops being a black box — it is a double-sum rearrangement and
nothing more.*

**C2.** Prove Jensen for twice-differentiable convex `g` by first-order Taylor expansion around
`E[X]`, then taking expectations.
*The linear term vanishes because `E[X−E[X]]=0`. Two lines once you see the tangent-line trick.*

---

## Code problems

Both live in `src/solvers/s1_probability/conditional_expectation_verify.py`. Standard library
only, no test framework. Each: one function computing the answer, one verifying it independently,
an `assert` in `__main__`, and a docstring with time and space complexity.

### 1 · Die-then-coins, against the tower property

Verify A5 by simulation.

> **Input:** number of trials
> **Output:** empirical `E[heads]` and `Var(heads)` from rolling a fair die then flipping that
> many fair coins
> **Verify:** both are within tolerance of the analytical answers A5 derives from the tower
> property and Eve's law.

**Complexity:** analytical `O(1)`; simulation `O(trials)`. State both.

*This file is the natural home for later first-step-conditioning checks — gambler's ruin will
reuse its shape. Note that in a comment; do not build the generalisation yet.*

### 2 · Chebyshev as a genuine upper bound

> **Input:** a concrete non-normal distribution (a two-point distribution or an exponential) and
> a number of trials
> **Output:** the empirical `P(|X−μ| ≥ kσ)` for `k = 2, 3`
> **Verify:** each is `≤ 1/k²`, within a small tolerance for Monte Carlo noise.

*The point is not a single number — it is showing the inequality holds on a shape where it is
**not** tight, so "Chebyshev is loose" is demonstrated rather than asserted.*

**Complexity:** `O(trials)`. Pick the trial count so the standard error is comfortably under the
tolerance, and say in a comment what you chose and why.

---

## Deliverables

**Feynman note** — `progress/feynman_notes/F1_7_expectation_variance_moments.md`. One note for
the whole topic.
- [ ] Teach-back per part, source closed
- [ ] Summary table: one row per named result — linearity, LOTUS, tower property, Eve's law,
      Markov, Chebyshev, Jensen, MGF — each with its formula and **the one thing that makes it
      fail**. That table is what the unlock test reproduces cold.
- [ ] Any `⚠️ GAP` logged — the next session opens on that list

**Problems**
- [ ] All of Tier A unhinted, on paper
- [ ] At least five from Tier B
- [ ] Log which needed hints

**Code** — both problems asserting, with complexity docstrings.

**Unlock test** — one week after the last part closes.

---

**When it gets hard and you start drifting:** stop reading, write the sentence you can't finish
into the note as a `⚠️ GAP`, and switch to Tier A on paper. **For the tower property specifically,
draw the two-stage tree** — branch on `Y`'s outcomes, write `E[X|Y=y]` at each leaf, weight and
sum. The formula is unreadable in the abstract and mechanical once four leaves are in front of
you. **For the MGF, write out `E[e^{tX}]` for a Bernoulli by hand** (`q + pe^t`, two terms) before
touching anything continuous.

**If a session collapses:** Part 1 → A1 and A3. Part 2 → A4 and A5. Part 3 → A6 and A7.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A — linearity and LOTUS (A1–A3)</summary>

**A1.** Discrete case, joint pmf `p(x,y)`:

```
E[X+Y] = ΣₓΣᵧ (x+y)p(x,y) = ΣₓΣᵧ x·p(x,y) + ΣₓΣᵧ y·p(x,y)
       = Σₓ x·Σᵧp(x,y) + Σᵧ y·Σₓp(x,y) = Σₓ x·p_X(x) + Σᵧ y·p_Y(y) = E[X]+E[Y]
```

Every step is re-summing — distributing multiplication over addition, then swapping summation
order, both always legal for absolutely convergent sums. No step used the joint distribution's
*shape*, only that it marginalises correctly, which is true regardless of dependence.

**Where `E[XY]=E[X]E[Y]` breaks:** `E[XY] = ΣₓΣᵧ xy·p(x,y)`. Factoring that into
`(Σₓ x·p_X(x))(Σᵧ y·p_Y(y))` requires `p(x,y)=p_X(x)p_Y(y)` — independence — because otherwise
the joint pmf does not split into a product and the double sum does not factor.

**Linearity survives because addition distributes regardless of the joint distribution. The
product does not.**

**A2.** `X~Uniform(0,1)`, `f_X(x)=1` on `[0,1]`.

*Via LOTUS:* `E[X²] = ∫₀¹ x²·1 dx = [x³/3]₀¹ = **1/3**`.

*Via the distribution of `Y=X²`:* `F_Y(y)=P(X≤√y)=√y` on `[0,1]`, so `f_Y(y)=1/(2√y)`. Then
`E[Y]=∫₀¹ y/(2√y) dy = (1/2)∫₀¹ √y dy = (1/2)[2y^{3/2}/3]₀¹ = **1/3**` ✓

Same answer, but the second route needed a CDF derivation and a change of variables before the
final integral could even be set up.

**A3.** `I_{ij}=1` if the pair at positions `i<j` is inverted. By symmetry over the two possible
orderings of any pair, `P(I_{ij}=1)=1/2` for every one of the `C(n,2)` pairs. By linearity,
regardless of the strong dependence between different indicators:

`E[inversions] = Σ_{i<j} E[I_{ij}] = C(n,2)·(1/2) = **C(n,2)/2**`

</details>

<details>
<summary>Tier A — tower property and Eve's law (A4–A5)</summary>

**A4.** Partition on hungry (`H`, probability `r`) versus not (`Hᶜ`). Let `T` be the time to stop
crying. By the tower property:

```
E[T | crying] = E[T | crying, H]·P(H|crying) + E[T | crying, Hᶜ]·P(Hᶜ|crying)
```

**The weights are a Bayes posterior, not the prior `r`** — you are conditioning on having observed
crying, and crying is more likely when hungry. That is where conditional probability plugs
straight into this stage.

The conditional expectations on each branch come from whatever crying-duration model the problem
specifies. The structure — identify the partition, get its posterior weights, get the conditional
expectation per branch, sum — is what every tower-property problem looks like.

**A5.** `E[heads|N]=N/2` by linearity, since each of `N` fair coins contributes `1/2`.

```
E[heads] = E[E[heads|N]] = E[N/2] = E[N]/2 = 3.5/2 = **1.75**
```

`Var(heads|N) = N/4`, being `N` independent fair flips each contributing `1/4`.

```
E[Var(heads|N)] = E[N]/4 = 3.5/4 = 0.875
Var(N) for a fair die: E[N²] = 91/6, E[N]² = 12.25, so Var(N) = 91/6 − 12.25 = 35/12 ≈ 2.9167
Var(E[heads|N]) = Var(N/2) = Var(N)/4 = 35/48 ≈ 0.7292
Var(heads) = 0.875 + 0.7292 ≈ **1.604**
```

*Within-group spread (0.875) plus between-group spread of the group means (0.729). Both terms are
real and neither is negligible here.*

</details>

<details>
<summary>Tier A — inequalities and MGF (A6–A9)</summary>

**A6.** For `X≥0`, `a>0`:

`E[X] = ∫₀^∞ x f(x)dx ≥ ∫_a^∞ x f(x)dx ≥ ∫_a^∞ a·f(x)dx = a·P(X≥a)`

Dividing by `a` gives **`P(X≥a) ≤ E[X]/a`**. The middle step drops `[0,a)`, which only discards
non-negative mass; the last replaces `x` by its lower bound `a` on what remains.

**Chebyshev from Markov:** let `Y=(X−μ)² ≥ 0` and apply Markov with `a=k²σ²`:

```
P(Y ≥ k²σ²) ≤ E[Y]/(k²σ²) = Var(X)/(k²σ²) = σ²/(k²σ²) = 1/k²
```

`Y ≥ k²σ²` is the same event as `|X−μ| ≥ kσ`, so **`P(|X−μ|≥kσ) ≤ 1/k²`**. One application of
Markov to a squared, recentred variable — that is the whole of Chebyshev.

**A7.** For convex `g`, the chord joining any two points on the graph lies **above** the graph.
Averaging outputs over the distribution of `X` is a chord-like weighted average and sits above
the curve; evaluating `g` at the averaged input is a single point on the curve. Hence
**`E[g(X)] ≥ g(E[X])`**.

Applied to `g(x)=x²`: `E[X²] ≥ (E[X])²`, and the gap is `E[X²]−(E[X])² = **Var(X) ≥ 0**`.

**Jensen applied to `x²` is exactly the statement that variance is non-negative.**

**A8.** Bernoulli(`p`): `M_X(t) = (1−p)e^0 + p·e^t = **q + pe^t**`, a finite sum, so it exists for
all `t`.

Exponential(`λ`): `M_X(t) = ∫₀^∞ e^{tx}·λe^{−λx}dx = λ∫₀^∞ e^{−(λ−t)x}dx`.

The integral converges only when `λ−t > 0`, i.e. **`t < λ`**, giving `M_X(t) = **λ/(λ−t)**`. For
`t ≥ λ` the integrand does not decay as `x→∞` and the integral diverges — the MGF simply does not
exist there.

**A distribution with heavier-than-exponential tails can fail to have a finite MGF on any
interval around 0**, which is why heavy-tailed models are described by characteristic functions
instead.

**A9.** `M_X'(t) = d/dt E[e^{tX}] = E[Xe^{tX}]`, differentiating under the expectation, valid where
the MGF exists on an open interval. At `t=0`: `M_X'(0) = E[X·e^0] = **E[X]**`. Repeating,
`M_X^{(n)}(0) = **E[X^n]**` — each derivative brings down one more factor of `X` before evaluation
at zero.

`M_X(t)=e^{3t+2t²}` matches the **normal** form `e^{μt+σ²t²/2}`: `μ = **3**`, and
`σ²/2 = 2` so `σ² = **4**`. So `X ~ N(3,4)`.

</details>

<details>
<summary>Tier B</summary>

**B1.** `M = max(X₁,…,X_n)`, i.i.d. `Uniform(0,1)`. `P(M≤t)=tⁿ`, so

`E[M] = ∫₀¹ P(M>t)dt = ∫₀¹(1−tⁿ)dt = 1 − 1/(n+1) = **n/(n+1)**`

As `n→∞`, `E[M]→1`: the maximum of many uniforms concentrates at the upper bound.

**B2.** `Var(aX+bY) = a²Var(X)+b²Var(Y)+2ab·Cov(X,Y)`, and `Cov(X,Y)=ρσ_Xσ_Y`, giving
**`a²σ_X² + b²σ_Y² + 2abρσ_Xσ_Y`**.

Fully invested, `b = 1−a`. Minimising `f(a)=a²σ_X²+(1−a)²σ_Y²+2a(1−a)ρσ_Xσ_Y`:

```
f'(a) = 2aσ_X² − 2(1−a)σ_Y² + 2ρσ_Xσ_Y(1−2a) = 0
a* = (σ_Y² − ρσ_Xσ_Y) / (σ_X² + σ_Y² − 2ρσ_Xσ_Y)
```

The two-asset minimum-variance weight — the same object a full Markowitz optimisation computes in
general with a Lagrange multiplier for the budget constraint.

**B3.** `g(S)=max(S−K,0)` is convex — the pointwise max of a linear function and zero, with the
kink pointing upward. Jensen gives `E[max(S−K,0)] ≥ max(E[S]−K,0)` directly.

**Implication:** an option is always worth at least its intrinsic value at the forward, and the
gap is **time value** — a consequence of payoff convexity, not a market phenomenon. Raising the
variance of `S` while holding `E[S]` fixed raises the left side and not the right, which is the
intuition for why option value increases with volatility.

**B4.** `μ = 0.1%`, `σ = 2%`. A 5% loss means `|X−μ| = 5.1% = kσ` with `k = 2.55`.

`P(|X−μ| ≥ kσ) ≤ 1/k² = 1/2.55² ≈ **0.154**`, about 15.4%.

Distribution-free — it assumes nothing about shape, only mean and variance, which is exactly why
it is loose. Under a normal assumption the probability would be about 0.5%. **Chebyshev trades
tightness for zero distributional assumptions**, the right trade when you distrust normality and
a poor one when you do not.

**B5.** `Var(X) = E[(X−E[X])²] ≥ 0`, an expectation of a non-negative quantity.

`Var(E[X|Y]) = 0` iff `E[X|Y]` is almost surely constant — **knowing `Y` tells you nothing about
where `X` is centred**, even though `Y` may still affect `X`'s spread through `Var(X|Y)`. Strictly
weaker than independence: it is "no information about the mean", not "no information at all".

**B6.** Markov needs only `E[X]` and non-negativity — loosest. Chebyshev adds `Var(X)` — tighter,
because variance encodes how concentrated `X` is. Jensen needs no moments at all, only convexity
of `g`; it is not "more assumptions" on the same axis but a structural fact about a
*transformation* of `X` rather than a tail bound on `X`.

**More structure assumed buys a bound that uses more of the available information, at the cost of
needing that information.**

**B7.** `P(X ≥ 2E[X]) ≤ E[X]/(2E[X]) = **1/2**` for any non-negative `X` with a finite mean.

Near-tight example: `X = 0` with probability `1−ε`, and `X = M` with probability `ε`, where
`E[X] = εM`. Then `2E[X] = 2εM`, and `P(X ≥ 2E[X]) = ε` whenever `2ε ≤ 1`. As `ε → 1/2` this
approaches `1/2`, matching the bound exactly.

**The bound is achievable, not merely safe** — which is why Markov cannot be improved without
assuming more.

**B8.** The **negative binomial(`r,p`)** — the geometric MGF raised to the `r`-th power,
consistent with a negative binomial being a sum of `r` i.i.d. geometrics. (That the MGF of a sum
is the product of MGFs is previewed here and proved with the convolution theorem later.)

**B9.** `p̂ = **0.7**`, the sample proportion. The probability of the observed data is
`C(10,7)p⁷(1−p)³`, maximised where its derivative in `p` vanishes, which happens at
successes/trials. This is the intuition that maximum likelihood formalises.

</details>

<details>
<summary>Tier C</summary>

**C1.** Discrete case, using `E[X|Y=y] = Σₓ x·P(X=x|Y=y)`:

```
E[E[X|Y]] = Σᵧ E[X|Y=y]·P(Y=y)
          = Σᵧ [Σₓ x·P(X=x|Y=y)]·P(Y=y)
          = ΣᵧΣₓ x·P(X=x|Y=y)P(Y=y)
          = ΣᵧΣₓ x·P(X=x,Y=y)        ← definition of conditional probability
          = Σₓ x·Σᵧ P(X=x,Y=y)        ← swap summation order
          = Σₓ x·P(X=x) = E[X]  ∎
```

Distributing a sum and swapping summation order — the same two moves as A1. **The tower property
and linearity are proved by the identical mechanism.**

**C2.** For convex twice-differentiable `g`, Taylor around `μ=E[X]` with Lagrange remainder gives
`g(x) = g(μ) + g'(μ)(x−μ) + ½g''(ξ)(x−μ)²` for some `ξ`. Convexity means `g'' ≥ 0`, so the
remainder is non-negative and

```
g(x) ≥ g(μ) + g'(μ)(x−μ)    for all x
```

Take expectations: `E[g(X)] ≥ g(μ) + g'(μ)·E[X−μ] = g(μ) = **g(E[X])**`, since `E[X−μ]=0`.

The tangent line lies below the curve, made algebraic — the same picture as A7's chord argument
seen from the other side.

</details>
