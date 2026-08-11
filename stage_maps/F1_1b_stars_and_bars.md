---
type: stage
id: F1.1b
name: Stars and Bars
kind: foundation
multiplier: 2.0
topic: "[[I-1-combinatorics-and-counting]]"
concepts: ["[[bijection-proof]]", "[[ordered-vs-unordered]]"]
roles: ["[[quant-research]]", "[[risk-management]]"]
sprint: S16
status: locked
budget_h: 2.5
actual_h: 
d4_due: 2026-08-22
baseline_closes: []
---

# Stars and Bars — Stage Map
`F1.1b` · foundation (new install, 2.0×) · `topics/section_I` §1
**Sprint 16, Day 10 (Wed 08-12)** · **Budget: 2.5h**

> Shares the Feynman note `progress/feynman_notes/F1_1_combinatorics.md` with `F1.1a` and
> `F1.1c`. Write §1(b) today; the note closes Saturday.

> **Prereq: `F1.1a` (Mon 08-10).** This stage is the bottom-right cell of A2's decision table —
> the one you could not fill. Open the map with that table in front of you.

**Why this stage exists:** "how many ways to distribute `n` identical things into `k` labelled
bins" is one formula, and it is the formula people fail to recognise. Unlike `F1.1a`, there is
no baseline evidence you have this — I.1 tested arrangement, not distribution. It also carries
the stage's real transferable skill: **proof by bijection.** You don't count the hard thing;
you build a one-to-one correspondence with an easy thing and count that instead. That move
recurs in lattice paths, in Catalan numbers, and in every "map this problem to a known one"
interview prompt.

**Scope:**
1. **The bijection** — `n` identical balls into `k` labelled bins ⟷ arrangements of `n` stars
   and `k−1` bars
2. **`C(n+k−1, k−1)`** — the count, and why it is `k−1` bars and not `k`
3. **Lower bounds** — "each bin gets at least one" → `C(n−1, k−1)`, by pre-filling
4. **Upper bounds** — capacity constraints, by inclusion–exclusion *(the hook into `F1.1c`)*

Out of scope: unlabelled bins (that is integer partitions — no closed form, deferred),
the full twelvefold way.

---

## Knowledge checklist — tick when you can produce it cold

**Built from Ross Ch.1 §1.6** ("The number of integer solutions of equations") — this is
Ross's name for stars and bars, and the chapter never uses the phrase "stars and bars".
**Expect the section to look unfamiliar by title; it is the right one.**

**§1.6 Integer solutions**
- [ ] **Proposition 6.1:** number of **positive** integer solutions to `x₁+⋯+x_k = n`
      is `C(n−1, k−1)`
- [ ] **Proposition 6.2:** number of **non-negative** integer solutions is `C(n+k−1, k−1)`
- [ ] Which of the two is the default "balls into bins" answer, and why *(non-negative —
      empty bins are allowed unless the problem forbids them)*
- [ ] The bijection itself: a solution ⟷ a row of `n` stars with `k−1` bars inserted
- [ ] **Why `k−1` bars, not `k`** — bars are the *dividers between* bins, and `k` bins have
      `k−1` gaps between them

