---
type: stage
id: F1.1
name: Combinatorics
topic: "[[I-1-combinatorics-and-counting]]"
concepts: ["[[ordered-vs-unordered]]", "[[multinomial-coefficient]]", "[[bijection-proof]]", "[[inclusion-exclusion]]", "[[complementary-counting]]"]
roles: ["[[signal-research]]", "[[market-making]]", "[[risk-management]]"]
sprint: S16
status: in-progress
est_h: 6.5
actual_h: 4
---

# Combinatorics

**Source:** Ross, *A First Course in Probability* 6th ed. — Ch. 1 §1.1–§1.6, then **Ch. 2 §2.5**.

> **The source crosses chapters, deliberately.** Counting rules and stars and bars are Ch.1.
> Inclusion–exclusion is **Ch.2 §2.5**, because that is where Ross puts it — stated as a
> probability identity, not a counting one. **Derangements are not a headed section anywhere**;
> Ross has them as the worked example inside §2.5. Expect §1.6 to look unfamiliar by title
> ("The number of integer solutions of equations") — the chapter never says "stars and bars",
> but that is the right section.

**Estimated: 6.5h** — roughly 1.5h for counting rules, 2.5h each for stars and bars and for
inclusion–exclusion.

---

## What this covers

Counting is the substrate for every discrete probability question — "probability = favourable /
total" is two counting problems in a trench coat.

**Three natural pauses.** Stop at a part boundary if the session ends; don't stop mid-part.

**Part 1 — Counting rules.** Product rule · permutations `P(n,k) = n!/(n−k)!` · combinations
`C(n,k) = n!/(k!(n−k)!)` · multinomial `n!/(k₁!⋯kₘ!)`. The organising question, asked of every
problem: **does order matter, and are the objects distinguishable?** Four rules, four answers.
Everything here is the product rule followed by division by whatever got overcounted — say what
is overcounted and by how much, and you can rebuild any of them cold.

**Part 2 — Stars and bars.** "How many ways to distribute `n` identical things into `k` labelled
bins" is one formula, and it is the formula people fail to recognise. It carries the real
transferable skill: **proof by bijection.** You don't count the hard thing; you build a one-to-one
correspondence with an easy thing and count that instead. That move recurs in lattice paths, in
Catalan numbers, and in every "map this to a known problem" interview prompt.

**Part 3 — Inclusion–exclusion and derangements.** Two reasons, and the second is the real one.
Inclusion–exclusion is the general answer to "count things satisfying *at least one* / *none* of
several overlapping conditions", and the general form of `P(A∪B) = P(A)+P(B)−P(A∩B)` — which you
will use far more often as a probability rule than as a counting one. But **complementary
counting** is the higher-yield reflex: "at least one" almost always means "one minus none".
Derangements are the canonical drill for it.

**Parts 2 and 3 join at the capacity constraint.** Stars and bars counts the unconstrained total;
inclusion–exclusion removes the violations. Problem B5 is that join, and it is the point.

**Not here:** unlabelled bins (integer partitions — no closed form) · Möbius inversion, the
general sieve, permanents · Catalan numbers, Stirling numbers, the ballot problem, the twelvefold
way. None are in the source chapters, and they are the fifth thing an interviewer reaches for, not
the first. Catalan returns with lattice paths when dynamic programming comes up.

---

## Knowledge checklist — tick when you can produce it cold

Tick at the close of a block, not while reading.

### Part 1 — Counting rules

**§1.2 The basic principle of counting**
- [x] Product rule, and the generalised version for `r` experiments
- [x] Why it is the only axiom here — everything below is the product rule plus a correction for
      overcounting

**§1.3 Permutations**
- [x] `n!` arrangements of `n` distinct objects
- [x] `P(n,k) = n!/(n−k)!` — ordered selection of `k` from `n`
- [x] **Permutations with repeated objects** = `n!/(n₁!n₂!⋯nᵣ!)` ← *this is MISSISSIPPI, and it is
      the same formula as the multinomial coefficient in §1.5*

