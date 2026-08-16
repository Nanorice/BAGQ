# Quantitative Interview Problem Set — Master Topic Index

> **Goal:** A comprehensive, systematic problem set covering every major topic that appears in quant interviews, with an emphasis on probability, stochastic processes, and codifiable solutions.
> Topics are ordered from foundational → advanced. Each bullet names the **theoretical discipline** behind it.

---

## Table of Contents

| Section | Topic | Focus | Details |
|---|---|---|---|
| **I** | Probability Theory & Combinatorics | Foundations — discrete/continuous distributions, Bayes, moments, generating functions | [📄](section_I_probability_combinatorics.md) |
| **II** | Classical Probability Puzzles | Dice, coins, cards, urns, geometric probability brain teasers | [📄](section_II_classical_puzzles.md) |
| **III** | Markov Chains (Discrete-Time) | Finite-state chains, absorbing chains, branching processes, HMMs, MCMC | [📄](section_III_markov_chains.md) |
| **IV** | Continuous-Time Stochastic Processes | Brownian motion, martingales, Itô calculus, Poisson/jump processes | [📄](section_IV_continuous_time_processes.md) |
| **V** | Stochastic Control & Dynamic Programming | Optimal stopping, MDPs, HJB equations | [📄](section_V_stochastic_control.md) |
| **VI** | Derivative Pricing & Financial Math | Binomial trees, Black-Scholes, exotics, Monte Carlo, PDE methods | [📄](section_VI_derivative_pricing.md) |
| **VII** | Linear Algebra & Matrix Theory | Eigendecomposition, PCA, covariance matrices, portfolio optimization | [📄](section_VII_linear_algebra.md) |
| **VIII** | Calculus, DEs & Analysis | ODEs, PDEs (heat equation ↔ Black-Scholes), optimization | [📄](section_VIII_calculus_des.md) |
| **IX** | Statistics & Estimation | MLE, hypothesis testing, regression, time series (GARCH), Bayesian inference | [📄](section_IX_statistics_estimation.md) |
| **X** | Algorithms & Data Structures | Sorting, DP, graph algorithms, numerical methods, complexity | [📄](section_X_algorithms_ds.md) |
| **XI** | Information Theory & Entropy | Shannon entropy, KL-divergence, Kelly criterion | [📄](section_XI_information_theory.md) |
| **XII** | Game Theory & Mechanism Design | Zero-sum games, auctions, Shapley value | [📄](section_XII_game_theory.md) |
| **XIII** | Measure Theory & Advanced Probability | σ-algebras, Girsanov's theorem, FTAP, convergence theorems | [📄](section_XIII_measure_theory.md) |

---

## I. Probability Theory & Combinatorics
> *Foundation: Kolmogorov axioms, σ-algebras, measure-theoretic probability*
> 📄 **Detailed problem list:** [section_I_probability_combinatorics.md](section_I_probability_combinatorics.md)

### 1. Classical (Discrete) Probability
- Equally-likely outcomes, sample spaces, counting arguments
- Permutations & combinations (binomial coefficients)
- Inclusion-exclusion principle
- Pigeonhole principle

### 2. Conditional Probability & Bayes' Theorem
- Law of total probability
- Bayes' rule and posterior updating
- Independence vs. conditional independence
- Prosecutor's fallacy / base-rate neglect

### 3. Combinatorics & Counting
- Stars and bars, balls-in-bins
- Multinomial coefficients
- Derangements (subfactorials)
- Catalan numbers (ballot problem, Dyck paths)
- Stirling numbers (partitions of sets)

### 4. Discrete Random Variables & Distributions
- Bernoulli, Binomial, Geometric, Negative Binomial
- Poisson distribution and Poisson approximation
- Hypergeometric distribution
- Discrete uniform distribution
- PMF, CDF, expectation, variance, moments

