# Backlog — every topic, one line each

> **Generated** by `vault/build_backlog.py` from `vault/topics/`, `stage_maps/`, and the
> concept→application→role wiring. Run it after closing a stage or writing a stage map.
> Hand edits between the markers are overwritten; change the source files instead.

`[x]` closed · `[~]` studied, awaiting its unlock test · `[ ]` not started

**Est** is the stage map's `est_h` where one exists, otherwise a rough guess that gets
replaced the moment a map is written. **Blocked by** comes from the DAG in
`03_gated_progression.md`, which owns sequencing — a topic with entries there is not ready
to pick. **Pays into** is why the topic is on the list at all.

<!-- BEGIN GENERATED:backlog -->

**0 closed · 4 awaiting test · 55 not started · ~292h remaining**

## I — Probability and combinatorics

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[F1_1_combinatorics]] Combinatorics & Counting | 6.5h | 4h | in progress | Market making · Signal research | — |
| [ ] | [[I-2-classical-probability]] Classical (Discrete) Probability | 2h | — | not started | — | — |
| [ ] | [[F1_2_conditional_probability_bayes]] Conditional Probability & Bayes' Theorem | 7h | — | in progress | Signal research | I.1 |
| [~] | [[F1_4_discrete_distributions]] Discrete Random Variables & Distributions | 3h | 6h | awaiting test | Market making | I.3 |
| [~] | [[F1_5_continuous_distributions]] Continuous Random Variables & Distributions | 6h | 5h | awaiting test | Market making · Options pricing · Risk management · Signal research | I.4, VIII.1 |
| [ ] | [[I-6-joint-distributions-and-multivariate-probability]] Joint Distributions & Multivariate Probability | 6h | — | not started | Options pricing · Portfolio construction · Risk management · Signal research | I.5, VII.1 |
| [ ] | [[F1_7_expectation_variance_moments]] Expectation, Variance & Moments | 8.5h | — | in progress | Market making · Signal research | I.6 |
| [ ] | [[I-8-generating-functions-and-transforms]] Generating Functions & Transforms | 5h | — | not started | — | I.7 |

## II — Classical puzzles

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[II-1-dice-problems]] Dice Problems | 3h | — | not started | — | I.1, I.7 |
| [ ] | [[II-2-coin-flipping-problems]] Coin-Flipping Problems | 3h | — | not started | Market making | I.1, I.7 |
| [ ] | [[II-3-card-and-poker-problems]] Card & Poker Problems | 3h | — | not started | — | I.1, I.7 |
| [ ] | [[II-4-urn-and-ball-problems]] Urn & Ball Problems | 3h | — | not started | — | I.1, I.7 |
| [ ] | [[II-5-geometric-and-spatial-probability]] Geometric & Spatial Probability | 3h | — | not started | — | I.1, I.7 |

## III — Markov chains

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[III-1-finite-state-markov-chains]] Finite-State Markov Chains | 6h | — | not started | Market making | I.4, I.7 |
| [ ] | [[III-2-absorbing-markov-chains-and-first-passage-problems]] Absorbing Markov Chains & First-Passage Problems | 6h | — | not started | — | III.1 |
| [ ] | [[III-3-branching-processes]] Branching Processes | 4h | — | not started | — | III.2 |
| [ ] | [[III-4-hidden-markov-models]] Hidden Markov Models (HMM) | 6h | — | not started | — | III.1, IX.1 |
| [ ] | [[III-5-markov-chain-monte-carlo]] Markov Chain Monte Carlo (MCMC) | 5h | — | not started | — | III.1 |

## IV — Stochastic processes

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[IV-1-brownian-motion]] Brownian Motion (Wiener Process) | 6h | — | not started | Options pricing | I.5, I.8 |
| [ ] | [[IV-2-martingale-theory]] Martingale Theory | 6h | — | not started | Options pricing | IV.1 |
| [ ] | [[IV-3-ito-calculus-and-stochastic-differential-equations]] Itô Calculus & Stochastic Differential Equations (SDEs) | 8h | — | not started | Options pricing | IV.2 |
| [ ] | [[IV-4-poisson-processes-and-jump-processes]] Poisson Processes & Jump Processes | 5h | — | not started | Market making | I.5 |
| [ ] | [[IV-5-stopping-times-and-first-passage-problems]] Stopping Times & First-Passage Problems (Continuous) | 5h | — | not started | — | IV.3 |

## V — Stochastic control

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[V-1-optimal-stopping-theory]] Optimal Stopping Theory | 5h | — | not started | — | III.2 |
| [ ] | [[V-2-markov-decision-processes]] Markov Decision Processes (MDP) | 5h | — | not started | — | V.1 |
| [ ] | [[V-3-continuous-time-stochastic-control]] Continuous-Time Stochastic Control (HJB) | 6h | — | not started | — | IV.3 |

