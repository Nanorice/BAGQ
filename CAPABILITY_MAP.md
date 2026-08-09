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

**Capabilities** are what a quant is hired to *do* — what an interview probes and what a desk
pays for. **Competencies** are the transferable machinery underneath. **Stages** are what you
sit down and study.

Read the diagram downward to answer *"what do I need for X?"*; read it upward to answer
*"why am I learning Y?"* Arrows point the way contribution flows: stage → competency → capability.

```mermaid
graph BT
    %% ============ LAYER 3: STAGES ============
    subgraph STAGES["LAYER 3 — Stages (what you study)"]
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
        S32[S3.2 Absorbing/first passage]
        S41[S4.1 Brownian motion]
        S42[S4.2 Martingales + OST]
        S43[S4.3 Ito + SDEs]
        S44[S4.4 Poisson processes]
        S61[S6.1 Binomial trees]
        S62[S6.2 Black-Scholes + Greeks]
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

    %% ============ LAYER 2: COMPETENCIES ============
    subgraph COMP["LAYER 2 — Competencies (transferable machinery)"]
        direction LR
        C1{{Probabilistic reasoning}}
        C2{{Stochastic modelling}}
        C3{{Statistical inference}}
        C4{{Linear algebra + optimisation}}
        C5{{Computation + complexity}}
        C6{{Arrival + queue modelling}}
    end

    %% ============ LAYER 1: CAPABILITIES ============
    subgraph CAP["LAYER 1 — Capabilities (what a quant is hired to do)"]
        direction LR
        K1([Options pricing<br/>and hedging]):::qr
        K2([Portfolio construction]):::qr
        K3([Signal research]):::qr
        K4([Market making<br/>and execution]):::hft
        K5([Risk management]):::both
        K6([Backtesting<br/>and infrastructure]):::both
    end

    classDef qr fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    classDef hft fill:#ffe6cc,stroke:#d79b00,stroke-width:2px
    classDef both fill:#e1d5e7,stroke:#9673a6,stroke-width:2px

    %% ---- stages → competencies ----
    F11 --> C1
    F14a --> C1
    F14b --> C1
    S12 --> C1
    S17s --> C1
    S2 --> C1
    S18 --> C1

    S31 --> C2
    S32 --> C2
    S41 --> C2
    S42 --> C2
    S43 --> C2
    RC --> C2
    S16s --> C2

    S91 --> C3
    S92 --> C3
    S93 --> C3
    S94 --> C3
    S12 --> C3
    S17s --> C3

    RL --> C4
    S7 --> C4
    S16s --> C4

    S101 --> C5
    S102 --> C5
    S103 --> C5
    S104 --> C5
    S65 --> C5

    F14a --> C6
    F14b --> C6
    S44 --> C6
    S31 --> C6

    %% ---- competencies → capabilities ----
    C1 --> K1
    C1 --> K3
    C1 --> K4
    C1 --> K5

    C2 --> K1
    C2 --> K5
    C2 --> K3

    C3 --> K3
    C3 --> K5
    C3 --> K6
    C3 --> K2

    C4 --> K2
    C4 --> K3
    C4 --> K5

    C5 --> K4
    C5 --> K6
    C5 --> K1

    C6 --> K4
    C6 --> K5

    %% ---- direct stage → capability, where the link is immediate ----
    S61 --> K1
    S62 --> K1
    S65 --> K1
    S7 --> K2
    S11i --> K2
    S93 --> K6
```

