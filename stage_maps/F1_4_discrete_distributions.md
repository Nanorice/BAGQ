---
type: stage
id: F1.4
name: Discrete Distributions
topic: "[[I-4-discrete-random-variables-and-distributions]]"
concepts: ["[[memorylessness]]", "[[poisson-exponential-duality]]", "[[first-step-conditioning]]", "[[linearity-of-expectation]]"]
roles: ["[[market-making]]"]
sprint: S15
status: ready-for-test
est_h: 3
actual_h: 6.0
---

# Discrete Distributions

**Source:** Ross, *A First Course in Probability* 6th ed. — Ch. 4. Navigate by heading: Ross does
Bernoulli and binomial first, then Poisson, then geometric later in the chapter. **Skip the
negative binomial and hypergeometric subsections** — same chapter, not this topic.

**If the Poisson-limit derivation is heavy going,** the single fallback is StatQuest, "The Poisson
Distribution", 12 minutes. That is the only video here.

**Estimated: 6h.** *(Budgeted 3h and took 6 — this is the stage that produced the 2× multiplier
for new material.)*

> **Closed partial.** The summary table lives in the handnote rather than the repo, and the code
> problems were folded into the shared continuous-distributions verifier.

---

## What this covers

Four distributions, and one structural fact tying them together. Each shows up in interviews as a
one-liner you either have or you do not — "expected number of trials until the first success" is
not a derivation you want to be doing live.

1. **Bernoulli** — the atom
2. **Binomial** — a sum of Bernoullis
3. **Geometric** — trials until the first success
4. **Poisson** — the limit of the binomial, and the arrival-count distribution

For each: PMF, `E[X]`, `Var(X)`, one classic problem. Plus **Poisson as the limit of binomial**,
which is what makes the four a family rather than a list.

**Not here:** negative binomial, hypergeometric, multinomial. Joint and conditional versions come
with joint distributions.

**Moment generating functions are deliberately absent.** They were originally listed as core here
and they are **not in Ross Ch.4** — Ross puts them in Ch.7. The gap was caught while studying and
the item was withdrawn rather than faked. They arrive with expectation and moments.

*That catch is why the checklist rule exists: build it from the source's real headings, and name
how you actually get anything outside the chapter.*

---

## Knowledge checklist — tick when you can produce it cold

**Bernoulli and binomial**
- [x] PMF of `Binomial(n,p)`
- [x] `E[X] = np` **by linearity over a sum of Bernoullis** — not by summing the series
- [x] `Var(X) = np(1−p)`, and **which step needs independence**
- [ ] The factorial-moment route to the variance

**Geometric**
- [x] PMF, and `E[X] = 1/p` by one-step conditioning: `E[X] = 1 + (1−p)E[X]`
- [x] **Memorylessness** `P(X > m+n | X > n) = P(X > m)`
- [ ] What memorylessness means for someone who has just seen ten tails in a row

**Poisson**
- [x] PMF, and that it sums to one via the Taylor series for `e^λ`
- [x] `E[X] = Var(X) = λ`
- [ ] **Poisson as the limit of `Binomial(n, λ/n)`** — and when modelling a count as Poisson is
      therefore legitimate
- [ ] Rate scaling: what happens to `λ` when the observation window shrinks
- [ ] **Overdispersion** — what `Var > E` tells you about real arrival data

---

## Problems

### Tier A — the floor. All four, unhinted, on paper.

**A1.** Write the PMF of `Binomial(n, p)`. Derive `E[X] = np` two ways: directly from the sum
`Σ k·C(n,k)p^k(1−p)^{n−k}`, and by writing `X = ΣXᵢ` as a sum of `n` Bernoullis and using
linearity.

*The second takes one line. Notice how much work the first is — decomposition beats summation,
and that is the whole method.*

**A2.** Derive `Var(X)` for `Binomial(n, p)` using the sum-of-Bernoullis decomposition, and say
explicitly **which step needs independence**. That is where an interviewer probes.

**A3.** `X ~ Geometric(p)`, the number of trials up to and including the first success. Write the
PMF. Derive `E[X] = 1/p` two ways: the sum `Σ k(1−p)^{k−1}p`, and the one-step conditioning
argument `E[X] = 1 + (1−p)E[X]`.

*The second is three lines and no series. Learn it as the reflex — it is the same first-step
analysis that solves gambler's ruin and every pattern-waiting puzzle.*

