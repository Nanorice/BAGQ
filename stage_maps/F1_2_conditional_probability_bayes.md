---
type: stage
id: F1.2
name: Conditional Probability & Bayes
topic: "[[I-3-conditional-probability-and-bayes-theorem]]"
concepts: ["[[bayes-rule]]", "[[law-of-total-probability]]", "[[base-rate-fallacy]]"]
roles: ["[[signal-research]]", "[[market-making]]"]
sprint: S17
status: unlocked
est_h: 7
actual_h:
---

# Conditional Probability and Bayes

**Source:** `inventory/section_I_probability_combinatorics.md` §3 — core concepts and all ten
problems.

**Why the topic file and not Ross:** Ross Ch.3 covers conditional probability well but buries the
base-rate vocabulary — sensitivity, specificity, PPV are medical-testing language, not a named
Ross subsection, and that vocabulary is exactly the gap. The topic file states it directly.
**Read Ross Ch.3 §3.1–§3.4 as a backup** only if total probability or independence will not land
from the one-liners.

**Estimated: 7h.**

---

## What this covers

Bayes' rule itself is one line. What fails under pressure is **which probability is which** —
sensitivity versus specificity versus prevalence versus posterior — and the disease-test, spam
filter and fraud-detection questions built on that confusion are asked more than almost anything
else in elementary probability.

1. **Conditional probability** `P(A|B) = P(A∩B)/P(B)` — the definition everything follows from
2. **Law of total probability** — partition the sample space, weight by the partition
3. **Bayes' rule** — invert the conditioning, and *why* you would want to
4. **Independence versus conditional independence** — different claims, not the same idea twice
5. **The base-rate vocabulary** — sensitivity, specificity, prevalence, PPV and NPV, named rather
   than merely computed

**Depends on combinatorics:** Bayes problems routinely need a denominator built by counting
equally likely outcomes. If a problem below needs a count you cannot produce, that is a counting
gap rather than a Bayes one — log it as such.

**Not here:** Simpson's paradox beyond one worked example, the two-envelopes resolution beyond
stating the flaw, the prosecutor's-fallacy legal context. Those are Tier B and C drills.

---

## Knowledge checklist — tick when you can produce it cold

Built from the topic file's own headings. Tick at the close of a block, not while reading.

**Core Concepts**
- [ ] `P(A|B) = P(A∩B)/P(B)`, stated and one sentence on *why* dividing by `P(B)` is "shrinking
      the sample space to B"
- [ ] Law of total probability: `P(A) = Σᵢ P(A|Bᵢ)P(Bᵢ)` for a partition `{Bᵢ}` — say what
      "partition" requires (disjoint, exhaustive)
- [ ] Bayes' rule: `P(B|A) = P(A|B)P(B)/P(A)`, derived from the definition in one line, not
      memorised as a separate formula
- [ ] Independence `P(A∩B)=P(A)P(B)` vs. conditional independence given `C` — construct one
      example where `A,B` are dependent but conditionally independent given `C`
- [ ] **The base-rate vocabulary, cold:**
      - Sensitivity = `P(test+ | disease)` — true positive rate
      - Specificity = `P(test− | no disease)` — true negative rate
      - Prevalence = `P(disease)` — the prior
      - PPV = `P(disease | test+)` — the posterior, what Bayes actually computes
      - **Say why PPV craters when prevalence is low even with a "good" test** — this is the
        entire content of baseline I.2

### Stretch — beyond the core five


- [ ] **Simpson's Paradox** → **INLINE**, one worked numerical example in Tier B (B3). Full
      causal-inference treatment is out of scope — the interview ask is "construct an example
      and explain it," not the deeper theory.
- [ ] **Two Envelopes Problem** → **INLINE**, Tier C, optional. It's a paradox about improper
      priors, not new machinery — worth seeing once, not worth a derivation budget.
- [ ] **Prosecutor's Fallacy** → **INLINE**, folded into Tier B's Bayes drills (same computation
      as the disease test with different labels — no new content, just a different cover story).

---

---

## Problems

### Tier A — the floor. All five, unhinted, on paper.

**A1.** Derive Bayes' rule from the definition of conditional probability in two lines:
start from `P(A∩B) = P(A|B)P(B) = P(B|A)P(A)`, solve for `P(B|A)`. Then state the law of total
probability and show why you'd substitute it into the denominator when you only know
`P(A|Bᵢ)` for each piece of a partition, not `P(A)` directly.
*Bayes' rule is not a separate fact to memorise — it's the definition of conditional probability
read in the other direction. If you can produce this derivation cold, you cannot forget the
formula, because you can rebuild it in ten seconds.*

