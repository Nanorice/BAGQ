# Topic Map — Stages ↔ Source Sections

> **What this file answers:** "I'm doing stage X. Which part of `topics/` does it cover,
> which problems there are in scope, and what am I deliberately not doing yet?"
>
> `topics/` (formerly `archive/`) is the **full scope inventory** — 911 problems across 13
> sections, written for someone who already has the material. It is not the curriculum and
> never was. A stage eats a *named subset* of it. This table records which subset, so that
> when you revisit a section you know what you already closed.
>
> **Last updated:** 2026-07-29

---

## Naming

| Prefix | Means | Example |
|---|---|---|
| `S<n>.<m>` | Section `n` (Roman numeral in `topics/`), subsection `m`. **Meaningful** — maps directly onto the source file. | `S1.7` = §I.7 Expectation & Moments |
| `T0.<x>` | Tier-0 setup stage. The letter is **sequence only**, no meaning. Legacy — kept because the DAG and closed notes reference it. | `R.calculus` = Calculus Refresher |

**Convention going forward:** lead with the plain English name, keep the ID as a subscript.
Write "Linear Algebra Refresher `R.linalg`", not "R.linalg". IDs are for the dependency graph in
[03_gated_progression.md](03_gated_progression.md); names are for humans.

Section number ↔ Roman numeral: `S1`→I, `S2`→II, `S3`→III, `S4`→IV, `S5`→V, `S6`→VI,
`S7`→VII, `S8`→VIII, `S9`→IX, `S10`→X, `S11`→XI, `S12`→XII, `S13`→XIII.

---

## Tier 0 — Foundations

### Calculus Refresher `R.calculus` ✅ CLOSED 2026-07-29 (5.0h)
**Source:** [§VIII Calculus, DEs & Analysis](topics/section_VIII_calculus_des.md)

| | |
|---|---|
| **In scope** | §VIII.1 ODEs — *Exponential Growth/Decay*, *Logistic Growth*. Plus §VIII.1 *Mean-Reverting ODE (Deterministic OU)* and *The Perpetual Annuity ODE* via problem-set B3/A6. §VIII.3 *Lagrange Multipliers* (concept) + *Markowitz Optimization — Lagrange Multipliers* (via R_calculus-C2). |
| **Deferred → post-S4/S6** | All of §VIII.2 (PDEs): *Heat Equation*, *Black-Scholes PDE*, *Feynman-Kac*, *Separation of Variables*, *Carr-Madan*, *Barrier/Basket PDEs*. Also §VIII.1 *Second-Order Linear ODE*, *Damped Oscillator*, *Systems of ODEs*, *Riccati*, *Phase Portraits*, *Green's Function*, *Stability Analysis*. §VIII.3 *Kelly Criterion*, *KKT*, *Euler-Lagrange*, *Brachistochrone*, *Duality*. |
| **Why deferred** | User note 2026-07-29: useful framing but needs the finance first. Revisit once S4 (BM/Itô) and S6 (BS/Greeks) are in hand — Feynman-Kac in particular is unreadable without both. |
| **Closes baseline** | VIII.1 (`dy/dx=y`), VIII.3 (Lagrange) |

### Linear Algebra Refresher `R.linalg` — Thu 2026-07-30
**Source:** [§VII Linear Algebra & Matrix Theory](topics/section_VII_linear_algebra.md)

| | |
|---|---|
| **In scope** | §VII.1 *Eigenvalues and Eigenvectors* (concept), *Symmetric Matrices*, *Positive Definite / Positive Semi-Definite*, *Spectral Theorem — Verification*. §VII.2 *Covariance Matrix*, *Correlation Matrix* (PSD property only). |
| **Deferred → S7/S20** | §VII.1 *Gaussian Elimination*, *LU Decomposition*, *SVD — Low-Rank Approximation*, *Cholesky — Correlated Samples* (implementation; the *reason* is in scope via B5), *Condition Number*, *Matrix Exponential*, *Rank and Null Space*, *Sherman-Morrison*, *Power Iteration*. All of §VII.2 applications: *PCA on Yield Curves*, *PCA on Equity Returns*, *Markowitz*, *Risk Parity*, *Ledoit-Wolf Shrinkage*, *Marchenko-Pastur*, *Factor Models*. |
| **Why deferred** | PCA proper is S7, scheduled S20. This stage builds its foundation (eigen-decomposition by hand + why Σ is PSD), not the application. |
| **Closes baseline** | VII.1 (eigenvalues of `[[2,1],[1,2]]`), VII.2 (PSD) |

