---
type: stage
id: F1.1a
name: Counting Rules
kind: foundation
multiplier: 1.2
topic: "[[I-1-combinatorics-and-counting]]"
concepts: ["[[ordered-vs-unordered]]", "[[multinomial-coefficient]]"]
roles: ["[[quant-research]]", "[[market-making]]"]
sprint: S16
status: unlocked
budget_h: 1.5
actual_h: 
d4_due: 2026-08-22
baseline_closes: [I.1]
---

# Counting Rules — Stage Map
`F1.1a` · **refresher-weighted (1.2×)** · `topics/section_I` §1
**Sprint 16, Day 8 (Mon 08-10)** · **Budget: 1.5h, one pass**

> **This file is the roadmap and the checklist.** The Feynman note at
> `progress/feynman_notes/F1_1_combinatorics.md` is shared across `F1.1a/b/c` — one note,
> three sub-stages. Do not create three notes.

> **Sized as a refresher, 2026-08-09.** Baseline I.1 (MISSISSIPPI) scored **4** — the highest
> Section I result and one of the three best answers in the whole diagnostic. The multinomial
> coefficient is *already installed*. This stage confirms it and adds the vocabulary, rather
> than re-teaching it. `F1.1b`/`F1.1c` carry the 2.0× weight, because stars-and-bars and
> inclusion–exclusion are where the actual gap is.

**Why this stage exists:** counting is the substrate for every discrete probability question —
"probability = favourable / total" is two counting problems in a trench coat. You can already
do the hardest one on the baseline. What you are missing is the **naming**: knowing that
MISSISSIPPI *is* a multinomial coefficient, and that the same object counts lattice paths,
means you recognise it in a problem that doesn't mention letters.

**Scope — four rules:**
1. **Product rule** — the thing everything else is built from
2. **Permutations** `P(n,k) = n!/(n−k)!` — ordered
3. **Combinations** `C(n,k) = n!/(k!(n−k)!)` — unordered
4. **Multinomial** `n!/(k₁!k₂!⋯kₘ!)` — the MISSISSIPPI object, generalised

The organising question, asked of every problem: **does order matter, and are the objects
distinguishable?** Four rules, four answers to that question.

Out of scope: stars and bars (`F1.1b`), inclusion–exclusion and derangements (`F1.1c`),
Catalan numbers, Stirling numbers, the ballot problem, the twelvefold way — see §Deferred.

---

## Knowledge checklist — tick when you can produce it cold

**Built from Ross Ch.1's actual section headings** (§1.1–§1.5). Tick at the close of the block,
not while reading.

**§1.2 The basic principle of counting**
- [ ] Product rule, and the generalised version for `r` experiments
- [ ] Why it is the only axiom here — everything below is the product rule plus a correction
      for overcounting

**§1.3 Permutations**
- [ ] `n!` arrangements of `n` distinct objects
- [ ] `P(n,k) = n!/(n−k)!` — ordered selection of `k` from `n`
- [ ] **Permutations with repeated objects** = `n!/(n₁!n₂!⋯nᵣ!)` ← *this is MISSISSIPPI,
      baseline I.1, and it is the same formula as the multinomial coefficient in §1.5*