**A4.** `X ~ Poisson(λ)`. Write the PMF, verify it sums to one — you need the Taylor series for
`e^λ` — and derive `E[X] = λ`.

### Tier B — the target. At least three.

**B1.** Show that `Binomial(n, λ/n) → Poisson(λ)` as `n → ∞`. Start from the binomial PMF,
substitute `p = λ/n`, take the limit term by term.

*You will need `(1 + x/n)^n → e^x`. State in one sentence what the result means: when is it
legitimate to model a count as Poisson?*

**B2.** Prove the geometric distribution is **memoryless**: `P(X > m+n | X > n) = P(X > m)`. Then
say in one sentence what that means for a trader who has just flipped ten tails in a row.

**B3.** A call desk receives on average 3 calls per hour. Find `P(exactly 5 calls in the next
hour)` and `P(no calls in the next 20 minutes)`.

*The second half is the one people fumble — the rate scales with the window. Say what happens to
`λ` when the window shrinks, and note that "no calls" is the bridge to a continuous waiting time.*

**B4.** You flip a fair coin until you get heads; `E[X] = 2` from A3. Now: what is the expected
number of flips until you see **two heads in a row**?

*Set up states and condition on the first flip. The intuitive answer of 4 is wrong.*

**B5.** `X ~ Binomial(n, p)`. Show `E[X(X−1)] = n(n−1)p²` and use it to get `Var(X)` without the
Bernoulli decomposition.

*The factorial-moment trick. It generalises to the Poisson in one line — do that too if there is
time, and note which is less work.*

### Tier C — only if A and B ran short.

**C1.** Coupon collector: `n` distinct coupons, one per box, uniformly at random. Show
`E[boxes to collect all n] = n·H_n ≈ n ln n` by decomposing into geometric waiting times.

**C2.** For `Poisson(λ)`, show `E[X] = Var(X) = λ`. Then say what **overdispersion** means in a
count model, and why it matters when fitting trade-arrival data.

---

## Code problems

Both live in `src/solvers/s1_probability/distributions_verify.py`, shared with continuous
distributions. Standard library only.

### 1 · Geometric expectation

> **Input:** success probability `p`, number of trials
> **Output:** the mean number of Bernoulli(`p`) attempts until the first success
> **Verify:** simulated mean ≈ `1/p`.

### 2 · Expected flips until two heads in a row

> **Input:** number of simulated runs
> **Output:** the mean number of fair-coin flips until `HH` appears
> **Verify:** the mean ≈ `6`.

*You have the first-step-conditioning answer from B4 on paper. The simulation is the referee.*

---

## Deliverables

**Feynman note** — `progress/feynman_notes/F1_4_discrete_distributions.md`
- [ ] Teach-back for all four distributions, source closed
- [ ] Summary table: one row per distribution — PMF, `E[X]`, `Var(X)`, and the one classic problem
- [ ] Any `⚠️ GAP` logged

**Problems**
- [ ] A1–A4 unhinted, on paper
- [ ] At least three from Tier B
- [ ] Log which needed hints

**Code** — both problems asserting, with complexity docstrings.

**Unlock test** — one week after close.

---

**When it gets hard and you start drifting:** stop reading, write the sentence you can't finish
into the note as a `⚠️ GAP`, and switch to Tier A on paper. **For these four specifically, write
the PMF down and compute `E[X]` for `n=2` or `n=3` by hand** — a distribution becomes concrete the
moment you have enumerated a tiny case, and never from re-reading its definition.

**If the day collapses, do A1 and A3.** A1 is linearity beating summation; A3 is first-step
conditioning, which recurs everywhere downstream.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** PMF: `P(X=k) = C(n,k) p^k (1−p)^{n−k}`, `k = 0…n`.

*(ii) first, because it is the honest way:* let `Xᵢ = 1` if trial `i` succeeds, else `0`. Each
`Xᵢ ~ Bernoulli(p)` with `E[Xᵢ] = p`. Then `X = ΣXᵢ` and by linearity of expectation
`E[X] = Σ E[Xᵢ] = **np**`. Linearity needs no independence — it holds for *any* dependence
structure, which is what makes it so strong.