### 5. Continuous Random Variables & Distributions
- Uniform, Exponential, Gamma
- Normal (Gaussian) distribution and its properties
- Log-normal distribution
- Beta distribution
- PDF, CDF, moment-generating functions (MGF), characteristic functions

### 6. Joint Distributions & Multivariate Probability
- Joint, marginal, and conditional distributions
- Covariance, correlation, independence
- Multivariate normal distribution
- Copulas (basics)
- Order statistics

### 7. Expectation, Variance & Moments
- Linearity of expectation
- Law of the unconscious statistician (LOTUS)
- Conditional expectation and the tower property $E[E[X|Y]] = E[X]$
- Variance decomposition: $\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$
- Moment inequalities (Jensen, Chebyshev, Markov)

### 8. Generating Functions & Transforms
- Probability generating functions (PGF)
- Moment generating functions (MGF)
- Characteristic functions
- Laplace transforms
- Z-transforms (discrete signals)

---

## II. Classical Probability Puzzles & Brain Teasers
> *Foundation: Discrete probability, conditional expectation, symmetry arguments*
> 📄 **Detailed problem list:** [section_II_classical_puzzles.md](section_II_classical_puzzles.md)

### 1. Dice Problems
- Expected value of max/min of $n$ dice
- Dice games with optimal stopping (Cayley-Moser)
- Non-transitive dice
- Sicherman dice

### 2. Coin-Flipping Problems
- Expected flips to get $k$ heads in a row
- Penney's game (pattern waiting times)
- Fair results from biased coins (von Neumann trick)
- Gambler's ruin via coin flips

### 3. Card & Poker Problems
- Poker hand probabilities (combinatorial counting)
- Expected number of cards to draw for a pair/flush
- Card shuffling and randomness (riffle shuffle analysis)
- Blackjack basic strategy (conditional expectation)

### 4. Urn & Ball Problems
- Pólya urn model
- Coupon collector's problem
- Birthday problem and generalizations
- Ehrenfest diffusion model

### 5. Geometric & Spatial Probability
- Buffon's needle
- Random points on a circle/sphere
- Bertrand's paradox
- Broken stick problem (triangle inequality)

---

## III. Markov Chains & Stochastic Processes (Discrete-Time)
> *Foundation: Markov property, transition kernels, ergodic theory*
> 📄 **Detailed problem list:** [section_III_markov_chains.md](section_III_markov_chains.md)

### 1. Finite-State Markov Chains
- Transition matrices and Chapman-Kolmogorov equations
- Classification of states: transient, recurrent, absorbing
- Stationary (invariant) distributions
- Ergodic theorem and convergence

