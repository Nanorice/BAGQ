---
type: prep-route
name: Route 1 — Books
status: active
opened: 2026-08-19
sources: ["Paleologo, Advanced Portfolio Management", "Isichenko, Quantitative Portfolio Management"]
---

# Route 1 — Books

**Mode: scrap + prime overflow.** This is the route that runs when you are not at a whiteboard —
commute, evening, phone. It is *background*, not the main line. Routes 2 and 3 outrank it every
time they conflict.

**One-source rule still applies.** Two books are in the folder; they are **not both open at once**.
Paleologo first, Isichenko second, and Isichenko is mostly *skimmed*.

---

## What these books do and do not cover

**Read this before planning around them.**

| Block in the map | Covered? | Where |
|---|---|---|
| A. VaR rebuild | ❌ **barely** | Isichenko §4.1 is ~4 pages. No parametric/historical/MC comparison |
| C3. VaR backtesting | ❌ **not at all** | No Kupiec, no Christoffersen, no Basel in either |
| D. Stress testing | ❌ **not at all** | Neither book does regulatory stress testing |
| C4. Strategy backtesting | ✅ **excellently** | Isichenko Ch.7 + §2.4.2 |
| E. Portfolio construction | ✅ **excellently** | Paleologo Ch.6–7, Isichenko Ch.6 |
| A3. Risk decomposition | ✅ **the good part** | Paleologo Ch.3 + §11.1.5 |
| A5. Covariance / factor models | ✅ | Paleologo Ch.4–5, Isichenko §4.2 |

**So: blocks A, C3 and D do not come from here.** They come from Hull (owned) plus written-inline
notes. Do not wait for the books to cover them — they never will.

---

## Paleologo — *Advanced Portfolio Management* (211 pp)

**Why this one first:** it is short, it is written for practitioners rather than researchers, and
Ch.3 is the closest thing in print to *what your VaR surface tool was doing*. Also: Paleologo was
at Citadel. This is close to house style.

### P1. Ch.3 "A Tour of Risk and Performance" — pp. 22–41 (19 pp) ⭐⭐ START HERE
The single highest-value 19 pages in either book, for this role.
- [ ] §3.4 What is risk / measuring risk and performance
- [ ] §3.5 **First steps in risk decomposition** — this is block A3 in the map, in book form
- [ ] §3.6 Simple hedging
- [ ] §3.7 Separation of concerns
> **Read §3.5 with your VaR surface open in your head.** You built the incremental version of this.
> Write down, while reading, the sentence that connects the two. That sentence goes in Route 2's
> block F story and gets said in the interview.

### P2. Ch.4 "An Introduction to Multi-Factor Models" — pp. 41–55 (14 pp) ⭐
- [ ] §4.1 From one factor to many
- [ ] §4.4 Takeaways
> Factor models are how a central risk desk actually decomposes risk. Map every claim back to
> `Σ = BΩBᵀ + D` — factor covariance plus idiosyncratic — and make sure you can write that.

### P3. Ch.7 "Manage Factor Risk" — pp. 109–134 (25 pp) ⭐⭐
The role, in a chapter.
- [ ] §7.1 Tactical factor risk management (incl. §7.1.1 "Optimize If You Must")
- [ ] §7.2 Strategic: limits on factor risk, market exposure, single-stock, single-factor
- [ ] §7.3 Systematic hedging
> §7.2 is *literally a central risk mandate written out*. If an interviewer asks "how would you
> set risk limits", this chapter is the answer.

### P4. §11.1 "Essential Risk Model Formulas" — pp. 179–~185 ⭐⭐ REFERENCE, NOT READING
- [ ] §11.1.1 Factor model
- [ ] §11.1.4 Betas
- [ ] §11.1.5 **Marginal Contribution to Factor Risk** — the formula behind block A3
- [ ] §11.3.1 Mean-variance portfolios · §11.3.2 robust formulation
> Treat as a formula sheet. Copy §11.1.5 and §11.3.1 onto **one index card** and carry it.

### P5. Ch.8 "Understand Your Performance" — pp. 134–160 (26 pp) — *if time*
- [ ] §8.1.1 Performance attribution · §8.2.2 performance vs diversification

