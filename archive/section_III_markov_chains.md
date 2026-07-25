# Section III: Markov Chains & Stochastic Processes (Discrete-Time) — Detailed Problem List

> *Foundation: Markov property, transition kernels, ergodic theory*

Markov chains are the first step from static probability into dynamic, sequential modeling. They appear everywhere in quant finance — from credit rating migrations to random walks on graphs to Monte Carlo simulation. The key insight is the Markov property: the future depends only on the present state, not the path taken to reach it. Mastering Markov chains means being able to set up transition matrices, classify states, compute hitting times, and extract long-run behavior.

---

## 1. Finite-State Markov Chains

### Core Concepts

- **Markov Property:** $P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots, X_0) = P(X_{n+1} = j \mid X_n = i) = p_{ij}$.
- **Transition Matrix:** $P = [p_{ij}]$ where rows sum to 1. The $n$-step transition matrix is $P^n$.
- **Chapman-Kolmogorov Equation:** $p_{ij}^{(m+n)} = \sum_k p_{ik}^{(m)} p_{kj}^{(n)}$, i.e., $P^{m+n} = P^m P^n$.
- **State Classification:**
  - *Communicating:* $i \leftrightarrow j$ if $i$ can reach $j$ and $j$ can reach $i$.
  - *Recurrent:* A state that the chain returns to with probability 1.
  - *Transient:* A state that the chain eventually leaves forever.
  - *Absorbing:* A state $i$ with $p_{ii} = 1$.
  - *Periodic:* A state with period $d > 1$ if returns are only possible at multiples of $d$ steps.
- **Stationary Distribution:** A probability vector $\pi$ such that $\pi P = \pi$. For an irreducible, aperiodic chain, $\pi$ is unique and $P^n \to \mathbf{1}\pi$ as $n \to \infty$.
- **Ergodic Theorem:** For an irreducible, positive recurrent chain, time averages converge to space averages: $\frac{1}{n}\sum_{k=0}^{n-1} f(X_k) \to \sum_i \pi_i f(i)$ a.s.

### Key Problems and Questions

- **Weather Chain:** Tomorrow's weather (Sunny/Rainy) depends only on today's. Given a $2 \times 2$ transition matrix, find the stationary distribution, expected duration of sunny/rainy spells, and the fraction of rainy days in the long run.
- **Drunkard's Walk on a Line:** A drunk starts at position $k$ on $\{0, 1, \ldots, N\}$ with absorbing barriers at $0$ and $N$. Steps left/right with probabilities $q, p$. Set up the transition matrix. Compute absorption probabilities and expected absorption time.
- **Page Rank (Simplified):** Model a 5-page web as a directed graph. Set up the transition matrix (with damping factor $\alpha = 0.85$). Compute the stationary distribution by power iteration. This is the core of Google's original algorithm.
- **Two-State Markov Chain — Explicit Solution:** For a $2 \times 2$ transition matrix $P = \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}$, derive $P^n$ in closed form using eigendecomposition. Verify numerically.
- **Periodicity Detection:** Construct a chain on $\{0, 1, 2\}$ that is irreducible with period 3. Show that $P^n$ does not converge. What happens to $\frac{1}{n}(I + P + P^2 + \cdots + P^{n-1})$?
- **Convergence Rate — Spectral Gap:** For a finite irreducible aperiodic chain, the rate of convergence to stationarity is governed by $|\lambda_2|$ (second largest eigenvalue magnitude). Compute $|\lambda_2|$ for various chains and relate to mixing time.
- **Random Walk on a Graph — Cycle:** A particle performs a random walk on a cycle of $n$ nodes (moving left or right with equal probability). Find the stationary distribution. Compute the expected hitting time from node 0 to node $n/2$.
- **Monopoly as a Markov Chain:** Model a simplified Monopoly board (40 squares) as a Markov chain with dice rolls. Which squares are visited most often in the long run? (Account for the "Go to Jail" rule.)
- **Doubly Stochastic Chains:** A transition matrix is doubly stochastic if both rows and columns sum to 1. Prove that the stationary distribution is uniform. Give an example from card shuffling.
- **Reversibility and Detailed Balance:** A chain is reversible if $\pi_i p_{ij} = \pi_j p_{ji}$ for all $i, j$. Show that detailed balance implies $\pi$ is stationary. Construct a 3-state chain that is irreducible but not reversible.

---

## 2. Absorbing Markov Chains & First-Passage Problems

### Core Concepts

