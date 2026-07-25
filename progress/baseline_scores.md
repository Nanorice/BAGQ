# Baseline scores — 2026-07-23/24 (both sittings complete)

## Combined summary

| Section | # Q | Raw sum | Mean (0–5) | Interpretation | Priority |
|---|---:|---:|---:|---|---|
| I  Probability & Combinatorics | 5 | 6 | 1.20 | Rusty | 🔴 Core |
| II Classical puzzles           | 4 | 6 | 1.50 | Rusty | 🔴 Core |
| III Markov chains              | 4 | 6 | 1.50 | Rusty | 🔴 Core |
| IV Continuous-time processes   | 4 | 3 | 0.60 | Cold start | 🟡 Later |
| V  Stochastic control          | 2 | 1 | 0.50 | Cold start | ⚫ Deferred |
| VI Derivative pricing          | 5 | 6 | 1.20 | Rusty | 🟡 Later |
| VII Linear algebra             | 3 | 4 | 1.33 | Rusty | 🔴 Core |
| VIII Calculus & DEs            | 3 | 3 | 1.00 | Cold/Rusty | 🔴 T0 refresher |
| IX Statistics & estimation     | 4 | 4 | 1.00 | Rusty (low) | 🔴🔴 Critical for target |
| X  Algorithms & DS             | 5 | 6 | 1.20 | Rusty (low) | 🔴🔴 Critical for target |
| XI Information theory          | 2 | 1 | 0.50 | Cold start | ⚫ Deferred |
| XII Game theory                | 2 | 0 | 0.00 | Cold start | ⚫ Deferred (20-min Vickrey read) |
| XIII Measure theory            | 2 | 0 | 0.00 | Cold start | ⚫ Deferred |

**Combined mean (unweighted across sections): 0.88**
**Highest:** II Puzzles (1.50) · **Lowest critical-path:** IX Stats & X Algos (both 1.00–1.20)
**Zero sections with auto-credit; zero accelerations triggered.**

---

## Per-question breakdown (Sitting 1)

### Section I — Probability & Combinatorics (1.20)
- I.1 MISSISSIPPI → **4** (34,650, correct)
- I.2 Bayes disease → **0** (vocabulary block; ~33%)
- I.3 E/Var of Exp(λ) → **1** (wrote e^λ, 0; correct = 1/λ, 1/λ²)
- I.4 X+Y, X²+Y² → **1** (said N(0,1); correct = N(0,2) and χ²(2))
- I.5 Tower property → **0**

### Section II — Classical Puzzles (1.50)
- II.1 E[flips for HH] → **1** (said 4; correct = 6)
- II.2 E[sum until first 6] → **3** (answer 21 correct via Wald, reasoning accidentally right)
- II.3 Coupon collector → **0**
- II.4 Broken stick → **2** (arrived at 1/2; correct = 1/4; right instinct)

### Section III — Markov Chains (1.50)
- III.1 Gambler's ruin, general k → **1** (invoked symmetry, said 1/2; correct = k/N)
- III.2 Stationary distribution → **0**
- III.3 Frog on tetrahedron → **4** (correct implicit recursion, answer 4)
- III.4 HMM forward algorithm → **1**

### Section IV — Continuous-Time Processes (0.60)
- IV.1–IV.4 → **1, 1, 1, 0** — cold start

### Section V — Stochastic Control (0.50)
- V.1, V.2 → **0, 1** — cold start

### Section VI — Derivative Pricing (1.20)
- VI.1 Binomial call → **0**
- VI.2 BS formula → **1**
- VI.3 Delta, Gamma, ATM 1w vs 1y → **3** (bright spot — real intuition)
- VI.4 Put-call parity → **1** (fuzzy shape)
- VI.5 Vol smile → **1**

### Section VII — Linear Algebra (1.33)
- VII.1 Eigenvalues [[2,1],[1,2]] → **2** (def correct, computation forgotten; correct = 1, 3)
- VII.2 PSD → **1**
- VII.3 PCA → **1**

---

## Per-question breakdown (Sitting 2)

### Section VIII — Calculus & DEs (1.00)
- VIII.1 dy/dx=y, y(0)=1 → **1** (⚠️ answered sqrt(2/(x-2)); correct = **eˣ**. Canonical ODE — red flag for T0.C)
- VIII.2 Heat equation ↔ BS → **1** (fuzzy recognition)
- VIII.3 Lagrange x²+y² s.t. x+y=1 → **1** (fuzzy; correct = x=y=1/2, min=1/2)

