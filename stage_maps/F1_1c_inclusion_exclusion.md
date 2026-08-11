---
type: stage
id: F1.1c
name: Inclusion–Exclusion and Derangements
kind: foundation
multiplier: 2.0
topic: "[[I-1-combinatorics-and-counting]]"
concepts: ["[[inclusion-exclusion]]", "[[bijection-proof]]", "[[complementary-counting]]"]
roles: ["[[quant-research]]", "[[market-making]]"]
sprint: S16
status: locked
budget_h: 2.5
actual_h: 
d4_due: 2026-08-22
baseline_closes: []
---

# Inclusion–Exclusion and Derangements — Stage Map
`F1.1c` · foundation (new install, 2.0×) · `topics/section_I` §1
**Sprint 16, Day 11 (Thu 08-13)** · **Budget: 2.5h**

> Shares the Feynman note `progress/feynman_notes/F1_1_combinatorics.md` with `F1.1a/b`.
> Write §1(c) today; **the note closes Saturday 08-15** — §2–§6, all three sub-stages.

> **⚠️ SOURCE CROSSES CHAPTERS — read this before opening the book.**
> `F1.1a` and `F1.1b` are Ross **Ch.1**. This stage is Ross **Ch.2 §2.5**, because that is where
> inclusion–exclusion actually lives (it is stated there as a probability identity, not a
> counting one). **Derangements are not a headed section anywhere** — Ross has them as a worked
> example in §2.5. They are therefore **written inline in §Stretch notes below**, in full.
>
> This is the `F1.4`-A5 / `F1.5`-A3 failure mode, caught in advance rather than after: a stage
> whose material is not in the chapter it claims. Naming the crossing is the fix
> (`04_deliverables_spec.md` §D2).

**Why this stage exists:** two reasons, and the second is the real one.

1. **Inclusion–exclusion** is the general answer to "count things satisfying *at least one* /
   *none* of several overlapping conditions" — and the overlap is what breaks naive counting.
   It is also the general form of `P(A∪B) = P(A) + P(B) − P(A∩B)`, which you will use far more
   often as a probability rule than as a counting one.
2. **Complementary counting.** The move "count the complement, subtract from the total" is the
   single highest-yield reflex in interview combinatorics — "at least one" almost always means
   "one minus none". Derangements are the canonical drill for it.

**Scope:**
1. **Two- and three-set** inclusion–exclusion, stated and proved by the element-counting argument
2. **General `n`-set** form, and the `(−1)^k` alternation
3. **Derangements** `D_n = n!·Σ(−1)^k/k!`, and the `D_n/n! → 1/e` limit
4. **Complementary counting** as a standalone habit

Out of scope: Möbius inversion, the general sieve, permanents. Surjection counting is Tier C.

---

## Knowledge checklist — tick when you can produce it cold

**Built from Ross Ch.2 §2.5's actual content** (verify the section number against your copy on
opening — 6th ed. puts the inclusion–exclusion identity in §2.5 with the matching problem as
its principal example).

**§2.5 Inclusion–exclusion**
- [ ] `P(A∪B) = P(A) + P(B) − P(A∩B)` — and **why** the subtraction (`A∩B` counted twice)
- [ ] Three sets: `+singles − pairs + triple`
- [ ] General form: `P(∪Aᵢ) = Σ|Aᵢ| − Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩A_k| − ⋯ + (−1)^{n+1}|∩Aᵢ|`
- [ ] **The counting version is the same statement** with `|·|` instead of `P(·)` — one
      identity, two readings
- [ ] Why the signs alternate: an element in exactly `m` of the sets must be counted **once**,
      and `Σₖ (−1)^{k+1} C(m,k) = 1` for `m ≥ 1` *(this is the proof, and it is one line
      from the binomial theorem)*

**Derangements (worked example, not a headed section — see §Stretch notes)**
- [ ] `D_n = n!·Σ_{k=0}^{n} (−1)^k/k!` by inclusion–exclusion on "person `i` gets their own coat"
- [ ] `D_n/n! → 1/e ≈ 0.368` — **the probability nobody gets their own coat, for large `n`**
- [ ] That the limit is essentially exact by `n = 7`, and **does not depend on `n`** in any
      practically useful way — the counterintuitive part, and the interview hook
- [ ] Recurrence `D_n = (n−1)(D_{n−1} + D_{n−2})` *(state it; deriving it is Tier C)*