- **Absorbing Chain:** A Markov chain with at least one absorbing state and where every transient state can reach an absorbing state.
- **Canonical Form:** Rearrange states so $P = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix}$ where $Q$ is the transient-to-transient block.
- **Fundamental Matrix:** $N = (I - Q)^{-1}$. Entry $n_{ij}$ = expected number of times the chain visits transient state $j$ starting from transient state $i$.
- **Expected Absorption Time:** From state $i$: $t_i = \sum_j n_{ij}$ (row sum of $N$).
- **Absorption Probabilities:** $B = NR$ gives the probability of being absorbed into each absorbing state from each transient state.

### Key Problems and Questions

- **Gambler's Ruin — Full Analysis:** A gambler starts with $\$a$, bets $\$1$ per round with $P(\text{win}) = p$. Absorbing states at $\$0$ and $\$N$. Set up the transition matrix. Compute ruin probability, expected duration, and expected number of visits to each wealth level using the fundamental matrix.
- **The Ant on a Cube:** An ant starts at vertex $A$ of a cube and performs a random walk (equal probability of each adjacent vertex). What is the expected number of steps to reach the opposite vertex $G$? Set up the absorbing chain (exploit symmetry to reduce to 4 states).
- **Random Walk on a Complete Graph:** A particle walks on $K_n$ (complete graph on $n$ vertices). What is the expected hitting time from any vertex to any other vertex? (Answer: $n - 1$.)
- **The Drunkard and the Cliff:** A drunkard is 3 steps from a cliff. Each step, he moves toward the cliff with probability $p$ and away with probability $1 - p$. What is the probability he falls off? Set up as an absorbing chain (absorbing at cliff, reflecting or absorbing at a far boundary).
- **Expected Steps in Snakes and Ladders:** Model a simplified Snakes and Ladders board as an absorbing Markov chain (final square is absorbing). Compute the expected number of moves to finish. Which snake/ladder has the biggest impact?
- **Mean First-Passage Times — General Formula:** For an irreducible chain with stationary distribution $\pi$, prove that the mean first-passage time from $i$ to $j$ is $m_{ij} = \frac{1}{\pi_j} + \sum_{k \neq j} \frac{n_{kj}^{(j)}}{\pi_j}$. Compute for a specific 4-state chain.
- **The Coupon Collector as an Absorbing Chain:** There are $n$ coupon types. States = number of distinct types collected so far. Set up the $(n+1)$-state chain with state $n$ absorbing. Recover $E[T] = nH_n$ via the fundamental matrix.
- **Escape from a Maze:** Model a simple maze as a graph. A random walker starts at the entrance. The exit is absorbing. Compute expected escape time and the probability of visiting each room before escaping.
- **The Voter Model (1D):** $n$ voters in a line, each holding opinion 0 or 1. At each step, a random voter copies the opinion of a random neighbor. Model as an absorbing chain (absorbing states: all-0 or all-1). What is the probability of consensus on opinion 1?
- **The Ruin Problem with Ties:** Two gamblers play until one is ruined. Starting capitals $a$ and $b$. Each round, one dollar transfers from the loser to the winner (fair coin). The game is interrupted after $T$ rounds. What is the probability each player is ahead?

---

## 3. Branching Processes

### Core Concepts

- **Galton-Watson Process:** A population model where each individual in generation $n$ independently produces a random number of offspring (with distribution $\{p_k\}$) to form generation $n+1$.
- **Offspring PGF:** $G(s) = \sum_{k=0}^{\infty} p_k s^k$. The PGF of generation $n$ is the $n$-fold composition $G_n(s) = G(G_{n-1}(s))$.
- **Mean Offspring:** $\mu = G'(1) = E[\text{offspring per individual}]$.
  - *Subcritical:* $\mu < 1$ → extinction with probability 1.
  - *Critical:* $\mu = 1$ → extinction with probability 1 (if variance > 0).
  - *Supercritical:* $\mu > 1$ → positive probability of survival.
- **Extinction Probability:** The smallest non-negative root of $G(s) = s$. For supercritical processes, this is strictly less than 1.

### Key Problems and Questions

