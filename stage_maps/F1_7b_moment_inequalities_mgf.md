---
type: stage
id: F1.7b
name: Moment Inequalities & MGF
kind: foundation
multiplier: 2.0
topic: "[[I-7-expectation-variance-and-moments]]"
concepts: ["[[moment-generating-function]]", "[[jensen-inequality]]"]
roles: ["[[signal-research]]", "[[market-making]]"]
sprint: S17
status: locked
budget_h: 3.5
actual_h:
d4_due: 2026-08-30
baseline_closes: []
---

# Moment Inequalities & MGF — Stage Map
`F1.7b` · foundation (new install, 2.0×) · `topics/section_I` §7 (part 2 of 2)
**Sprint 17, Day 6 (Sat 08-22)** · **Budget: 3.5h, one pass + note close**

> **PRINT THIS PAGE.** Second half of the `S1.7` split — `F1.7a` (Thu/Fri) covered linearity,
> LOTUS, tower property, Eve's Law. This stage covers the moment-inequality trio (already used,
> unhinted, in `F1.7a`-B3/B4 — Jensen and Chebyshev) plus a **first, deliberately light** pass at
> the MGF, which was explicitly deferred here from `F1.4` (see that stage map's note, 08-09).

> **This is also `F1.1`'s D4 test day** (2026-08-22, committed from Sprint 16). Check
> `sprints/S17.md` for the day's full shape before starting — this stage map assumes the D4 test
> happens first, this stage second.

**Why this stage exists:** `F1.4`'s scope correction (08-09) removed MGF as a listed problem
because Ross covers it in Ch.7, not Ch.4 — the deferral target was always "`S1.8`", but MGF's
*definition* and the mechanical moment-extraction property belong with expectation, not with
the dedicated generating-functions stage (`S1.8`, which is about *using* MGFs for sums via
convolution — machinery this stage doesn't build). This stage installs the definition and the
two things you actually need before `S1.8`: what an MGF is, and how to read moments off it.

**Scope — two things:**
1. **Moment inequalities** — Markov, Chebyshev, Jensen — three different kinds of "how spread
   out / how skewed" bound
2. **MGF, definition only** — `M_X(t) = E[e^{tX}]`, moment extraction via derivatives at 0,
   and the existence caveat (`t` range matters)

Out of scope: MGF *uniqueness* proofs, convolution via MGF product, characteristic functions,
PGF. All of that is `S1.8`, not here — this stage's MGF section is intentionally thin.

---

## Knowledge checklist — tick when you can produce it cold

**Built from `topics/section_I` §7's remaining headings.**

**Moment Inequalities**
- [ ] **Markov:** `P(X≥a) ≤ E[X]/a` for `X≥0`, `a>0` — derive it, don't just quote it
- [ ] **Chebyshev:** `P(|X-μ|≥kσ) ≤ 1/k²` — derive it **from Markov**, applied to `(X-μ)²`
- [ ] **Jensen:** `E[g(X)] ≥ g(E[X])` for convex `g` (flips for concave) — state the geometric
      intuition (a chord lies above/below the function)
- [ ] Rank the three by how much information they use: Markov (mean only) → Chebyshev (mean +
      variance) → Jensen (convexity, no explicit spread parameter) — and say what each buys you
      in exchange for its assumption

**Moment Generating Function (definition only — full treatment is `S1.8`)**
- [ ] `M_X(t) = E[e^{tX}]`
- [ ] `M_X'(0)=E[X]`, `M_X''(0)=E[X²]`, and in general `M_X^{(n)}(0)=E[X^n]` — say why
      (differentiate under the expectation, then set `t=0`)
- [ ] **The existence caveat: an MGF only exists on some interval of `t` containing 0** — state
      the exponential's MGF `λ/(λ-t)` for `t<λ` as the concrete example, and say what "MGF
      doesn't exist" would mean for a heavy-tailed distribution
- [ ] Identify a distribution from a given MGF form, at the level of pattern-matching to the
      table (this is Tier A-A4, not a derivation)

### Stretch — explicitly NOT this stage

- [ ] **MGF uniqueness, convolution via MGF product, characteristic functions, PGF**
      → **DEFERRED to `S1.8`**, per the traversal table. Reason: those require the convolution
      theorem, which needs its own derivation and is `S1.8`'s actual subject — cramming it here
      would recreate the `F1.4`-A5 mis-scoping this stage exists to fix.

---

## Source — one file, one sitting

| Source | Covers | Time |
|---|---|---|
| **`topics/section_I_probability_combinatorics.md` §7**, lines 184–186 + 200–207 (inequality bullets + MGF bullet + problems 6–9) | Inequalities + MGF definition | **20 min, hard stop** |

**Backup only if a concept doesn't click:**

| Backup | Covers | Use only if |
|---|---|---|
| Ross 6th ed. Ch. 7, §7.7.1–§7.7.2 (moment inequalities), §7.7 opening (MGF definition) | Formal derivations | Markov/Chebyshev derivation or MGF moment-extraction isn't landing |

**One pass.** This stage is the second half of what was already sized as new material across
two days (`F1.7a` Thu/Fri, `F1.7b` today) — today does not need its own two-pass structure
because it directly follows `F1.7a`'s Pass 2 and shares the same `⚠️ GAP` mechanism via the
note. If today's read surfaces real gaps, log them for the D4 review, don't force a same-day
re-read.

---

## The shape of the block (3.5h, after the F1.1 D4 test)

| Block | Minutes | Do |
|---|---:|---|
| Read | 20 | Topic file §7 remainder, hard stop |
| Teach-back | 15 | Note §1(b) — file **closed** |
| Tier A | 60 | A1–A4 on paper |
| Tier B | 30 | ≥2 of 4 |
| Code | 15 | `F1.7-CODE2` |
| **Note close** | 30 | §2–§6 for the **whole `F1.7` note** (a + b together) |

**If the day collapses: A1, A2.** A1 is Markov→Chebyshev (the derivation chain, the
transferable skill); A2 is Jensen applied to the option-payoff case, already previewed in
`F1.7a`-B3 — confirming it, not learning it fresh.

**The drift move (Adj #13).** Stop reading, write the unfinished sentence into note §2 as a
`⚠️ GAP`, switch to Tier A on paper. **For MGF specifically: write out `E[e^{tX}]` for a
Bernoulli by hand** (`qe^0 + pe^t = q+pe^t`, two terms) before touching anything continuous —
the definition is concrete immediately in the two-point case.

---

## Tier A — the floor (all four, unhinted, on paper)

**F1.7b-A1.** Derive Markov's inequality: for `X≥0`, `a>0`,
`E[X] ≥ a·P(X≥a)`, hence `P(X≥a) ≤ E[X]/a`. Then derive Chebyshev **from Markov**: apply Markov
to the non-negative random variable `(X-μ)²` with threshold `a=k²σ²`.
*Chebyshev is not a separate inequality to memorise — it is Markov applied to a squared,
recentered variable. If you can produce Chebyshev from Markov in under a minute, you have the
one fact that actually matters here; the two "different" formulas are one idea used twice.*

**F1.7b-A2.** State Jensen's inequality for convex `g`, with the one-sentence geometric
intuition (secant line lies above/below the graph, on which side, and why that gives the
inequality direction). Apply it to `g(x)=x²`: what does Jensen say about `E[X²]` vs. `(E[X])²`,
and what familiar quantity is the gap between them?
*The gap is exactly `Var(X) = E[X²]-(E[X])² ≥ 0` — Jensen applied to the convex function `x²` **is**
the statement that variance is non-negative. This is worth seeing once: Jensen isn't a separate
tool from variance, it generalizes the same fact to any convex function.*

**F1.7b-A3.** Write `M_X(t)=E[e^{tX}]` for a Bernoulli(`p`) and for an Exponential(`λ`). For the
exponential, state the range of `t` for which the MGF exists and say **what goes wrong** outside
that range (the integral diverges — show the integral and where it fails to converge).
*The existence range isn't a technicality to skip — a distribution with no MGF near 0 (e.g. a
genuinely heavy-tailed one) is a real and interview-relevant failure mode, and you can't say
anything sensible about it without having derived a case where the range is finite.*

**F1.7b-A4.** Differentiate `M_X(t)=E[e^{tX}]` once and evaluate at `t=0` to show
`M_X'(0)=E[X]`. State (don't necessarily derive) the general pattern `M_X^{(n)}(0)=E[X^n]`. Then:
given `M_X(t)=e^{3t+2t²}`, identify the distribution family and its parameters by pattern-
matching to a known MGF form.
*Answer: Normal, since `e^{μt+σ²t²/2}` is the normal MGF form — match `μ=3`, `σ²/2=2` so
`σ²=4`. Pattern-matching an MGF to a table is a real interview move; you don't re-derive the
whole table under time pressure, you recognise the shape.*

---

## Tier B — the target (≥2 of 4)

**F1.7b-B1.** Rank Markov, Chebyshev, and Jensen by "how much you need to know about `X`" to
apply each, and correspondingly by how tight the resulting bound tends to be. Give one sentence
on why more assumptions buy a tighter bound.
*Markov needs only `E[X]` and non-negativity — very loose. Chebyshev adds `Var(X)` — tighter.
Jensen needs the shape of `g` (convexity) rather than moments of `X` at all — different axis
entirely, not strictly "more assumptions" but a different kind of structure.*

**F1.7b-B2.** Use Markov to bound `P(X≥2E[X])` for any non-negative `X`, then say why this bound
is the same regardless of `X`'s actual distribution — and construct one distribution where the
Markov bound is nearly tight (i.e. the true probability is close to the bound) to show the bound
isn't vacuous.
*`P(X≥2E[X])≤1/2` always. Near-tight example: `X` is `0` with probability `1-ε` and
`E[X]/ε` with probability `ε`, for small `ε` — a two-point distribution concentrating almost all
its mass near the bound's threshold.*

**F1.7b-B3.** Given the MGF `M(t)=(pe^t/(1-qe^t))^r` for `t<-\ln q`, identify the distribution.
*Negative Binomial(`r,p`) — pattern-match to the table; this is the topic file's own listed
drill, included here because pattern-matching MGF forms is exactly A4's skill exercised again on
a less obvious case.*

**F1.7b-B4.** MLE preview (informal, not a derivation): you observe 7 heads in 10 flips of a
coin with unknown `p`. What value of `p` maximizes the probability of seeing exactly this data?
State the answer and the one-line reasoning, without formal calculus if you can see it directly.
*`p̂=0.7` — the sample proportion. This previews `S9.1` MLE; the point here is just recognising
"maximize probability of the data" as a concept before the machinery arrives, not deriving the
likelihood function formally.*

---

## Tier C — only if A+B ran short

**F1.7b-C1.** Prove Jensen's inequality for a twice-differentiable convex `g` using a first-order
Taylor expansion around `E[X]`: `g(X) ≥ g(E[X]) + g'(E[X])(X-E[X])`, then take expectations of
both sides.
*The linear term vanishes in expectation (`E[X-E[X]]=0`), leaving `E[g(X)]≥g(E[X])` directly —
a clean two-line proof once you see that the tangent line trick is the whole idea.*

---

## Code problems

Add to `src/solvers/s1_probability/conditional_expectation_verify.py` (created by `F1.7a`), or a
new adjacent file if that one is getting long — your call, keep it to one file if under ~60 lines
combined.

**F1.7-CODE2** — Verify Chebyshev's bound is a genuine upper bound (not necessarily tight): pick
a concrete non-normal distribution (e.g. a two-point distribution or an exponential), compute
`Var(X)` analytically, then Monte Carlo estimate `P(|X-μ|≥kσ)` for `k=2,3` and assert the
empirical probability is `≤ 1/k²` (with a small numerical tolerance for MC noise).
*Complexity: MC estimate `O(trials)`. The point of this solver isn't computing a single number —
it's demonstrating that the inequality holds as an upper bound across a distribution shape where
it is **not** tight, so "Chebyshev is loose" isn't just an assertion in the note, it's shown.*

---

## Deliverables

**D1 — Feynman note** `progress/feynman_notes/F1_7_expectation_variance_moments.md` — **§1(b)
today, then CLOSE THE NOTE**
- [ ] §1(b) teach-back: inequalities + MGF definition, source closed
- [ ] **Today's close:** §2 gaps · §3 napkin ≤200 words, said out loud · §4 where I'd meet it ·
      §5 summary table (linearity/LOTUS/tower/Eve's Law/Markov/Chebyshev/Jensen/MGF, one row
      each) · §6 where this breaks (≥2)
- [ ] Zero unresolved `⚠️ GAP`

**Note §5 for `F1.7` is a concept-and-one-liner table**, not a distribution table — one row per
named result (tower property, Eve's Law, Markov, Chebyshev, Jensen, MGF), each with its formula
and the one thing that makes it fail. That table is what the D4 test reproduces cold.

**D2 — Problems** (this file)
- [ ] A1–A4 unhinted, on paper
- [ ] ≥2 of Tier B
- [ ] Log which needed hints

**D3 — Code**
- [ ] `F1.7-CODE2`, asserting, with complexity docstring

**D3.5 — Concept notes** (2 min each, at today's close)
- [ ] `vault/concepts/linearity-of-expectation.md`
- [ ] `vault/concepts/tower-property.md`
- [ ] `vault/concepts/first-step-conditioning.md` — started here, extended by `S3` Markov chains
- [ ] `vault/concepts/moment-generating-function.md`
- [ ] `vault/concepts/jensen-inequality.md`
- [ ] Set `status: ready-for-test` and `actual_h:` in **both** `F1.7a` and `F1.7b` maps

**D4 — Unlock test → 2026-08-30**, one test covering `F1.7a`+`F1.7b` together.
- [ ] 5 fresh questions, 45 min, closed-book (Feynman note allowed). Pass ≥80%.
- [ ] Grade the day after.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** For `X≥0`, `a>0`: `E[X] = ∫₀^∞ x f(x)dx ≥ ∫_a^∞ x f(x)dx ≥ ∫_a^∞ a·f(x)dx = a·P(X≥a)`.
Dividing by `a`: `**P(X≥a) ≤ E[X]/a**`. (The middle step drops the `[0,a)` region, which only
loses non-negative mass; the last inequality replaces `x` with its lower bound `a` on the
remaining region.)

**Chebyshev from Markov:** let `Y=(X-μ)²≥0`. Apply Markov with threshold `a=k²σ²`:
```
P(Y ≥ k²σ²) ≤ E[Y]/(k²σ²) = Var(X)/(k²σ²) = σ²/(k²σ²) = 1/k²
```
`Y≥k²σ²` is the same event as `|X-μ|≥kσ` (both sides non-negative, square root preserves the
inequality), so `**P(|X-μ|≥kσ) ≤ 1/k²**`. One application of Markov to a squared variable — that
is the entire content of Chebyshev.

**A2.** Convex `g`: the chord connecting any two points on the graph lies **above** the graph.
Taking a "chord" over the distribution of `X` (weighted average of points on the curve) versus
evaluating `g` at the weighted average of the `x`-values (a single point on the curve) — the
chord/average-of-outputs sits above the curve/output-of-average: `**E[g(X)] ≥ g(E[X])**`.

Applied to `g(x)=x²` (convex): `E[X²] ≥ (E[X])²`. The gap `E[X²]-(E[X])² = **Var(X) ≥ 0**` —
Jensen applied to `x²` is exactly the statement that variance is non-negative.

**A3.** Bernoulli(`p`): `M_X(t) = E[e^{tX}] = (1-p)e^{0} + p·e^{t} = **q + pe^t**` (exists for
all `t`, finite sum).

Exponential(`λ`): `M_X(t) = ∫₀^∞ e^{tx}·λe^{-λx}dx = λ∫₀^∞ e^{-(λ-t)x}dx`. This integral
converges only if `λ-t>0`, i.e. **`t<λ`**, giving `M_X(t) = **λ/(λ-t)**`. For `t≥λ`, the
integrand `e^{-(λ-t)x}` doesn't decay (or grows) as `x→∞`, so the integral diverges — the MGF
simply doesn't exist there. **A distribution with heavier-than-exponential tails can fail to
have a finite MGF on any interval around 0**, which is why some heavy-tailed models (e.g. certain
Pareto/Cauchy-type distributions) are described by characteristic functions instead.

**A4.** `M_X'(t) = d/dt E[e^{tX}] = E[Xe^{tX}]` (differentiating under the expectation, valid
where the MGF exists on an open interval around `t`). At `t=0`: `M_X'(0)=E[Xe^{0}]=**E[X]**`.
Repeating, `M_X^{(n)}(0) = E[X^n e^{0}] = **E[X^n]**` — each derivative brings down one more
factor of `X` before evaluating at `t=0`.

`M_X(t)=e^{3t+2t²}` matches the **Normal** MGF form `e^{μt+σ²t²/2}`: `μ=**3**`,
`σ²/2=2 ⟹ σ²=**4**`. So `X ~ N(3,4)`.

</details>

<details>
<summary>Tier B</summary>

**B1.** Markov needs only `E[X]≥0` — the loosest bound, works for any non-negative distribution
with a mean. Chebyshev adds knowledge of `Var(X)` — tighter, because variance encodes more shape
information (how concentrated `X` is around its mean). Jensen needs no moments at all beyond
what's implicit in `g`'s convexity — it's not "more assumptions" in the same axis as Markov/
Chebyshev, it's a structural fact about a *transformation* of `X` rather than a tail bound on
`X` itself. **More structure assumed (variance, then a specific functional shape) buys a bound
that uses more of the actual information available, at the cost of needing that information.**

**B2.** `P(X≥2E[X]) ≤ E[X]/(2E[X]) = **1/2**`, for any non-negative `X` with finite mean —
distribution-free.

Near-tight example: let `X=0` with probability `1-ε` and `X=E[X]/ε` (call it `M`) with
probability `ε`, so `E[X]=ε·M`, meaning `M=E[X]/ε`. Then `2E[X] = 2εM`, and
`P(X≥2E[X]) = P(X=M)·\mathbb{1}[M≥2εM] = ε` when `2ε≤1`, i.e. `ε≤1/2`. As `ε→1/2`, this
probability approaches `1/2`, matching the Markov bound — showing the bound is achievable, not
just a loose worst case invented for no distribution.

**B3.** Matches the **Negative Binomial(`r,p`)** MGF form directly — same structure as `F1.4`'s
geometric (`r=1` case) raised to the `r`-th power, consistent with negative binomial being a sum
of `r` i.i.d. geometrics (MGF of a sum = product of MGFs, previewed here, proved in `S1.8`).

**B4.** `p̂ = **0.7**` — the sample proportion `7/10`. Informally: the binomial probability of
seeing exactly 7 heads in 10 flips, `C(10,7)p^7(1-p)^3`, is maximized where the derivative
w.r.t. `p` is zero, and by symmetry/calculus that happens exactly at `p = (\text{observed
successes})/(\text{trials})`. This is the intuitive answer `S9.1` will formalize as the MLE for
a binomial parameter.

</details>

<details>
<summary>Tier C</summary>

**C1.** For convex, twice-differentiable `g`, the first-order Taylor expansion around the point
`μ=E[X]` with Lagrange remainder gives, for any `x`:
`g(x) = g(μ) + g'(μ)(x-μ) + (1/2)g''(ξ)(x-μ)²` for some `ξ` between `x` and `μ`. Since `g` is
convex, `g''≥0` everywhere, so the remainder term is `≥0`, giving:
```
g(x) ≥ g(μ) + g'(μ)(x-μ)   for all x
```
Take expectations of both sides (treating `x` as the random variable `X`):
```
E[g(X)] ≥ g(μ) + g'(μ)·E[X-μ] = g(μ) + g'(μ)·0 = **g(μ) = g(E[X])**
```
The linear term vanishes because `E[X-μ]=E[X]-μ=0` by definition of `μ`. This is the tangent-
line-lies-below-the-curve statement, made algebraic — the same picture as A2's chord argument,
proved from the other side of the curve.

</details>