**Legend:** 🟦 QR-weighted · 🟧 HFT-weighted · 🟪 both equally.
The shading is *tilt*, not ownership — every capability matters to both roles. See
[the fork](#the-fork-sprint-21).

---

## The capabilities, one table each

**Status** counts stages closed / stages listed. `✅` closed · `~` partial · blank = not started.

### 🟦 Options pricing and hedging

| | |
|---|---|
| **What it is** | Given a contract, produce a price and the sensitivities that let you hedge it. |
| **Interview form** | "Price a European call." · "What's delta on a 1-week ATM vs a 1-year ATM?" · "Why is gamma highest near expiry?" |
| **Work form** | Pricing library, Greeks engine, vol surface, hedge P&L attribution |
| **Capstone** | **P1 Options Pricer** (Sprint 26) |
| **Stages** | R.calculus ✅ · F1.4b · S1.6 · S1.8 · S4.1 · S4.2 · S4.3 · S6.1 · S6.2 · S6.5 |
| **Status** | **1 / 10** |

*Baseline signal:* VI.3 (Greeks intuition) scored **3** — your best derivative answer, and it was
pure reasoning. VI.1 (binomial call) scored 0. The intuition is there; the machinery isn't.

### 🟦 Portfolio construction

| | |
|---|---|
| **What it is** | Turn a set of return forecasts and a covariance estimate into position sizes. |
| **Interview form** | "What does a covariance matrix have to satisfy?" · "Why does Markowitz blow up in practice?" · "How would you size a bet with edge?" |
| **Work form** | Mean-variance / risk-parity optimisers, factor models, shrinkage, position limits |
| **Stages** | R.linalg ✅ · S1.6 · S7 · S9.3 · S11 (Kelly) |
| **Status** | **1 / 5** |

*Already banked:* your `R.linalg` note derived why Σ is PSD **and** why it's PSD-not-PD — the
singular case that breaks Cholesky and naive Markowitz. That is a portfolio-construction insight
sitting in a linear algebra note.

### 🟦 Signal research

| | |
|---|---|
| **What it is** | Find something that predicts returns, and establish it isn't noise. |
| **Interview form** | "How do you know this signal isn't overfit?" · "What are the OLS assumptions?" · "What's the difference between in-sample and out-of-sample R²?" |
| **Work form** | Feature construction, regression, multiple-testing control, decay analysis |
| **Stages** | F1.1 · S1.2 · S1.7 · S9.1 · S9.2 · S9.3 · S9.4 · S7 |
| **Status** | **0 / 8** |

*Baseline signal:* Section IX scored **1.00** — joint lowest with algos, and this is the single
most QR-relevant capability on the list. MLE scored 0.

### 🟧 Market making and execution

| | |
|---|---|
| **What it is** | Quote two-sided prices, manage inventory, and get filled at good prices. |
| **Interview form** | "Expected number of trades before your quote is hit?" · "What's your edge if you're picked off X% of the time?" · fast mental arithmetic, LC-medium under time pressure |
| **Work form** | Queue position modelling, adverse-selection cost, order routing, latency budgets |
| **Stages** | F1.4a ~ · F1.4b · S2 · S3.1 · S4.4 · S10.1 · S10.2 · S10.3 · S10.4 |
| **Status** | **0.5 / 9** |

*Baseline red flag:* X.4 — "don't know what BFS is." Named an HFT-screen blocker; S10.3 is the
primary focus of Sprint 19. **This capability is where the exponential distribution stops being
abstract**: memorylessness *is* the model for time-to-next-trade, and `min(X,Y) ~ Exp(λ₁+λ₂)` is
first-to-fill across venues.

### 🟪 Risk management

| | |
|---|---|
| **What it is** | Quantify what you can lose, and know where the estimate fails. |
| **Interview form** | "Compute 99% 1-day VaR." · "Why is VaR not coherent?" · "What breaks when returns aren't normal?" |
| **Work form** | VaR / ES, stress testing, factor risk decomposition, tail modelling |
| **Stages** | F1.4b · S1.6 · S7 · S9.2 · S9.3 · S4.2 |
| **Status** | **0 / 6** |

*Note the direct line from Wednesday's stage:* 1.645 vs 1.96 vs 2.326 is a VaR calculation, and
mixing them up is a production bug, not a quiz slip. `Var > E` breaking the Poisson fit is why
naive arrival models understate tail risk.

### 🟪 Backtesting and infrastructure

| | |
|---|---|
| **What it is** | Simulate a strategy on history without lying to yourself. |
| **Interview form** | Less directly asked — shows up as "how would you test that?" and in code screens |
| **Work form** | Event-driven backtesters, look-ahead / survivorship control, transaction costs, reproducibility |
| **Stages** | S9.2 · S9.3 · S10.1 · S10.2 · S10.4 · S6.5 |
| **Status** | **0 / 6** |
| **Overlap credit** | Contract §A.1a — quantamental work touching §IX or §X **dual-counts** here. This is the one capability your 6h/week side project directly advances. |

---

## The fork (Sprint 21)

You are **pre-occupation**. Everything scheduled through roughly Sprint 22 is common tier — no
question in it is answered differently by a buy-side QR and an HFT market maker.

The map above deliberately shows **all six capabilities in full**, including the ones a given role
weights less, so the Sprint-21 decision is made against a complete picture rather than by default.

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