- **Binary Branching — Extinction Probability:** Each individual has 0 offspring with probability $q$ and 2 offspring with probability $p = 1-q$. Find the extinction probability as a function of $p$. Plot and identify the phase transition at $p = 1/2$.
- **Poisson Branching Process:** Offspring distribution is $\text{Poisson}(\lambda)$. Derive the PGF $G(s) = e^{\lambda(s-1)}$. Find the extinction probability by solving $e^{\lambda(s-1)} = s$. Plot the extinction probability vs. $\lambda$.
- **Family Name Extinction (Galton's Original Problem):** In Victorian England, Galton asked: what is the probability a family name goes extinct? Model with empirical offspring distributions from census data. Simulate over many generations.
- **Expected Generation Size:** If $Z_0 = 1$ and $\mu = E[\text{offspring}]$, prove $E[Z_n] = \mu^n$. Compute $\text{Var}(Z_n)$ in terms of $\mu$ and $\sigma^2$. Simulate and verify.
- **Branching Process — Total Progeny:** For a subcritical process ($\mu < 1$), the total number of individuals ever born is $T = \sum_{n=0}^{\infty} Z_n$. Derive $E[T] = 1/(1-\mu)$ using PGFs.
- **Geometric Offspring Distribution:** Each individual has $k$ offspring with probability $p(1-p)^k$ for $k = 0, 1, 2, \ldots$. Compute the PGF, mean, and extinction probability. Show the critical threshold is $p = 1/2$.
- **Multi-Type Branching Process:** Two types of individuals (A and B). Type A produces offspring of both types according to one distribution; Type B according to another. Set up the matrix mean and determine the criticality condition (spectral radius of the mean matrix).
- **Branching Process with Immigration:** At each generation, a fixed number $m$ of immigrants arrive in addition to the offspring. Show that the population never goes extinct. Find the stationary distribution for a Poisson offspring model.
- **Nuclear Chain Reaction:** Each fission event produces a random number of neutrons (offspring). If the average is $\mu > 1$, the reaction is supercritical. Model with a branching process. Estimate the probability of a sustained reaction given $\mu = 1.5$ and $P(\text{0 neutrons}) = 0.3$, $P(\text{1}) = 0.2$, $P(\text{2}) = 0.3$, $P(\text{3}) = 0.2$.
- **Branching Process Conditioned on Survival:** For a supercritical process, condition on non-extinction. What does the size distribution look like? Simulate the "immortal" lineage and show it grows exponentially at rate $\mu$.

---

## 4. Hidden Markov Models (HMM)

### Core Concepts

- **HMM Structure:** A hidden (unobservable) Markov chain $\{X_t\}$ with states $S = \{s_1, \ldots, s_N\}$ and an observation process $\{Y_t\}$ where $Y_t$ depends only on $X_t$.
- **Parameters:** $\lambda = (A, B, \pi_0)$ where $A$ = transition matrix, $B$ = emission probabilities, $\pi_0$ = initial state distribution.
- **Three Fundamental Problems:**
  1. *Evaluation:* Given $\lambda$ and observations $Y_{1:T}$, compute $P(Y_{1:T} \mid \lambda)$. → **Forward algorithm**.
  2. *Decoding:* Find the most likely hidden state sequence $X_{1:T}^*$ given observations. → **Viterbi algorithm**.
  3. *Learning:* Estimate $\lambda$ from observations. → **Baum-Welch (EM) algorithm**.
- **Forward Variable:** $\alpha_t(i) = P(Y_1, \ldots, Y_t, X_t = s_i \mid \lambda)$, computed recursively.
- **Backward Variable:** $\beta_t(i) = P(Y_{t+1}, \ldots, Y_T \mid X_t = s_i, \lambda)$.

### Key Problems and Questions

- **The Dishonest Casino:** A casino alternates between a fair die and a loaded die (using a hidden Markov chain). Given a sequence of rolls, decode which die was used at each time step using the Viterbi algorithm. Implement from scratch.
- **Forward Algorithm — Evaluation:** For a 2-state HMM with known parameters, compute the probability of observing a specific sequence $Y_1, \ldots, Y_T$. Implement the forward algorithm and verify against brute-force enumeration for small $T$.
- **Viterbi Algorithm — Decoding:** Implement the Viterbi algorithm for a 3-state HMM. Given a sequence of 100 observations, find the most likely state sequence. Compare with the individually most likely states (posterior decoding via forward-backward).
- **Baum-Welch — Parameter Estimation:** Generate data from a known 2-state HMM. Then "forget" the parameters and re-estimate them using the Baum-Welch (EM) algorithm. How many iterations until convergence? How sensitive is the result to initialization?
- **Regime Detection in Markets:** Model daily stock returns as emissions from a 2-state HMM (bull/bear market). States have different means and variances. Fit the model to real S&P 500 data. Decode the regime at each time point. Does it capture known recessions?
- **Speech Recognition (Simplified):** A simplified speech recognizer models phonemes as HMM states. Given a dictionary of 3 words (each a sequence of phonemes), recognize which word was spoken from a noisy observation sequence.
- **CpG Islands in DNA:** In genetics, CpG islands are regions with different nucleotide transition probabilities. Model a DNA sequence as emissions from a 2-state HMM (CpG island vs. non-CpG). Decode the sequence.
- **HMM vs. Explicit Markov Chain:** When does it matter that the states are hidden? Construct an example where the observed process $\{Y_t\}$ is *not* Markov even though $\{X_t\}$ is. Show the conditional dependencies.
- **Scaling and Numerical Stability:** The forward algorithm involves multiplying many probabilities, leading to underflow. Implement the log-space version and the scaling approach. Compare numerical accuracy.
- **Model Selection — Number of Hidden States:** Fit HMMs with $k = 2, 3, 4, 5$ states to the same financial time series. Use BIC/AIC to select the optimal number of states. Is more always better?

---

## 5. Markov Chain Monte Carlo (MCMC)

### Core Concepts

- **Goal:** Sample from a target distribution $\pi$ that is difficult to sample from directly, by constructing a Markov chain whose stationary distribution is $\pi$.
- **Metropolis-Hastings Algorithm:** Propose a move $y$ from current state $x$ using proposal distribution $q(y|x)$. Accept with probability $\alpha = \min\left(1, \frac{\pi(y) q(x|y)}{\pi(x) q(y|x)}\right)$.
- **Gibbs Sampling:** A special case of MH where you cycle through coordinates, sampling each from its full conditional distribution. Acceptance rate is always 1.
- **Detailed Balance:** MH constructs a reversible chain satisfying $\pi(x) K(x,y) = \pi(y) K(y,x)$, guaranteeing $\pi$ is stationary.
- **Burn-In:** Initial samples before the chain has converged are discarded.
- **Mixing Time:** The number of steps until the chain is "close" to stationarity (measured by total variation distance).

### Key Problems and Questions

- **Sampling from a 1D Distribution:** Use Metropolis-Hastings with a Gaussian proposal to sample from a target $\pi(x) \propto e^{-x^4}$. Tune the proposal variance. Plot the chain, histogram, and compare with the true density.
- **Random Walk Metropolis — 2D Banana Distribution:** Sample from $\pi(x,y) \propto \exp(-((1-x)^2 + 10(y-x^2)^2)/2)$ (Rosenbrock/banana shape). Visualize the chain's trajectory. Diagnose mixing issues.
- **Gibbs Sampler — Bivariate Normal:** Sample from a bivariate normal with correlation $\rho$ using Gibbs sampling (alternating conditionals). Show convergence for $\rho = 0.5, 0.9, 0.99$. How does high correlation affect mixing?
- **Bayesian Inference for a Coin:** You observe $k$ heads in $n$ flips. Prior: $p \sim \text{Beta}(\alpha, \beta)$. Use MH to sample from the posterior $p | \text{data}$. Compare with the known analytical posterior $\text{Beta}(\alpha + k, \beta + n - k)$.
- **Ising Model Simulation:** Simulate a 2D Ising model on an $L \times L$ grid using Gibbs sampling (single-site updates). Observe the phase transition near the critical temperature $T_c$. Compute magnetization vs. temperature.
- **Bayesian Linear Regression:** Given data $(x_i, y_i)$, fit $y = \beta_0 + \beta_1 x + \epsilon$ with priors on $\beta_0, \beta_1, \sigma^2$. Implement a Gibbs sampler cycling through the full conditionals. Compare posterior means with OLS estimates.
- **Slice Sampling:** Implement slice sampling for a multimodal target distribution. Compare mixing with standard MH. When does slice sampling outperform MH?
- **Convergence Diagnostics — Gelman-Rubin:** Run 4 independent MH chains targeting the same distribution. Compute the Gelman-Rubin $\hat{R}$ statistic. How many samples are needed for $\hat{R} < 1.1$?
- **MCMC for Option Pricing:** Use MCMC to sample from the posterior distribution of volatility given observed option prices. Prior: $\sigma \sim \text{LogNormal}$. Likelihood: Black-Scholes prices vs. market prices. Compute the posterior predictive distribution of option prices.
- **Hamiltonian Monte Carlo (HMC) — Basics:** Implement a basic HMC sampler for a 2D Gaussian target. Compare the effective sample size per computation with random walk MH. Explain why HMC suppresses random walk behavior.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive the answer by hand where possible (transition matrices, eigenvectors, PGFs).
> 2. **Simulation** — build the Markov chain / branching process / HMM and verify via Monte Carlo.
> 3. **Visualization** — plot state trajectories, convergence of distributions, hitting time histograms, or regime overlays on price data.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