### Section IX — Statistics & Estimation (1.00) — critical for target
- IX.1 MLE for Exp rate → **0** (correct: λ̂ = 1/x̄)
- IX.2 Type I/II errors → **2** (Type I/II correct; missed statistical power definition)
- IX.3 OLS assumptions → **1** (recognizes acronym, no content)
- IX.4 GARCH(1,1) → **1** (knows it's autoregressive; no equation)

### Section X — Algorithms & DS (1.20) — critical for target
- X.1 Two-sum → **2** (⚠️ wrote O(n²) brute force; question required O(n); need hash-map pattern)
- X.2 Longest palindrome → **3** (O(n³) brute force works; correct)
- X.3 Coin change DP → **0** ("not familiar with DP")
- X.4 BFS → **0** (⚠️ "don't know what BFS is" — serious HFT-screen blocker)
- X.5 Fair 7-die from 5-die → **1** (attempted rejection-sampling idea, stuck; correct ≈ 2.38 calls avg)

### Section XI — Information Theory (0.50)
- XI.1 Shannon entropy → **0**
- XI.2 Kelly criterion → **1**

### Section XII — Game Theory (0.00)
- XII.1, XII.2 → **0, 0**

### Section XIII — Measure Theory (0.00)
- XIII.1, XIII.2 → **0, 0** (expected)

---

## Positives across both sittings

1. **III.3 (frog on tetrahedron)** — clean implicit recursion mentally
2. **VI.3 (Greeks intuition)** — correct that short-dated ATM gamma dwarfs long-dated
3. **II.4 (broken stick)** — constructive geometric attempt; right instinct, wrong answer
4. **II.2 (Wald-by-accident)** — right number, wrong reasoning path
5. **IX.2 (Type I/II)** — half-credit; partial recall
6. **X.2 (palindrome)** — correct logic, works

## Red flags across both sittings

1. **VIII.1** — Missing the *most canonical* ODE (y'=y → y=eˣ). T0.C calculus refresher must be executed, not skimmed.
2. **X.4** — "Don't know what BFS is." This is not a knowledge gap; it's a *blocker* for HFT interviews. S10.3 must ship solid, not just checked off.
3. **I.5, IX.1** — Tower property and MLE both scored 0. Both are *tools*, not topics. They compound: without tower you can't do Bayesian stats; without MLE you can't fit anything.
4. **X.1 complexity awareness** — Wrote a correct answer but at wrong complexity. Interviewers grade on Big-O explicitly. Include complexity annotations in every solver from Sprint 17 onward.

## Diagnosis (updated)

Same as after Sitting 1: **reasoning ≥ formalism**. When a question maps to raw thinking (III.3, II.4, X.2), you produce work. When it maps to named machinery (I.5, VIII.1, IX.1, X.4), you're empty. This is a *vocabulary-and-machinery* problem, not an *ability* problem — closable in 6 months of disciplined Feynman notes.

The two additional insights Sitting 2 gave:
- **Section IX and X are both at ~1.0** and both are critical for buy-side QR + HFT. Neither gets accelerated. Both sprints (23–25 for stats, 17–22 for algo parallel track) run at full duration.
- **Section VIII is worse than assumed.** T0.C (calculus refresher) needs to actually cover: ODEs (separation of variables + linear first-order), Lagrange multipliers, chain rule / implicit differentiation. Cannot be skimmed.

---

## Adjustments to `03_gated_progression.md` (updated after Sitting 2)

Already applied from Sitting 1:
1. ✅ S1.7 pulled forward to Sprint 17
2. ✅ Sprint 16 gains "Named distributions" mini-stage
3. ✅ Sprint 16 gains Bayes vocabulary block
4. ✅ T0.D extended to 2×2/3×3 eigenvalue computation by hand
5. ✅ Sprint 17 carries 3 stages (watch velocity)

New from Sitting 2:
6. **T0.C calculus refresher expanded and made mandatory-deep**: ODEs (dy/dx = y, separable + linear), Lagrange multipliers, chain rule. Not a skim. Add Feynman-note requirement.
7. **Sprint 17 S10.1 must include hash-map pattern explicitly** (Two-sum, contains-duplicate, group-anagrams). Complexity annotations required on every solver.
8. **Sprint 19 S10.3 (graphs/BFS/DFS) upgraded from "parallel" to "primary focus of Sprint 19"**. BFS being unknown is a critical blocker.
9. **Every solver from Sprint 17 onward must include a docstring with time + space complexity.** This becomes part of D3 (code twin) deliverable spec.
10. **Add a "cheap wins" week to Sprint 16**: 30-min blocks on vocabulary-only topics that scored 0 due to terminology (Bayes disease-test, coupon collector, put-call parity direction). These are all <30 min each and would jump scores by ~1 point.

---

*Grading conducted: 2026-07-24 by AI reviewer, both sittings graded together with honest rubric.*

<!-- NOTE: radar_chart.py was previously pasted below this line by accident.
     Split out to progress/radar_chart.py on 2026-07-25. -->