## VI — Derivatives pricing

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[VI-1-binomial-tree-models]] Binomial Tree Models | 4h | — | not started | Options pricing | — |
| [ ] | [[VI-2-black-scholes-merton-framework]] Black-Scholes-Merton Framework | 8h | — | not started | — | IV.3, VI.1, VIII.2 |
| [ ] | [[VI-3-exotic-option-pricing]] Exotic Option Pricing | 6h | — | not started | — | VI.2, IV.5 |
| [ ] | [[VI-4-interest-rate-models]] Interest Rate Models | 5h | — | not started | — | — |
| [ ] | [[VI-5-monte-carlo-methods-for-pricing]] Monte Carlo Methods for Pricing | 5h | — | not started | — | VI.2 |
| [ ] | [[VI-6-numerical-pde-methods]] Numerical PDE Methods | 5h | — | not started | — | — |

## VII — Linear algebra

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [~] | [[R_linear_algebra]] Core Linear Algebra | 3h | 3.5h | awaiting test | Portfolio construction · Risk management · Signal research | — |
| [ ] | [[VII-2-applications-in-quant-finance]] Applications in Quant Finance | 5h | — | not started | Portfolio construction · Risk management · Signal research | — |

## VIII — Calculus and ODEs

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [~] | [[R_calculus]] Ordinary Differential Equations (ODEs) | 4h | 5h | awaiting test | — | — |
| [ ] | [[VIII-2-partial-differential-equations]] Partial Differential Equations (PDEs) | 6h | — | not started | — | VIII.1 |
| [ ] | [[VIII-3-optimization-and-calculus-of-variations]] Optimization & Calculus of Variations | 5h | — | not started | — | — |

## IX — Statistics and inference

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[IX-1-estimation-theory]] Estimation Theory | 7h | — | not started | Signal research | I.7 |
| [ ] | [[IX-2-hypothesis-testing-and-confidence-intervals]] Hypothesis Testing & Confidence Intervals | 6h | — | not started | — | IX.1 |
| [ ] | [[IX-3-regression-and-time-series]] Regression & Time Series | 8h | — | not started | Risk management | IX.2, I.6 |
| [ ] | [[IX-4-bayesian-inference]] Bayesian Inference | 5h | — | not started | Signal research | IX.3 |

## X — Algorithms and computation

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[X-1-sorting-and-searching]] Sorting & Searching | 5h | — | not started | — | — |
| [ ] | [[X-2-dynamic-programming]] Dynamic Programming (Algorithmic) | 7h | — | not started | — | X.1 |
| [ ] | [[X-3-graph-algorithms]] Graph Algorithms | 6h | — | not started | — | X.1 |
| [ ] | [[X-4-numerical-methods-and-simulation]] Numerical Methods & Simulation | 5h | — | not started | — | VI.5, I.5 |
| [ ] | [[X-5-complexity-and-big-o-analysis]] Complexity & Big-O Analysis | 3h | — | not started | — | — |

## XI — Information theory

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[XI-1-entropy-and-information-content]] Entropy & Information Content | 3h | — | not started | — | — |
| [ ] | [[XI-2-kl-divergence-and-cross-entropy]] KL-Divergence & Cross-Entropy | 3h | — | not started | — | — |
| [ ] | [[XI-3-mutual-information]] Mutual Information | 3h | — | not started | — | — |
| [ ] | [[XI-4-kelly-criterion-and-applications]] Kelly Criterion & Applications | 4h | — | not started | — | I.7 |

## XII — Game theory

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[XII-1-two-player-zero-sum-games]] Two-Player Zero-Sum Games | 3h | — | not started | — | — |
| [ ] | [[XII-2-non-zero-sum-games-and-general-equilibria]] Non-Zero-Sum Games & General Equilibria | 3h | — | not started | — | — |
| [ ] | [[XII-3-auction-theory]] Auction Theory | 3h | — | not started | — | — |
| [ ] | [[XII-4-cooperative-games-and-fair-division]] Cooperative Games & Fair Division | 3h | — | not started | — | — |

## XIII — Measure theory

| | Topic | Est | Actual | Status | Pays into | Blocked by |
|---|---|--:|--:|---|---|---|
| [ ] | [[XIII-1-probability-spaces-and-algebras]] Probability Spaces & σ-Algebras | 5h | — | not started | — | — |
| [ ] | [[XIII-2-lebesgue-integration-and-measure]] Lebesgue Integration & Measure | 6h | — | not started | — | — |
| [ ] | [[XIII-3-change-of-measure-and-girsanovs-theorem]] Change of Measure & Girsanov's Theorem | 6h | — | not started | — | IV.3 |
| [ ] | [[XIII-4-fundamental-theorems-of-asset-pricing]] Fundamental Theorems of Asset Pricing | 5h | — | not started | — | — |
| [ ] | [[XIII-5-convergence-of-random-variables-and-limit-theorems]] Convergence of Random Variables & Limit Theorems | 5h | — | not started | — | — |

<!-- END GENERATED:backlog -->