*(i) the direct sum:* `E[X] = Σ_{k=0}^{n} k·C(n,k)p^k(1−p)^{n−k}`. Drop `k=0`, use the identity
`k·C(n,k) = n·C(n−1,k−1)`, factor out `np`, reindex `j = k−1`, and the remaining sum is the full
Binomial(n−1, p) PMF summing to 1. Gives `np`. Five lines versus one.

**A2.** `Var(X) = **np(1−p)**`. For a single Bernoulli, `Var(Xᵢ) = E[Xᵢ²] − E[Xᵢ]² = p − p² = p(1−p)`
(using `Xᵢ² = Xᵢ` since `Xᵢ ∈ {0,1}` — that trick is worth keeping).
Then `Var(ΣXᵢ) = ΣVar(Xᵢ) = np(1−p)`.
**The independence step is the second equality**: variance is additive only when the terms are
uncorrelated. In general `Var(ΣXᵢ) = ΣVar(Xᵢ) + 2Σ_{i<j}Cov(Xᵢ,Xⱼ)`. Compare with A1, where
linearity of expectation needed no such assumption. That asymmetry is the point.

**A3.** PMF: `P(X=k) = (1−p)^{k−1}p`, `k = 1,2,…`

*(ii) one-step conditioning:* flip once. With probability `p` you are done in 1 trial. With
probability `1−p` you have burned a trial and are back where you started, memorylessly. So
`E[X] = 1 + (1−p)E[X]` → `E[X]·p = 1` → `**E[X] = 1/p**`.

*(i) the series:* `E[X] = Σ k(1−p)^{k−1}p = p·Σ k q^{k−1}` with `q = 1−p`. Recognise
`Σ k q^{k−1} = d/dq (Σ q^k) = d/dq (1/(1−q)) = 1/(1−q)² = 1/p²`. So `E[X] = p·(1/p²) = 1/p`. ✓
*(Also `Var(X) = (1−p)/p²`.)*

**A4.** PMF: `P(X=k) = e^{−λ}λ^k/k!`, `k = 0,1,2,…`
Sums to 1: `Σ_k e^{−λ}λ^k/k! = e^{−λ}·Σ_k λ^k/k! = e^{−λ}·e^{λ} = 1` ✓ — the sum is exactly the
Taylor series of `e^λ`.
`E[X] = Σ k·e^{−λ}λ^k/k!` — drop `k=0`, cancel one `k`, reindex `j=k−1`:
`= λe^{−λ}Σ_j λ^j/j! = λe^{−λ}e^{λ} = **λ**`.


</details>

<details>
<summary>Tier B</summary>

**B1.** Set `p = λ/n` in `P(X=k) = C(n,k)p^k(1−p)^{n−k}`:

`= [n(n−1)…(n−k+1)/k!]·(λ/n)^k·(1−λ/n)^{n−k}`
`= (λ^k/k!)·[n(n−1)…(n−k+1)/n^k]·(1−λ/n)^n·(1−λ/n)^{−k}`

Take `n → ∞` with `k`, `λ` fixed, term by term:
- the bracket `→ 1` (it is `k` factors each `→ 1`)
- `(1−λ/n)^n → e^{−λ}` ← **this is your R.calculus §6(e) `(1+dx)^{1/dx}` fact**
- `(1−λ/n)^{−k} → 1`

Product: `**e^{−λ}λ^k/k!**` = Poisson(λ). ∎

*Meaning:* a Poisson is legitimate when you have **many independent opportunities, each with
tiny probability, with the product `np` held at a moderate constant**. Rare events, many trials.
That is why it models trade arrivals, order-book events, defaults, and typos per page — and why
it fails when events cluster (arrivals trigger arrivals), which is what Hawkes processes exist
to fix.

**B2.** `P(X > n) = (1−p)^n` (first `n` trials all failed). Then

`P(X > m+n | X > n) = P(X > m+n)/P(X > n) = (1−p)^{m+n}/(1−p)^n = (1−p)^m = P(X > m)` ∎

*Meaning:* the coin has no memory of the 10 tails. The expected additional flips to the first
head is still `1/p`, exactly as it was at the start. The gambler's fallacy is precisely the
denial of this line. **Geometric is the only memoryless discrete distribution; the exponential
is the only memoryless continuous one** — same theorem, two settings, and tomorrow's stage is
the continuous half.