### 2. Absorbing Markov Chains & First-Passage Problems
- Expected hitting times (first-passage times)
- Gambler's ruin as an absorbing chain
- Random walks on graphs (ant on a cube, drunkard's walk)
- Mean first-passage via fundamental matrix

### 3. Branching Processes
- Galton-Watson process
- Extinction probability
- Generating function methods for branching

### 4. Hidden Markov Models (HMM)
- Forward-backward algorithm
- Viterbi algorithm
- Baum-Welch (EM) for parameter estimation
- Applications: regime detection in financial markets

### 5. Markov Chain Monte Carlo (MCMC)
- Metropolis-Hastings algorithm
- Gibbs sampling
- Convergence diagnostics
- Applications: Bayesian inference in finance

---

## IV. Continuous-Time Stochastic Processes
> *Foundation: Brownian motion, filtrations, martingale theory, Itô calculus*
> 📄 **Detailed problem list:** [section_IV_continuous_time_processes.md](section_IV_continuous_time_processes.md)

### 1. Brownian Motion (Wiener Process)
- Definition and properties (independent increments, Gaussian, continuous paths)
- Quadratic variation
- Reflection principle
- Donsker's theorem (functional CLT)
- Geometric Brownian motion (GBM)

### 2. Martingale Theory
- Definition: sub/super-martingales
- Optional stopping theorem (and when it fails)
- Martingale convergence theorems
- Doob's maximal inequality
- Martingale representation theorem

### 3. Itô Calculus & Stochastic Differential Equations (SDEs)
- Itô integral vs. Stratonovich integral
- Itô's lemma (stochastic chain rule)
- Ornstein-Uhlenbeck process (mean-reversion)
- CIR (Cox-Ingersoll-Ross) process
- Geometric Brownian motion SDE

### 4. Poisson Processes & Jump Processes
- Homogeneous and inhomogeneous Poisson processes
- Compound Poisson process
- Jump-diffusion models (Merton's model)
- Lévy processes (basics)

### 5. Stopping Times & First-Passage Problems (Continuous)
- Hitting times for Brownian motion
- Boundary crossing probabilities
- Inverse Gaussian (Wald) distribution
- Applications to barrier options

---

## V. Stochastic Control & Dynamic Programming
> *Foundation: Bellman optimality, HJB equations, viscosity solutions*
> 📄 **Detailed problem list:** [section_V_stochastic_control.md](section_V_stochastic_control.md)

### 1. Optimal Stopping Theory
### 2. Markov Decision Processes (MDP)
### 3. Continuous-Time Stochastic Control (HJB)

---

## VI. Derivative Pricing & Financial Mathematics
> *Foundation: Risk-neutral valuation, no-arbitrage, fundamental theorems of asset pricing*
> 📄 **Detailed problem list:** [section_VI_derivative_pricing.md](section_VI_derivative_pricing.md)

### 1. Binomial Tree Models
- One-step and multi-step binomial trees
- Risk-neutral probability
- Replicating portfolios
- Convergence to Black-Scholes

### 2. Black-Scholes-Merton Framework
- Derivation via replication and via risk-neutral expectation
- Black-Scholes PDE
- Greeks (Delta, Gamma, Vega, Theta, Rho)
- Implied volatility and the volatility smile/surface

### 3. Exotic Option Pricing
- Barrier options (knock-in, knock-out)
- Asian options (arithmetic vs. geometric average)
- Lookback options
- Digital/binary options
- Compound options

### 4. Interest Rate Models
- Vasicek model
- CIR model
- Hull-White model
- HJM framework
- LIBOR market model (BGM)

### 5. Monte Carlo Methods for Pricing
- Basic Monte Carlo simulation
- Variance reduction: antithetic variates, control variates, importance sampling
- Quasi-Monte Carlo (low-discrepancy sequences)
- Least-squares Monte Carlo (Longstaff-Schwartz for American options)

### 6. Numerical PDE Methods
- Finite difference methods (explicit, implicit, Crank-Nicolson)
- Stability and convergence
- Free-boundary problems for American options

---

## VII. Linear Algebra & Matrix Theory
> *Foundation: Vector spaces, eigendecomposition, positive-definite matrices*
> 📄 **Detailed problem list:** [section_VII_linear_algebra.md](section_VII_linear_algebra.md)

### 1. Core Linear Algebra
- Systems of linear equations, Gaussian elimination
- Eigenvalues and eigenvectors
- Matrix decompositions (LU, QR, SVD, Cholesky)
- Positive-definite and semi-definite matrices

### 2. Applications in Quant Finance
- Covariance and correlation matrices
- Principal Component Analysis (PCA) for yield curves / factor models
- Markov chain transition matrix analysis
- Portfolio optimization (mean-variance, quadratic programming)

---

## VIII. Calculus, Differential Equations & Analysis
> *Foundation: Real analysis, ODEs, PDEs*
> 📄 **Detailed problem list:** [section_VIII_calculus_des.md](section_VIII_calculus_des.md)

### 1. Ordinary Differential Equations (ODEs)
- First-order linear ODEs, integrating factors
- Second-order ODEs (constant coefficients)
- Systems of ODEs

### 2. Partial Differential Equations (PDEs)
- Heat equation and its connection to Black-Scholes
- Feynman-Kac formula (link between PDEs and expectations)
- Green's functions
- Fourier transform methods

### 3. Optimization & Calculus of Variations
- Lagrange multipliers
- Convex optimization basics
- Euler-Lagrange equation
- KKT conditions

---

## IX. Statistics & Estimation
> *Foundation: Statistical inference, likelihood theory, hypothesis testing*
> 📄 **Detailed problem list:** [section_IX_statistics_estimation.md](section_IX_statistics_estimation.md)

### 1. Estimation Theory
- Maximum Likelihood Estimation (MLE)
- Method of moments
- Bias-variance tradeoff
- Fisher information and Cramér-Rao bound

### 2. Hypothesis Testing & Confidence Intervals
- Neyman-Pearson lemma
- t-tests, chi-squared tests
- Multiple testing corrections (Bonferroni, FDR)
- Power analysis

### 3. Regression & Time Series
- Ordinary least squares (OLS) and assumptions
- Logistic regression
- Autoregressive (AR), MA, ARMA, ARIMA models
- GARCH models for volatility
- Cointegration and pairs trading

### 4. Bayesian Inference
- Prior, likelihood, posterior
- Conjugate priors
- Bayesian updating in sequential problems
- Bayesian vs. frequentist interpretation

---

## X. Algorithms, Data Structures & Pseudo-Code
> *Foundation: Computational complexity, algorithm design, numerical methods*
> 📄 **Detailed problem list:** [section_X_algorithms_ds.md](section_X_algorithms_ds.md)

### 1. Sorting & Searching
- Binary search and variations
- Merge sort, quicksort, heap sort
- Hash tables and collision resolution

### 2. Dynamic Programming (Algorithmic)
- Memoization vs. tabulation
- Longest common subsequence, knapsack
- Optimal BST, matrix chain multiplication
- Connection to Bellman equations in finance

### 3. Graph Algorithms
- BFS, DFS, topological sort
- Shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning tree (Kruskal, Prim)
- Network flow (max-flow min-cut)

### 4. Numerical Methods & Simulation
- Root finding (Newton-Raphson, bisection)
- Numerical integration (trapezoidal, Simpson's)
- Random number generation (LCG, Mersenne Twister)
- Inverse transform sampling, acceptance-rejection

### 5. Complexity & Big-O Analysis
- Time and space complexity
- Amortized analysis
- NP-completeness (awareness level)

---

## XI. Information Theory & Entropy
> *Foundation: Shannon entropy, KL-divergence, mutual information*
> 📄 **Detailed problem list:** [section_XI_information_theory.md](section_XI_information_theory.md)

- Entropy of discrete distributions
- Cross-entropy and KL-divergence
- Mutual information
- Applications: Kelly criterion, optimal betting, model selection

---

## XII. Game Theory & Mechanism Design
> *Foundation: Nash equilibrium, minimax theorem, auction theory*
> 📄 **Detailed problem list:** [section_XII_game_theory.md](section_XII_game_theory.md)

### 1. Two-Player Zero-Sum Games
- Minimax theorem
- Mixed strategies and Nash equilibrium
- Bluffing models (simplified poker)

### 2. Auction Theory
- First-price, second-price (Vickrey) auctions
- Revenue equivalence theorem
- Winner's curse

### 3. Cooperative Games
- Shapley value
- Core of a game
- Applications to cost/profit allocation

---

## XIII. Measure Theory & Advanced Probability (Theoretical Foundations)
> *Foundation: σ-algebras, Lebesgue integration, Radon-Nikodym theorem*
> 📄 **Detailed problem list:** [section_XIII_measure_theory.md](section_XIII_measure_theory.md)

- Probability spaces and σ-algebras
- Radon-Nikodym derivative and change of measure
- Girsanov's theorem (change of drift under equivalent measure)
- Fundamental theorems of asset pricing (1st and 2nd FTAP)
- Convergence of random variables (a.s., in probability, in distribution, in $L^p$)
- Central Limit Theorem and its extensions
- Law of Large Numbers (weak and strong)