**Derived moves (in the chapter's examples, not headed)**
- [ ] **Lower bound `xᵢ ≥ 1`:** substitute `yᵢ = xᵢ − 1`, reduces to the non-negative case
      with `n − k` stars
- [ ] **General lower bound `xᵢ ≥ cᵢ`:** pre-allocate `Σcᵢ`, then distribute the remainder
- [ ] Equivalence of the three phrasings — *integer solutions* = *identical balls into
      labelled bins* = *unordered selection with repetition* (`F1.1a`-A2's missing cell)

### Stretch — NOT in Ross Ch.1 §1.6

- [ ] **Upper bounds / capacity constraints** (`xᵢ ≤ cᵢ`)
      → **INLINE, see §Stretch notes below**, but the *technique* is inclusion–exclusion, which
      is **`F1.1c` tomorrow**. Today: know that the naive stars-and-bars answer is wrong when a
      cap exists, and know the name of the fix. Do not try to compute it today.
- [ ] **Unlabelled bins → integer partitions `p(n)`**
      → **DEFERRED, no stage assigned.** Reason: no closed form exists; it is a DP problem, and
      it belongs with S10 dynamic programming rather than with counting formulas. Named here so
      you know the labelled/unlabelled distinction is load-bearing, not so you compute it.

---

## Stretch notes

### Capacity constraints (read only after B3, or if stuck)

How many non-negative solutions to `x₁+x₂+x₃ = 10` with **`x₁ ≤ 4`**?

Count everything, then subtract what violates:
```
total (no cap)          C(10+3−1, 2) = C(12,2) = 66
violating x₁ ≥ 5:       set y₁ = x₁−5 ≥ 0, so y₁+x₂+x₃ = 5
                        C(5+3−1, 2) = C(7,2) = 21
answer                  66 − 21 = 45
```
**The trick is the substitution:** "`x₁ ≥ 5`" becomes an unconstrained problem with 5 fewer
stars. With two or more caps, the violation sets overlap and you need full
inclusion–exclusion — which is exactly `F1.1c`. That is why the two stages sit adjacent.

---

## Source — one book, one sitting

| Source | Covers | Time |
|---|---|---|
| **Ross, *A First Course in Probability* 6th ed. — Ch. 1, §1.6** | Both propositions + examples | **40 min per pass, hard stop** |

**§1.6 is short — a few pages and two propositions.** If you finish the reading in 15 minutes,
that is correct, not a sign you missed something. The hours in this stage are meant to go into
problems, because the failure mode with stars and bars is never "I didn't read it", it is
"I didn't recognise it."

**Two passes, separate sittings — this is new material** (Adj #12). Pass 2 is the 20-minute
re-read at the top of `F1.1c` (Thu 08-13), opening on your `⚠️ GAP` list.

**Input cap: 40 min.**

---

## The shape of the block (2.5h)

| Block | Minutes | Do |
|---|---:|---|
| Read | 40 | Ross §1.6, hard stop |
| Teach-back | 20 | Note §1(b) — book **closed**, and **draw the bijection** |
| Tier A | 55 | A1–A4 on paper |
| Tier B | 25 | B1–B2 |
| Code | 20 | `F1.1-CODE1` |

**If the day collapses: A1, A3.** A1 is the bijection (without it the formula is a magic
string); A3 is the lower-bound substitution (the most-asked variant).

**The drift move (Adj #13):** stop reading, write the unfinished sentence into note §2 as a
`⚠️ GAP`, switch to Tier A on paper. **For this stage specifically: draw `n=4, k=3` by hand
and enumerate.** Stars and bars is a formula that only becomes obvious once you have physically
written out `**|*|*` a few times. Small cases beat re-reading, every time.

---

## Tier A — the floor (all four, unhinted, on paper)

**F1.1b-A1.** Derive `C(n+k−1, k−1)` for the number of ways to place `n` **identical** balls
into `k` **labelled** bins. Build the bijection explicitly: draw the stars-and-bars diagram
for `n=4, k=3`, write down the solution `(x₁,x₂,x₃)` it corresponds to, and **state why the
correspondence is one-to-one in both directions.**
*A bijection proof needs both directions — every arrangement gives exactly one solution, and
every solution exactly one arrangement. Saying only one direction is the standard incomplete
answer, and an interviewer will ask for the other.*

**F1.1b-A2.** Answer these, and for each say which proposition applies:
(i) 20 identical candies to 4 children, any number each
(ii) 20 identical candies to 4 children, **each gets at least 1**
(iii) 20 identical candies to 4 children, **each gets at least 2**
*(iii) is the `F1.1b` version of the topic file's named problem. The move for (ii) and (iii)
is the same substitution — do (iii) by pre-allocating, not by a new formula.*

**F1.1b-A3.** State the substitution `yᵢ = xᵢ − cᵢ` in general: how many non-negative integer
solutions to `x₁+⋯+x_k = n` with `xᵢ ≥ cᵢ` for each `i`? **Say what happens when `Σcᵢ > n`**,
and why the formula must return zero there.
*Edge cases are where counting formulas get tested. `C(m, r)` with `m < r` is 0, and the
formula handles it — but only if you know that's what `C` does.*

**F1.1b-A4.** Show that "unordered selection of `k` items from `n` types, repetition allowed"
= `C(n+k−1, k)` **is the same problem as balls-into-bins.** Then fill in `F1.1a`-A2's
missing bottom-right cell, and confirm the ice-cream answer: 4 scoops from 10 flavours.
*Two problems, one formula, and they look nothing alike until you name the bijection: each
**type** is a bin, each **selected item** is a ball. This is the recognition step that the
whole stage exists to install.*

---

## Tier B — the target (≥2 of 3)

**F1.1b-B1.** How many non-negative integer solutions to `x₁+x₂+x₃+x₄ = 15`? How many
**positive** ones? How many with `x₁ ≥ 3, x₂ ≥ 1`?
*Three variants of one formula. Do all three in under five minutes or the substitution isn't
automatic yet.*

**F1.1b-B2.** A trader must allocate 10 identical units of risk budget across 4 strategies.
(a) How many allocations? (b) How many give every strategy at least 1 unit? (c) How many give
strategy A **no more than 3** units?
*(c) is the capacity constraint — attempt it cold with the subtract-the-violations idea before
reading §Stretch notes. Also: this is a real allocation-counting question, and the reason
stars-and-bars shows up in portfolio-construction interviews.*

**F1.1b-B3.** ⚡ How many terms are there in the expansion of `(x₁+x₂+⋯+x_k)ⁿ` before
collecting like terms — and how many **after**?
*Before: `kⁿ`. After: one term per multiset of exponents summing to `n`, i.e.
`C(n+k−1, k−1)` — stars and bars again, now counting monomials. The multinomial theorem and
stars and bars are the same combinatorial object seen from two sides.*

---

## Tier C — only if A+B ran short

**F1.1b-C1.** How many ways to distribute `n` identical balls into `k` labelled bins with
**no bin empty and no bin holding more than 2**? Do `n=6, k=4` by hand.
*Small enough to brute-force, and the answer disagrees with naive stars-and-bars — which is
the motivation for tomorrow's inclusion–exclusion.*

---

## Code problems

Add to `src/solvers/s1_probability/` (created by `F1.5`). New file:
`src/solvers/s1_probability/counting_verify.py`. Docstring with time + space complexity
(baseline adj #9), one `assert`-based `__main__`, no test framework.

**F1.1-CODE1** — Stars and bars, verified by brute force. Write
`stars_and_bars(n, k)` returning `math.comb(n+k-1, k-1)`, and
`brute_force(n, k)` enumerating tuples via `itertools.product` and counting those summing to
`n`. Assert they agree for all `n ≤ 8`, `k ≤ 4`.
*The verifier here is **exact enumeration**, not Monte Carlo — the answer is an integer and
small cases are cheap, so an exact check is strictly better than a statistical one. Use MC only
when exact enumeration is infeasible.*

*Complexity note for the docstring: the closed form is `O(k)` multiplications; the brute force
is `O((n+1)^k · k)`. State both, and state why the brute force is acceptable **as a test** at
these sizes and unacceptable as an implementation.*

---

## Deliverables

**D1 — Feynman note** `progress/feynman_notes/F1_1_combinatorics.md` **§1(b)**
- [ ] Teach-back for stars and bars, source closed
- [ ] **The bijection drawn**, not just described — `n=4, k=3` in the note
- [ ] `F1.1a`-A2's decision table completed (the bottom-right cell)
- [ ] Any `⚠️ GAP` logged in §2 — Pass 2 tomorrow opens on this list

**D2 — Problems** (this file)
- [ ] A1–A4 unhinted, on paper
- [ ] ≥2 of Tier B
- [ ] Log which needed hints

**D3 — Code**
- [ ] `F1.1-CODE1` in `counting_verify.py`, asserting, with the complexity docstring

**D3.5 — Concept notes:** at `F1.1c` close (Sat), not today.

**D4 — Unlock test:** shared across `F1.1a/b/c` on **2026-08-22**.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** Represent a distribution as a row of `n` stars (the identical balls) with `k−1` bars
inserted to divide them into `k` groups. `n=4, k=3`:

```
* * | * | *        →  (x₁,x₂,x₃) = (2,1,1)
* * * * | |        →  (4,0,0)
| * * | * *        →  (0,2,2)
```

The row has `n + (k−1)` symbol positions; choosing which `k−1` are bars determines everything.
So the count is `C(n+k−1, k−1)` — equivalently `C(n+k−1, n)`, choosing the star positions
instead. ∎

**Both directions:** *Arrangement → solution:* given any row, read off the gap sizes; that is
one specific tuple. *Solution → arrangement:* given any `(x₁,…,x_k)` with `xᵢ ≥ 0` summing to
`n`, write `x₁` stars, a bar, `x₂` stars, a bar, …; that is one specific row. Neither map loses
or duplicates anything, so it is a bijection and the counts are equal.

**Why `k−1` bars:** bars are **dividers**, and `k` groups in a row have `k−1` boundaries
between them. The ends of the row are not divisions. Using `k` bars counts something else
(`k+1` bins).

**A2.**
(i) `n=20, k=4`, non-negative → `C(20+4−1, 3) = C(23,3) = **1771**`
(ii) each ≥ 1 → positive solutions → `C(20−1, 3) = C(19,3) = **969**`
    *(or: pre-allocate 1 each, distribute the remaining 16 freely → `C(16+3, 3) = C(19,3)` ✓)*
(iii) each ≥ 2 → pre-allocate 8, distribute remaining 12 freely →
    `C(12+4−1, 3) = C(15,3) = **455**`

**A3.** With `xᵢ ≥ cᵢ`, set `yᵢ = xᵢ − cᵢ ≥ 0`. Then `Σyᵢ = n − Σcᵢ`, an unconstrained
non-negative problem:
`**C(n − Σcᵢ + k − 1, k − 1)**`

If `Σcᵢ > n` the required minimum exceeds what's available, so there are **zero** solutions —
and the formula agrees, because the top argument `n − Σcᵢ + k − 1` is then less than `k−1`,
and `C(m,r) = 0` for `m < r`. *The formula is self-policing, which is why it is worth trusting
over ad-hoc casework.*

**A4.** Choosing `k` items from `n` **types** with repetition, order irrelevant: an outcome is
fully described by *how many of each type you took* — `(x₁,…,x_n)` with `xᵢ ≥ 0` and
`Σxᵢ = k`. That is literally balls-into-bins with `k` balls and `n` bins:
`**C(k+n−1, n−1) = C(n+k−1, k)**`.

**The bijection: type ⟷ bin, selected item ⟷ ball.**

Ice cream: 4 scoops, 10 flavours → `C(10+4−1, 4) = C(13,4) = **715**` ✓ *(matches
`F1.1a`-A2 (iv))*.

The bottom-right cell of the decision table is `C(n+k−1, k)` — **unordered, with repetition**.

</details>

<details>
<summary>Tier B</summary>

**B1.** `x₁+x₂+x₃+x₄ = 15`:
- non-negative: `C(15+4−1, 3) = C(18,3) = **816**`
- positive: `C(15−1, 3) = C(14,3) = **364**`
- `x₁ ≥ 3, x₂ ≥ 1`: pre-allocate 4, so `C(11+4−1, 3) = C(14,3) = **364**`

**B2.** 10 units across 4 strategies:
(a) `C(10+4−1, 3) = C(13,3) = **286**`
(b) each ≥ 1 → `C(9,3) = **84**`
(c) `x_A ≤ 3`: total 286, minus those with `x_A ≥ 4` (substitute, 6 units left):
`C(6+4−1, 3) = C(9,3) = 84`. Answer `286 − 84 = **202**`.

*Note the shape of (c): **count everything, subtract the violations**. With one constraint
that is a single subtraction. With several overlapping constraints the violations overlap and
you must add back the double-subtracted cases — that is inclusion–exclusion, tomorrow.*

**B3.** Before collecting: each of the `n` factors contributes one of `k` variables
independently → `**kⁿ**` terms.

After collecting: a monomial is determined by its exponent vector `(e₁,…,e_k)` with `eᵢ ≥ 0`
and `Σeᵢ = n` — stars and bars → `**C(n+k−1, k−1)**` distinct terms.

*The multinomial theorem says the coefficient on each is `n!/(e₁!⋯e_k!)`, which is `F1.1a`-A4's
formula. So: **stars and bars counts the terms; the multinomial coefficient counts each term's
multiplicity.** Two `F1.1` formulas, one expansion — that is the cleanest statement of how the
sub-stages fit together.*

</details>

<details>
<summary>Tier C</summary>

**C1.** `n=6, k=4`, every bin in `{1,2}`. Since each bin holds 1 or 2 and there are 4 bins
summing to 6, exactly two bins hold 2 and two hold 1. Choose which two hold 2:
`C(4,2) = **6**`.

Naive stars-and-bars with only the lower bound (each ≥1) would give `C(5,3) = 10` — it counts
the four `(3,1,1,1)`-type allocations and `(2,2,1,1)`-types alike, overshooting by the 4
arrangements that put 3 in some bin. **The cap is not expressible as a substitution**, which is
precisely why inclusion–exclusion exists.

</details>
