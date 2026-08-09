# Capability Map — what all this is *for*

> **The question this file answers:** "I'm deriving `E[Exp(λ)] = 1/λ` on a Wednesday evening.
> What does that have to do with being a quant?"
>
> [03_gated_progression.md](03_gated_progression.md) is **bottom-up**: what can I start next,
> given prerequisites. This file is **top-down**: which real capabilities am I building, and
> which stages feed them. Same stages, opposite direction.
>
> ⚠️ **This is reference, not a plan.** It never drives sequencing — the DAG does that. Two
> competing calendars is exactly what made the DAG's traversal table go stale.
>
> **Last updated:** 2026-08-09

---

## The three layers

**Capabilities** are what a quant is hired to *do*. **Concepts** are the named ideas that do the
actual work — this is the payload layer, and the reason this file exists. **Stages** are what you
sit down and study.

The middle layer is deliberately *concepts*, not generic competencies. "Stochastic modelling" as
a box explains nothing; **memorylessness → interarrival times → time-to-fill** explains why
Wednesday's exponential distribution is a market-making tool.

Read upward for *"why am I learning this?"*, downward for *"what do I need for X?"*
Arrows follow contribution: stage → concept → concept → capability.

```mermaid
graph BT
    %% ============ STAGES ============
    subgraph STAGES["STAGES — what you study"]
        direction LR
        RC[R.calculus ✅]
        RL[R.linalg ✅]
        F14a[F1.4a Discrete dists ~]
        F14b[F1.4b Continuous dists]
        F11[F1.1 Combinatorics]
        S12[S1.2 Bayes]
        S16s[S1.6 Joint + MVN]
        S17s[S1.7 Expectation + tower]
        S18[S1.8 MGF]
        S2[S2 Puzzles]
        S31[S3.1 Markov chains]
        S32[S3.2 Absorbing + first passage]
        S41[S4.1 Brownian motion]
        S42[S4.2 Martingales + OST]
        S43[S4.3 Ito + SDEs]
        S44[S4.4 Poisson processes]
        S61[S6.1 Binomial trees]
        S62[S6.2 Black-Scholes]
        S65[S6.5 Monte Carlo pricing]
        S7[S7 PCA + covariance]
        S91[S9.1 MLE]
        S92[S9.2 Hypothesis testing]
        S93[S9.3 Regression + GARCH]
        S94[S9.4 Bayesian]
        S101[S10.1 Arrays/hash]
        S102[S10.2 DP]
        S103[S10.3 Graphs/BFS]
        S104[S10.4 Numerical methods]
        S11i[S11 Kelly + entropy]
    end

    %% ============ CONCEPTS ============
    subgraph CONCEPTS["CONCEPTS — the ideas that do the work"]
        direction LR
        X1(memorylessness)
        X2(interarrival times)
        X3(time-to-fill · queue position)
        X4(adverse selection)
        X5(first-step conditioning)
        X6(expected waiting time)
        X7(state machines)
        X8(linearity of expectation)
        X9(tower property)
        X10(change of variables)
        X11(log-normal prices)
        X12(risk-neutral measure)
        X13(replication · no-arbitrage)
        X14(delta · hedge ratio)
        X15(Ito's lemma)
        X16(random walk limit)
        X17(standardisation · z-scores)
        X18(CLT)
        X19(tail probability · VaR)
        X20(fat tails · vol clustering)
        X21(estimator + bias/variance)
        X22(significance · multiple testing)
        X23(overfitting · out-of-sample)
        X24(covariance structure)
        X25(eigen-decomposition · factors)
        X26(PSD · why Markowitz breaks)
        X27(bet sizing · Kelly)
        X28(complexity · Big-O)
        X29(vectorisation · MC convergence)
        X30(graph traversal)
    end

    %% ============ CAPABILITIES ============
    subgraph CAP["CAPABILITIES — what a quant is hired to do"]
        direction LR
        K1([Options pricing<br/>and hedging])
        K2([Portfolio construction])
        K3([Signal research])
        K4([Market making<br/>and execution])
        K5([Risk management])
        K6([Backtesting<br/>and infrastructure])
    end

    classDef cap fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    class K1,K2,K3,K4,K5,K6 cap

    %% ---- ARRIVALS / MARKET MAKING chain ----
    F14b --> X1
    F14a --> X1
    X1 --> X2
    S44 --> X2
    X2 --> X3
    X3 --> K4
    F14a --> X4
    S12 --> X4
    X4 --> K4
    X4 --> K5

    %% ---- CONDITIONING / PUZZLES chain ----
    F14a --> X5
    S2 --> X5
    X5 --> X6
    X6 --> X3
    S31 --> X7
    S32 --> X7
    X7 --> X6
    X7 --> K4
    S17s --> X8
    F11 --> X8
    X8 --> X6
    X8 --> X21
    S17s --> X9
    S12 --> X9
    X9 --> X21
    X9 --> X12

    %% ---- PRICING chain ----
    F14b --> X10
    X10 --> X11
    S41 --> X16
    S16s --> X11
    X11 --> X13
    S61 --> X13
    X13 --> X12
    S42 --> X12
    X12 --> K1
    RC --> X15
    S43 --> X15
    X15 --> X11
    S62 --> X14
    X14 --> K1
    X14 --> K5
    S18 --> X18
    S65 --> X29
    X29 --> K1

    %% ---- DISTRIBUTION / RISK chain ----
    F14b --> X17
    X17 --> X19
    X16 --> X18
    X18 --> X17
    X19 --> K5
    S93 --> X20
    X20 --> X19
    X20 --> K5
    F14b --> X19

    %% ---- INFERENCE / SIGNAL chain ----
    S91 --> X21
    X21 --> X23
    S92 --> X22
    X22 --> X23
    S94 --> X21
    X23 --> K3
    X23 --> K6
    S93 --> X23
    X21 --> K3

    %% ---- LINEAR ALGEBRA / PORTFOLIO chain ----
    RL --> X24
    S16s --> X24
    X24 --> X25
    S7 --> X25
    X25 --> X26
    RL --> X26
    X26 --> K2
    X25 --> K3
    X24 --> X19
    S11i --> X27
    X27 --> K2
    X27 --> K4

    %% ---- COMPUTATION chain ----
    S101 --> X28
    S102 --> X28
    S103 --> X30
    X30 --> X28
    X28 --> K4
    X28 --> K6
    S104 --> X29
    X29 --> K6
    S102 --> X30
```

