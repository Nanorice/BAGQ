# Baseline Assessment

The diagnostic: 60 questions across the 13 sections of `inventory/`, timed, closed book, no AI.
Taken 2026-07-23/24 → **0.88 / 5 combined**. Results and red flags in
[`progress/baseline_scores.md`](../../progress/baseline_scores.md).

Kept as the **retest instrument** — the questions below are reused at the mid-checkpoint (S21)
and the final retest (S27), which is what makes the scores comparable. Two sittings of ~2h on
consecutive days; grade the next day with fresh eyes. Do not study for it: the point is to
measure today's self.

---

## Self-grading rubric (per question)

| Score | Meaning |
|---:|---|
| 0 | No idea what the question is asking. |
| 1 | Recognize the topic; cannot start. |
| 2 | Can set up the problem; cannot finish or made a critical error. |
| 3 | Correct approach; algebra/arithmetic slip; near-correct answer. |
| 4 | Fully correct; would need to double-check under pressure. |
| 5 | Fully correct; could explain to someone else on the spot. |

**Section score = mean of question scores in that section.**

**Interpretation:**
- 0.0–1.0 → **Cold start** — begin at Tier 0 for that section.
- 1.1–2.5 → **Rusty** — start at the section's earliest stage; expect standard time.
- 2.6–3.5 → **Working knowledge** — start mid-section; some early stages may auto-credit after a Feynman note.
- 3.6–5.0 → **Solid** — auto-credit early stages; go straight to unlock test to confirm.

---

## Sitting 1 — Sections I–VII (~2 h)

### Section I — Probability & Combinatorics (5 Q)

**I.1** How many ways to arrange the letters of `MISSISSIPPI`?
11!/(4! * 4! * 2!) (permutation and combinations)
**I.2** A test for a disease is 99% sensitive and 99% specific. Disease prevalence is 0.5%. You test positive. What is P(you have the disease)?
dont know what is sensitive and specific and prevalence. since it's an honest test I wont guess.
**I.3** X ~ Exp(λ). Compute E[X] and Var(X) from the definition (any method).
E[x] = integral(e^lambda)=e^lambda [this one i searched to confirm, knew it but not 100% certain]. variance is sum of x-e(x)/e(x) = 0 
**I.4** X, Y iid N(0,1). What is the distribution of X + Y? Of X² + Y²?
x+y ~ N(0,1) (not sure)
**I.5** State the tower property of conditional expectation and give one non-trivial application.
don't know
### Section II — Classical Puzzles (4 Q)

**II.1** Expected number of coin flips to see the pattern `HH` for the first time (fair coin).
4
**II.2** You roll a fair die repeatedly. What is E[sum of rolls until you first roll a 6]?
expected number of rolls until first 6 is 6, expected value of each throw is 3.5; so sum is 3.5*6=21****
**II.3** Coupon collector: expected draws to collect all n coupons, uniform. Formula + intuition.
don't know what this question is
**II.4** Broken stick: break a unit stick at two uniform random points. P(three pieces form a triangle)?
uniform distribution I know, and each point has probability 1/l, l being length of rod. we mark the length of the 3 segments la,lb,lc. 
la + lb + lc = 1; la + lb > lc; lb + lc > la; lc + la > lb. starting from a extreme case, a point at 1/4 ,the other point at 1/2. this is a case not forming a triangle. but if we move both points to the right a unit, they will form. until a symmetric case where the point that used to be at 1/2 now move to 3/4. so the length covered is 1/2. this is the probability of forming a triangle.

### Section III — Markov Chains (4 Q)

**III.1** A drunkard on integers {0,1,…,N} moves ±1 with prob 1/2 each. Starting at k, probability of hitting N before 0?
this i know from green book. probability of hitting N before 0 is same as hitting 0 before N. they are symmetrical, so probability is 1/2. 

**III.2** Define stationary distribution. When does it exist and when is it unique?
the mean is constant?

**III.3** A frog on the vertices of a tetrahedron jumps to a uniform-random neighbor each step. Starting at A, expected number of jumps to return to A.

4 vertics. each point other than A can be reached in 1 jump. when it jumpt to points other than A, it has 1/3 chance of jumping back, so from there expected number is 3. so total is 4

**III.4** Sketch the forward algorithm for HMMs (what does it compute, in what time complexity?).
only know it's hidden markov model, with current status for predict future status. but don't know how it works.

### Section IV — Continuous-Time Processes (4 Q)

**IV.1** State three defining properties of standard Brownian motion.
1
**IV.2** For BM `W_t`, compute E[W_s W_t] for s ≤ t.
1
**IV.3** State Itô's lemma. Apply it to derive the SDE for `S_t = exp(W_t)`.
1
**IV.4** Is `W_t² − t` a martingale? Prove or disprove.
0
### Section V — Stochastic Control (2 Q, quick)

**V.1** State the Bellman equation for a finite-horizon discrete MDP.
0
**V.2** Describe (in words) the secretary problem and its ~1/e optimal stopping threshold.
1
### Section VI — Derivative Pricing (5 Q)

