---
type: feynman-note
stage: "[[F1_1a_counting_rules]]"
id: F1.1
---

# Combinatorics
`F1.1` · **Started:** ____ · **Completed:** ____
**Time spent:** __h · **Source(s):** Ross 6th ed. Ch.1 §1.1–§1.6, Ch.2 §2.5

> This note is **yours** — what you understood. What to *do* lives in three maps:
> `stage_maps/F1_1a_counting_rules.md` · `F1_1b_stars_and_bars.md` · `F1_1c_inclusion_exclusion.md`

> **One note, three sub-stages.** Write §1(a) Mon, §1(b) Wed, §1(c) Thu. Everything else
> (§2–§6) gets written at the Saturday close. Do not try to finish sections early.

## Review log
- [ ] +1 week (2026-08-22): reproduce the §5 decision table cold, then derive `D_n` → pass/fail
- [ ] +1 month (2026-09-13): stars-and-bars with a lower bound, cold → pass/fail
- [ ] +3 months (2026-11-13): re-take I.1, plus one unseen counting problem → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

<!-- Four things. Write (a) Monday, (b) Wednesday, (c) Thursday.
     (a) The four counting rules — what question does each answer? What is being
         overcounted, and by how much, in each division?
     (b) Stars and bars — DRAW the bijection. Why k−1 bars and not k?
     (c) Inclusion–exclusion — why do the signs alternate? Then derangements: why does e
         show up in a problem with no calculus in it?
     No jargon shortcuts. If you use a term, define it in the same paragraph. -->

**(a) Counting rules** *(Mon 08-10)*



**(b) Stars and bars** *(Wed 08-12)*



**(c) Inclusion–exclusion + derangements** *(Thu 08-13)*



## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Log gaps ON THE DAY — Wednesday's list is what Thursday's Pass 2 re-reads (Adj #12).
     Watch for: saying a bijection exists without giving BOTH directions. That is the
     standard incomplete answer and an interviewer will ask for the other half. -->



## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist.
     Suggested spine: counting is the product rule plus a division for whatever got
     overcounted — say what gets divided out in each of the four rules, then the two
     harder objects (stars-and-bars, inclusion–exclusion) in one line each. -->



## 4. Where I'd actually meet this

<!-- One line each, technical is fine. Your F1.5 answers (VaR, order filling) were the model.
     Candidates if you're stuck: risk-budget allocation across strategies · counting order
     book states · combinatorial explosion as the reason a brute-force backtest is infeasible ·
     the birthday problem as a hash-collision estimate. Concrete beats clever. -->



## 5. THE DECISION TABLE — this is the deliverable

<!-- NOT a distribution table this time. Fill from memory first, THEN check.
     This is what the D4 test reproduces cold on 08-22. -->

**Choosing `k` from `n`:**

|                        | Order matters | Order doesn't |
| ---------------------- | ------------- | ------------- |
| **No repetition**      |               |               |
| **Repetition allowed** |               |               |

**Arrangement and distribution — the other three objects:**

| Object | Formula | Counts what | The one fact |
| ------ | ------- | ----------- | ------------ |
| **Multinomial** | | | |
| **Stars and bars** | | | |
| **Derangements** `D_n` | | | |

**Inclusion–exclusion, two sets:** <!-- one line -->

**Inclusion–exclusion, general form + why the signs alternate:** <!-- one line -->

**Numerical anchors (from memory):** MISSISSIPPI = ______ · `D_4` = ____ ·
`D_n/n!` → ______ · birthday 50% at n = ____

## 6. Where this breaks

<!-- ≥2 items, and prefer ones you can defend over ones copied from this comment.
     Candidates you will meet in the problems:
     - labelled vs unlabelled groups: divide by m! for one, not the other (F1.1a-B1)
     - "choose 3 women then 2 more" overcounts — distinct-then-fill needs distinguishable
       roles (F1.1a-B3)
     - stars and bars is WRONG under a capacity cap; needs inclusion–exclusion (F1.1b-C1)
     - bins must be labelled — unlabelled bins are integer partitions, no closed form -->



## 7. Links

- **Problems solved:** F1.1a-A1…A4, F1.1b-A1…A4, F1.1c-A1…A3, B__
- **Prereqs:** none — this is the floor of Section I
- **Unlocks:** `S1.2` conditional probability (S17) · S2 classical puzzles ·
  S9.2 hypothesis testing (counting arguments) · S10 DP (Catalan, lattice paths)
- **Baseline questions this closes:** I.1 (MISSISSIPPI, scored 4 — **confirming, not
  installing**) · indirectly II.3 coupon collector via complementary counting
- **Deliberately deferred:** Catalan → S10 with DP · Stirling numbers, ballot problem,
  twelvefold way → S17+ *(scope inventory, not curriculum)* · integer partitions `p(n)` →
  S10 DP · Möbius inversion → no stage, no interview footprint

---

*Completion checklist lives in the stage maps (§Deliverables), not here.*