---

## Tier 1 — Distributions (was `T1.X`, split 2026-07-29)

> **Rename note:** `T1.X` was a placeholder ID that froze into the syllabus. It was also
> mis-scoped — [S15.md:49](progress/sprints/S15.md) flagged it as "Tier-1 sized wearing a
> Tier-0 label" (9 distributions ≈ 8h vs. the ≤90-min-block rule in contract §A.0). Split
> into two stages, named, and mapped onto the section IDs they actually belong to.

### Discrete Distributions `F1.4a` — Fri 2026-07-31
**Source:** [§I.4 Discrete Random Variables & Distributions](topics/section_I_probability_combinatorics.md) · **Book:** Ross 6th ed., Ch. 4

| | |
|---|---|
| **In scope** | Bernoulli, Binomial, Geometric, Poisson. For each: PMF, E[X], Var, MGF, one classic problem. Poisson-as-limit-of-binomial derivation. |
| **Deferred** | Negative binomial, hypergeometric → S1.4 (S18). |
| **Closes baseline** | Partial: I.4 (scored 1) |

### Continuous Distributions `F1.4b` — Sat 2026-08-01
**Source:** [§I.5 Continuous Random Variables & Distributions](topics/section_I_probability_combinatorics.md) · **Book:** Ross 6th ed., Ch. 5

| | |
|---|---|
| **In scope** | Uniform, Exponential, Normal. Memorylessness of the exponential. |
| **Deferred** | Log-normal → S6 (belongs next to Black-Scholes). χ² → S9.2 (belongs next to hypothesis testing). Both were in the original 9; moved because they are cheaper to learn where they get used. |
| **Closes baseline** | I.3 (exponential, scored 1). χ² (I.4) deferred with the topic. |

---

## Sections not yet touched

| Section | Stages | First scheduled |
|---|---|---|
| [§I Probability & Combinatorics](topics/section_I_probability_combinatorics.md) | S1.1 Combinatorics, S1.2 Bayes, S1.6 Joint/MVN, S1.7 Expectation/Tower, S1.8 MGF | S16 (Aug 3) |
| [§II Classical Puzzles](topics/section_II_classical_puzzles.md) | S2.1 | S21 |
| [§III Markov Chains](topics/section_III_markov_chains.md) | S3.1, S3.2 | S22 |
| [§IV Continuous-Time Processes](topics/section_IV_continuous_time_processes.md) | S4.1 BM, S4.2 Martingales/OST, S4.3 Itô | S25 |
| [§VI Derivative Pricing](topics/section_VI_derivative_pricing.md) | S6.1 Binomial, S6.2 BS/Greeks, S6.5 MC | S26 |
| [§IX Statistics & Estimation](topics/section_IX_statistics_estimation.md) | S9.1 MLE, S9.2 Hyp testing, S9.3 Regression/TS, S9.4 Bayesian | S23 |
| [§X Algorithms & DS](topics/section_X_algorithms_ds.md) | S10.1 arrays/hash, S10.2 DP, S10.3 graphs/BFS, S10.4 numerical | S17 |

**Deferred whole (post-Q1 backlog):** §V Stochastic Control, §XI Information Theory
(except a 20-min Kelly read), §XII Game Theory (except a 20-min Vickrey read),
§XIII Measure Theory. See [SYLLABUS.md](SYLLABUS.md) deferred list.

---

## How to maintain this

When you close a stage, add or update its row: what you actually did (quote the **bolded
problem names** from the source file — those sections have no numeric indices), what you
deferred, and why. The "why" is the part that pays off in three months when you reopen a
section and can't remember whether you skipped something because it was hard or because it
was out of scope.