### The chain that started this

Read the market-making path upward and it is the concrete answer to *"why am I studying the
exponential distribution?"*:

```
F1.4b  →  memorylessness  →  interarrival times  →  time-to-fill / queue position  →  MARKET MAKING
```

Memorylessness says a quote that has waited 10 seconds is no more "due" a fill than a fresh one.
That single property is the model for time-to-next-trade, and `min(X,Y) ~ Exp(λ₁+λ₂)` is
first-to-fill across two venues. The same stage also runs:

```
F1.4b  →  change of variables  →  log-normal prices  →  replication  →  risk-neutral  →  OPTIONS PRICING
F1.4b  →  standardisation      →  tail probability / VaR                              →  RISK
```

Three capabilities, one Wednesday. **Concepts with two or more outgoing edges are the
load-bearing ones** — `tower property`, `linearity of expectation`, `covariance structure`,
`complexity` — and they are the last things to cut when a sprint is under pressure.

---
---

## The capabilities, one table each

**Status** counts stages closed / stages listed. `✅` closed · `~` partial · blank = not started.

### Options pricing and hedging

| | |
|---|---|
| **What it is** | Given a contract, produce a price and the sensitivities that let you hedge it. |
| **Interview form** | "Price a European call." · "What's delta on a 1-week ATM vs a 1-year ATM?" · "Why is gamma highest near expiry?" |
| **Work form** | Pricing library, Greeks engine, vol surface, hedge P&L attribution |
| **Capstone** | **P1 Options Pricer** (Sprint 26) |
| **Stages** | R.calculus ✅ · F1.4b · S1.6 · S1.8 · S4.1 · S4.2 · S4.3 · S6.1 · S6.2 · S6.5 |
| **Key concepts** | change of variables → log-normal prices · replication → no-arbitrage → risk-neutral measure · Ito's lemma · delta / hedge ratio · MC convergence |
| **Status** | **1 / 10** |

*Baseline signal:* VI.3 (Greeks intuition) scored **3** — your best derivative answer, and it was
pure reasoning. VI.1 (binomial call) scored 0. The intuition is there; the machinery isn't.

### Portfolio construction

| | |
|---|---|
| **What it is** | Turn a set of return forecasts and a covariance estimate into position sizes. |
| **Interview form** | "What does a covariance matrix have to satisfy?" · "Why does Markowitz blow up in practice?" · "How would you size a bet with edge?" |
| **Work form** | Mean-variance / risk-parity optimisers, factor models, shrinkage, position limits |
| **Stages** | R.linalg ✅ · S1.6 · S7 · S9.3 · S11 (Kelly) |
| **Key concepts** | covariance structure → eigen-decomposition → factors · PSD (why Markowitz breaks) · bet sizing / Kelly |
| **Status** | **1 / 5** |

*Already banked:* your `R.linalg` note derived why Σ is PSD **and** why it's PSD-not-PD — the
singular case that breaks Cholesky and naive Markowitz. That is a portfolio-construction insight
sitting in a linear algebra note.

### Signal research