### P6. Ch.6 "Alpha Sizing" — pp. 83–109 · Ch.9 "Manage Your Losses" — pp. 160–171 — *skim only*
Ch.9 (11 pp) is drawdown control — cheap, relevant, read it if a slot is short.

**Paleologo total on the starred path (P1–P4): ~60 pp.**

---

## Isichenko — *Quantitative Portfolio Management* (298 pp)

**Do not read this book front to back.** Ch.2 alone is 122 pages of forecasting and machine
learning — it is the alpha-research book, and you are interviewing for the risk seat. It is dense,
it is written at research level, and it will eat your whole prep if you let it.

**Three chapters, in this order:**

### I1. Ch.4 "Risk" — pp. 190–207 (17 pp) ⭐⭐
- [ ] §4.1 **Value at risk and expected shortfall** — the only VaR text you have in these books
- [ ] §4.2 Factor models · §4.3 Types of risk factors
- [ ] §4.4 **Return and risk decomposition**
- [ ] §4.5–4.6 Weighted PCA, PCA transformation
- [ ] §4.7 **Crowding and liquidation** · §4.8 liquidity risk and short squeeze
> §4.7–4.8 are the *modern* central-risk questions and they are not in any textbook you own.
> Crowding is what a multi-manager platform's central risk team worries about most —
> Citadel especially. Read these two twice.

### I2. Ch.7 "Simulation" — pp. 261–279 (18 pp) ⭐⭐
- [ ] §7.1 Simulation vs production
- [ ] §7.2 **Simulation and overfitting** — block C4
- [ ] §7.4 Paper trading · §7.5 Bugs
> Pair with §2.4.2 (Overfitting, ~2 pp) and §3.8.1.8 (Overfit handling). Together they are the
> backtesting-credibility answer.

### I3. Ch.6 "Portfolio Construction" — pp. 220–261 (41 pp) — ⭐ SELECTIVE
- [ ] §6.1 Hedged allocation
- [ ] §6.6 Portfolio capacity
- [ ] §6.9 **Kelly criterion and optimal leverage**
- [ ] §6.8 Portfolio optimization with forecast uncertainty — *concept only, skip the derivation*
> §6.4–6.5 are heavy optimisation-with-impact-costs derivations. **Skip them.** They are a
> stat-arb execution concern, not a central risk one.

### I4. §3.8.2 "Pnl attribution" — pp. ~180 (3 pp) ⭐
- [ ] §3.8.2.1 **Marginal attribution** · §3.8.2.2 regression-based attribution
> Three pages, directly on the marginal-contribution theme. High value per page.

### Deliberately skipped in Isichenko
**Ch.2 (122 pp, forecasting/ML)** — wrong seat. **Ch.5 (trading costs)** — execution, not risk.
**Ch.1 (market data)** — 6 pp, read if curious.
*If an interviewer goes deep on alpha research, the honest answer is "that is the PM side; my
edge is the risk side" — which is true and is the job you are applying for.*

**Isichenko total on the starred path: ~40 pp of real reading.**

---

## How to read these

**Not cover to cover, and not passively.** Same rule as the curriculum: **40-minute hard stop per
session**, one section, then stop.

**Every starred section leaves one artifact** — not a Feynman note (too heavy for this route), but
**three lines in `route_1_notes.md`**: the claim, why it matters for the role, and one question it
would let you answer in an interview. If a section produces no such three lines, it was not worth
reading and you skip the rest of that chapter.

**When it gets hard and you start drifting:** these are practitioner books, not textbooks — the
drift move here is *skip the derivation and take the result*. Paleologo marks optional material
with asterisks (§1.2 explains the convention). Honour them.

---

## Order

**P1 → I1 → P3 → P4 → I2 → P2 → I4 → I3 → P5/P6.**

P1 and I1 first because between them they are the entire risk-decomposition and VaR content of
both books, in 36 pages. If this route never gets past those two, it still paid for itself.

**~100 pp on the starred path. At 40 min/session, ~8–10 sessions.**
