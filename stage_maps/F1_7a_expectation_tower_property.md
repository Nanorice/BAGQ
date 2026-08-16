---
type: stage
id: F1.7a
name: Linearity, LOTUS, Tower Property
kind: foundation
multiplier: 2.0
topic: "[[I-7-expectation-variance-and-moments]]"
concepts: ["[[linearity-of-expectation]]", "[[tower-property]]", "[[first-step-conditioning]]"]
roles: ["[[signal-research]]", "[[market-making]]"]
sprint: S17
status: locked
budget_h: 5
actual_h:
d4_due: 2026-08-30
baseline_closes: []
---

# Linearity, LOTUS, Tower Property — Stage Map
`F1.7a` · foundation (new install, 2.0×) · `topics/section_I` §7 (part 1 of 2)
**Sprint 17, Days 4–5 (Thu 08-20 → Fri 08-21)** · **Budget: 5h across two passes**

> **PRINT THIS PAGE.** Split from `S1.7` because §7 carries five distinct concepts — too wide
> for one day-stage (the `F1.1`/`F1.5` lesson: split when a subsection is too big for a 90-min
> learning phase). This half carries the **baseline-critical** items — tower property scored
> **0** on the diagnostic and gates `S3` Markov chains and `S9` MLE. The lighter half
> (inequalities + MGF) is `F1.7b`.

> **Prereq: `F1.2` (this sprint, Days 1–2).** Tower property problems condition on a random
> variable the way Bayes conditions on an event — same reflex, continuous flavor instead of
> discrete. If A1's setup feels unfamiliar, that's a signal to re-open `F1.2`'s note, not a new
> gap here.

**Why this stage exists:** Adjustment #1 (baseline-driven, `03_gated_progression.md`) pulled
the tower property forward from Sprint 21 to Sprint 17 because it scored **0** and blocks two
entire tiers: `S3` Markov chains (first-step analysis *is* the tower property) and `S9` MLE/
estimation. This is the single highest-leverage stage remaining in the common-tier curriculum —
more things depend on it than on any other ungated item.

**Scope — three things:**
1. **Linearity of expectation** `E[aX+bY] = aE[X]+bE[Y]` — always true, dependence irrelevant
2. **LOTUS** — computing `E[g(X)]` without finding the distribution of `g(X)` first
3. **Tower property** `E[X] = E[E[X|Y]]` — and its twin, **Eve's Law**
   `Var(X) = E[Var(X|Y)] + Var(E[X|Y])`

Out of scope: moment inequalities (Markov/Chebyshev/Jensen) and MGF — `F1.7b`, tomorrow.

---

## Knowledge checklist — tick when you can produce it cold

**Built from `topics/section_I` §7's actual headings**, first half.

