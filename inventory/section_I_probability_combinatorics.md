# Section I: Probability Theory & Combinatorics — Detailed Problem List

> *Foundation: Kolmogorov axioms, σ-algebras, measure-theoretic probability*

Probability Theory and Combinatorics form the bedrock of every quant interview. Nearly every brain teaser, pricing question, or stochastic modeling problem ultimately reduces to counting, conditioning, or computing expectations. Mastery here means being able to set up a problem from first principles — define the sample space, assign probabilities, and extract the answer via conditioning, symmetry, or generating functions.

---

## 1. Combinatorics & Counting

Counting underpins discrete probability. Many interview problems are "just" counting in disguise.

### Core Concepts

- **Permutations:** $P(n, k) = n! / (n-k)!$ — ordered selections.
- **Combinations:** $\binom{n}{k} = n! / (k!(n-k)!)$ — unordered selections.
- **Multinomial Coefficients:** $\binom{n}{k_1, k_2, \ldots, k_m} = n! / (k_1! k_2! \cdots k_m!)$.
- **Stars and Bars:** The number of ways to place $n$ indistinguishable balls into $k$ distinguishable bins is $\binom{n+k-1}{k-1}$.
- **Derangements:** $D_n = n! \sum_{k=0}^{n} (-1)^k / k!$ — permutations with no fixed points.
- **Catalan Numbers:** $C_n = \binom{2n}{n}/(n+1)$ — count Dyck paths, valid parenthesizations, binary trees, etc.
- **Stirling Numbers (2nd kind):** $S(n,k)$ counts the number of ways to partition $n$ elements into $k$ non-empty subsets.

### Key Problems and Questions

