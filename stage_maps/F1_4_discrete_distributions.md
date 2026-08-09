---
type: stage
id: F1.4
name: Discrete Distributions
kind: foundation
multiplier: 2.0
topic: "[[I-4-discrete-random-variables-and-distributions]]"
concepts: ["[[memorylessness]]", "[[poisson-exponential-duality]]", "[[first-step-conditioning]]", "[[linearity-of-expectation]]"]
roles: ["[[market-making]]"]
sprint: S15
status: ready-for-test
budget_h: 3
actual_h: 6.0
d4_due: 2026-08-15
baseline_closes: [II.1, II.3]
---

# Discrete Distributions — Stage Map
`F1.4` · foundation (new install, 2.0×) · `topics/section_I` §4
**Sprint 15, Days 12–14 (Fri 07-31 → Sun 08-02)** · **Budget was 3h · actual 6.0h**

> **CLOSED PARTIAL 2026-08-02.** Summary table lives in the handnote; code problems deferred to
> the shared `F1.5` verifier. **D4 unlock test: 2026-08-15.**
>
> **Scope correction, 2026-08-09:** MGF was listed as core here and it is **not in Ross Ch.4** —
> Ross puts MGFs in Ch.7. You correctly wrote *"deferred, this is not in the book chapter 4"* in
> the note, and you were right; A5 was mis-specified, not skipped. It is now marked stretch below.
> The general fix is in `04_deliverables_spec.md` §D2: **checklists get built from the source's
> real section headings, and every stretch item names how you actually get it.**

**Why this stage exists:** baseline I.3 asked for `E[X]` and `Var(X)` of an exponential and got
`e^λ` and `0` — the *named-distribution* machinery is missing, not the reasoning. This stage
installs the discrete half of that machinery. Every one of these four shows up in interviews as
a one-liner you either have or you don't: "what's the expected number of trials until the first
success?" is not a derivation you want to be doing live.

**Scope — four distributions, one table each:**
1. **Bernoulli** — the atom
2. **Binomial** — sum of Bernoullis
3. **Geometric** — trials until first success
4. **Poisson** — the limit of binomial, and the arrival-count distribution

For each: **PMF · E[X] · Var(X) · one classic problem.** Plus the one structural fact that ties
them together: **Poisson as the limit of Binomial.**

Out of scope: negative binomial, hypergeometric, multinomial, discrete uniform beyond a
mention. Conditional/joint versions are S1.6.

**Stretch — not in Ross Ch.4:**
- **MGF** → **DEFERRED to S1.8.** Reason: Ross covers MGFs in **Ch.7**, and *using* them for sums
  needs convolution machinery this stage doesn't have. The definition is in `F1.5`'s
  §Stretch notes so the term isn't cold when S1.8 arrives.
  *(This was originally listed as core and as problem A5 — the error you caught on 07-31.)*

---

## Source — one book, one sitting

| Source | Covers | Time |
|---|---|---|
| **Ross, *A First Course in Probability* 6th ed. — Ch. 4** | All four, plus the Poisson limit | **40 min, hard stop** |

Navigate by heading, not section number. The four you want are the named-distribution
subsections; Ross does Bernoulli/Binomial first, then Poisson, then Geometric later in the
chapter. **Skip the negative binomial and hypergeometric subsections entirely** — they are in
the same chapter and they are not in this stage.

**If Ross's Poisson-limit derivation is heavy going,** the single named fallback is
**StatQuest, "The Poisson Distribution", 12 min**. That is the *only* video in this stage.

**Input cap: 40 min.** Same discipline that made R.linalg land on budget: read once, close the
book, write from memory.

---

## The three-block shape

Same shape as R.linalg, which hit its 3h allocation. Blocks break cleanly at the hour.