**A2. Monty Hall.** You pick one of three doors. The host, who knows what's behind each
door, opens a losing door you didn't pick. Should you switch? Compute `P(win | switch)` and
`P(win | stay)` explicitly, conditioning on which door hides the car.
*The standard trap is treating the host's action as uninformative. It isn't — the host's choice
is constrained by what you picked and where the car is, and that constraint is where the
information comes from. Say explicitly what the host **cannot** do.*

**A3.** The disease test: sensitivity 99%, specificity 95%, prevalence 1%. Compute
`P(disease | positive test)`. **Do it two ways:** once with Bayes' rule symbolically, once with
a table of 10,000 people split by the four combinations of {disease, test result}. Confirm they
agree.
*This is baseline I.2, verbatim. The table method is the one to trust under interview pressure
— it is harder to make a sign error with actual head-counts than with symbols.*

**A4.** State the difference between independence and conditional independence in one
sentence each, then construct a concrete example (three events/variables) where `A` and `B` are
**dependent** unconditionally but **independent given `C`**.
*The standard example: two coins where `C` = "at least one is heads." Marginally the coins are
independent; conditioned on `C`, knowing one is heads changes what you know about the other.
Getting your own example, not the textbook one, is the point — it proves you understand the
mechanism, not just the label.*

**A5.** Define sensitivity, specificity, prevalence, and PPV in one sentence each, **cold,
no formula sheet.** Then explain in your own words why PPV can be low (e.g., under 20%) even
when both sensitivity and specificity are above 95%, if prevalence is low enough.
*This is the vocabulary baseline I.2 was missing. The number in A3 is the proof; this problem
is the naming, which is what actually transfers to a differently-worded interview question.*

---

### Tier B — the target. At least three.

**B1. The Taxi-Cab Problem.** 85% of cabs are green, 15% blue. A witness who is correct
80% of the time says the cab was blue. What's `P(cab was blue | witness says blue)`?
*Same computation as A3, different cover story — confirm you recognise it as the same problem
before computing. The point of this tier is pattern recognition, not new arithmetic.*

**B2. Updating with multiple evidence.** A coin is fair or double-headed, prior 50/50. You
observe 5 heads in a row. What's the posterior it's fair?
*Sequential Bayes update — each flip's likelihood multiplies in. Do it as one Bayes computation
with the combined likelihood, not five separate updates, and note that both give the same
answer (this is worth confirming once).*

**B3. Simpson's Paradox, constructed.** Build a two-treatment, two-subgroup numerical
example where Treatment A has a higher success rate in *both* subgroups but a lower overall
success rate. Explain the mechanism in one sentence.
*The mechanism is always an imbalance in how the subgroups are weighted between the two
treatment arms — say that explicitly, don't just present the numbers.*

**B4. Prosecutor's Fallacy.** A DNA match has a `10⁻⁶` false-match probability. In a city of
1,000,000 people with no other evidence, what's `P(guilty | match)` if you assume the true
culprit is equally likely to be anyone in the city? Why does this differ from `P(match | guilty)`?
*The fallacy is treating the two conditional probabilities as interchangeable. Compute the
actual posterior — it is much lower than `1 − 10⁻⁶` — and say in one sentence why the city's
population size, not just the test's accuracy, determines the answer.*

**B5. Two Envelopes.** One envelope has twice the money of the other. You pick one, see
`$x`. The "switching" argument says the other envelope has expected value `1.25x`. Where does
the argument break?
*It assigns a fixed prior distribution to the unknown amount that can't actually be uniform over
all positive reals — say what property a valid prior would need and why no such prior exists
here. You don't need the full resolution, just the location of the flaw.*

---

### Tier C — only if A and B ran short.

**C1. The Broken Stick.** A stick of length 1 is broken at a uniform random point. Given
the longer piece is `> 0.7`, what's the expected length of the shorter piece?
*Conditioning restricts the sample space to a sub-interval of the break point — reparametrise
and integrate over just that restricted region.*

---

## Code problems

`src/solvers/s1_probability/bayes_verify.py` — new file. Docstring with time + space
complexity, one `assert`-based `__main__`.

**CODE1** — Verify A3 (the disease test) two ways: (1) closed-form Bayes' rule, (2) Monte
Carlo — simulate 1,000,000 people with the given prevalence, apply sensitivity/specificity as
random flips, and estimate `P(disease | positive)` empirically. Assert the two agree within
0.5% absolute.
*Complexity: closed form `O(1)`; Monte Carlo `O(n)` in population size. State both, and note
in a comment why `n=1,000,000` was chosen — large enough that the MC standard error is well
under the assert tolerance given the ~1% base rate.*