**§1.4 Combinations**
- [ ] `C(n,k) = n!/(k!(n−k)!)`, and **why the `k!` divides out** (order within the chosen
      set doesn't matter)
- [ ] Symmetry `C(n,k) = C(n,n−k)` — choosing who's in = choosing who's out
- [ ] Pascal's rule `C(n,k) = C(n−1,k−1) + C(n−1,k)` — condition on whether item `n` is in
- [ ] Binomial theorem `(x+y)ⁿ = Σ C(n,k)xᵏy^{n−k}`

**§1.5 Multinomial coefficients**
- [ ] `C(n; k₁,…,kₘ) = n!/(k₁!⋯kₘ!)` — split `n` items into `m` labelled groups of fixed size
- [ ] **That this is the same object as §1.3's repeated-permutation formula.** Two derivations,
      one number. Say why in one sentence.

**Cross-cutting**
- [ ] The decision table: order matters / doesn't × repetition allowed / not → which formula

### Stretch — NOT in Ross Ch.1. Each names how you get it.

*Rule (`04_deliverables_spec.md` §D2): a stretch item is written inline, given a named chapter
in a book you own, or deferred **with the reason**.*

- [ ] **Combinations with repetition** `C(n+k−1, k)` → **that is `F1.1b`, tomorrow.** Not
      stretch, just next.
- [ ] **Catalan numbers, ballot problem, Stirling numbers, twelvefold way**
      → **DEFERRED to S17+**, reason: they are in `topics/section_I` §1 because that file is a
      *scope inventory*, not a curriculum. None appear in Ross Ch.1, and they are the fifth
      thing an interviewer reaches for, not the first. Catalan returns with lattice paths in
      S10 (DP); the rest stay parked until the core four are cold.

---

## Source — one book, one sitting

| Source | Covers | Time |
|---|---|---|
| **Ross, *A First Course in Probability* 6th ed. — Ch. 1, §1.1–§1.5** | All four rules | **30 min, hard stop** |

**Input cap: 30 min** — shorter than the usual 40 because this is a refresher and the chapter
is short. If you are still reading at 30 minutes, the problems are what's missing, not the text.

**Skip §1.6** (the number of integer solutions to an equation) — that is `F1.1b`'s entire
subject and it lands better tomorrow with a fresh head.

**Read for naming, not for novelty.** You can already compute MISSISSIPPI. Read to attach
the words *multinomial coefficient* to the thing you already do.

---

## The shape of the block (1.5h)

| Block | Minutes | Do |
|---|---:|---|
| Read | 30 | Ross §1.1–§1.5, hard stop |
| Teach-back | 15 | Note §1(a) — book **closed** |
| Tier A | 35 | A1–A4 on paper |
| Tier B | 10 | B1 (or B2 if B1 lands fast) |

**If the day collapses: A2, A4.** A2 is the decision table (the transferable skill); A4 is
MISSISSIPPI generalised (the baseline item, confirming it wasn't luck).

**When it gets hard and you start drifting** (Adj #13) — **stop reading, write the sentence you
can't finish into note §2 as a `⚠️ GAP`, and switch to Tier A on paper.** Combinatorics
especially: re-reading a counting argument almost never fixes it, and writing out `n=3` by hand
almost always does.

**One pass, not two.** Refreshers get one input pass (Adj #12 applies to *new* material). If
this stage needs a second pass, that is a finding — log it in note §2 and say so at the retro,
because it means the refresher sizing is wrong.

---

## Tier A — the floor (all four, unhinted, on paper)

**F1.1a-A1.** Derive `P(n,k) = n!/(n−k)!` from the product rule, then derive
`C(n,k) = P(n,k)/k!` from `P(n,k)`. **Say in one sentence why the `k!` is dividing.**
*The whole of elementary counting is "count the ordered version, then divide by the overcount."
If you can say what is being overcounted and by how much, you can rebuild any of these cold.*

**F1.1a-A2.** Build the **decision table** from memory — the four cells of
{order matters, order doesn't} × {repetition allowed, not allowed}, with the formula in each.
Then place these five problems in it, one line each:
(i) 3-digit PIN codes · (ii) a 5-card poker hand · (iii) podium finish from 8 runners ·
(iv) 4 scoops from 10 flavours, repeats allowed, order irrelevant · (v) MISSISSIPPI.
*This table is the single most useful artefact of the stage. One of the five cells is `F1.1b`'s
stars-and-bars — find out which by noticing you can't fill it.*

**F1.1a-A3.** Prove Pascal's rule `C(n,k) = C(n−1,k−1) + C(n−1,k)` **combinatorially** — not by
algebra. Condition on whether a specific item is in the chosen set.
*Conditioning on one element is the same move as first-step conditioning in `F1.4`'s geometric
derivation. Same reflex, different setting.*

**F1.1a-A4.** MISSISSIPPI: how many distinct arrangements? Then generalise — state the
repeated-permutation formula, and **show it is the multinomial coefficient** by giving the
second derivation (choose positions for each letter in turn:
`C(11,4)·C(7,4)·C(3,2)·C(1,1)`) and confirming the two agree.
*You scored 4 on this cold. The job here is not the number (34,650) — it is producing the
formula's **name** and both derivations, so that a problem about bins or teams triggers it.*

---

## Tier B — the target (≥1 of 3, more if time)

**F1.1b-B1.** How many ways to deal 52 cards into 4 hands of 13? Write it as a multinomial
coefficient. Then: how many ways to split 12 people into 4 **unlabelled** teams of 3?
*The second is the first divided by `4!`, and knowing **when** that division applies —
labelled vs unlabelled groups — is the most common counting error there is. Say out loud
why bridge hands are labelled (North/South/East/West) and generic teams are not.*

**F1.1a-B2.** How many lattice paths from `(0,0)` to `(m,n)` using only right and up steps?
*Answer `C(m+n, m)`: a path **is** a word in R's and U's, so counting paths = counting
arrangements = A4's formula. This is the first time a counting formula shows up wearing a
disguise, which is the whole reason for learning the names.*

**F1.1a-B3.** A committee of 5 from 6 men and 9 women, with at least 3 women. Count it.
*Case-split and add. Then say why you cannot instead count "choose 3 women, then choose 2
from the rest" — that classic wrong answer overcounts, and being able to explain the
overcount is worth more than the right number.*

---

## Tier C — only if A+B ran short

**F1.1a-C1.** Prove Vandermonde's identity `C(m+n, k) = Σⱼ C(m,j)C(n,k−j)` combinatorially.
*Split the `m+n` items into two groups and condition on how many come from the first.*

---

## Code problems

**None this sub-stage.** Solvers land in `F1.1b` and `F1.1c`, where a Monte Carlo verifier
actually earns its keep (stars-and-bars counts and the derangement `1/e` limit). Writing a
solver for `C(n,k)` would be re-implementing `math.comb`.

*If you want the reflex anyway: `math.comb(11,4)*math.comb(7,4)*math.comb(3,2) == 34650` is a
one-liner worth typing once, in the REPL, not in a file.*

---

## Deliverables

**D1 — Feynman note** `progress/feynman_notes/F1_1_combinatorics.md` **§1(a) only**
- [ ] Teach-back for the four counting rules, source closed
- [ ] The **decision table** (A2) written into note §5 — it is this stage's row of the summary
- [ ] Any `⚠️ GAP` logged in §2

*The note is shared across `F1.1a/b/c` and is not closed until Saturday. Today writes §1(a)
and one table row — nothing else.*

**D2 — Problems** (this file)
- [ ] A1–A4 unhinted, on paper
- [ ] ≥1 of Tier B
- [ ] Log which needed hints

**D3 — Code:** none (see above)

**D3.5 — Concept notes:** at `F1.1c` close, not today.

**D4 — Unlock test:** `F1.1a/b/c` share **one** D4 on **2026-08-22** (+1wk from this block).
Not on Sat 08-15 — that day already carries four D4 tests, which is the real bottleneck
in the system right now.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** `P(n,k)`: fill `k` ordered slots — `n` choices for the first, `n−1` for the second, …,
`n−k+1` for the `k`-th. Product rule gives
`n(n−1)⋯(n−k+1) = **n!/(n−k)!**`.

`C(n,k)`: every unordered set of `k` items was counted **`k!` times** in `P(n,k)`, once per
internal ordering. So `C(n,k) = P(n,k)/k! = **n!/(k!(n−k)!)**`.

**The one sentence:** *the `k!` divides out the orderings of the chosen set, which `P` counted
separately and we don't care about.* Every formula in this stage is the product rule followed
by division by whatever got overcounted — that is the entire method.

**A2.** Choosing `k` from `n`:

| | **Order matters** | **Order doesn't** |
|---|---|---|
| **No repetition** | `n!/(n−k)!` | `C(n,k) = n!/(k!(n−k)!)` |
| **Repetition allowed** | `nᵏ` | `C(n+k−1, k)` ← **stars and bars, `F1.1b`** |

(i) 3-digit PIN → `10³`, ordered with repetition.
(ii) Poker hand → `C(52,5)`, unordered, no repetition.
(iii) Podium from 8 → `P(8,3) = 336`, ordered, no repetition.
(iv) 4 scoops from 10, repeats OK, order irrelevant → `C(13,4) = 715` — **the bottom-right
cell, and the one you couldn't fill.** That is tomorrow.
(v) MISSISSIPPI → none of the four cells: it is not "choose `k` from `n`" but "arrange a
multiset". Multinomial, `11!/(4!4!2!1!)`. *Noticing it doesn't fit the table is the point —
the table covers selection, A4 covers arrangement.*

**A3.** Fix a specific item, say item `n`. Every `k`-subset either contains it or does not —
these are disjoint and exhaustive.
- Contains item `n`: choose the other `k−1` from the remaining `n−1` → `C(n−1,k−1)`
- Does not: choose all `k` from the remaining `n−1` → `C(n−1,k)`

Sum: `C(n,k) = C(n−1,k−1) + C(n−1,k)` ∎
*Conditioning on one element, exactly as `F1.4`'s geometric conditioned on the first trial.
This is also the recurrence that builds Pascal's triangle, and the DP recurrence you will
meet again in S10.*

**A4.** MISSISSIPPI has 11 letters: M×1, I×4, S×4, P×2.
`11!/(1!·4!·4!·2!) = 39,916,800/(1·24·24·2) = 39,916,800/1152 = **34,650**` ✓ *(baseline I.1)*

*Second derivation — choose positions:* `C(11,4)` positions for the I's, then `C(7,4)` of the
remaining for the S's, then `C(3,2)` for the P's, then `C(1,1)` for the M:
`330 · 35 · 3 · 1 = **34,650**` ✓

**Why they agree:** expand the second — `[11!/(4!7!)]·[7!/(4!3!)]·[3!/(2!1!)]·1` — and every
intermediate factorial cancels telescopically, leaving `11!/(4!4!2!1!)`. **The
repeated-permutation formula and the multinomial coefficient are the same object**: arranging a
multiset *is* partitioning the 11 positions into labelled groups, one group per letter.

</details>

<details>
<summary>Tier B</summary>

**B1.** Bridge deal: `C(52; 13,13,13,13) = **52!/(13!)⁴** ≈ 5.36×10²⁸`. The four hands are
**labelled** — North's hand is a different outcome from South's, so no further division.

12 people into 4 unlabelled teams of 3: start with the multinomial `12!/(3!)⁴ = 369,600`,
which treats the teams as labelled Team 1…Team 4. The teams are interchangeable, so each
partition was counted `4!` times: `369,600/4! = **15,400**`.

**The rule:** divide by `m!` when the `m` groups are **indistinguishable**, don't when they
carry identities. Bridge seats have identities; "split into teams" usually does not. Getting
this wrong in either direction is the most common counting error at interview, and it is worth
saying out loud which one you are in before you compute.

**B2.** A path is a sequence of `m` R's and `n` U's in some order — every such word is exactly
one path, and every path exactly one word. So the count is the number of arrangements of that
multiset: `(m+n)!/(m!n!) = **C(m+n, m)**`.
*Same formula as A4, wearing a disguise. This is why the names matter: "arrangements of a
multiset" and "lattice paths" and "which subset of steps are rights" are one problem.*

**B3.** At least 3 women from 6M/9W, committee of 5. Case-split on the number of women:
- 3W2M: `C(9,3)C(6,2) = 84·15 = 1260`
- 4W1M: `C(9,4)C(6,1) = 126·6 = 756`
- 5W0M: `C(9,5)C(6,0) = 126·1 = 126`

Total = **2142**.

*The classic wrong answer:* `C(9,3)·C(12,2) = 84·66 = 5544` — "pick 3 women, then any 2 from
the remaining 12." This **overcounts**, because a committee with 4 women is produced multiple
times: any 3 of its 4 women could have been the "chosen 3", with the 4th arriving in the
second step. The distinct-then-fill move only works when the two stages produce
distinguishable roles. **Overcounting is the failure mode of counting, and the cure is always
to partition into disjoint cases first.**

</details>

<details>
<summary>Tier C</summary>

**C1.** Vandermonde. Take `m` red items and `n` blue. Choosing `k` from all `m+n` gives
`C(m+n,k)`. Alternatively, condition on `j`, the number of reds chosen: pick `j` reds
(`C(m,j)`) and `k−j` blues (`C(n,k−j)`). The cases `j = 0…k` are disjoint and exhaustive, so
`C(m+n,k) = Σⱼ C(m,j)C(n,k−j)` ∎
*Same method as A3 — partition by a feature, count each block, add. A3 is the special case
`m=1`.*

</details>