| Block | When | Do | Out |
|---|---|---|---|
| **1** | 08:00–09:00 | Read (40 min, hard stop) → close book → start §1 teach-back | Teach-back drafted |
| **2** | afternoon scrap, 30–45 min | Tier A, on paper, closed-book | A1–A5 done |
| **3** | evening, 60 min | Gap-hunt §1 · Tier B · §3–§6 · numerical anchor | Note closed |

Note skeleton: `progress/feynman_notes/F1_4_discrete_distributions.md`

**If the day collapses: A1, A3, B1 only.** A3 (geometric expectation) is the highest-frequency
interview item in the stage; B1 (Poisson as binomial limit) is the one that explains *why*
Poisson exists at all.

---

## Tier A — the floor (A1–A4, unhinted, on paper · A5 withdrawn, see below)

**F1.4-A1.** Write the PMF of `Binomial(n, p)`. Derive `E[X] = np` two ways: (i) directly from
the sum `Σ k·C(n,k)p^k(1−p)^{n−k}`, and (ii) by writing `X = ΣXᵢ` as a sum of `n` Bernoullis
and using linearity.
*Method (ii) takes one line. Notice how much work (i) is. That contrast is the lesson —
decomposition beats summation, and it is the same move as B1 in R.linalg.*

**F1.4-A2.** Derive `Var(X)` for `Binomial(n, p)`. Use the sum-of-Bernoullis decomposition and
say explicitly **which step needs independence** — that is where the interviewer probes.

**F1.4-A3.** `X ~ Geometric(p)`, the number of trials up to and including the first success.
Write the PMF. Derive `E[X] = 1/p` two ways: (i) the sum `Σ k(1−p)^{k−1}p`, and (ii) the
one-step conditioning argument `E[X] = 1 + (1−p)E[X]`.
*Method (ii) is three lines and no series. Learn it as the reflex — it is the same
first-step-analysis that solves gambler's ruin (baseline III.1, scored 1) and the HH-flip puzzle
(II.1, scored 1).*

**F1.4-A4.** `X ~ Poisson(λ)`. Write the PMF, verify it sums to 1 (you need the Taylor series
for `e^λ` — you derived `e` from `dy/dx = y` in R.calculus), and derive `E[X] = λ`.

**F1.4-A5.** ~~Derive the MGF for Bernoulli, Binomial, and Poisson.~~
**WITHDRAWN 2026-08-09 — out of chapter.** Ross covers MGFs in Ch.7, not Ch.4. You flagged this
correctly on 07-31; the answer key below is kept for reference but **A5 does not count against
Tier A completion**, and the MGF column comes out of the summary table. Moved to S1.8.
*Tier A for this stage is A1–A4.*

---

## Tier B — the target (≥3 of 5)

**F1.4-B1.** Show that `Binomial(n, λ/n) → Poisson(λ)` as `n → ∞`. Start from the binomial PMF,
substitute `p = λ/n`, and take the limit term by term.
*You will need `(1 + x/n)^n → e^x` — which is exactly the `(1+dx)^{1/dx}` insight you wrote into
R.calculus §6(e). This is that fact doing real work. State in one sentence what the result means:
when is it legitimate to model a count as Poisson?*

**F1.4-B2.** Prove the geometric distribution is **memoryless**: `P(X > m+n | X > n) = P(X > m)`.
Then say in one sentence what this means for a trader who has flipped 10 tails in a row.
*The exponential is the continuous twin of this — you meet it tomorrow in `F1.5`, and it is
baseline I.3. Getting the discrete version today makes tomorrow's free.*

**F1.4-B3.** A call desk receives on average 3 calls per hour. What is `P(exactly 5 calls in the
next hour)`? `P(no calls in the next 20 minutes)`?
*The second half is the one people fumble: the rate scales with the window. Say what happens to
`λ` when the window shrinks, and note that "no calls" is the bridge to the exponential
waiting time.*