- **The Ballot Problem:** Candidate A gets $a$ votes, B gets $b$ votes ($a > b$). What is the probability A is strictly ahead throughout the counting? (Answer: $(a-b)/(a+b)$.)
- **Counting Lattice Paths:** How many paths from $(0,0)$ to $(m,n)$ using only right and up steps? How many avoid the diagonal (Catalan)?
- **Distributing Identical Objects:** How many ways to distribute 20 identical candies to 4 children so each gets at least 2? (Stars and bars with lower bounds.)
- **The Anagram Problem:** How many distinct arrangements of the letters in "MISSISSIPPI"? Generalize to any word with repeated letters.
- **Derangement Probability:** At a party of $n$ people, coats are returned at random. What is the probability nobody gets their own coat? Show the limit approaches $1/e$.
- **Catalan Applications — Valid Parentheses:** How many ways to arrange $n$ pairs of parentheses so they are balanced?
- **Surjections (Onto Functions):** How many surjective functions are there from a set of size $n$ to a set of size $k$? (Inclusion-exclusion.)
- **Grid Paths with Obstacles:** Count lattice paths from $(0,0)$ to $(n,n)$ that avoid a specific set of blocked squares. (Lindström-Gessel-Viennot lemma.)
- **The Twelvefold Way:** Classify the 12 types of ball-into-bin problems (labeled/unlabeled balls, labeled/unlabeled bins, any/injective/surjective maps) and give the formula for each.
- **Partitions of an Integer:** How many ways can you write $n$ as a sum of positive integers (order doesn't matter)? Implement a dynamic programming solution.

---

## 2. Classical (Discrete) Probability

Classical probability deals with finite or countable sample spaces where outcomes can be enumerated and counted directly.

### Core Concepts

- **Sample Space (Ω):** The set of all possible outcomes of an experiment.
- **Event:** A subset of the sample space; probability is assigned to events.
- **Equally-Likely Outcomes:** When $P(\omega) = 1/|\Omega|$ for all $\omega$, probability reduces to counting: $P(A) = |A|/|\Omega|$.
- **Inclusion-Exclusion Principle:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, generalized to $n$ events.
- **Pigeonhole Principle:** If $n$ items are placed into $m$ containers with $n > m$, at least one container holds more than one item.

### Key Problems and Questions

- **Dice Probability Basics:** What is the probability that the sum of two fair dice equals 7? Generalize to $n$ dice summing to $k$.
- **Matching Problem (Montmort):** $n$ people each place a hat in a box; hats are redistributed randomly. What is the probability that no one gets their own hat? (Derangements.)
- **The Lottery Problem:** Given $n$ tickets with $k$ winners, compute the probability of holding at least one winner if you buy $m$ tickets.
- **Sampling With vs. Without Replacement:** A bag has $r$ red and $b$ blue balls. You draw $k$ balls. Compare probabilities of "all red" under both schemes.
- **The Sock Drawer Problem:** A drawer has $n$ pairs of socks in $n$ colors. You draw socks one at a time in the dark. How many draws until you have a matching pair? (Pigeonhole.)
- **Dice Divisibility:** Roll a fair die twice. What is the probability the product of the two rolls is divisible by 6?
- **Committee Selection with Constraints:** From a group of $m$ men and $w$ women, how many ways can you form a committee of size $k$ with at least 2 women?
- **The Poker Dice Problem:** Roll 5 dice. What is the probability of getting exactly one pair? A full house? Five of a kind?

---

## 3. Conditional Probability & Bayes' Theorem

Conditional probability is the workhorse of interview math. Most real-world problems require updating beliefs given partial information.

### Core Concepts

- **Conditional Probability:** $P(A|B) = P(A \cap B) / P(B)$.
- **Law of Total Probability:** $P(A) = \sum_i P(A|B_i) P(B_i)$ for a partition $\{B_i\}$ of $\Omega$.
- **Bayes' Rule:** $P(B|A) = P(A|B) P(B) / P(A)$ — invert the conditioning.
- **Independence:** Events $A$, $B$ are independent iff $P(A \cap B) = P(A)P(B)$.
- **Conditional Independence:** $A$ and $B$ may be dependent marginally but independent given $C$ (or vice versa).

### Key Problems and Questions

- **The Boy or Girl Paradox:** A family has two children. Given that at least one is a boy, what is the probability both are boys? What if you know the *older* child is a boy?
- **The Monty Hall Problem:** You pick one of three doors. The host (who knows what's behind them) opens a losing door. Should you switch? Compute the probabilities.
- **Disease Testing (Base-Rate Problem):** A test has 99% sensitivity and 95% specificity. If the disease prevalence is 1%, what is the probability a positive test result is a true positive?
- **The False Positive Paradox:** Extend the disease testing problem: show that even with a "good" test, most positives can be false when prevalence is low.
- **Two Envelopes Problem:** One envelope has twice the money of the other. You pick one and see $x$. Should you switch? Resolve the apparent paradox.
- **Simpson's Paradox:** Construct a scenario where a treatment appears better in every subgroup but worse overall. Explain via conditional probability.
- **The Broken Stick Conditioned:** A stick of length 1 is broken at a uniform random point. Given that the longer piece is > 0.7, what is the expected length of the shorter piece?
- **Prosecutor's Fallacy:** A DNA match has probability $10^{-6}$. In a city of 1 million, what is the probability the suspect is guilty given a match? Show why $P(\text{match}|\text{guilty}) \neq P(\text{guilty}|\text{match})$.
- **Updating with Multiple Pieces of Evidence:** You flip a coin that is either fair or double-headed (prior: 50/50). You observe 5 heads in a row. What is the posterior probability the coin is fair?
- **The Taxi-Cab Problem (Kahneman & Tversky):** 85% of cabs are green, 15% blue. A witness (80% reliable) says the cab was blue. What is the probability it was actually blue?


---

## 4. Discrete Random Variables & Distributions

### Core Concepts

- **PMF (Probability Mass Function):** $p(x) = P(X = x)$ for discrete $X$.
- **CDF (Cumulative Distribution Function):** $F(x) = P(X \le x)$.
- **Expectation:** $E[X] = \sum_x x \cdot p(x)$.
- **Variance:** $\text{Var}(X) = E[X^2] - (E[X])^2$.
- **Key Distributions:**
  - *Bernoulli($p$):* Single trial, $P(X=1)=p$.
  - *Binomial($n,p$):* Number of successes in $n$ independent trials.
  - *Geometric($p$):* Number of trials until first success.
  - *Negative Binomial($r,p$):* Trials until $r$-th success.
  - *Poisson($\lambda$):* Limit of Binomial for rare events; $P(X=k) = e^{-\lambda}\lambda^k/k!$.
  - *Hypergeometric:* Sampling without replacement from a finite population.

### Key Problems and Questions

- **Expected Rolls to See All Faces:** Roll a fair die repeatedly. What is the expected number of rolls to see all 6 faces? (Coupon collector: $6 \cdot H_6$ where $H_n$ is the harmonic number.)
- **Geometric Distribution — Memorylessness:** Prove that $P(X > m+n | X > m) = P(X > n)$ for geometric $X$. Give an intuitive explanation.
- **Poisson Approximation:** A book has 1000 pages, each with a $0.001$ probability of a typo. What is the probability of exactly 2 typos? Compare Binomial vs. Poisson.
- **Sum of Independent Poissons:** If $X \sim \text{Poisson}(\lambda)$ and $Y \sim \text{Poisson}(\mu)$ are independent, prove $X + Y \sim \text{Poisson}(\lambda + \mu)$. Codify via simulation.
- **Binomial Confidence:** You observe 7 heads in 10 flips. Compute the MLE for $p$ and a 95% confidence interval (exact binomial or normal approximation).
- **Negative Binomial — Waiting for $r$ Successes:** A gambler needs 3 wins to leave. Each game is won with probability $0.4$. What is the expected number of games played?
- **Hypergeometric — Aces in a Hand:** A 5-card poker hand is dealt from a standard deck. What is the probability of exactly 2 aces? Compare with the binomial approximation.
- **The Random Walk (1D):** A particle starts at 0 and moves $\pm1$ with equal probability. What is the probability it returns to 0 after $2n$ steps? What is the expected number of returns?
- **Entropy of a Discrete Distribution:** Compute the Shannon entropy $H(X) = -\sum p(x) \log p(x)$ for a loaded die. Which distribution maximizes entropy?
- **Simulating Distributions:** Write Python code to simulate Bernoulli, Binomial, Geometric, and Poisson random variables from scratch using only `random.uniform(0,1)` (inverse transform and acceptance-rejection).

---

## 5. Continuous Random Variables & Distributions

### Core Concepts

- **PDF (Probability Density Function):** $f(x)$ such that $P(a \le X \le b) = \int_a^b f(x) dx$.
- **CDF:** $F(x) = P(X \le x) = \int_{-\infty}^{x} f(t) dt$.
- **Expectation:** $E[X] = \int x f(x) dx$.
- **Key Distributions:**
  - *Uniform($a,b$):* $f(x) = 1/(b-a)$ on $[a,b]$.
  - *Exponential($\lambda$):* Memoryless; $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
  - *Normal($\mu, \sigma^2$):* The bell curve; closed under linear combinations.
  - *Log-Normal:* $\ln X \sim N(\mu, \sigma^2)$; models asset prices in Black-Scholes.
  - *Gamma($\alpha, \beta$):* Generalizes exponential; sum of $\alpha$ independent Exponentials when $\alpha \in \mathbb{N}$.
  - *Beta($\alpha, \beta$):* Defined on $[0,1]$; conjugate prior for Bernoulli.

### Key Problems and Questions

- **Uniform Order Statistics:** Generate $n$ i.i.d. $\text{Uniform}(0,1)$ random variables. What is the distribution of the $k$-th smallest (the $k$-th order statistic)? Derive the PDF (Beta distribution).
- **Exponential Memorylessness:** Prove $P(X > s+t | X > s) = P(X > t)$ for $X \sim \text{Exp}(\lambda)$. Why does this make it the continuous analogue of the geometric?
- **Sum of Exponentials → Gamma:** Show by convolution that the sum of $n$ independent $\text{Exp}(\lambda)$ r.v.s is $\text{Gamma}(n, \lambda)$.
- **Minimum of Exponentials:** If $X_1, \ldots, X_n$ are independent with $X_i \sim \text{Exp}(\lambda_i)$, prove $\min(X_1, \ldots, X_n) \sim \text{Exp}(\lambda_1 + \cdots + \lambda_n)$. Application: competing Poisson processes.
- **Normal Distribution — 68-95-99.7 Rule:** Derive the exact probabilities $P(|Z| \le 1)$, $P(|Z| \le 2)$, $P(|Z| \le 3)$ numerically.
- **Sum of Normals:** If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, prove $X+Y \sim N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ via MGFs.
- **Log-Normal Moments:** If $X \sim \text{LogNormal}(\mu, \sigma^2)$, derive $E[X]$ and $\text{Var}(X)$. Why is this distribution important for GBM asset prices?
- **Inverse Transform Sampling:** Given a CDF $F$, show that $F^{-1}(U)$ where $U \sim \text{Uniform}(0,1)$ has CDF $F$. Implement for Exponential and Normal (Box-Muller).
- **The Broken Stick Problem (Continuous):** A stick of length 1 is broken at two uniform random points. What is the probability the three pieces form a triangle? (Answer: $1/4$.)
- **Tail Probabilities and Mills' Ratio:** For $Z \sim N(0,1)$, show that $P(Z > x) \approx \phi(x)/x$ for large $x$ (Mills' ratio). Why does this matter for VaR calculations?

---

## 6. Joint Distributions & Multivariate Probability

### Core Concepts

- **Joint PMF/PDF:** $p(x,y)$ or $f(x,y)$ describing the simultaneous behavior of two (or more) random variables.
- **Marginal Distribution:** $f_X(x) = \int f(x,y) dy$ — "integrate out" the other variable.
- **Conditional Distribution:** $f_{Y|X}(y|x) = f(x,y) / f_X(x)$.
- **Covariance:** $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$.
- **Correlation:** $\rho = \text{Cov}(X,Y) / (\sigma_X \sigma_Y)$, with $-1 \le \rho \le 1$.
- **Multivariate Normal:** Fully characterized by mean vector $\mu$ and covariance matrix $\Sigma$.
- **Order Statistics:** Given i.i.d. sample $X_1, \ldots, X_n$, the $k$-th order statistic $X_{(k)}$ is the $k$-th smallest value.

### Key Problems and Questions

- **Uncorrelated but Dependent:** Construct two random variables with $\text{Cov}(X,Y) = 0$ but $X$ and $Y$ are not independent. (Classic: $X \sim N(0,1)$, $Y = X^2$.)
- **Bivariate Normal Conditional:** If $(X,Y)$ is bivariate normal with correlation $\rho$, derive the conditional distribution $Y | X = x$. Show it is normal with mean $\mu_Y + \rho(\sigma_Y/\sigma_X)(x - \mu_X)$.
- **Max and Min of Two Uniforms:** If $X, Y \sim \text{Uniform}(0,1)$ i.i.d., find the CDF and PDF of $M = \max(X,Y)$ and $L = \min(X,Y)$. Compute $E[M]$ and $E[L]$.
- **Sum of Two Uniforms:** Find the PDF of $Z = X + Y$ where $X, Y \sim \text{Uniform}(0,1)$ are independent. (Triangular distribution via convolution.)
- **Correlation ≠ Causation — Simulation:** Simulate two variables that are highly correlated but have no causal relationship (spurious correlation). Then simulate a case where causation exists but correlation is near zero.
- **Order Statistics of Uniforms:** For $n$ i.i.d. $\text{Uniform}(0,1)$, derive the joint density of $(X_{(i)}, X_{(j)})$ for $i < j$. Compute $E[X_{(n)} - X_{(1)}]$ (range).
- **Jacobian Transformations:** If $(X,Y) \sim \text{Uniform}$ on the unit square, find the joint density of $(U,V) = (X+Y, X-Y)$ using the Jacobian method.
- **Copulas — Basics:** Given two marginals, construct a joint distribution with a specified correlation using a Gaussian copula. Simulate and plot.
- **Multinomial Distribution:** A die is rolled $n$ times. The counts of each face $(N_1, \ldots, N_6)$ follow a Multinomial. Compute $\text{Cov}(N_i, N_j)$ for $i \neq j$. Why is it always negative?
- **The Buffon-Laplace Needle:** A needle of length $l$ is dropped on a grid of lines spaced $d$ apart ($l < d$). Derive the probability of crossing a line. Estimate $\pi$ by simulation.

---

## 7. Expectation, Variance & Moments

### Core Concepts

- **Linearity of Expectation:** $E[aX + bY] = aE[X] + bE[Y]$ — always, even if $X, Y$ are dependent.
- **LOTUS (Law of the Unconscious Statistician):** $E[g(X)] = \sum g(x) p(x)$ or $\int g(x) f(x) dx$.
- **Tower Property (Law of Iterated Expectations):** $E[X] = E[E[X|Y]]$.
- **Variance Decomposition (Eve's Law):** $\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$.
- **Moment Inequalities:**
  - *Markov:* $P(X \ge a) \le E[X]/a$ for $X \ge 0$.
  - *Chebyshev:* $P(|X - \mu| \ge k\sigma) \le 1/k^2$.
  - *Jensen:* $E[g(X)] \ge g(E[X])$ for convex $g$ (inequality flips for concave $g$).
- **Moment Generating Function (MGF):** $M_X(t) = E[e^{tX}]$; uniquely determines the distribution (when it exists).

### Key Problems and Questions

- **Linearity Trick — Expected Inversions:** Given a random permutation of $\{1, \ldots, n\}$, what is the expected number of inversions? (Use indicator r.v.s and linearity; answer: $\binom{n}{2}/2$.)
- **Expected Value of the Max:** What is $E[\max(X_1, \ldots, X_n)]$ for i.i.d. $\text{Uniform}(0,1)$? For i.i.d. standard normals (requires integral or simulation)?
- **Conditional Expectation — The Screaming Baby:** A baby cries with probability $p$ if hungry and $q$ if not. The baby is hungry with probability $r$. The baby is crying. What is $E[\text{time to stop}|$crying$]$? (Tower property practice.)
- **Variance of a Sum — Correlated Assets:** Portfolio of two assets with correlation $\rho$. Derive $\text{Var}(aX + bY) = a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab\rho\sigma_X\sigma_Y$. Find the weights that minimize variance.
- **Eve's Law in Practice:** You roll a fair die to determine $N$, then flip $N$ coins. What is $E[\text{heads}]$ and $\text{Var}(\text{heads})$? (Tower + Eve's Law.)
- **Jensen's Inequality — Option Pricing Intuition:** Explain why $E[\max(S-K, 0)] \ge \max(E[S]-K, 0)$ using Jensen's inequality. What does this say about option prices vs. intrinsic value?
- **Markov & Chebyshev — Tail Bounds:** A stock's daily return has mean 0.1% and std 2%. Use Chebyshev to bound the probability of a daily loss exceeding 5%.
- **MGF Identification:** You are given $M_X(t) = e^{3t + 2t^2}$. Identify the distribution and its parameters.
- **Moment Problem — Method of Moments:** Given a sample, estimate the parameters of a Gamma distribution using the first two moments. Code it.
- **The St. Petersburg Paradox:** A coin is flipped until heads. You win $2^n$ dollars if heads appears on flip $n$. What is $E[\text{winnings}]$? Why won't anyone pay the "fair" price? Discuss truncation and utility.

---

## 8. Generating Functions & Transforms

### Core Concepts

- **Probability Generating Function (PGF):** $G_X(s) = E[s^X] = \sum_{k=0}^{\infty} p_k s^k$ for non-negative integer-valued $X$.
  - $G_X(1) = 1$, $G_X'(1) = E[X]$, $G_X''(1) = E[X(X-1)]$.
- **Moment Generating Function (MGF):** $M_X(t) = E[e^{tX}]$.
  - $M_X'(0) = E[X]$, $M_X''(0) = E[X^2]$, etc.
  - Uniqueness: if two r.v.s have the same MGF in a neighborhood of 0, they have the same distribution.
- **Characteristic Function:** $\varphi_X(t) = E[e^{itX}]$ — always exists, even when MGF doesn't.
- **Convolution Theorem:** The PGF/MGF of a sum of independent r.v.s is the product of their PGFs/MGFs.
- **Laplace Transform:** $\mathcal{L}\{f\}(s) = \int_0^\infty e^{-sx} f(x) dx$ — used for non-negative continuous r.v.s.

### Key Problems and Questions

- **PGF for Branching Processes:** In a Galton-Watson process, each individual has $k$ offspring with probability $p_k$. Derive the PGF of the $n$-th generation size as an iterated composition $G_n(s) = G(G_{n-1}(s))$. Compute extinction probability.
- **Sum of Random Number of Random Variables:** $N \sim \text{Poisson}(\lambda)$ customers arrive; each spends $X_i \sim \text{Exp}(\mu)$. Find the MGF of total spending $S = \sum_{i=1}^N X_i$ using the compound distribution formula.
- **Proving Poisson is the Limit of Binomial:** Use MGFs to prove that $\text{Binomial}(n, \lambda/n) \to \text{Poisson}(\lambda)$ as $n \to \infty$.
- **CLT via Characteristic Functions:** Sketch the proof of the Central Limit Theorem using characteristic functions: show $\varphi_{\bar{X}_n}(t) \to e^{-t^2/2}$.
- **Identifying a Distribution from its MGF:** Given $M(t) = (pe^t / (1 - qe^t))^r$ for $t < -\ln q$, identify the distribution. (Negative Binomial.)
- **Random Sums — Wald's Identity:** If $N$ is a stopping time and $X_i$ are i.i.d., prove $E[\sum_{i=1}^N X_i] = E[N] \cdot E[X_1]$. Give conditions under which this holds.
- **PGF — Number of Fixed Points:** A random permutation of $\{1, \ldots, n\}$ is drawn. Let $X$ = number of fixed points. Use the PGF to find the distribution of $X$ and show $X \to \text{Poisson}(1)$ for large $n$.
- **Laplace Transform of First-Passage Time:** For a standard Brownian motion with drift $\mu$, derive the Laplace transform of the hitting time $\tau_a = \inf\{t : W_t + \mu t = a\}$.
- **Z-Transform and Recursions:** Solve the Fibonacci recurrence $a_n = a_{n-1} + a_{n-2}$ using Z-transforms. Apply the same technique to a random walk recursion.
- **Tilt / Exponential Change of Measure:** Given a random variable $X$ with MGF $M(t)$, define a new distribution by "tilting": $\tilde{p}(x) = e^{\theta x} p(x) / M(\theta)$. Show this is a valid distribution. Apply to importance sampling for rare-event simulation of a portfolio loss.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive the answer by hand (pen-and-paper).
> 2. **Simulation** — verify via Monte Carlo simulation.
> 3. **Visualization** — plot distributions, convergence, or sensitivity to parameters.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