**Linearity of Expectation**
- [ ] `E[aX+bY] = aE[X]+bE[Y]` holds **even when `X,Y` are dependent** — say why the proof
      never uses independence (it's a property of the integral/sum, not of the joint distribution)
- [ ] The indicator-variable trick: write a count as a sum of `0/1` indicators, apply linearity
      term-by-term, never touch the joint distribution of the indicators

**LOTUS (Law of the Unconscious Statistician)**
- [ ] `E[g(X)] = Σ g(x)p(x)` or `∫g(x)f(x)dx` — compute directly on `X`'s distribution, no need
      to derive the distribution of `Y=g(X)` first
- [ ] Say explicitly when you'd reach for this vs. deriving `f_Y` — LOTUS is almost always less
      work when you only need a number, not the full distribution

**Tower Property**
- [ ] `E[X] = E[E[X|Y]]` — state it, and say what `E[X|Y]` is: a **random variable**, a function
      of `Y`, not a number
- [ ] **First-step conditioning** — partition on the outcome of the "first" random event, write
      `E[X] = Σᵧ E[X|Y=y]P(Y=y)`, solve for the unknown
- [ ] Recognise the tower property as the *continuous/general* version of the law of total
      probability from `F1.2` — same partition-and-weight structure, expectations instead of
      probabilities

**Eve's Law (Variance Decomposition)**
- [ ] `Var(X) = E[Var(X|Y)] + Var(E[X|Y])` — "expected conditional variance" plus "variance of
      conditional mean"
- [ ] One sentence on what each term means physically — within-group spread, plus between-group
      spread of the group means

### Stretch — none this stage

Moment inequalities and MGF are core material in `F1.7b`, not stretch — they simply don't fit
in this day-stage's budget. No deferrals needed here.

---

## Source — one file, one sitting

| Source | Covers | Time |
|---|---|---|
| **`topics/section_I_probability_combinatorics.md` §7**, lines 179–199 (Core Concepts + first 5 problems) | Linearity, LOTUS, tower, Eve's Law | **25 min, hard stop** |

**Backup only if a concept doesn't click:**

| Backup | Covers | Use only if |
|---|---|---|
| Ross 6th ed. Ch. 7, §7.1–§7.4, §7.7.1 | Formal treatment with more worked conditional-expectation examples | Tower property or Eve's Law derivation isn't landing from the topic file alone |

**Two passes, separate days** (Adj #12, new material). Pass 2 (Fri 08-21) opens on Thu's
`⚠️ GAP` list, ≤20 min.

---

## The shape of the two sessions

**Pass 1 — Thu 08-20, AM block (before work).**

| Block | Minutes | Do |
|---|---:|---|
| Read | 25 | Topic file §7 (linearity/LOTUS/tower/Eve's), hard stop |
| Teach-back | 20 | Note §1 — file **closed** |

**Target 45 min.** Stop at 45 regardless; unfinished sentences become `⚠️ GAP`s for Pass 2.

**Pass 2 — Fri 08-21, AM block + evening block. The 130 min of problems does not fit before
work — only the gap re-read does.**

| When | Block | Minutes | Do |
|---|---|---:|---|
| AM | Gap re-read | 20 | Open ONLY on Thu's `⚠️ GAP` list |
| PM | Tier A | 70 | A1–A5 on paper, unhinted |
| PM | Tier B | 40 | ≥3 of 5 |
| PM | Code | 20 | `F1.7-CODE1` (needs PC) |

**If the day collapses: A2, A3.** A2 is first-step conditioning (the mechanical core of the
tower property, and the direct baseline-closing item); A3 is Eve's Law applied once, concretely.

**The drift move (Adj #13).** Stop reading, write the unfinished sentence into note §2 as a
`⚠️ GAP`, switch to Tier A on paper. **For tower property specifically: draw the two-stage tree**
— first branch on `Y`'s outcomes, then write `E[X|Y=y]` at each leaf, then weight and sum. The
formula is unreadable in the abstract; it is mechanical once you have four leaves in front of you.

---

## Tier A — the floor (all five, unhinted, on paper)

**F1.7a-A1.** Prove linearity of expectation for the discrete case:
`E[X+Y] = ΣΣ(x+y)p(x,y) = Σx·p_X(x) + Σy·p_Y(y) = E[X]+E[Y]`. **State explicitly which line
would break if you tried to prove `E[XY]=E[X]E[Y]` the same way** — and why that one genuinely
needs independence while linearity doesn't.
*This is the single most commonly mis-attributed fact in probability interviews: `E[X+Y]=E[X]+
E[Y]` gets explained via independence when the real reason is that summation is linear. Being
able to point at exactly which step needs independence (the `E[XY]` factorization) and which
doesn't (this one) is what separates "knows the formula" from "knows why."*

**F1.7a-A2. Screaming baby (first-step conditioning).** A baby cries with probability `p` if
hungry, `q` if not. The baby is hungry with probability `r`. Set up — don't necessarily fully
solve — `E[time to stop crying | crying now]` as a tower-property computation: define the
partition, write the conditional expectations at each branch, and show the equation you'd solve.
*The setup is the skill being tested, not the algebra. State the partition `{hungry, not
hungry}`, the conditional expectation on each branch, and the weighted sum — that structure is
identical in every first-step-conditioning problem you'll ever see, including every gambler's-
ruin and every Markov first-passage problem in `S3`.*

**F1.7a-A3. Eve's Law, worked.** Roll a fair die to get `N ∈ {1,...,6}`, then flip `N` fair
coins. Find `E[\text{heads}]` and `Var(\text{heads})` using the tower property and Eve's Law.
*`E[heads|N]=N/2`, so `E[heads]=E[N]/2=3.5/2=1.75` by tower. For Eve's Law:
`Var(heads|N)=N/4`, so `E[Var(heads|N)]=E[N]/4=3.5/4=0.875`; and `Var(E[heads|N])=Var(N/2)=
Var(N)/4`. Compute `Var(N)` for a fair die (`=35/12`) and finish the sum yourself — the point is
running both terms of Eve's Law end to end, not just quoting the formula.*

**F1.7a-A4.** State when LOTUS saves you work vs. when you'd need the full distribution of
`Y=g(X)`. Compute `E[X²]` for `X ~ Uniform(0,1)` via LOTUS directly, **and** by deriving the
distribution of `Y=X²` first and integrating `y·f_Y(y)dy`. Confirm they agree.
*Both give `1/3`. The point isn't the number — it's feeling, once, how much extra work the
second route costs (a change-of-variables derivation) versus the first (one integral). That felt
difference is why LOTUS is a default reflex, not a special-case trick.*

**F1.7a-A5.** Expected number of inversions in a random permutation of `{1,...,n}`. Set up the
indicator-variable decomposition explicitly (`I_{ij} = 1` if positions `i<j` are inverted), state
`P(I_{ij}=1)` for each pair, and apply linearity. **Do not** attempt to find the distribution of
the total inversion count.
*Answer `C(n,2)/2`. This is the cleanest possible demonstration that linearity requires zero
independence and zero knowledge of the joint distribution — each `I_{ij}` is wildly dependent on
every other, and it doesn't matter at all.*

---

## Tier B — the target (≥3 of 5)

**F1.7a-B1. Expected max of uniforms.** `E[\max(X_1,...,X_n)]` for i.i.d. `Uniform(0,1)`.
*Via order statistics or via `E[M] = ∫₀¹ P(M>t)dt = ∫₀¹(1-(1-t)ⁿ)dt`. Either route, get
`n/(n+1)` and note the limiting behavior as `n→∞`.*

**F1.7a-B2. Variance of correlated assets.** Portfolio of two assets with correlation `ρ`.
Derive `Var(aX+bY) = a²σ_X² + b²σ_Y² + 2abρσ_Xσ_Y`, then find the weights `a,a-1` (fully
invested, two-asset case) that minimize portfolio variance.
*This is the two-asset Markowitz minimum-variance derivation — say that connection explicitly.
Differentiate w.r.t. `a`, set to zero, solve.*

**F1.7a-B3. Jensen's Inequality — option intuition.** Explain why
`E[\max(S-K,0)] ≥ \max(E[S]-K,0)` using Jensen, and say what this implies about option prices
vs. intrinsic value computed at the forward.
*`max(S-K,0)` is convex in `S`, so Jensen gives the inequality directly. The implication: option
time value is non-negative precisely because of this convexity — it's not a market inefficiency,
it's a mathematical consequence of the payoff's shape.*

**F1.7a-B4. Markov & Chebyshev on returns.** A stock's daily return has mean 0.1%, std 2%. Use
Chebyshev to bound `P(\text{daily loss} > 5%)`.
*`P(|X-μ|≥kσ)≤1/k²` with `kσ=5.1%` (accounting for the mean), giving a (very loose) bound. State
the bound and say explicitly that Chebyshev is distribution-free and therefore conservative —
that looseness is the price of not assuming normality.*

**F1.7a-B5.** Prove `Var(X) ≥ 0` always, and identify the one case where the Eve's Law term
`Var(E[X|Y])` is zero. What does that case mean in words?
*`Var(E[X|Y])=0` iff `E[X|Y]` is a.s. constant — i.e. knowing `Y` gives you no information about
`X`'s conditional mean. Say why that's a natural notion of "`Y` doesn't predict `X`'s average,"
distinct from full independence.*

---

## Tier C — only if A+B ran short

**F1.7a-C1.** Prove the tower property itself for the discrete case:
`E[E[X|Y]] = Σᵧ E[X|Y=y]P(Y=y) = Σᵧ Σₓ x·P(X=x|Y=y)P(Y=y) = ΣₓΣᵧ x·P(X=x,Y=y) = Σₓ x P(X=x) =
E[X]`.
*Worth doing once by hand so the formula stops being a black box — it's a double sum
rearrangement and nothing more.*

---

## Code problems

`src/solvers/s1_probability/conditional_expectation_verify.py` — new file. Docstring with time
+ space complexity, one `assert`-based `__main__`.

**F1.7-CODE1** — Verify A3 (die-then-coins) by Monte Carlo: simulate rolling a die then flipping
that many coins, many trials, estimate `E[heads]` and `Var(heads)` empirically. Assert both are
within tolerance of the analytical tower/Eve's Law answers from A3.
*Complexity: analytical `O(1)`; simulation `O(trials)`. This solver is the natural home for
future first-step-conditioning verifications too (gambler's ruin in `S3` will reuse this file's
shape) — note that in a comment, don't build the generalization yet.*

---

## Deliverables

**D1 — Feynman note** `progress/feynman_notes/F1_7_expectation_variance_moments.md` **§1(a) only**
- [ ] Teach-back for linearity/LOTUS/tower/Eve's Law, source closed
- [ ] Any `⚠️ GAP` logged in §2 — `F1.7b` opens on this list
- [ ] Note is **shared with `F1.7b`** — do not create a second file; `F1.7b` closes it Saturday

**D2 — Problems** (this file)
- [ ] A1–A5 unhinted, on paper
- [ ] ≥3 of Tier B
- [ ] Log which needed hints

**D3 — Code**
- [ ] `F1.7-CODE1` in `conditional_expectation_verify.py`, asserting, with complexity docstring

**D3.5 — Concept notes:** at `F1.7b` close, not today.

**D4 — Unlock test:** `F1.7a`+`F1.7b` share **one** D4 on **2026-08-30** (+1wk from `F1.7b`'s
Saturday close — see `sprints/S17.md`).

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** Discrete case, joint pmf `p(x,y)`:
```
E[X+Y] = ΣₓΣᵧ (x+y)p(x,y) = ΣₓΣᵧ x·p(x,y) + ΣₓΣᵧ y·p(x,y)
       = Σₓ x·Σᵧp(x,y) + Σᵧ y·Σₓp(x,y) = Σₓ x·p_X(x) + Σᵧ y·p_Y(y) = **E[X]+E[Y]**
```
Every step is just re-summing — distributing multiplication over addition and swapping
summation order (always legal for finite/absolutely-convergent sums). No step used the joint
distribution's *shape*, only that it marginalizes correctly — which is true regardless of
dependence.

**Where `E[XY]=E[X]E[Y]` breaks:** `E[XY] = ΣₓΣᵧ xy·p(x,y)`. To factor this into
`(Σₓx·p_X(x))(Σᵧy·p_Y(y))` you need `p(x,y)=p_X(x)p_Y(y)` — i.e., independence — because
otherwise the joint pmf doesn't split into a product and the double sum doesn't factor into two
single sums. **Linearity survives because addition distributes regardless of the joint
distribution; the product does not, because multiplication doesn't distribute over a sum that
way without the factorization independence provides.**

**A2.** Partition on hungry (`H`, prob `r`) vs. not hungry (`H^c`, prob `1-r`). Let `T` = time to
stop crying. By the tower property:
```
E[T | crying] = E[T | crying, H]·P(H|crying) + E[T | crying, H^c]·P(H^c|crying)
```
where `P(H|crying)` itself needs Bayes (this is where `F1.2` plugs in — the partition weights
are a Bayes posterior, not the prior `r`, because you're conditioning on having observed
"crying"). The conditional expectations `E[T|crying,H]` and `E[T|crying,H^c]` are whatever the
problem's crying-duration model specifies per state — the point of this problem is producing the
equation's *structure*, which is: identify the partition, get its (posterior) weights, get the
conditional expectation on each branch, sum. Every tower-property problem has exactly this shape.

**A3.** `E[heads|N]=N/2` (each of `N` fair coins contributes `1/2` in expectation, linearity).
```
E[heads] = E[E[heads|N]] = E[N/2] = E[N]/2 = 3.5/2 = **1.75**
```
`Var(heads|N) = N/4` (variance of `N` independent fair-coin flips, each contributing `1/4`).
```
E[Var(heads|N)] = E[N]/4 = 3.5/4 = 0.875
Var(N) for fair die on {1,...,6}: E[N²]=91/6, E[N]²=(3.5)²=12.25, Var(N)=91/6-12.25=**35/12**≈2.9167
Var(E[heads|N]) = Var(N/2) = Var(N)/4 = (35/12)/4 = 35/48 ≈ 0.7292
Var(heads) = 0.875 + 0.7292 ≈ **1.604**
```

**A4.** `X~Uniform(0,1)`, `f_X(x)=1` on `[0,1]`.

**Via LOTUS:** `E[X²] = ∫₀¹ x²·1 dx = [x³/3]₀¹ = **1/3**`.

**Via distribution of `Y=X²`:** `F_Y(y)=P(X²≤y)=P(X≤√y)=√y` for `y∈[0,1]`, so
`f_Y(y)=1/(2√y)`. Then `E[Y]=∫₀¹ y·1/(2√y) dy = ∫₀¹ (1/2)√y dy = (1/2)·[2y^{3/2}/3]₀¹ = **1/3**` ✓.

Same answer, but the second route required a CDF derivation and a change of variables before
you could even set up the final integral — LOTUS skips straight to it.

**A5.** `I_{ij}=1` if the pair at positions `i<j` is inverted (i.e., the earlier position holds
the larger value), else 0. By symmetry over the two possible orderings of any pair,
`P(I_{ij}=1)=1/2` for every one of the `C(n,2)` pairs. By linearity (regardless of the strong
dependence between different `I_{ij}`'s):
```
E[\text{inversions}] = Σ_{i<j} E[I_{ij}] = C(n,2)·(1/2) = **C(n,2)/2**
```

</details>

<details>
<summary>Tier B</summary>

**B1.** `M=\max(X_1,...,X_n)`, i.i.d. `Uniform(0,1)`. `P(M≤t)=tⁿ`, so
`E[M]=∫₀¹ P(M>t)dt = ∫₀¹(1-tⁿ)dt = 1 - 1/(n+1) = **n/(n+1)**`.
As `n→∞`, `E[M]→1` — the max of many uniforms concentrates near the upper bound.

**B2.** `Var(aX+bY) = a²Var(X)+b²Var(Y)+2ab·Cov(X,Y)`, and `Cov(X,Y)=ρσ_Xσ_Y` by definition of
correlation, giving `**a²σ_X²+b²σ_Y²+2abρσ_Xσ_Y**`.

Fully invested two-asset: `b=1-a`. Minimize `f(a)=a²σ_X²+(1-a)²σ_Y²+2a(1-a)ρσ_Xσ_Y` over `a`:
```
f'(a) = 2aσ_X² - 2(1-a)σ_Y² + 2ρσ_Xσ_Y(1-2a) = 0
a* = (σ_Y² - ρσ_Xσ_Y) / (σ_X² + σ_Y² - 2ρσ_Xσ_Y)
```
This is the two-asset minimum-variance portfolio weight — the same object Markowitz optimization
computes in full generality with a Lagrange multiplier for the budget constraint (`R.calculus`).

**B3.** `g(S)=\max(S-K,0)` is convex (it's the max of a linear function and zero, and pointwise
max of convex functions is convex — or just note the kink is upward). Jensen for convex `g`:
`E[g(S)] ≥ g(E[S])`, i.e. `E[\max(S-K,0)] ≥ \max(E[S]-K,0)`.

**Implication:** the option's price is always at least its "intrinsic value at the forward"
(`max(E[S]-K,0)`), and the gap is the option's **time value** — which is therefore a direct
consequence of payoff convexity, not a separate market phenomenon. Higher variance of `S`
(holding `E[S]` fixed) increases the LHS without changing the RHS, which is the intuition for
why option value increases with volatility.

**B4.** `μ=0.1%`, `σ=2%`. A "5% loss" is a return of `-5%`, which is `|X-μ| = |-5%-0.1%| =
5.1% = kσ` where `k=5.1/2=2.55`. Chebyshev:
`P(|X-μ|≥kσ) ≤ 1/k² = 1/2.55² ≈ **0.154**` (an upper bound, ≈15.4%).

This is distribution-free — it makes no assumption about the shape of daily returns, only mean
and variance — which is exactly why it's so loose: the true probability under a normal
assumption would be far smaller (`Φ(-2.55) ≈ 0.5%`). **Chebyshev trades tightness for zero
distributional assumptions**, which is the correct trade when you don't trust normality
(e.g., fat-tailed returns) but a poor one when you do.

**B5.** `Var(X)≥0` because it's `E[(X-E[X])²]`, an expectation of a non-negative random
variable — a sum/integral of non-negative terms is non-negative.

`Var(E[X|Y])=0` iff `E[X|Y]` equals a constant almost surely — i.e., **the conditional mean of
`X` doesn't actually depend on which value `Y` takes.** In words: knowing `Y` tells you nothing
about where `X` is centered on average, even though `Y` might still affect `X`'s spread
(`Var(X|Y)` can still vary with `Y`). This is strictly weaker than full independence of `X` and
`Y` — it's a "no information about the mean" condition, not "no information at all."

</details>

<details>
<summary>Tier C</summary>

**C1.** Discrete case, by definition `E[X|Y=y] = Σₓ x·P(X=x|Y=y)`:
```
E[E[X|Y]] = Σᵧ E[X|Y=y]·P(Y=y)
          = Σᵧ [Σₓ x·P(X=x|Y=y)]·P(Y=y)
          = ΣᵧΣₓ x·P(X=x|Y=y)P(Y=y)
          = ΣᵧΣₓ x·P(X=x,Y=y)          ← definition of conditional probability
          = Σₓ x·Σᵧ P(X=x,Y=y)          ← swap summation order
          = Σₓ x·P(X=x) = **E[X]** ∎
```
Nothing here is more than distributing a sum and swapping summation order — the same two moves
as A1's linearity proof. The tower property and linearity are proved by the identical mechanism.

</details>