**VI.1** One-step binomial tree: S₀=100, up=110, down=90, r=0. Price a call struck at 100.
0
**VI.2** Write the Black-Scholes formula for a European call. Define every symbol.
1
**VI.3** What is delta? What is gamma? Which is larger for an ATM 1-week option vs. an ATM 1-year option?
delta: change in derives price with respect to underlying price. gamma: change in delta with respect to underlying price. ATM 1 week
**VI.4** Put-call parity for a non-dividend stock. Prove it by arbitrage.
1; vaguely remember something + cash = something + stock
**VI.5** Explain the volatility smile in one paragraph. Why does it exist?
1;
### Section VII — Linear Algebra (3 Q)

**VII.1** Define eigenvalue and eigenvector. Compute eigenvalues of `[[2,1],[1,2]]`.
eigenvalue and eigenvector of a matrix, is a combination such that the transformation applied to eigenvector by the matri, is the same as the eigenvalue. but forgot how to compute. 
**VII.2** What does it mean for a matrix to be positive semi-definite? Give one financial context where it matters.
1;
**VII.3** Given a covariance matrix Σ, briefly describe how PCA gives you principal components.
1;
---

## Sitting 2 — Sections VIII–XIII + Coding (~2 h)

### Section VIII — Calculus & DEs (3 Q)

**VIII.1** Solve dy/dx = y with y(0)=1.
y = sqrt(2/(x-2))
**VIII.2** State the heat equation. State (informally) why it is connected to Black-Scholes.
1;
**VIII.3** Use Lagrange multipliers to minimize `x² + y²` subject to `x + y = 1`.
1
### Section IX — Statistics & Estimation (4 Q)

**IX.1** Derive the MLE for the rate parameter of an Exponential distribution from n iid samples.
0
**IX.2** Explain Type I and Type II errors. What does statistical power mean?
1: false positive and false negative?
**IX.3** OLS assumptions — list them and describe what breaks if each is violated.
1; ordinary least square. don't know boundary
**IX.4** GARCH(1,1) — write the variance equation. What does each parameter capture intuitively?
1; only know it's auto regression, time series model?
### Section X — Algorithms & Data Structures (5 Q — timed coding)

Write actual code (Python). Note complexity.
I'll do psedo code for now
**X.1** Two-sum: given array + target, return indices of two elements summing to target. O(n).
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
**X.2** Longest palindromic substring. Any correct approach.
palindromic's definition is a string that reads the same backward as forward. 
def is_palindrome(s):
    return s == s[::-1]
longest = ''
for i in range(len(s)):
    for j in range(i, len(s)):
        if is_palindrome(s[i:j+1]):
            # check if it's the longest found so far
            if j - i + 1 > len(longest):
                longest = s[i:j+1]

**X.3** Coin change: min number of coins for amount N, given denominations. DP.
not familiar with dp. 
**X.4** BFS on a graph represented as adjacency list; return shortest path length from src to dst.
don't know what bfs is.
**X.5** Simulate a fair 7-sided die using only a fair 5-sided die. Expected calls per output?
for 7-sided dies each face has prob 1/7;
for 5-sided dies each face has prob 1/5;
we can use sequence in 5-sided dies to simulate 7-sided dies. 
hmm, stuck..

### Section XI — Information Theory (2 Q)

**XI.1** Define Shannon entropy for a discrete distribution. Compute H for a fair coin and a coin with p=0.9.
0
**XI.2** State the Kelly criterion for a favorable bet. What does it optimize?
1
### Section XII — Game Theory (2 Q)

**XII.1** In a second-price sealed-bid auction, why is bidding your true value a (weakly) dominant strategy?
0; don;t know the term
**XII.2** Rock-paper-scissors: what is the Nash equilibrium and its expected payoff?
0
### Section XIII — Measure Theory (2 Q — expect low scores; that's fine)

**XIII.1** Define a σ-algebra. Why do we need one for probability?
0
**XIII.2** State (informally) Girsanov's theorem and where it is used in finance.
0
---

## Scoring template

Save as `progress/baseline_scores.md`:

```markdown
# Baseline scores — <YYYY-MM-DD>

| Section | # questions | Raw sum | Mean (0–5) | Interpretation |
|---|---:|---:|---:|---|
| I  Probability & Combinatorics | 5 | __ | _.__ | ___ |
| II Classical puzzles           | 4 | __ | _.__ | ___ |
| III Markov chains              | 4 | __ | _.__ | ___ |
| IV Continuous-time processes   | 4 | __ | _.__ | ___ |
| V  Stochastic control          | 2 | __ | _.__ | ___ |
| VI Derivative pricing          | 5 | __ | _.__ | ___ |
| VII Linear algebra             | 3 | __ | _.__ | ___ |
| VIII Calculus & DEs            | 3 | __ | _.__ | ___ |
| IX Statistics & estimation     | 4 | __ | _.__ | ___ |
| X  Algorithms & DS             | 5 | __ | _.__ | ___ |
| XI Information theory          | 2 | __ | _.__ | ___ |
| XII Game theory                | 2 | __ | _.__ | ___ |
| XIII Measure theory            | 2 | __ | _.__ | ___ |

## Notes
- Which sections surprised me (better than expected)?
- Which sections surprised me (worse than expected)?
- Adjustments to the traversal plan in `progression.md`:
```

---

## Retest cadence

- **First retake:** Week 10 mid-checkpoint (Sections I–III + IX + X focus).
- **Second retake:** Week 25 final (all sections).
- Track deltas; a *regression* on any section = schedule a Feynman refresh for its stages.

---

*Version: 0.1 | Created: 2026-07-23*