---

## Deliverables

**Feynman note** — `progress/feynman_notes/F1_2_conditional_probability_bayes.md`
- [ ] Teach-back (Pass 1), source closed
- [ ] Zero remaining `⚠️ GAP`
- [ ] Napkin ≤200 words, said out loud
- [ ] Summary: the base-rate vocabulary table (sensitivity/specificity/prevalence/PPV) in §5
- [ ] ≥2 items in "Where this breaks"

**Problems**
- [ ] A1–A5 unhinted, on paper
- [ ] ≥3 of Tier B
- [ ] Log which needed hints

**Code**
- [ ] `CODE1` in `bayes_verify.py`, asserting, with the complexity docstring


**Unlock test** — one week after close.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** From the definition: `P(A|B) = P(A∩B)/P(B)` and `P(B|A) = P(A∩B)/P(A)`, so
`P(A∩B) = P(A|B)P(B) = P(B|A)P(A)`. Solving the right-hand equality for `P(B|A)`:
`**P(B|A) = P(A|B)P(B)/P(A)**` — Bayes' rule.

When `P(A)` isn't known directly but `A` can be reached via a partition `{Bᵢ}` of the sample
space, substitute the law of total probability: `P(A) = Σᵢ P(A|Bᵢ)P(Bᵢ)`. This is the standard
"expand the denominator" move — you almost never have `P(A)` for free in a word problem; you
build it from the pieces you're given.

**A2.** Condition on which door hides the car, `P(car=i) = 1/3` for `i=1,2,3`. Say you pick
door 1. The host must open a door that (a) you didn't pick and (b) doesn't have the car.