**B3.** `λ = 3` per hour. `P(X = 5) = e^{−3}3^5/5! = e^{−3}·243/120 ≈ 0.0498·2.025 ≈ **0.101**`.

For 20 minutes = 1/3 hour, the rate scales with the window: `λ' = 3 × (1/3) = 1`.
`P(X = 0) = e^{−1}·1^0/0! = **e^{−1} ≈ 0.368**`.
*Rate scales linearly with the window because Poisson counts have independent increments —
that is the defining property of the Poisson process (S4.4, deferred).*
**The bridge:** `P(no calls in [0,t]) = e^{−λt}` is exactly `P(T > t)` for the waiting time `T`
to the first call. So `T` has CDF `1 − e^{−λt}` — the **exponential distribution**. Poisson
counts and exponential gaps are the same process described two ways. That is tomorrow's stage,
and it is baseline I.3.

**B4.** States by current progress toward `HH`. Let `E₀` = expected additional flips from
"no useful streak", `E₁` = from "one head so far".

`E₀ = 1 + ½E₁ + ½E₀`  (flip: heads → state 1, tails → back to 0)
`E₁ = 1 + ½·0 + ½E₀`  (flip: heads → done, tails → back to 0)

From the first: `½E₀ = 1 + ½E₁` → `E₀ = 2 + E₁`. Substitute into the second:
`E₁ = 1 + ½(2 + E₁)` → `E₁ = 2 + ½E₁` → `E₁ = 4`. So `**E₀ = 6**`. ✓

*(Baseline II.1: you said 4 — which is `E₁`, the answer from one head in. Worth noting that your
error was a state-labelling slip, not a method failure.)*
Contrast with `HT`, which takes only **4** — because a failed `HT` attempt leaves you *still* in
"have H" state, whereas a failed `HH` attempt sends you back to zero. Same first-step analysis
as A3(ii), and the same machinery as gambler's ruin (III.1) and the frog puzzle (III.3, which
you got right).

**B5.** `E[X(X−1)] = Σ k(k−1)C(n,k)p^k q^{n−k}`. Drop `k=0,1`, use
`k(k−1)C(n,k) = n(n−1)C(n−2,k−2)`, factor `n(n−1)p²`, reindex — the remaining sum is a full
Binomial(n−2,p) PMF = 1. Gives `**n(n−1)p²**`.
Then `E[X²] = E[X(X−1)] + E[X] = n(n−1)p² + np`, so
`Var = n(n−1)p² + np − n²p² = np − np² = **np(1−p)**` ✓ matches A2.

*Poisson version, one line:* `E[X(X−1)] = λ²` by the same reindex, so
`Var = λ² + λ − λ² = λ`. The factorial-moment route is shorter for Poisson than for Binomial,
and both are longer than the moment-generating-function route. Three ways up the same hill, and
that scales.

</details>

<details>
<summary>Tier C</summary>

**C1.** Let `Tᵢ` = boxes needed to get the `i`-th *new* coupon after having `i−1`. When you hold
`i−1` distinct coupons, the chance a fresh box is new is `(n−i+1)/n`, so
`Tᵢ ~ Geometric((n−i+1)/n)` and `E[Tᵢ] = n/(n−i+1)` by A3.

`E[T] = Σ_{i=1}^{n} n/(n−i+1) = n·(1 + 1/2 + … + 1/n) = **n·H_n ≈ n ln n + γn**`

For `n = 50` coupons: `≈ 50·ln50 + 0.577·50 ≈ 196 + 29 ≈ 225` boxes.
*(Baseline II.3, scored 0 — closed. The whole problem is "decompose into geometrics and use
linearity", which is A1(ii) and A3 combined. Note that linearity applies even though the `Tᵢ`
are dependent in the ordering sense — you never needed independence.)*

**C2.** Both equal `λ` — shown in A4. This is a **strong, testable restriction**: real
count data with `Var > E` is *overdispersed* and the Poisson fit is wrong.
For trade arrivals this is the norm, not the exception: trades cluster (one large order triggers
responses), so empirical variance exceeds the mean, often by a lot. The standard fixes are the
negative binomial (Poisson with a random `λ`) or a Hawkes process (arrivals raise the intensity
of future arrivals). **Checking `sample var / sample mean ≈ 1` is a 10-second diagnostic on any
count model** — and failing it is the single most common reason a naive Poisson arrival model
underestimates tail risk.

</details>