**Complementary counting**
- [ ] "At least one" → `1 − P(none)`, and when that is easier than the direct count
- [ ] The birthday-problem shape: `P(≥1 shared) = 1 − (365·364⋯)/365ⁿ`

### Stretch — beyond Ross §2.5

- [ ] **Surjection counting** `k!·S(n,k) = Σⱼ(−1)^j C(k,j)(k−j)ⁿ`
      → **Tier C2, optional.** It is inclusion–exclusion applied to "some codomain element is
      missed", and it is the honest general form of the twelvefold way's hardest cell.
      *Do it only if A+B finished early.*
- [ ] **Möbius inversion / the general sieve**
      → **DEFERRED, no stage assigned.** Reason: it is the number-theory generalisation and has
      no quant-interview footprint. Named only so the word is not alarming.

---

## Stretch notes — derangements, in full

*Ross has this as an example, not a section. Written out here so the stage does not depend on
finding it.*

**The problem.** `n` people check coats; coats are returned at random. What is the probability
**nobody** gets their own coat?

**Set up the complement.** Let `Aᵢ` = "person `i` gets their own coat". You want
`P(no fixed points) = 1 − P(A₁ ∪ ⋯ ∪ Aₙ)`.

**Count the intersections.** If a specific set of `k` people all get their own coats, the
remaining `n−k` coats are arbitrary: `(n−k)!` permutations. There are `C(n,k)` such sets, so
```
Σ over k-subsets |Aᵢ₁ ∩ ⋯ ∩ Aᵢₖ| = C(n,k)·(n−k)! = n!/k!
```
*That collapse — `C(n,k)(n−k)! = n!/k!` — is the whole computation. Everything else is
bookkeeping.*

**Apply inclusion–exclusion.**
```
|A₁ ∪ ⋯ ∪ Aₙ| = Σₖ₌₁ⁿ (−1)^{k+1} · n!/k!
D_n = n! − |A₁ ∪ ⋯ ∪ Aₙ| = n!·Σₖ₌₀ⁿ (−1)^k/k!
```

**The limit.** `Σₖ₌₀^∞ (−1)^k/k! = e^{−1}`, so
```
P(derangement) = D_n/n! → 1/e ≈ 0.3679
```
Convergence is *fast* — the error after `n` terms is under `1/(n+1)!`, so `n=7` already
matches `1/e` to four decimals.

**Why it is asked:** the answer barely depends on `n`. With 5 people or 5,000, it is about 37%.
That is genuinely surprising, it is one line to state, and the derivation shows whether you can
run inclusion–exclusion under pressure. *`e` appearing in a pure counting problem, with no
calculus in sight, is the same species of surprise as `π` in the Gaussian integral.*

---

## Source

| Source | Covers | Time |
|---|---|---|
| **Ross, *A First Course in Probability* 6th ed. — Ch. 2, §2.5** | Inclusion–exclusion + the matching problem | **40 min, hard stop** |
| **§Stretch notes above** | Derangements in full | *(already written — do not go hunting)* |

**Ross states this probabilistically** (`P(∪Aᵢ)`), not as a counting formula. They are the same
identity — the counting version is the probability version times the sample-space size. Read it
as stated and do the translation yourself; that translation is Tier A-A2.

**Input cap: 40 min.**

