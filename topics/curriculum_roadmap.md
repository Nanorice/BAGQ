# STS Desk Strat — Accelerated Curriculum Design
## AI-Augmented Learning Framework & Team-Based Skill Distribution

---

## 1. Overview & Philosophy

This curriculum is designed for quantitative strategists ("desk strats") joining or supporting
a **Systematic Trading Strategies (STS)** desk focused on volatility and options-based index
products (e.g., GSVIMLVL-style strategies).

### Core Principles

| Principle | Description |
|:---|:---|
| **Framework first, details later** | Build a working end-to-end skeleton before deepening any single component |
| **AI-accelerated** | Use AI tools (ChatGPT, Copilot, Claude) to compress knowledge acquisition and code production by 50–70% |
| **Team-based skill distribution** | No individual masters everything — skills are distributed across roles |
| **Learn by building** | Every concept is anchored to a concrete project with a deliverable |
| **Iterative enrichment** | Revisit and deepen each module over successive phases |

---

## 2. Model Ownership Map — Who Builds What?

Before designing individual learning paths, it's critical to understand which models the STS
desk strat **owns**, **co-owns**, or **consumes** from other teams.

| Model | Owned By | STS Desk Strat Role |
|:---|:---|:---|
| Volatility surface model | Equities Derivatives Strats / Core Quant | **Consumer** — uses as input; may build lightweight overlays |
| Options pricing engine (BS, local vol, stochastic vol) | Core Quant Library / Risk Strats | **Consumer** — calls the library; may extend for exotic payoffs |
| Realized vol estimation | Shared / built in-house | **Builder** — builds estimators tuned to specific frequencies |
| Correlation / dispersion model | Equity Derivatives Strats + STS | **Co-builder** — builds dispersion analytics on top of core framework |
| Conditional trigger model (e.g., 1σ drawdown) | STS desk strats | **Full owner** — bespoke to the strategy |
| Backtesting engine | STS desk strats | **Full owner** — custom-built for systematic strategy simulation |
| Execution / market impact model | Electronic Trading / Execution Strats | **Consumer + collaborator** |
| Index calculation engine | STS desk strats + Index team | **Co-owner** — strats define methodology, index team handles production |
| Swap pricing / fee model | STS desk strats + Structuring | **Co-owner** |
| Client customisation models | STS desk strats | **Full owner** |
| P&L attribution | STS desk strats + Risk | **Co-owner** |

> **Key takeaway:** The STS desk strat is a **power user** of core quant infrastructure but a
> **full owner** of strategy-specific models. The skill is knowing how to leverage shared
> infrastructure while building differentiated, strategy-specific tools.

---

## 3. AI Acceleration — How It Changes the Timeline

| Traditional Approach | AI-Accelerated Approach | Time Savings |
|:---|:---|:---|
| Read Hull cover-to-cover (3 months) | AI explains concepts on-demand with tailored examples | ~60–70% |
| Build a backtesting engine from scratch (2–3 months) | AI generates boilerplate code; you debug and iterate | ~50–60% |
| Learn vol surface construction via Gatheral (2 months) | AI walks through SVI calibration step-by-step with your data | ~50% |
| Debug a Greeks calculation for 2 days | AI identifies the error in minutes | ~90% |
| Write index methodology documentation (weeks) | AI drafts structure; you refine with domain knowledge | ~60% |

### Compressed Timeline Summary

| Phase | Traditional | AI-Accelerated | Focus |
|:---|:---|:---|:---|
| Tier 1 (Foundation) | 6 months | **2–3 months** | Learn frameworks, not every detail |
| Tier 2 (Core Competency) | 12 months | **4–6 months** | Build working prototypes fast, deepen iteratively |
| Tier 3 (Advanced / Mastery) | 12 months | **6–9 months** | Differentiation via experience + judgment |
| **Total** | **36 months** | **12–18 months** | **~50–60% compression** |