**F1.4-B4.** You flip a fair coin until you get heads. `E[X] = 2` from A3. Now: what is the
expected number of flips until you see **two heads in a row**?
*This is baseline II.1, which you scored 1 on — you said 4, the answer is 6. Set up states and
condition on the first flip. If you can do this cold, that red flag is closed.*

**F1.4-B5.** `X ~ Binomial(n, p)`. Show `E[X(X−1)] = n(n−1)p²` and use it to get `Var(X)`
without the Bernoulli decomposition.
*This is the factorial-moment trick. It generalises to the Poisson in one line — do that too if
there's time, and note which is less work.*

---

## Tier C — only if A+B ran short

**F1.4-C1.** Coupon collector: `n` distinct coupons, one per box, uniformly at random. Show
`E[boxes to collect all n] = n·H_n ≈ n ln n`. Decompose into geometric waiting times.
*This is baseline II.3, scored 0, and it is on the scrap-time cheap-win list. It is a sum of
geometrics — which you now own from A3.*

**F1.4-C2.** For `Poisson(λ)`, show that `E[X] = Var(X) = λ`. Then say what "overdispersion"
means in a count model and why it matters when you fit trade-arrival data.

---

## Deliverables

- [ ] `progress/feynman_notes/F1_4_discrete_distributions.md` — all 6 sections real, zero
      `⚠️ GAP`, napkin ≤200 words **said out loud once**
- [ ] Tier A A1–A5 unhinted, on paper
- [ ] ≥3 of 5 Tier B
- [ ] **Summary table in the note** — four rows (Bernoulli/Binomial/Geometric/Poisson) ×
      three columns (PMF, E[X], Var — MGF withdrawn 08-09). This table *is* the deliverable; it is what you
      recall cold in a year.
- [ ] **Unlock test:** re-answer baseline I.3 cold *(E and Var of an exponential — you will not
      have covered the exponential yet; answer the discrete analogue, geometric, and note the
      pairing)*. Plus II.1 (E[flips for HH]) cold, fully correct.

**Create `src/solvers/` this stage** — first real need. One file:
`src/solvers/s1_probability/discrete_verify.py`, ~20 lines: simulate the geometric to check
`E[X]=1/p`, and the B4 two-heads-in-a-row to check it converges to 6. Docstring with complexity,
per baseline adjustment #9.

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

**A5.** Bernoulli: `M(t) = E[e^{tX}] = (1−p) + pe^t`.
Binomial: `X = ΣXᵢ` independent, and the MGF of a sum of independents is the *product* of MGFs,
so `M(t) = **((1−p) + pe^t)^n**` — the Bernoulli's raised to the `n`, exactly as the
decomposition predicts. **That is why MGFs earn their keep: they turn convolution (hard) into
multiplication (easy).** You will use this properly in S1.8.
Poisson: `M(t) = Σ e^{tk}e^{−λ}λ^k/k! = e^{−λ}Σ(λe^t)^k/k! = e^{−λ}e^{λe^t} = **e^{λ(e^t −1)}**`.
Check: `M'(t) = λe^t·e^{λ(e^t−1)}`, so `M'(0) = λ = E[X]` ✓.
`M''(0) = λ + λ²= E[X²]`, so `Var = λ + λ² − λ² = **λ**` ✓ — matches A4.

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
and both are longer than the MGF route in A5. Three ways up the same hill — the MGF is the one
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

**C2.** Both equal `λ` — shown in A4 and A5. This is a **strong, testable restriction**: real
count data with `Var > E` is *overdispersed* and the Poisson fit is wrong.
For trade arrivals this is the norm, not the exception: trades cluster (one large order triggers
responses), so empirical variance exceeds the mean, often by a lot. The standard fixes are the
negative binomial (Poisson with a random `λ`) or a Hawkes process (arrivals raise the intensity
of future arrivals). **Checking `sample var / sample mean ≈ 1` is a 10-second diagnostic on any
count model** — and failing it is the single most common reason a naive Poisson arrival model
underestimates tail risk.

</details>