| | |
|---|---|
| **What it is** | Find something that predicts returns, and establish it isn't noise. |
| **Interview form** | "How do you know this signal isn't overfit?" · "What are the OLS assumptions?" · "What's the difference between in-sample and out-of-sample R²?" |
| **Work form** | Feature construction, regression, multiple-testing control, decay analysis |
| **Stages** | F1.1 · S1.2 · S1.7 · S9.1 · S9.2 · S9.3 · S9.4 · S7 |
| **Key concepts** | estimator + bias/variance · significance / multiple testing · overfitting vs out-of-sample · tower property · linearity of expectation · factor structure |
| **Status** | **0 / 8** |

*Baseline signal:* Section IX scored **1.00** — joint lowest with algos, and this is the single
most QR-relevant capability on the list. MLE scored 0.

### Market making and execution

| | |
|---|---|
| **What it is** | Quote two-sided prices, manage inventory, and get filled at good prices. |
| **Interview form** | "Expected number of trades before your quote is hit?" · "What's your edge if you're picked off X% of the time?" · fast mental arithmetic, LC-medium under time pressure |
| **Work form** | Queue position modelling, adverse-selection cost, order routing, latency budgets |
| **Stages** | F1.4a ~ · F1.4b · S2 · S3.1 · S4.4 · S10.1 · S10.2 · S10.3 · S10.4 |
| **Key concepts** | memorylessness → interarrival times → time-to-fill / queue position · adverse selection · first-step conditioning → expected waiting time · state machines · complexity / Big-O |
| **Status** | **0.5 / 9** |

*Baseline red flag:* X.4 — "don't know what BFS is." Named an HFT-screen blocker; S10.3 is the
primary focus of Sprint 19. **This capability is where the exponential distribution stops being
abstract**: memorylessness *is* the model for time-to-next-trade, and `min(X,Y) ~ Exp(λ₁+λ₂)` is
first-to-fill across venues.

### Risk management

| | |
|---|---|
| **What it is** | Quantify what you can lose, and know where the estimate fails. |
| **Interview form** | "Compute 99% 1-day VaR." · "Why is VaR not coherent?" · "What breaks when returns aren't normal?" |
| **Work form** | VaR / ES, stress testing, factor risk decomposition, tail modelling |
| **Stages** | F1.4b · S1.6 · S7 · S9.2 · S9.3 · S4.2 |
| **Key concepts** | standardisation / z-scores → tail probability / VaR · fat tails + vol clustering · adverse selection · delta · covariance structure |
| **Status** | **0 / 6** |

*Note the direct line from Wednesday's stage:* 1.645 vs 1.96 vs 2.326 is a VaR calculation, and
mixing them up is a production bug, not a quiz slip. `Var > E` breaking the Poisson fit is why
naive arrival models understate tail risk.

### Backtesting and infrastructure

| | |
|---|---|
| **What it is** | Simulate a strategy on history without lying to yourself. |
| **Interview form** | Less directly asked — shows up as "how would you test that?" and in code screens |
| **Work form** | Event-driven backtesters, look-ahead / survivorship control, transaction costs, reproducibility |
| **Stages** | S9.2 · S9.3 · S10.1 · S10.2 · S10.4 · S6.5 |
| **Key concepts** | overfitting vs out-of-sample · complexity / Big-O · vectorisation / MC convergence · graph traversal |
| **Status** | **0 / 6** |
| **Overlap credit** | Contract §A.1a — quantamental work touching §IX or §X **dual-counts** here. This is the one capability your 6h/week side project directly advances. |

---

## The fork (Sprint 21)

You are **pre-occupation**. Everything scheduled through roughly Sprint 22 is common tier — no
question in it is answered differently by a buy-side QR and an HFT market maker.

The map above deliberately shows **all six capabilities in full**, including the ones a given role
weights less, so the Sprint-21 decision is made against a complete picture rather than by default.

**Nothing in the diagram is colour-coded by role.** An earlier version shaded capabilities by
QR/HFT tilt; that was dropped 2026-08-09 because it read as a verdict on which branch is
"real" — market making is a first-class quant role, and plenty of MM desks are options desks.
The tilt is a scheduling weight, described in the table below, not a property of the work.

| | Weighted UP | Still required |
|---|---|---|
| **Buy-side QR** | Signal research · Portfolio construction · Backtesting | Options pricing, risk, and enough market-microstructure literacy to not sound naive |
| **HFT / MM** | Market making · Computation-heavy stages (S10.x) · Arrival modelling | Options pricing (many MM desks are options desks), risk, statistics |

**What the fork actually changes:** how many sprints each capability gets in S23–S27 — not which
ones exist. Nobody gets to skip a column.

---

## How to use this file

- **When a stage feels pointless**, find it in the diagram and follow the arrows up. If it doesn't
  reach a capability you care about, that is worth raising — it may genuinely be cuttable.
- **At the Sprint-21 mid-checkpoint**, read the status counts. They are a progress bar against
  things you actually want, rather than against stage counts.
- **Do not schedule from this file.** The DAG owns order; this owns motivation.

**Update cadence:** status counts at each sprint retro. Structure only when a stage is added or
dropped — the capability and competency layers should be near-static. If they churn, the target
is drifting.