**Pass 2 for `F1.1b` happens first today** (Adj #12): open with **≤20 min re-reading only what
Wednesday's `⚠️ GAP` list names.** New material gets two passes on separate days, and today is
`F1.1b`'s second day. Do not skip this to get to the new chapter.

---

## The shape of the block (2.5h)

| Block | Minutes | Do |
|---|---:|---|
| **`F1.1b` Pass 2** | 20 | Re-read **only** the `⚠️ GAP` list from Wednesday |
| Read | 40 | Ross §2.5, hard stop |
| Teach-back | 15 | Note §1(c) — book **closed** |
| Tier A | 45 | A1–A3 on paper |
| Tier B | 20 | B1–B2 |
| Code | 10 | `F1.1-CODE2` |

**If the day collapses: A1, A3.** A1 is the identity itself; A3 is derangements, the named
interview classic. Skip Pass 2 only if the `⚠️ GAP` list is empty.

**The drift move (Adj #13):** stop reading, write the unfinished sentence into note §2 as a
`⚠️ GAP`, switch to Tier A on paper. **For inclusion–exclusion specifically: do `n=3` with an
actual Venn diagram.** The general formula is unreadable until the three-set picture is in
your hand; the picture makes the alternation obvious in about thirty seconds.

---

## Tier A — the floor (all three, unhinted, on paper)

**F1.1c-A1.** State and prove two-set inclusion–exclusion, then three-set. **Prove the general
`n`-set version** by the element-counting argument: take an element lying in exactly `m` of the
sets and show the right-hand side counts it exactly once.
*The proof is `Σₖ₌₁^m (−1)^{k+1}C(m,k) = 1`, which is `1 − (1−1)^m` by the binomial theorem.
That is the entire content of inclusion–exclusion, and it fits on one line — worth knowing
because "prove it" is a fair follow-up to "state it".*

**F1.1c-A2.** Write the **counting** form alongside the **probability** form and say why they
are the same statement. Then: how many integers in `1…1000` are divisible by 2, 3, or 5?
*The classic drill. Also: `|A∩B|` for divisibility is a divisibility by the lcm — say why
that is, don't just use it.*

**F1.1c-A3.** Derive `D_n` from scratch by inclusion–exclusion on the events `Aᵢ` = "person `i`
gets their own coat". Compute `D_4` explicitly and **check it by hand-enumerating** the
derangements of `{1,2,3,4}`. Then show `D_n/n! → 1/e`.
*`D_4 = 9`, small enough to list completely — do list them. A formula you have verified by
enumeration once is a formula you trust under pressure.*

---

## Tier B — the target (≥2 of 3)

**F1.1c-B1.** Finish `F1.1b`-C1 properly: how many non-negative integer solutions to
`x₁+x₂+x₃+x₄ = 6` with **every `xᵢ ≤ 2`**? Use inclusion–exclusion on the violation events
`Bᵢ` = "`xᵢ ≥ 3`", and check against Wednesday's hand count.
*This is the capacity constraint `F1.1b` deferred to today. The two stages join here, and the
join is the point: stars and bars counts the unconstrained total, inclusion–exclusion removes
the violations.*

**F1.1c-B2.** The birthday problem: with `n` people, `P(at least two share a birthday)`.
Set it up by complementary counting and say roughly where it crosses 50%.
*`n = 23`. The reason it feels wrong is that people count *people* (23) instead of *pairs*
(`C(23,2) = 253`) — and pairs is what matters. This is the most-asked probability puzzle in
existence and it is pure complementary counting.*

**F1.1c-B3.** How many permutations of `1…n` have **exactly** `k` fixed points?
*`C(n,k)·D_{n−k}` — choose which `k` are fixed, derange the rest. Then note that
`P(exactly k fixed) → e^{−1}/k!`: the number of fixed points is asymptotically **Poisson(1)**.
That connects straight back to `F1.4` — rare events, many trials, mean 1.*

---

## Tier C — only if A+B ran short

**F1.1c-C1.** Prove the derangement recurrence `D_n = (n−1)(D_{n−1} + D_{n−2})` combinatorially.
*Condition on where element 1 goes and whether the swap is mutual.*

**F1.1c-C2.** How many surjections from an `n`-set onto a `k`-set?
*Inclusion–exclusion on "element `j` of the codomain is missed":
`Σⱼ(−1)^j C(k,j)(k−j)ⁿ`.*

---

## Code problems

Add to `src/solvers/s1_probability/counting_verify.py` (created by `F1.1b`).

**F1.1-CODE2** — Derangements. Write `derangements(n)` from the formula
`round(math.factorial(n) / math.e)` *(valid for `n ≥ 1`)* **and** an exact version from the
recurrence, plus a Monte Carlo check: shuffle `list(range(n))` many times and estimate the
fraction with no fixed point. Assert the MC estimate is within tolerance of `1/e` for `n = 10`.
*Here MC **is** the right verifier — unlike `F1.1b`, where exact enumeration was cheap,
`10! = 3.6M` permutations is enough that sampling is the sensible check. Pick your `n_trials`
so the standard error is comfortably under the assert threshold and say in a comment what you
chose and why. A flaky assert is worse than no assert.*

*Docstring: closed form `O(1)` after `n!`; recurrence `O(n)` time, `O(1)` space; MC
`O(trials · n)`. State all three.*

---

## Deliverables

**D1 — Feynman note** `progress/feynman_notes/F1_1_combinatorics.md` — **§1(c) today, then
CLOSE THE NOTE SATURDAY**
- [ ] §1(c) teach-back: inclusion–exclusion + derangements, source closed
- [ ] **Saturday close:** §2 gaps · §3 napkin ≤200 words, said out loud · §4 where I'd meet it ·
      **§5 the decision table + the I–E identity** · §6 where this breaks (≥2)
- [ ] Zero unresolved `⚠️ GAP`

**Note §5 for `F1.1` is the decision table, not a distribution table** — `F1.1a`-A2's four
cells, plus one row each for the multinomial, stars-and-bars, and inclusion–exclusion forms.
That table is the deliverable the D4 test reproduces cold.

**D2 — Problems** (this file)
- [ ] A1–A3 unhinted, on paper
- [ ] ≥2 of Tier B
- [ ] Log which needed hints

**D3 — Code**
- [ ] `F1.1-CODE2` in `counting_verify.py`, asserting, with the complexity docstring

**D3.5 — Concept notes** (2 minutes each, at Saturday's close)
- [ ] `vault/concepts/inclusion-exclusion.md`
- [ ] `vault/concepts/bijection-proof.md` — started by `F1.1b`'s stars-and-bars argument
- [ ] `vault/concepts/complementary-counting.md`
- [ ] `vault/concepts/ordered-vs-unordered.md` — from `F1.1a`'s decision table
- [ ] Set `status: ready-for-test` and `actual_h:` in **all three** `F1.1x` maps

**D4 — Unlock test → 2026-08-22**, one test covering `F1.1a/b/c` together.
- [ ] 5 fresh questions, 45 min, closed-book (Feynman note allowed). Pass ≥80%.
- [ ] Grade the day after.
- [ ] **Not on Sat 08-15** — that day carries four already-overdue D4 tests
      (`R.calculus`, `R.linalg`, `F1.4`, `F1.5`), which are the higher priority.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** Two sets: `|A∪B| = |A| + |B| − |A∩B|`. Elements of `A∩B` are counted in both `|A|` and
`|B|`, so once must be removed.

Three: `|A∪B∪C| = |A|+|B|+|C| − |A∩B|−|A∩C|−|B∩C| + |A∩B∩C|`. An element in all three is
counted `3` times by the singles, removed `3` times by the pairs — reaching 0 — so it must be
added back once.

**General proof.** Take an element in exactly `m` of the sets (`m ≥ 1`). On the right-hand side
it is counted `C(m,k)` times in the `k`-fold intersection sum, with sign `(−1)^{k+1}`. Total:
```
Σₖ₌₁^m (−1)^{k+1} C(m,k) = −Σₖ₌₁^m (−1)^k C(m,k)
                         = −[ (1−1)^m − C(m,0) ]      ← binomial theorem
                         = −[ 0 − 1 ] = 1
```
Counted exactly once — which is what `|∪Aᵢ|` requires. Elements in no set contribute 0 to both
sides. ∎

**A2.** Counting form `|∪Aᵢ| = Σ|Aᵢ| − Σ|Aᵢ∩Aⱼ| + ⋯`; probability form is the same with
`P(·)`. They are equivalent because `P(A) = |A|/|S|` for equally likely outcomes — divide the
counting identity through by `|S|`. *Ross states the probability version because Ch.2 is about
probability; the counting version is what you use in Ch.1-style problems.*

Divisible by 2, 3, or 5 in `1…1000`:
```
|2| = 500 · |3| = 333 · |5| = 200
|2∩3| = ⌊1000/6⌋ = 166 · |2∩5| = 100 · |3∩5| = 66
|2∩3∩5| = ⌊1000/30⌋ = 33
500+333+200 − 166−100−66 + 33 = **734**
```
`|A∩B|` is divisibility by `lcm(a,b)`: a number divisible by both `a` and `b` is divisible by
their least common multiple, and conversely. For coprime `a,b` that is just `ab`, which is why
`2∩3` is `⌊1000/6⌋`.

**A3.** `Aᵢ` = person `i` gets their own coat. `|Aᵢ₁∩⋯∩Aᵢₖ| = (n−k)!` (those `k` fixed, rest
free), and there are `C(n,k)` such intersections, so the `k`-th sum is
`C(n,k)(n−k)! = n!/k!`.
```
|∪Aᵢ| = Σₖ₌₁ⁿ (−1)^{k+1} n!/k!
D_n   = n! − |∪Aᵢ| = n! Σₖ₌₀ⁿ (−1)^k/k!
```
`D_4 = 24(1 − 1 + 1/2 − 1/6 + 1/24) = 24·(9/24) = **9**`.

The nine derangements of `1234`: `2143, 2341, 2413, 3142, 3412, 3421, 4123, 4312, 4321`. ✓

Limit: `Σₖ₌₀^∞(−1)^k/k!` is the Taylor series of `e^x` at `x = −1`, so
`D_n/n! → **e^{−1} ≈ 0.3679**`. Already 0.3667 at `n=4`, 0.36788 at `n=7`.

</details>

<details>
<summary>Tier B</summary>

**B1.** `x₁+⋯+x₄ = 6`, all `xᵢ ≤ 2`. Total unconstrained: `C(6+3,3) = C(9,3) = 84`.
`Bᵢ` = "`xᵢ ≥ 3`": substitute, 3 units left → `C(3+3,3) = C(6,3) = 20`, and there are 4 such.
`Bᵢ∩Bⱼ`: both ≥3 uses all 6, leaving 0 → `C(0+3,3) = C(3,3) = 1`, and there are `C(4,2)=6`.
Triples impossible (would need 9 > 6).
```
84 − 4(20) + 6(1) = 84 − 80 + 6 = **10**
```
*Cross-check against `F1.1b`-C1, which asked for every `xᵢ ∈ {1,2}` — that was the extra
constraint "no bin empty", giving 6. Here empty bins are allowed, giving 10. The four extra
are the `(2,2,2,0)` arrangements: `C(4,1) = 4`. `6 + 4 = 10` ✓*

**B2.** `P(no shared) = 365·364⋯(365−n+1)/365ⁿ = P(365,n)/365ⁿ`, so
`P(at least one shared) = 1 − P(365,n)/365ⁿ`.

At `n = 22`: 0.4757. At `n = **23**`: 0.5073 — crosses 50%.

*Why it surprises: with 23 people there are `C(23,2) = 253` pairs, each with a `1/365` chance
of matching. `253/365 ≈ 0.69`, and `1 − e^{−0.69} ≈ 0.50` — the right ballpark by the Poisson
approximation. **Count the pairs, not the people.** The direct "at least one" computation would
require summing over every collision pattern; the complement is a single product. That is the
entire case for complementary counting.*

**B3.** Choose the `k` fixed points (`C(n,k)`), derange the remaining `n−k`
(`D_{n−k}` — they must have no further fixed points, or you'd have more than `k`):
`**C(n,k)·D_{n−k}**`.

`P(exactly k) = C(n,k)D_{n−k}/n! → (1/k!)·e^{−1}` as `n → ∞`, which is the **Poisson(1)** pmf.
*Fixed points are rare events (`1/n` each) across many trials (`n` of them) with mean `n·(1/n)
= 1` — precisely the `F1.4` Poisson limit regime. The expected number of fixed points is
exactly 1 for every `n ≥ 1`, by linearity of expectation, and that is worth saying: it needs no
inclusion–exclusion at all.*

</details>

<details>
<summary>Tier C</summary>

**C1.** Where does element 1 go? Some `j ≠ 1`, so `n−1` choices. Then either:
- `j` maps back to 1 (a mutual swap): the remaining `n−2` elements must be deranged → `D_{n−2}`
- `j` does not map to 1: treat "`j` must not map to 1" as "`j` must not map to its own
  position" in a relabelled problem on `n−1` elements → `D_{n−1}`

So `D_n = (n−1)(D_{n−1} + D_{n−2})` ∎ with `D_1 = 0`, `D_2 = 1`.
*Check: `D_3 = 2(1+0) = 2` ✓ · `D_4 = 3(2+1) = 9` ✓*

**C2.** Surjections from `[n]` onto `[k]`. Let `Cⱼ` = "codomain element `j` is not hit".
Total functions `kⁿ`; functions missing a specified set of `j` elements: `(k−j)ⁿ`.
```
#surjections = Σⱼ₌₀^k (−1)^j C(k,j)(k−j)ⁿ
```
This equals `k!·S(n,k)` where `S(n,k)` is the Stirling number of the second kind — partition
into `k` unlabelled blocks, then label them.

</details>