> **Caveat:** AI accelerates knowledge acquisition and code production but cannot replace
> market intuition, judgment under pressure, or relationship-building with traders. Those
> require time on the desk.
> — [McKinsey: The Future of AI in Banking](https://www.mckinsey.com/industries/financial-services/our-insights/the-future-of-ai-in-banking)

---

## 4. Three-Phase Learning Architecture

### Phase 1: Skeleton (Months 1–3) — End-to-End Framework

**Goal:** Get the full picture working, even if each component is crude.

| Component | What to Build | Depth Level |
|:---|:---|:---|
| Options pricing | Black-Scholes pricer in Python; understand delta, gamma, theta, vega intuitively | Use AI to generate code; focus on **intuition not derivation** |
| Vol surface | Consume a pre-built surface (e.g., from [QuantLib](https://www.quantlib.org/)); plot it; understand smile/skew visually | Don't build from scratch — just **use it** |
| Backtester | Simple framework: load data → apply rules → compute P&L → plot results | AI scaffolds in hours; you refine |
| Strategy logic | Implement a simplified version of ONE leg (e.g., buy weekly straddles, delta-hedge daily) | Understand **mechanics**, not optimization |
| Greeks dashboard | Real-time Greek computation for a small portfolio | Spreadsheet or simple Python dashboard |

**Phase 1 Deliverable:** A working end-to-end prototype that takes historical data → applies
a systematic vol strategy → computes P&L and Greeks.

---

### Phase 2: Enrich Components (Months 3–9) — Deepen Each Module

| Component | Enrichment | AI Role |
|:---|:---|:---|
| Options pricing | Add local vol, stochastic vol; understand when BS breaks down | AI explains model differences with numerical examples |
| Vol surface | Build your own SVI calibration; understand arbitrage constraints | AI debugs calibration code, explains parameter sensitivities |
| Backtester | Add transaction costs, slippage, realistic roll logic, regime tagging | AI generates test cases and edge-case scenarios |
| Strategy logic | Add Legs B and C; implement conditional triggers, dispersion logic | AI helps with correlation matrices, gamma-weighting |
| Execution model | Add market impact estimation, optimal execution timing | AI helps implement Almgren-Chriss or simpler heuristics |
| Client customisation | Build a module that swaps underlyings (SPX → Russell), adjusts parameters | AI helps build flexible, parameterized architecture |

---

### Phase 3: Production & Mastery (Months 9–18) — Real-World Hardening

| Component | Focus |
|:---|:---|
| Production robustness | Error handling, data quality checks, monitoring, alerting |
| P&L attribution | Decompose returns into Greek components; explain to traders daily |
| Client-facing analytics | Build reports, scenario analyses, customisation tools |
| Market intuition | Sit with traders, watch strategies in real-time, experience drawdowns |

---

## 5. Skill Domain Map by Role

This is a **team-level** skill distribution. No single person covers everything.

| Skill Domain | Trader | Desk Strat | Structurer | Index Team | Sales |
|:---|:---:|:---:|:---:|:---:|:---:|
| Options theory & Greeks | ★★★ | ★★★ | ★★☆ | ★☆☆ | ★☆☆ |
| Volatility modeling | ★★☆ | ★★★ | ★☆☆ | ★☆☆ | ☆☆☆ |
| Python / coding | ★☆☆ | ★★★ | ★☆☆ | ★★★ | ☆☆☆ |
| Stochastic calculus | ★☆☆ | ★★★ | ★☆☆ | ☆☆☆ | ☆☆☆ |
| Backtesting & simulation | ★☆☆ | ★★★ | ★☆☆ | ★★☆ | ☆☆☆ |
| Correlation / dispersion | ★★☆ | ★★★ | ★☆☆ | ★☆☆ | ☆☆☆ |
| Execution & microstructure | ★★★ | ★★☆ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| Client communication | ★☆☆ | ★☆☆ | ★★★ | ☆☆☆ | ★★★ |
| Product structuring (swaps, notes) | ★★☆ | ★★☆ | ★★★ | ★☆☆ | ★★☆ |
| Risk management | ★★★ | ★★☆ | ★☆☆ | ★☆☆ | ☆☆☆ |
| Data engineering / SQL | ☆☆☆ | ★★★ | ☆☆☆ | ★★★ | ☆☆☆ |
| Regulatory / legal | ☆☆☆ | ☆☆☆ | ★★☆ | ★☆☆ | ★☆☆ |

> ★★★ = Deep expertise required | ★★☆ = Working knowledge | ★☆☆ = Awareness | ☆☆☆ = Not required

---

## 6. Recommended Resources by Tier

### Tier 1: Foundation

| Topic | Resource | Link |
|:---|:---|:---|
| Options theory | Hull — *Options, Futures, and Other Derivatives* | [Pearson](https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005938) |
| Volatility fundamentals | Natenberg — *Option Volatility and Pricing* | [Amazon](https://www.amazon.com/Option-Volatility-Pricing-Strategies-Techniques/dp/0071818774) |
| Python for finance | Hilpisch — *Python for Finance* | [O'Reilly](https://www.oreilly.com/library/view/python-for-finance/9781492024323/) |
| Probability & statistics | MIT OCW — Intro to Probability | [MIT](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/) |
| Linear algebra | 3Blue1Brown — Essence of Linear Algebra | [3B1B](https://www.3blue1brown.com/topics/linear-algebra) |
| Practical vol trading | Sinclair — *Volatility Trading* | [Amazon](https://www.amazon.com/Volatility-Trading-Euan-Sinclair/dp/1118347137) |

### Tier 2: Core Competency

| Topic | Resource | Link |
|:---|:---|:---|
| Vol surface construction | Gatheral — *The Volatility Surface* | [Amazon](https://www.amazon.com/Volatility-Surface-Practitioners-Guide/dp/0471792519) |
| Stochastic calculus | Shreve — *Stochastic Calculus for Finance II* | [Springer](https://www.springer.com/gp/book/9780387401010) |
| Backtesting methodology | de Prado — *Advances in Financial Machine Learning* | [Amazon](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089) |
| Correlation trading | Bossu — *Correlation Trading* (SSRN) | [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1722475) |
| Dynamic hedging | Taleb — *Dynamic Hedging* | [Amazon](https://www.amazon.com/Dynamic-Hedging-Managing-Vanilla-Options/dp/0471152803) |
| SQL & data engineering | Mode Analytics SQL Tutorial | [Mode](https://mode.com/sql-tutorial) |
| Time series analysis | Tsay — *Analysis of Financial Time Series* | [Amazon](https://www.amazon.com/Analysis-Financial-Time-Ruey-Tsay/dp/0470414359) |

### Tier 3: Advanced / Differentiating

| Topic | Resource | Link |
|:---|:---|:---|
| Exotic options pricing | Wilmott — *Paul Wilmott on Quantitative Finance* | [Amazon](https://www.amazon.com/Paul-Wilmott-Quantitative-Finance-Set/dp/0470018704) |
| Market microstructure | Bouchaud — *Trades, Quotes and Prices* | [Cambridge](https://www.cambridge.org/core/books/trades-quotes-and-prices/029A71078A0A2B1B1B30B4010AAAD97C) |
| Execution optimization | Almgren & Chriss (2000) — Optimal Execution | [NYU](https://www.math.nyu.edu/~almgren/papers/optliq.pdf) |

---

## 7. AI Tools Recommended for Each Phase

| Phase | Tool | Use Case |
|:---|:---|:---|
| All phases | [ChatGPT](https://chat.openai.com/) / [Claude](https://claude.ai/) | Concept explanation, code generation, debugging, document drafting |
| Coding | [GitHub Copilot](https://github.com/features/copilot) | In-IDE code completion, boilerplate generation |
| Data analysis | [ChatGPT Code Interpreter](https://openai.com/blog/chatgpt-plugins) | Upload data, generate plots, run quick analyses |
| Research | [Perplexity AI](https://www.perplexity.ai/) | Find papers, verify facts, discover resources |
| Documentation | [Notion AI](https://www.notion.so/product/ai) | Draft methodology documents, meeting notes, project specs |

---

## 8. Success Metrics by Phase

| Phase | You Know You're Ready When... |
|:---|:---|
| **Phase 1 complete** | You can explain what each leg of a vol strategy does, price a vanilla option, run a simple backtest, and have a working prototype |
| **Phase 2 complete** | You can build a multi-leg strategy backtest with realistic costs, calibrate a vol surface, compute and explain P&L attribution, and customise a strategy for a different underlying |
| **Phase 3 complete** | You can run a strategy in production, explain daily P&L to a trader, handle a client customisation request end-to-end, and identify when a model is breaking down in real market conditions |

---

*Document version: 1.0 | Last updated: 2026-03-19*