- If car is behind door 1 (`p=1/3`): host opens 2 or 3 at random; switching loses.
- If car is behind door 2 (`p=1/3`): host **must** open door 3 (can't open your door or the
  car's door); switching to door 2 wins.
- If car is behind door 3 (`p=1/3`): symmetric, switching wins.

`P(win | switch) = 2/3`, `P(win | stay) = 1/3`. **What the host cannot do:** open your door, or
open the door with the car. That constraint is what makes the host's action informative — he is
forced to reveal information about the other two doors conditional on your original pick.

**A3.** Let `D` = disease (prevalence 1%), `T+` = positive test.
```
P(D|T+) = P(T+|D)P(D) / [P(T+|D)P(D) + P(T+|D^c)P(D^c)]
        = (0.99)(0.01) / [(0.99)(0.01) + (0.05)(0.99)]
        = 0.0099 / (0.0099 + 0.0495)
        = 0.0099 / 0.0594
        ≈ **0.1667 (16.7%)**
```

**Table method**, 10,000 people:
```
                Disease (100)      No disease (9,900)
Test +          99 (0.99×100)      495 (0.05×9,900)
Test −          1                  9,405
```
`P(D|T+) = 99 / (99+495) = 99/594 ≈ **0.1667**` ✓ — same answer, and far harder to sign-error.

**A4.** Independence: `P(A∩B) = P(A)P(B)`, unconditionally. Conditional independence given `C`:
`P(A∩B|C) = P(A|C)P(B|C)` — a claim about the *conditional* distribution, which says nothing
about whether `A,B` are independent unconditionally, and vice versa.

**Example:** flip two fair coins, `X₁, X₂`, independently. Let `C` = "at least one shows heads."
Unconditionally `X₁ ⊥ X₂`. But conditioned on `C`: the sample space shrinks to {HH, HT, TH}
(each `1/3`). `P(X₁=H | C) = 2/3`, `P(X₂=H | C) = 2/3`, but `P(X₁=H, X₂=H | C) = P(HH|C) = 1/3
≠ (2/3)(2/3) = 4/9`. So two **marginally independent** variables become **dependent** once
conditioned on `C` — the reverse of what the problem asked, which is also worth noting: the
relationship runs both directions, and interviewers will ask for either.

**A5.**
- **Sensitivity** = `P(test+ | disease)` — how often the test catches true cases
- **Specificity** = `P(test− | no disease)` — how often the test correctly clears healthy people
- **Prevalence** = `P(disease)` — the base rate in the population, independent of the test
- **PPV** = `P(disease | test+)` — what you actually want to know when you get a positive result

**Why PPV craters:** with low prevalence, the pool of healthy people vastly outnumbers the sick
pool, so even a small false-positive rate (`1 − specificity`) applied to the huge healthy pool
generates more false positives in absolute count than the sick pool generates true positives.
A3's numbers: 495 false positives vs. 99 true positives, despite 99%/95% accuracy — the
imbalance comes entirely from the 99:1 ratio of healthy to sick people, not from the test being
bad. **Sensitivity and specificity are properties of the test; PPV depends on the population
you're screening**, and conflating the two is the entire content of the base-rate fallacy.

</details>

<details>
<summary>Tier B</summary>

**B1.** Same structure as A3 with `sensitivity=specificity=0.80` (witness reliability applies
symmetrically to both colors, stated as "correct 80% of the time"), prevalence `P(blue)=0.15`:
```
P(blue|says blue) = (0.8)(0.15) / [(0.8)(0.15) + (0.2)(0.85)]
                   = 0.12 / (0.12 + 0.17) = 0.12/0.29 ≈ **0.41**
```
Despite the witness being 80% reliable, the posterior is still under 50% — because green cabs
outnumber blue 85:15, the same base-rate mechanism as A3.

**B2.** `P(fair)=P(double)=0.5`. Likelihood of 5 heads: fair coin `(1/2)⁵=1/32`; double-headed
coin `1⁵=1`.
```
P(fair|5H) = (1/32)(0.5) / [(1/32)(0.5) + (1)(0.5)]
           = 0.015625 / 0.515625 ≈ **0.0303 (3%)**
```
Doing it as five sequential updates multiplies the same two likelihoods in the same order and
reaches the identical posterior — sequential Bayes updating is just factoring the joint
likelihood, so there's no reason to prefer one over the other except computational convenience.

**B3.** Construct: Treatment A vs B, subgroups "mild" and "severe" cases.
```
              Mild                    Severe                  Overall
Treatment A   90/100 = 90%  (mostly mild patients)   10/100 = 10%   100/200 = 50%
Treatment B   80/90  = 89%  (mostly severe patients) 5/10   = 50%   85/200  = 42.5%... 
```
*(Concrete numeric instance — construct your own with these proportions: give Treatment A far
more of its patients in the easy "mild" subgroup and Treatment B far more in the hard "severe"
subgroup, so A wins both subgroups narrowly but the overall pool is dominated by each
treatment's respective easy/hard mix.)* **Mechanism:** the treatment arms are not given the same
mix of easy/hard cases, so the overall rate is a weighted average with different weights per
arm — a within-subgroup comparison and a pooled comparison are answering different questions
whenever the group sizes differ between arms.

**B4.** Let `G` = guilty (assume uniform prior over 1,000,000 people, so `P(G)=10⁻⁶` for any
given innocent-until-matched individual — more precisely, treat this as: 1 true culprit,
999,999 innocent people, each innocent person matches with probability `10⁻⁶`).
```
Expected false matches among the innocent: 999,999 × 10⁻⁶ ≈ 1
P(guilty | match) ≈ 1 / (1 + 1) = **~0.5**, not ~1
```
`P(match|guilty) ≈ 1` (assume the true culprit always matches their own DNA) is not
`P(guilty|match)`, because the denominator has to account for the ~1 innocent person in a city
of a million who is *expected* to also match by chance. **The fallacy is ignoring the size of
the suspect pool** — the same match probability produces a near-certain conviction in a
100-person village and a coin-flip in a million-person city.

**B5.** The switching argument implicitly assumes a prior where, for any value `x` you might
see, "the other envelope has `2x`" and "the other envelope has `x/2`" are equally likely — i.e.
a **uniform prior over all positive reals**, which does not exist (it can't integrate to 1). Any
*actual* valid prior on the envelope amounts is not flat, so the "other envelope" posterior
depends on `x` in a way that generally cancels the naive `1.25x` expected-value argument once
you integrate correctly over a real (proper) prior. **The flaw is invoking an improper prior and
treating it as if it were a real one.**

</details>

<details>
<summary>Tier C</summary>

**C1.** Stick broken at `U ~ Uniform(0,1)`. Longer piece `= max(U, 1−U)`. Condition on
`max(U,1−U) > 0.7`, i.e. `U < 0.3` or `U > 0.7`. By symmetry consider `U > 0.7` (double the
density, same answer by symmetry): given `U > 0.7`, `U ~ Uniform(0.7, 1)`, and the shorter piece
is `1−U ~ Uniform(0, 0.3)`. `E[\text{shorter}] = **0.15**`.

</details>
