# Syllabus — Q1-2027 Buy-Side QR + HFT Prep

**Duration:** 25 weeks · 13 two-week sprints (S15 → S27)
**Runway ends:** 2027-01-15 (Day 12 of S27)
**Weekly cadence:** ~11 h prime + ~3 h scrap
**Baseline:** 0.88 / 5 combined (see `progress/baseline_scores.md`)

---

## The 4 Tiers

### Tier 0 — Foundations (Sprint 15 tail + early S16)
Reboot the math and tools. **~10 hours total.**

- T0.A Python + NumPy env ✅
- T0.B Git hygiene ✅
- T0.C Calculus refresher — ODEs (separable + linear), Lagrange, chain rule
- T0.D Linear algebra refresher — matrix ops, 2×2/3×3 eigenvalues by hand, PSD

### Tier 1 — Probability + Puzzles + Stats + Algos (S16 → S24)
The core interview surface. **~120 hours across 9 sprints.**

**Probability (S1)** — 6 stages: Combinatorics, Bayes, Discrete RVs, Continuous RVs, Joint/MVN, Expectation/Tower, MGF
**Distributions** — 2 stages: Discrete `S1.3` (Bernoulli/Binomial/Geometric/Poisson) · Continuous `S1.5` (Uniform/Exponential/Normal). *Log-normal → S6, χ² → S9.2.*
**Puzzles (S2)** — 1 stage: dice/coin/urn/geometric
**Statistics (S9)** — 4 stages: MLE, hypothesis testing, regression + time series, Bayesian
**Linear algebra deepen (S7)** — 1 stage: PCA + covariance
**Algorithms (S10)** — 4 stages: arrays/hash, DP, graphs/BFS, numerical methods

### Tier 2 — Processes (S22 → S26)
Markov + Brownian motion + microstructure. **~50 hours across 5 sprints.**

- S3.1 Finite Markov chains · S3.2 Absorbing + first passage
- S4.1 Brownian motion · S4.2 Martingales + OST · S4.3 Itô + SDEs
- Microstructure primer (LOB, queues, Almgren-Chriss lite)

### Tier 3 — Derivatives + Capstones + Mocks (S26 → S27)
The final push. **~40 hours across 2 sprints.**

- S6.1 Binomial · S6.2 BS + Greeks · S6.5 Monte Carlo
- **Capstone P1** — Options Pricer (Sprint 26)
- **Capstone P16** — HMM Regime Detection (Sprint 27)
- **4 mock interviews** — Sprints 26–27

### Deferred (post-Q1 backlog)
S3.3 Branching · S4.4 Poisson/jump · S4.5 Stopping times · S5 Stochastic control · S6.3 Exotics · S6.4 Rates · S8.2 PDE/Feynman-Kac · S11 Info theory (except 20-min Kelly read) · S12 Game theory (except 20-min Vickrey read) · S13 Measure theory · STS projects P2–P20 except P1, P5, P16

---

## Sprint calendar

| Sprint | Dates | Theme | Capstone / milestone |
|---|---|---|---|
| S15 | 07-20 → 08-02 | Setup + baseline + T0 refreshers | Baseline logged, Sprint 16 planned |
| S16 | 08-03 → 08-16 | Named distributions + S1.1 Combinatorics kickoff | 2 Feynman notes |
| S17 | 08-17 → 08-30 | S1.1 finish + S1.2 Bayes + S1.7 Tower + S10.1 arrays/hash | 3 stages · 10 LC-easy |
| S18 | 08-31 → 09-13 | S1.4 Discrete RVs + S10.2 DP | 20 LC-easy total |
| S19 | 09-14 → 09-27 | S1.5 Continuous RVs + **S10.3 graphs/BFS (critical)** | Graph solvers |
| S20 | 09-28 → 10-11 | S1.6 Joint/MVN + S7 LA deepen | PCA on toy covariance |
| S21 | 10-12 → 10-25 | S1.8 MGF + S2.1 puzzles + **mid-checkpoint retest** | Radar update; adjust S22–S27 |
| S22 | 10-26 → 11-08 | S3.1 Markov (start) + S10.2 DP deepen | 5 LC-medium |
| S23 | 11-09 → 11-22 | S3.1 finish + S3.2 + S9.1 MLE | Gambler's ruin solver |
| S24 | 11-23 → 12-06 | S9.2 Hyp testing + S9.3 Regression/TS | Regression notebook |
| S25 | 12-07 → 12-20 | S9.3 GARCH + S4.1 BM + microstructure | GARCH(1,1), BM simulator |
| S26 | 12-21 → 2027-01-03 | S4.2 OST + S4.3 Itô + S6.1/6.2 → **P1** · **Mock #1** | P1 shipped |
| S27 | 01-04 → 01-17 | S6.5 MC + S9.4 Bayesian → **P16** · **Mocks #2–4** · **final retest** | Ready for 01-15 |

---

## Study material (already owned — no new purchases needed)

| Book | Primary for |
|---|---|
| Ross, *First Course in Probability* | S1, S2 |
| Green Book (Xinfeng Zhou) | S2, S3, general interview drill |
| Campbell / Lo / MacKinlay, *Econometrics of Financial Markets* | S9 (reference, not cover-to-cover) |
| Hull, *Options Futures and Other Derivatives* | S6 |

**Free supplements:** MIT OCW 6.041 (probability), 3Blue1Brown (LA + calc), NeetCode 150 (algos), StatQuest (stats).

---

## Success metrics

- **External:** ≥1 onsite passed, ≥2 first-round interviews by end of S27
- **Internal (real target):** quiet confidence in the room, sourced from demonstrated mastery — Feynman notes shipped + solvers passing + unlock tests passed
- **Leading indicator:** confidence trend line on mocks S26→S27 must be positive

---

*See `03_gated_progression.md` for the full DAG diagram and per-sprint rationale.*