**§1.4 Combinations**
- [x] `C(n,k) = n!/(k!(n−k)!)`, and **why the `k!` divides out**
- [x] Symmetry `C(n,k) = C(n,n−k)` — choosing who's in = choosing who's out
- [ ] Pascal's rule `C(n,k) = C(n−1,k−1) + C(n−1,k)` — condition on whether item `n` is in
- [ ] Binomial theorem `(x+y)ⁿ = Σ C(n,k)xᵏy^{n−k}`

**§1.5 Multinomial coefficients**
- [ ] `C(n; k₁,…,kₘ) = n!/(k₁!⋯kₘ!)` — split `n` items into `m` labelled groups of fixed size
- [ ] **That this is the same object as §1.3's repeated-permutation formula.** Two derivations,
      one number. Say why in one sentence.
- [ ] The decision table: order matters / doesn't × repetition allowed / not → which formula

### Part 2 — Stars and bars

**§1.6 Integer solutions of equations**
- [ ] **Proposition 6.1:** number of **positive** integer solutions to `x₁+⋯+x_k = n` is `C(n−1, k−1)`
- [ ] **Proposition 6.2:** number of **non-negative** integer solutions is `C(n+k−1, k−1)`
- [ ] Which is the default "balls into bins" answer, and why *(non-negative — empty bins are
      allowed unless the problem forbids them)*
- [ ] The bijection itself: a solution ⟷ a row of `n` stars with `k−1` bars inserted
- [ ] Why `k−1` bars and not `k`
- [ ] Lower bounds by substitution `yᵢ = xᵢ − cᵢ`, and what happens when `Σcᵢ > n`
- [ ] That "unordered selection with repetition" and "balls into bins" are the same problem

### Part 3 — Inclusion–exclusion and derangements

**§2.5 Inclusion–exclusion**
- [ ] `P(A∪B) = P(A) + P(B) − P(A∩B)` — and **why** the subtraction (`A∩B` counted twice)
- [ ] Three sets: `+singles − pairs + triple`
- [ ] General form `P(∪Aᵢ) = Σ|Aᵢ| − Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩A_k| − ⋯ + (−1)^{n+1}|∩Aᵢ|`
- [ ] **The counting version is the same statement** with `|·|` instead of `P(·)` — one identity,
      two readings
- [ ] Why the signs alternate: an element in exactly `m` sets must be counted **once**, and
      `Σₖ (−1)^{k+1} C(m,k) = 1` for `m ≥ 1` *(one line from the binomial theorem — that is the
      whole proof)*

**Derangements** *(worked example in §2.5, not a headed section)*
- [ ] `D_n = n!·Σ_{k=0}^{n} (−1)^k/k!` by inclusion–exclusion on "person `i` gets their own coat"
- [ ] `D_n/n! → 1/e ≈ 0.368` — the probability nobody gets their own coat, for large `n`
- [ ] That the limit is essentially exact by `n = 7`, and **does not depend on `n`** in any
      practically useful way — the counterintuitive part, and the interview hook
- [ ] Recurrence `D_n = (n−1)(D_{n−1} + D_{n−2})` *(state it; deriving it is Tier C)*

**Complementary counting**
- [ ] "At least one" → `1 − P(none)`, and when that is easier than the direct count
- [ ] The birthday-problem shape: `P(≥1 shared) = 1 − (365·364⋯)/365ⁿ`

---

## Problems

### Tier A — the floor. All of them, unhinted, on paper.

**A1.** Derive `P(n,k) = n!/(n−k)!` from the product rule, then derive `C(n,k) = P(n,k)/k!` from
`P(n,k)`. **Say in one sentence why the `k!` is dividing.**

**A2.** Build the **decision table** from memory — the four cells of {order matters, order
doesn't} × {repetition allowed, not allowed}, with the formula in each. Then place these five
problems in it, one line each:
(i) 3-digit PIN codes · (ii) a 5-card poker hand · (iii) podium finish from 8 runners ·
(iv) 4 scoops from 10 flavours, repeats allowed, order irrelevant · (v) MISSISSIPPI.

*The single most useful artefact of this stage. One cell is Part 2's subject — find out which by
noticing you can't fill it yet.*

**A3.** Prove Pascal's rule `C(n,k) = C(n−1,k−1) + C(n−1,k)` **combinatorially**, not by algebra.
Condition on whether a specific item is in the chosen set.

*Conditioning on one element is the same move as first-step conditioning in the geometric
distribution's derivation. Same reflex, different setting.*

**A4.** MISSISSIPPI: how many distinct arrangements? Then generalise — state the
repeated-permutation formula, and **show it is the multinomial coefficient** by giving the second
derivation (choose positions for each letter in turn: `C(11,4)·C(7,4)·C(3,2)·C(1,1)`) and
confirming the two agree.

*The job is not the number — it is producing the formula's **name** and both derivations, so that
a problem about bins or teams triggers it.*

**A5.** Derive `C(n+k−1, k−1)` for placing `n` **identical** balls into `k` **labelled** bins.
Build the bijection explicitly: draw the diagram for `n=4, k=3`, write down the solution
`(x₁,x₂,x₃)` it corresponds to, and **state why the correspondence is one-to-one in both
directions.**

*A bijection proof needs both directions — every arrangement gives exactly one solution, and every
solution exactly one arrangement. Giving only one direction is the standard incomplete answer, and
an interviewer will ask for the other.*

**A6.** Answer these, and for each say which proposition applies:
(i) 20 identical candies to 4 children, any number each
(ii) 20 identical candies to 4 children, **each gets at least 1**
(iii) 20 identical candies to 4 children, **each gets at least 2**

*Do (iii) by pre-allocating, not by a new formula.*

**A7.** State the substitution `yᵢ = xᵢ − cᵢ` in general: how many non-negative integer solutions
to `x₁+⋯+x_k = n` with `xᵢ ≥ cᵢ` for each `i`? **Say what happens when `Σcᵢ > n`**, and why the
formula must return zero there.

*Edge cases are where counting formulas get tested. `C(m,r)` with `m < r` is 0, and the formula
handles it — but only if you know that's what `C` does.*

**A8.** Show that "unordered selection of `k` items from `n` types, repetition allowed"
= `C(n+k−1, k)` **is the same problem as balls-into-bins.** Then fill in A2's missing bottom-right
cell and confirm the ice-cream answer: 4 scoops from 10 flavours.

*Two problems, one formula, and they look nothing alike until you name the bijection: each **type**
is a bin, each **selected item** is a ball. This is the recognition step Part 2 exists to install.*

**A9.** State and prove two-set inclusion–exclusion, then three-set. **Prove the general `n`-set
version** by the element-counting argument: take an element lying in exactly `m` of the sets and
show the right-hand side counts it exactly once.

*The proof is `Σₖ₌₁^m (−1)^{k+1}C(m,k) = 1`, which is `1 − (1−1)^m` by the binomial theorem. That
is the entire content of inclusion–exclusion, and it fits on one line — worth knowing, because
"prove it" is a fair follow-up to "state it".*

**A10.** Write the **counting** form alongside the **probability** form and say why they are the
same statement. Then: how many integers in `1…1000` are divisible by 2, 3, or 5?

*Also: `|A∩B|` for divisibility is divisibility by the lcm — say why that is, don't just use it.*

**A11.** Derive `D_n` from scratch by inclusion–exclusion on the events `Aᵢ` = "person `i` gets
their own coat". Compute `D_4` explicitly and **check it by hand-enumerating** the derangements of
`{1,2,3,4}`. Then show `D_n/n! → 1/e`.

*`D_4 = 9`, small enough to list completely — do list them. A formula you have verified by
enumeration once is a formula you trust under pressure.*

### Tier B — the target. At least four.

**B1.** How many ways to deal 52 cards into 4 hands of 13? Write it as a multinomial coefficient.
Then: how many ways to split 12 people into 4 **unlabelled** teams of 3?

*The second is the first divided by `4!`, and knowing **when** that division applies — labelled vs
unlabelled groups — is the most common counting error there is. Say out loud why bridge hands are
labelled (North/South/East/West) and generic teams are not.*

**B2.** How many lattice paths from `(0,0)` to `(m,n)` using only right and up steps?

*A path **is** a word in R's and U's, so counting paths = counting arrangements = A4's formula.
The first time a counting formula shows up wearing a disguise, which is the whole reason for
learning the names.*

**B3.** A committee of 5 from 6 men and 9 women, with at least 3 women. Count it.

*Case-split and add. Then say why you cannot instead count "choose 3 women, then choose 2 from the
rest" — that classic wrong answer overcounts, and explaining the overcount is worth more than the
right number.*

**B4.** How many non-negative integer solutions to `x₁+x₂+x₃+x₄ = 15`? How many **positive** ones?
How many with `x₁ ≥ 3, x₂ ≥ 1`?

*Three variants of one formula. Do all three in under five minutes or the substitution isn't
automatic yet.*

**B5.** A trader must allocate 10 identical units of risk budget across 4 strategies.
(a) How many allocations? (b) How many give every strategy at least 1 unit? (c) How many give
strategy A **no more than 3** units?

*(c) is the capacity constraint — the join between Parts 2 and 3. Attempt it cold with the
subtract-the-violations idea. This is also a real allocation-counting question, and the reason
stars and bars shows up in portfolio-construction interviews.*

**B6.** How many terms are in the expansion of `(x₁+x₂+⋯+x_k)ⁿ` before collecting like terms — and
how many **after**?

*Before: `kⁿ`. After: one term per multiset of exponents summing to `n`, i.e. `C(n+k−1, k−1)` —
stars and bars again, now counting monomials. The multinomial theorem and stars and bars are the
same object seen from two sides.*

**B7.** The birthday problem: with `n` people, `P(at least two share a birthday)`. Set it up by
complementary counting and say roughly where it crosses 50%.

*`n = 23`. It feels wrong because people count *people* (23) instead of *pairs* (`C(23,2) = 253`)
— and pairs is what matters. The most-asked probability puzzle in existence, and pure
complementary counting.*

**B8.** How many permutations of `1…n` have **exactly** `k` fixed points?

*`C(n,k)·D_{n−k}` — choose which `k` are fixed, derange the rest. Then note that
`P(exactly k fixed) → e^{−1}/k!`: the number of fixed points is asymptotically **Poisson(1)**.
Rare events, many trials, mean 1.*

### Tier C — only if A and B ran short.

**C1.** Prove Vandermonde's identity `C(m+n, k) = Σⱼ C(m,j)C(n,k−j)` combinatorially.
*Split the `m+n` items into two groups and condition on how many come from the first.*

**C2.** Prove the derangement recurrence `D_n = (n−1)(D_{n−1} + D_{n−2})` combinatorially.
*Condition on where element 1 goes and whether the swap is mutual.*

**C3.** How many surjections from an `n`-set onto a `k`-set?
*Inclusion–exclusion on "element `j` of the codomain is missed": `Σⱼ(−1)^j C(k,j)(k−j)ⁿ`.*

---

## Code problems

Both live in `src/solvers/s1_probability/counting_verify.py`. Standard library only, no test
framework. Each: one function computing the answer, one verifying it independently, and an
`assert` in `__main__` that fails loudly if they disagree.

### 1 · Stars and bars, checked by brute force

Count the ways to place `n` **identical** balls into `k` **labelled** bins.

> **Input:** `n ≥ 0` balls, `k ≥ 1` bins
> **Output:** the number of distinct distributions
> **Closed form:** `stars_and_bars(n, k)` returning `math.comb(n+k-1, k-1)`
> **Verify:** `brute_force(n, k)` enumerates all `k`-tuples via `itertools.product(range(n+1), repeat=k)`
> and counts those summing to `n`. Assert both agree for every `n ≤ 8`, `k ≤ 4`.

**Complexity:** closed form is `O(k)` multiplications; brute force is `O((n+1)^k · k)`. State both
in the docstring, **and state why the brute force is acceptable as a test at these sizes and
unacceptable as an implementation.**

### 2 · Derangements, three ways

Count the permutations of `n` items with **no** fixed point.

> **Input:** `n ≥ 1`
> **Output:** `D_n`, the number of derangements
> **Closed form:** `round(math.factorial(n) / math.e)`
> **Exact:** the same value from the recurrence `D_n = (n−1)(D_{n−1} + D_{n−2})`, `D_1 = 0`, `D_2 = 1`
> **Verify:** shuffle `list(range(n))` many times, estimate the fraction with no fixed point, and
> assert it lands within tolerance of `1/e` for `n = 10`.

*Monte Carlo is the right verifier here, unlike problem 1 — `10!` is 3.6M permutations, enough that
sampling beats enumeration. Choosing which of the two to reach for is the transferable skill.*

**Complexity:** closed form `O(1)` after `n!`; recurrence `O(n)` time and `O(1)` space; Monte Carlo
`O(trials · n)`. State all three.

**Tolerance:** pick the trial count so the standard error is comfortably under the assert
threshold, and say in a comment what you chose and why. A flaky assert is worse than none.

*Nothing for Part 1 — writing a solver for `C(n,k)` is re-implementing `math.comb`.*

---

## Deliverables

**Feynman note** — `progress/feynman_notes/F1_1_combinatorics.md`. One note for the whole topic.
- [ ] Teach-back per part, source closed
- [ ] The **decision table** (A2) in the summary table
- [ ] The bijection **drawn** for `n=4, k=3`, not just described
- [ ] Any `⚠️ GAP` logged — the next session opens on that list

**Problems**
- [ ] All of Tier A unhinted, on paper
- [ ] At least four from Tier B
- [ ] Log which needed hints

**Code** — both problems asserting, with complexity docstrings.

**Unlock test** — one week after the last part closes.

---

**When it gets hard and you start drifting:** stop reading, write the sentence you can't finish
into the note as a `⚠️ GAP`, and switch to Tier A on paper. Combinatorics especially — re-reading a
counting argument almost never fixes it, and writing out the `n=3` case by hand almost always does.
For stars and bars specifically, **draw `n=4, k=3` and enumerate**; the formula only becomes
obvious once you have physically written `**|*|*` a few times.

**If a session collapses:** Part 1 → A2 and A4. Part 2 → A5 and A7. Part 3 → A9 and A11.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A — counting rules (A1–A4)</summary>

**A1.** `P(n,k)`: fill `k` ordered slots — `n` choices for the first, `n−1` for the second, …,
`n−k+1` for the `k`-th. Product rule gives `n(n−1)⋯(n−k+1) = **n!/(n−k)!**`.

`C(n,k)`: every unordered set of `k` items was counted **`k!` times** in `P(n,k)`, once per
internal ordering. So `C(n,k) = P(n,k)/k! = **n!/(k!(n−k)!)**`.

**The one sentence:** *the `k!` divides out the orderings of the chosen set, which `P` counted
separately and we don't care about.*

**A2.** Choosing `k` from `n`:

| | **Order matters** | **Order doesn't** |
|---|---|---|
| **No repetition** | `n!/(n−k)!` | `C(n,k) = n!/(k!(n−k)!)` |
| **Repetition allowed** | `nᵏ` | `C(n+k−1, k)` ← **stars and bars, Part 2** |

(i) 3-digit PIN → `10³`, ordered with repetition.
(ii) Poker hand → `C(52,5)`, unordered, no repetition.
(iii) Podium from 8 → `P(8,3) = 336`, ordered, no repetition.
(iv) 4 scoops from 10, repeats OK, order irrelevant → `C(13,4) = 715` — **the bottom-right cell,
and the one you couldn't fill.** That is Part 2.
(v) MISSISSIPPI → none of the four cells: it is not "choose `k` from `n`" but "arrange a
multiset". Multinomial, `11!/(4!4!2!1!)`. *Noticing it doesn't fit is the point — the table covers
selection, A4 covers arrangement.*

**A3.** Fix a specific item, say item `n`. Every `k`-subset either contains it or does not — these
are disjoint and exhaustive.
- Contains item `n`: choose the other `k−1` from the remaining `n−1` → `C(n−1,k−1)`
- Does not: choose all `k` from the remaining `n−1` → `C(n−1,k)`

Sum: `C(n,k) = C(n−1,k−1) + C(n−1,k)` ∎

*Conditioning on one element, exactly as the geometric distribution conditions on the first trial.
This is also the recurrence that builds Pascal's triangle, and the dynamic-programming recurrence
you will meet again.*

**A4.** MISSISSIPPI has 11 letters: M×1, I×4, S×4, P×2.
`11!/(1!·4!·4!·2!) = 39,916,800/1152 = **34,650**` ✓

*Second derivation — choose positions:* `C(11,4)` for the I's, then `C(7,4)` of the remaining for
the S's, then `C(3,2)` for the P's, then `C(1,1)` for the M: `330 · 35 · 3 · 1 = **34,650**` ✓

**Why they agree:** expand the second — `[11!/(4!7!)]·[7!/(4!3!)]·[3!/(2!1!)]·1` — and every
intermediate factorial cancels telescopically, leaving `11!/(4!4!2!1!)`. **The
repeated-permutation formula and the multinomial coefficient are the same object**: arranging a
multiset *is* partitioning the 11 positions into labelled groups, one group per letter.

</details>

<details>
<summary>Tier A — stars and bars (A5–A8)</summary>

**A5.** Represent a distribution as a row of `n` stars (the identical balls) with `k−1` bars
inserted to divide them into `k` groups. `n=4, k=3`:

```
* * | * | *        →  (x₁,x₂,x₃) = (2,1,1)
* * * * | |        →  (4,0,0)
| * * | * *        →  (0,2,2)
```

The row has `n + (k−1)` symbol positions; choosing which `k−1` are bars determines everything. So
the count is `C(n+k−1, k−1)` — equivalently `C(n+k−1, n)`, choosing the star positions instead. ∎

**Both directions:** every arrangement of stars and bars reads off exactly one solution tuple (the
gaps between bars give the `xᵢ`), and every solution tuple writes down as exactly one arrangement.
One-to-one both ways, so the counts are equal.

**`k−1` bars, not `k`:** `k` bins need `k−1` internal dividers. Bars at the ends would be
redundant — the row already has two ends.

**A6.** (i) Non-negative, Prop 6.2: `C(20+4−1, 3) = C(23,3) = **1771**`.
(ii) Positive, Prop 6.1: `C(20−1, 3) = C(19,3) = **969**`.
(iii) Pre-allocate 2 to each child (8 candies), then distribute the remaining 12 freely:
`C(12+4−1, 3) = C(15,3) = **455**`.

**A7.** Substitute `yᵢ = xᵢ − cᵢ`, so `yᵢ ≥ 0` and `Σyᵢ = n − Σcᵢ`. The count is
`C(n − Σcᵢ + k − 1, k − 1)`.

When `Σcᵢ > n` the argument `n − Σcᵢ + k − 1` is less than `k − 1`, and `C(m,r) = 0` for `m < r`.
**The formula returns zero on its own** — correctly, since you cannot satisfy lower bounds summing
to more than you have to give.

**A8.** Choosing `k` items from `n` types with repetition, order irrelevant, means recording only
**how many of each type** you took. Let `xᵢ` = the number of type-`i` items chosen. Then `xᵢ ≥ 0`
and `Σxᵢ = k` — which is exactly balls-into-bins with `k` balls and `n` bins. So the count is
`C(k+n−1, n−1) = **C(n+k−1, k)**`.

**The bijection to name:** each *type* is a bin, each *selected item* is a ball.

Ice cream: 4 scoops from 10 flavours → `C(10+4−1, 4) = C(13,4) = **715**`, filling A2's
bottom-right cell.

</details>

<details>
<summary>Tier A — inclusion–exclusion (A9–A11)</summary>

**A9.** Two sets: `|A∪B| = |A| + |B| − |A∩B|`. Elements in both were counted twice on the right,
so subtract once.

Three: `|A∪B∪C| = |A|+|B|+|C| − |A∩B|−|A∩C|−|B∩C| + |A∩B∩C|`. An element in all three is counted
`3 − 3 + 1 = 1` time.

**General `n`.** Take an element in exactly `m` of the sets, `m ≥ 1`. It is counted `C(m,1)` times
in the singles, `C(m,2)` in the pairs, and so on. Its total contribution is

`Σₖ₌₁^m (−1)^{k+1} C(m,k) = −Σₖ₌₁^m (−1)^k C(m,k) = −[(1−1)^m − 1] = **1**`

by the binomial theorem. Every element in at least one set is counted exactly once, and elements
in none are counted zero times. ∎

**A10.** The counting and probability forms are the same identity with `|·|` in place of `P(·)`:
on a finite equiprobable space `P(A) = |A|/|S|`, so dividing the counting identity by `|S|` gives
the probability one. One statement, two readings.

Divisible by 2, 3, or 5 in `1…1000`:
`⌊1000/2⌋ + ⌊1000/3⌋ + ⌊1000/5⌋ = 500 + 333 + 200 = 1033`
`− ⌊1000/6⌋ − ⌊1000/10⌋ − ⌊1000/15⌋ = −166 − 100 − 66 = −332`
`+ ⌊1000/30⌋ = +33`
Total = **734**.

**Why lcm:** `x` is divisible by both `a` and `b` exactly when it is divisible by `lcm(a,b)` — the
common multiples of `a` and `b` are precisely the multiples of their least common multiple. For
coprime `a,b` that is `ab`, which is why the pairs above are 6, 10, 15.

**A11.** Let `Aᵢ` = "person `i` gets their own coat". Then `|Aᵢ| = (n−1)!`, `|Aᵢ∩Aⱼ| = (n−2)!`, and
generally an intersection of `k` of them has `(n−k)!` permutations. There are `C(n,k)` such
intersections, so

`|∪Aᵢ| = Σₖ₌₁ⁿ (−1)^{k+1} C(n,k)(n−k)! = Σₖ₌₁ⁿ (−1)^{k+1} n!/k!`

Derangements are the complement:
`D_n = n! − |∪Aᵢ| = n!·Σ_{k=0}^{n} (−1)^k/k!` ∎

`D_4 = 24(1 − 1 + 1/2 − 1/6 + 1/24) = 24 · 9/24 = **9**`.

The nine derangements of `1234`: `2143, 2341, 2413, 3142, 3412, 3421, 4123, 4312, 4321`. ✓

**The limit:** `Σ_{k=0}^{n} (−1)^k/k!` is the truncated series for `e^{−1}`, so `D_n/n! → 1/e ≈
0.368`. The tail is smaller than `1/(n+1)!`, so by `n = 7` the agreement is already to six decimal
places — **the answer stops depending on `n` almost immediately**, which is the counterintuitive
part worth saying out loud.

</details>

<details>
<summary>Tier B</summary>

**B1.** Bridge deal: `C(52; 13,13,13,13) = **52!/(13!)⁴** ≈ 5.36×10²⁸`. The four hands are
**labelled** — North's hand is a different outcome from South's, so no further division.

12 people into 4 unlabelled teams of 3: start with the multinomial `12!/(3!)⁴ = 369,600`, which
treats the teams as labelled Team 1…Team 4. The teams are interchangeable, so each partition was
counted `4!` times: `369,600/4! = **15,400**`.

**The rule:** divide by `m!` when the `m` groups are **indistinguishable**, don't when they carry
identities. Bridge seats have identities; "split into teams" usually does not. Getting this wrong
in either direction is the most common counting error at interview, and it is worth saying out
loud which one you are in before you compute.

**B2.** A path is a sequence of `m` R's and `n` U's in some order — every such word is exactly one
path, and every path exactly one word. So the count is the number of arrangements of that
multiset: `(m+n)!/(m!n!) = **C(m+n, m)**`.

*Same formula as A4, wearing a disguise. This is why the names matter: "arrangements of a
multiset", "lattice paths", and "which subset of steps are rights" are one problem.*

**B3.** At least 3 women from 6M/9W, committee of 5. Case-split on the number of women:
- 3W2M: `C(9,3)C(6,2) = 84·15 = 1260`
- 4W1M: `C(9,4)C(6,1) = 126·6 = 756`
- 5W0M: `C(9,5)C(6,0) = 126·1 = 126`

Total = **2142**.

*The classic wrong answer:* `C(9,3)·C(12,2) = 84·66 = 5544` — "pick 3 women, then any 2 from the
remaining 12." This **overcounts**, because a committee with 4 women is produced multiple times:
any 3 of its 4 women could have been the "chosen 3", with the 4th arriving in the second step. The
distinct-then-fill move only works when the two stages produce distinguishable roles.
**Overcounting is the failure mode of counting, and the cure is always to partition into disjoint
cases first.**

**B4.** Non-negative: `C(15+4−1, 3) = C(18,3) = **816**`.
Positive: `C(15−1, 3) = C(14,3) = **364**`.
With `x₁ ≥ 3, x₂ ≥ 1`: pre-allocate 4, distribute 11 freely →
`C(11+4−1, 3) = C(14,3) = **364**`.

**B5.** (a) `C(10+4−1, 3) = C(13,3) = **286**`.
(b) Each at least 1: `C(10−1, 3) = C(9,3) = **84**`.
(c) Strategy A at most 3. Total minus violations: violations are `x_A ≥ 4`, which by
pre-allocating 4 gives `C(6+4−1, 3) = C(9,3) = 84`. So `286 − 84 = **202**`.

*One violation event, so a single subtraction suffices. Multiple simultaneous capacity constraints
are where inclusion–exclusion becomes unavoidable — see B6's neighbour, C3.*

**B6.** Before collecting: each of the `n` factors contributes one of `k` variables independently,
so `**kⁿ**` terms.

After collecting: a distinct monomial is determined by the exponent vector `(e₁,…,e_k)` with
`eᵢ ≥ 0` and `Σeᵢ = n` — non-negative integer solutions, so `**C(n+k−1, k−1)**`.

*The multinomial theorem and stars and bars are the same object seen from two sides: the exponent
vector *is* the balls-into-bins allocation.*

**B7.** `P(≥1 shared) = 1 − P(all distinct) = 1 − (365·364⋯(365−n+1))/365ⁿ`.

At `n = 22` it is ≈0.476; at **`n = 23`** it is ≈0.507 — the crossing.

*It feels wrong because intuition counts people (23 against 365) rather than pairs: there are
`C(23,2) = 253` pairs, each with a `1/365` chance of matching, so the expected number of matching
pairs is ≈0.69. Pairs is what matters.*

**B8.** Choose which `k` positions are fixed (`C(n,k)`), then derange the remaining `n−k` so that
none of *those* is fixed: `**C(n,k)·D_{n−k}**`.

As `n → ∞`: `C(n,k)·D_{n−k}/n! = [1/k!]·[D_{n−k}/(n−k)!] → e^{−1}/k!` — which is the
**Poisson(1)** pmf. The number of fixed points in a random permutation is asymptotically Poisson
with mean 1, and the mean is 1 by linearity: `n` positions each fixed with probability `1/n`.

*Rare events, many trials, mean 1 — the same limit that turns a binomial into a Poisson.*

</details>

<details>
<summary>Tier C</summary>

**C1.** Vandermonde. Take `m` red items and `n` blue. Choosing `k` from all `m+n` gives
`C(m+n,k)`. Alternatively, condition on `j`, the number of reds chosen: pick `j` reds (`C(m,j)`)
and `k−j` blues (`C(n,k−j)`). The cases `j = 0…k` are disjoint and exhaustive, so
`C(m+n,k) = Σⱼ C(m,j)C(n,k−j)` ∎

*Same method as A3 — partition by a feature, count each block, add. A3 is the special case `m=1`.*

**C2.** Derangement recurrence. In a derangement of `1…n`, element 1 maps to some `i ≠ 1` —
`n−1` choices. Given that, split on where `i` maps:
- `i → 1` (a mutual swap): the remaining `n−2` elements must be deranged among themselves →
  `D_{n−2}`
- `i ↛ 1`: treat "`i` must not map to 1" as "`i` must not map to its own slot" in a relabelled
  problem on `n−1` elements → `D_{n−1}`

So `D_n = (n−1)(D_{n−1} + D_{n−2})` ∎

**C3.** Surjections from an `n`-set onto a `k`-set. Let `Bⱼ` = "codomain element `j` is missed".
Total functions `kⁿ`; subtract those missing at least one target:

`|surjections| = Σⱼ₌₀^k (−1)^j C(k,j)(k−j)ⁿ`

*Inclusion–exclusion on "something is missed" — the same shape as the derangement derivation,
where the missed thing was a fixed point.*

</details>
