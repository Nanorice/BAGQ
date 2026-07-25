# Phase 1: Skeleton Build
## Months 1–3 | End-to-End Framework

---

## 1. Phase 1 Objective

> **Build a crude but complete end-to-end pipeline:**
> Price an option → visualize the vol surface → run a simple strategy → backtest it → see P&L.
>
> Every component will be rough. That's the point. You are building the **skeleton**
> that Phase 2 and Phase 3 will flesh out.

---

## 2. Phase 1 Module Overview

| Week | Module | Topic | Project | AI Acceleration |
|:---|:---|:---|:---|:---|
| 1–2 | **M1** | Options Pricing Foundations | P1: Black-Scholes Pricer | AI generates BS code; you focus on intuition |
| 3–4 | **M2** | Vol Surface Basics | P2: Vol Surface Visualizer | AI explains SVI; you plot real data |
| 5–8 | **M3** | Backtesting Framework | P3: Simple Backtest Engine | AI scaffolds engine; you design strategy rules |
| 9–12 | **M4** | Single-Leg Strategy | P4: Covered Call / Put-Spread Strategy | AI helps with payoff diagrams; you tune parameters |

---

## 3. Module M1: Options Pricing Foundations (Weeks 1–2)

### 3.1 Learning Objectives

By the end of this module you should be able to:

- Explain the Black-Scholes formula **intuitively** (not just mathematically)
- Price European calls and puts in Python
- Compute and interpret all first-order Greeks: $\Delta$, $\Gamma$, $\Theta$, $\mathcal{V}$, $\rho$
- Invert the BS formula to solve for **implied volatility** given a market price
- Understand the **assumptions and limitations** of BS (and why it still matters)

### 3.2 Key Concepts

| Concept | What to Know | Depth |
|:---|:---|:---|
| Black-Scholes formula | $C = S \cdot N(d_1) - K e^{-rT} \cdot N(d_2)$ | Understand each term; don't memorize derivation |
| $d_1$ and $d_2$ | $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$, $d_2 = d_1 - \sigma\sqrt{T}$ | Know what drives them |
| Delta ($\Delta$) | Rate of change of option price w.r.t. spot | **Most important Greek** — understand as hedge ratio |
| Gamma ($\Gamma$) | Rate of change of delta w.r.t. spot | Convexity — why gamma scalping works |
| Theta ($\Theta$) | Time decay per day | The "rent" you collect when selling options |
| Vega ($\mathcal{V}$) | Sensitivity to implied vol | Critical for vol-selling strategies |
| Implied Volatility | The vol that makes BS price = market price | Solve numerically (Newton-Raphson or Brent) |
| Put-Call Parity | $C - P = S - K e^{-rT}$ | Arbitrage relationship; sanity check |

### 3.3 AI-Accelerated Learning Path

| Task | How to Use AI | Time |
|:---|:---|:---|
| "Explain Black-Scholes to me like I'm a trader, not a mathematician" | ChatGPT / Claude | 30 min |
| "Generate a Python BS pricer with all Greeks" | Copilot / Claude | 1 hour |
| "Walk me through Newton-Raphson IV solver step by step" | ChatGPT | 1 hour |
| "Show me how delta changes as spot moves — plot it" | Copilot | 30 min |
| "What breaks in BS and why do we still use it?" | ChatGPT | 30 min |

### 3.4 Recommended References

| Resource | Type | Use |
|:---|:---|:---|
| [Hull — Options, Futures, and Other Derivatives, Ch. 13–15, 19](https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005938) | Textbook | Skim for structure; use AI to clarify |
| [QuantLib Python Cookbook](https://quantlib-python-docs.readthedocs.io/) | Code reference | See how production libraries implement pricing |
| [Option Alpha — Greeks Guide](https://optionalpha.com/guides/option-greeks) | Visual guide | Quick intuition builder |

---

### 3.5 Project P1: Black-Scholes Pricer

#### Specification

```
Project:     P1 — Black-Scholes Pricer & Greeks Calculator
Objective:   Build a fully functional European options pricer in Python
Duration:    ~1 week (AI-accelerated)
Deliverable: Python module + Jupyter notebook with examples
```

#### Requirements

| # | Requirement | Priority |
|:---|:---|:---|
| 1 | Price European calls and puts given $$S, K, T, r, \sigma, q$$ | Must have |
| 2 | Compute $$\Delta, \Gamma, \Theta, \mathcal{V}, \rho$$ analytically | Must have |
| 3 | Implied volatility solver (Newton-Raphson with fallback to Brent) | Must have |
| 4 | Vectorized — price arrays of options at once (NumPy) | Must have |
| 5 | Greeks surface plots: delta vs spot vs vol, gamma vs spot vs time, etc. | Should have |
| 6 | Put-call parity verification | Should have |
| 7 | Compare your pricer output to QuantLib output | Nice to have |

#### Suggested File Structure

```
src/pricer/
├── __init__.py
├── black_scholes.py       # Core BS pricing functions
├── greeks.py              # Greeks calculations
├── implied_vol.py         # IV solver
└── utils.py               # Helper functions (N(d), etc.)

notebooks/
├── 01_bs_pricer_demo.ipynb
└── 02_greeks_visualization.ipynb

tests/
└── test_black_scholes.py
```

#### Starter Code Skeleton

```
python
# src/pricer/black_scholes.py

import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

def bs_price(S: float, K: float, T: float, r: float, sigma: float,
             q: float = 0.0, option_type: str = "call") -> float:
    """
    Black-Scholes European option price.

    Parameters
    ----------
    S : float — Spot price
    K : float — Strike price
    T : float — Time to expiry (years)
    r : float — Risk-free rate (annualized)
    sigma : float — Volatility (annualized)
    q : float — Continuous dividend yield
    option_type : str — 'call' or 'put'

    Returns
    -------
    float — Option price
    """
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def bs_delta(S, K, T, r, sigma, q=0.0, option_type="call"):
    """Compute BS delta."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return np.exp(-q * T) * norm.cdf(d1)
    else:
        return np.exp(-q * T) * (norm.cdf(d1) - 1)


def bs_gamma(S, K, T, r, sigma, q=0.0):
    """Compute BS gamma (same for call and put)."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return np.exp(-q * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))


def bs_theta(S, K, T, r, sigma, q=0.0, option_type="call"):
    """Compute BS theta (per year — divide by 365 for daily)."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    term1 = -(S * np.exp(-q * T) * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        term2 = q * S * np.exp(-q * T) * norm.cdf(d1)
        term3 = -r * K * np.exp(-r * T) * norm.cdf(d2)
    else:
        term2 = -q * S * np.exp(-q * T) * norm.cdf(-d1)
        term3 = r * K * np.exp(-r * T) * norm.cdf(-d2)

    return term1 - term2 + term3  # Note: typically negative for long options


def bs_vega(S, K, T, r, sigma, q=0.0):
    """Compute BS vega (same for call and put). Per 1 vol point."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return S * np.exp(-q * T) * norm.pdf(d1) * np.sqrt(T) / 100  # per 1 vol point


def implied_vol(price: float, S: float, K: float, T: float, r: float,
                q: float = 0.0, option_type: str = "call",
                tol: float = 1e-8, max_iter: int = 100) -> float:
    """
    Solve for implied volatility using Brent's method.

    Parameters
    ----------
    price : float — Observed market price of the option

    Returns
    -------
    float — Implied volatility
    """
    def objective(sigma):
        return bs_price(S, K, T, r, sigma, q, option_type) - price

    try:
        return brentq(objective, 1e-6, 5.0, xtol=tol, maxiter=max_iter)
    except ValueError:
        return np.nan  # No solution found in range
```

#### Test File Skeleton

```
python
# tests/test_black_scholes.py

import pytest
import numpy as np
from src.pricer.black_scholes import bs_price, bs_delta, bs_gamma, implied_vol


class TestBSPrice:
    """Test Black-Scholes pricing."""

    def test_call_price_basic(self):
        """Known result: S=100, K=100, T=1, r=0.05, sigma=0.2"""
        price = bs_price(100, 100, 1, 0.05, 0.2, option_type="call")
        assert abs(price - 10.4506) < 0.01  # Known BS result

    def test_put_call_parity(self):
        """C - P = S*exp(-qT) - K*exp(-rT)"""
        S, K, T, r, sigma, q = 100, 105, 0.5, 0.05, 0.25, 0.02
        call = bs_price(S, K, T, r, sigma, q, "call")
        put = bs_price(S, K, T, r, sigma, q, "put")
        parity = S * np.exp(-q * T) - K * np.exp(-r * T)
        assert abs((call - put) - parity) < 1e-8

    def test_deep_itm_call_approaches_intrinsic(self):
        """Deep ITM call ≈ S - K*exp(-rT) for very high S."""
        price = bs_price(200, 100, 1, 0.05, 0.2, option_type="call")
        intrinsic = 200 - 100 * np.exp(-0.05)
        assert abs(price - intrinsic) < 1.0

    def test_implied_vol_roundtrip(self):
        """Price with known vol → recover that vol via IV solver."""
        true_vol = 0.25
        price = bs_price(100, 100, 1, 0.05, true_vol, option_type="call")
        recovered_vol = implied_vol(price, 100, 100, 1, 0.05, option_type="call")
        assert abs(recovered_vol - true_vol) < 1e-6


class TestGreeks:
    """Test Greeks calculations."""

    def test_call_delta_range(self):
        """Call delta should be between 0 and 1."""
        delta = bs_delta(100, 100, 1, 0.05, 0.2, option_type="call")
        assert 0 < delta < 1

    def test_atm_delta_approximately_half(self):
        """ATM call delta ≈ 0.5 (slightly above due to drift)."""
        delta = bs_delta(100, 100, 1, 0.05, 0.2, option_type="call")
        assert 0.45 < delta < 0.65

    def test_gamma_positive(self):
        """Gamma is always positive for long options."""
        gamma = bs_gamma(100, 100, 1, 0.05, 0.2)
        assert gamma > 0
```

#### Notebook Outline: `01_bs_pricer_demo.ipynb`

```markdown
## Notebook: Black-Scholes Pricer Demo

### Cell 1: Setup
- Import bs_price, greeks, implied_vol
- Set base parameters: S=100, K=100, T=1, r=0.05, sigma=0.20

### Cell 2: Price a Call and Put
- Print call price, put price
- Verify put-call parity

### Cell 3: Greeks Table
- Compute all Greeks for a range of strikes (80–120)
- Display as pandas DataFrame

### Cell 4: Delta vs Spot
- Plot delta as a function of spot price (60–140)
- Show call delta and put delta on same chart

### Cell 5: Gamma vs Spot vs Time
- 3D surface plot: gamma as function of (S, T)
- Show how gamma concentrates near ATM as expiry approaches

### Cell 6: Implied Volatility
- Given a set of market prices, recover IV
- Plot IV vs strike → this is your first "smile" plot

### Cell 7: Theta Decay
- Plot option price vs days to expiry
- Show the acceleration of time decay near expiry

### Cell 8: Vega vs Moneyness
- Plot vega across strikes
- Explain why ATM options have highest vega
```

---

## 4. Module M2: Vol Surface Basics (Weeks 3–4)

### 4.1 Learning Objectives

- Understand why implied volatility varies by strike and tenor (the **smile** and **term structure**)
- Load or generate a grid of implied vols and plot a **3D volatility surface**
- Understand the **SVI parameterization** at a conceptual level
- Consume a vol surface as an **input** to strategy pricing — you are not building the production surface

### 4.2 Key Concepts

| Concept | What to Know | Depth |
|:---|:---|:---|
| Volatility smile / skew | IV is higher for OTM puts (downside protection demand) | Intuition — know **why** it exists |
| Term structure of vol | Short-dated vol reacts more to events; long-dated vol is more stable | Understand shape drivers |
| SVI parameterization | $$w(k) = a + b\left(\rho(k - m) + \sqrt{(k - m)^2 + \sigma^2}\right)$$ | Know the 5 params; don't derive |
| Moneyness metrics | Log-moneyness $$k = \ln(K/F)$$, delta-space, standardized moneyness | Know which to use when |
| Sticky strike vs sticky delta | Two regimes for how the surface moves with spot | Conceptual understanding |
| No-arbitrage constraints | Calendar spread and butterfly arbitrage conditions | Know they exist; check them |

### 4.3 Project P2: Vol Surface Visualizer

#### Specification

```
Project:     P2 — Implied Volatility Surface Visualizer
Objective:   Load IV data, interpolate, and plot an interactive 3D vol surface
Duration:    ~1 week
Deliverable: Python module + interactive Plotly notebook
```

#### Requirements

| # | Requirement | Priority |
|:---|:---|:---|
| 1 | Load IV data from CSV or API (strikes × tenors grid) | Must have |
| 2 | Interpolate missing points (bilinear or cubic spline) | Must have |
| 3 | Plot 3D surface using Plotly (interactive rotation/zoom) | Must have |
| 4 | Plot 2D smile slices for individual tenors | Must have |
| 5 | Plot 2D term structure for fixed delta (e.g., ATM, 25-delta put) | Should have |
| 6 | Overlay two surfaces (e.g., today vs 1 week ago) | Nice to have |
| 7 | Basic SVI calibration to a single smile slice | Nice to have |

#### Suggested File Structure

```
src/vol_surface/
├── __init__.py
├── loader.py              # Load IV data from CSV / API
├── interpolator.py        # 2D interpolation of the surface
├── plotter.py             # 3D and 2D plotting functions
└── svi.py                 # SVI parameterization (basic)

notebooks/
└── 03_vol_surface_demo.ipynb

data/raw/
└── sample_iv_surface.csv  # Sample data file
```

#### Sample Data Format (`sample_iv_surface.csv`)

```csv
strike_pct,1W,1M,2M,3M,6M,1Y
80,32.5,28.1,26.8,25.9,24.5,23.8
85,27.8,24.5,23.6,23.0,22.1,21.6
90,23.5,21.2,20.7,20.3,19.8,19.5
95,20.1,18.8,18.5,18.3,18.0,17.9
100,18.2,17.5,17.3,17.2,17.0,17.0
105,19.0,18.0,17.8,17.6,17.3,17.2
110,21.5,19.8,19.3,19.0,18.5,18.2
115,24.8,22.5,21.8,21.3,20.5,20.0
120,28.5,25.8,24.8,24.0,23.0,22.2
```

---

## 5. Module M3: Backtesting Framework (Weeks 5–8)

### 5.1 Learning Objectives

- Design a **modular backtesting engine** that separates data, strategy logic, execution, and reporting
- Understand the critical pitfalls: **look-ahead bias**, **survivorship bias**, **transaction costs**
- Compute standard performance metrics: Sharpe, max drawdown, Calmar, win rate
- Generate a **backtest report** with equity curve, drawdown chart, and summary statistics

### 5.2 Key Concepts

| Concept | What to Know | Depth |
|:---|:---|:---|
| Event-driven vs vectorized backtesting | Vectorized is faster for simple strategies; event-driven for complex | Start vectorized |
| Look-ahead bias | Never use future data in signal generation | Critical — must understand deeply |
| Transaction costs | Bid-ask spread, commissions, slippage | Model as fixed + proportional cost |
| Rebalancing frequency | Daily, weekly, monthly, on-signal | Understand trade-offs |
| Performance metrics | Sharpe, Sortino, max drawdown, Calmar ratio, hit rate | Compute all from scratch |
| Benchmark comparison | Compare strategy vs buy-and-hold, vs risk-free | Always include |

### 5.3 Project P3: Simple Backtest Engine

#### Specification

```
Project:     P3 — Systematic Strategy Backtesting Engine
Objective:   Build a reusable, modular backtesting framework
Duration:    ~2–3 weeks
Deliverable: Python package + sample strategy backtest + report notebook
```

#### Requirements

| # | Requirement | Priority |
|:---|:---|:---|
| 1 | Load historical price data (CSV or yfinance) | Must have |
| 2 | Define strategy as a class with `generate_signals()` and `execute()` methods | Must have |
| 3 | Support long/short/flat positions | Must have |
| 4 | Track portfolio value, positions, cash, P\&L daily | Must have |
| 5 | Compute: Sharpe, max drawdown, Calmar, annualized return, win rate | Must have |
| 6 | Plot: equity curve, drawdown chart, monthly returns heatmap | Must have |
| 7 | Transaction cost model (configurable bps) | Should have |
| 8 | Support multiple assets | Nice to have |
| 9 | Generate HTML or PDF report | Nice to have |

#### Architecture

```
src/backtester/
├── __init__.py
├── data_loader.py         # Load and clean price data
├── strategy.py            # Base strategy class (abstract)
├── engine.py              # Core backtesting loop
├── portfolio.py           # Track positions, cash, P&L
├── metrics.py             # Performance metrics calculations
├── report.py              # Generate plots and summary report
└── costs.py               # Transaction cost models

strategies/
├── __init__.py
├── moving_average.py      # Sample: MA crossover (for testing the engine)
└── vol_selling.py         # Placeholder for Phase 1 strategy

notebooks/
└── 04_backtest_demo.ipynb
```

#### Core Engine Skeleton

```
python
# src/backtester/engine.py

import pandas as pd
from abc import ABC, abstractmethod


class Strategy(ABC):
    """Abstract base class for all strategies."""

    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate trading signals.

        Returns
        -------
        pd.Series — Signal series: +1 (long), -1 (short), 0 (flat)
        """
        pass


class BacktestEngine:
    """Core backtesting engine."""

    def __init__(self, strategy: Strategy, data: pd.DataFrame,
                 initial_capital: float = 1_000_000,
                 cost_bps: float = 5.0):
        self.strategy = strategy
        self.data = data
        self.initial_capital = initial_capital
        self.cost_bps = cost_bps / 10_000
        self.results = None

    def run(self) -> pd.DataFrame:
        """Execute the backtest."""
        signals = self.strategy.generate_signals(self.data)
        returns = self.data["close"].pct_change()

        # Strategy returns = signal(t-1) * return(t) — no look-ahead
        strategy_returns = signals.shift(1) * returns

        # Subtract transaction costs on position changes
        trades = signals.diff().abs()
        costs = trades * self.cost_bps
        net_returns = strategy_returns - costs

        # Build equity curve
        equity = self.initial_capital * (1 + net_returns).cumprod()

        self.results = pd.DataFrame({
            "close": self.data["close"],
            "signal": signals,
            "returns": returns,
            "strategy_returns": strategy_returns,
            "net_returns": net_returns,
            "equity": equity,
            "drawdown": equity / equity.cummax() - 1
        })

        return self.results
```

#### Metrics Module Skeleton

```
python
# src/backtester/metrics.py

import numpy as np
import pandas as pd


def compute_metrics(results: pd.DataFrame, risk_free_rate: float = 0.0) -> dict:
    """Compute standard performance metrics."""
    r = results["net_returns"].dropna()

    total_return = (results["equity"].iloc[-1] / results["equity"].iloc[0]) - 1
    ann_return = (1 + total_return) ** (252 / len(r)) - 1
    ann_vol = r.std() * np.sqrt(252)
    sharpe = (ann_return - risk_free_rate) / ann_vol if ann_vol > 0 else 0
    max_dd = results["drawdown"].min()
    calmar = ann_return / abs(max_dd) if max_dd != 0 else 0
    win_rate = (r > 0).sum() / (r != 0).sum() if (r != 0).sum() > 0 else 0

    return {
        "Total Return": f"{total_return:.2%}",
        "Annualized Return": f"{ann_return:.2%}",
        "Annualized Volatility": f"{ann_vol:.2%}",
        "Sharpe Ratio": f"{sharpe:.2f}",
        "Max Drawdown": f"{max_dd:.2%}",
        "Calmar Ratio": f"{calmar:.2f}",
        "Win Rate": f"{win_rate:.2%}",
        "Number of Trades": int(results["signal"].diff().abs().sum() / 2),
    }
```

---

## 6. Module M4: Single-Leg Strategy (Weeks 9–12)

### 6.1 Learning Objectives

- Implement a **systematic covered call** or **put-spread selling** strategy
- Understand the **payoff profile** and **risk characteristics** of basic options strategies
- Connect the pricer (P1), vol surface (P2), and backtester (P3) into a working pipeline
- Analyze strategy performance across different vol regimes

### 6.2 Key Concepts

| Concept | What to Know | Depth |
|:---|:---|:---|
| Covered call | Long stock + short OTM call → collect premium, cap upside | Full understanding |
| Put spread | Short put + long further OTM put → defined-risk premium collection | Full understanding |
| Strike selection | ATM, % OTM, delta-based (e.g., 30-delta put) | Implement delta-based |
| Roll mechanics | Close expiring position, open new one at next tenor | Understand cost of rolling |
| Vol regime sensitivity | Strategy performs differently in low-vol vs high-vol vs crash | Analyze in backtest |
| Premium decay (theta) | Why systematic selling works over time — and when it doesn't | Core intuition |

### 6.3 Project P4: Systematic Put-Spread Strategy

#### Specification

```
Project:     P4 — Systematic Put-Spread Selling Strategy
Objective:   Implement, backtest, and analyze a rules-based put-spread strategy
Duration:    ~2–3 weeks
Deliverable: Strategy module + full backtest report + regime analysis
```

#### Requirements

| # | Requirement | Priority |
|:---|:---|:---|
| 1 | Sell monthly 95%-strike put, buy 85%-strike put on SPX | Must have |
| 2 | Roll at expiry (or T-1) | Must have |
| 3 | Use BS pricer (P1) to price the spread at entry and exit | Must have |
| 4 | Run through backtester (P3) with transaction costs | Must have |
| 5 | Compute all performance metrics | Must have |
| 6 | Regime analysis: split results by VIX level (low/med/high) | Should have |
| 7 | Strike sensitivity: compare 90/80 vs 95/85 vs 97/90 spreads | Should have |
| 8 | Overlay equity curve vs SPX buy-and-hold | Should have |
| 9 | Drawdown analysis: identify worst periods and explain | Should have |

#### Strategy Logic Pseudocode

```
python
# Simplified strategy logic

class PutSpreadStrategy(Strategy):
    """
    Systematic monthly put-spread selling on SPX.

    - Sell put at strike = spot * short_strike_pct (e.g., 0.95)
    - Buy put at strike = spot * long_strike_pct (e.g., 0.85)
    - Hold to expiry, then roll
    """

    def __init__(self, short_strike_pct=0.95, long_strike_pct=0.85,
                 tenor_days=30, vol_surface=None):
        self.short_strike_pct = short_strike_pct
        self.long_strike_pct = long_strike_pct
        self.tenor_days = tenor_days
        self.vol_surface = vol_surface  # From P2

    def generate_signals(self, data):
        # On each roll date:
        #   1. Compute short_strike = spot * 0.95
        #   2. Compute long_strike = spot * 0.85
        #   3. Price both puts using BS (P1) with IV from vol surface (P2)
        #   4. Net premium = short_put_price - long_put_price
        #   5. Track daily P&L as the spread value changes
        pass
```

---

## 7. Phase 1 Milestone Checklist

At the end of Phase 1 (Month 3), you should be able to check off:

| # | Milestone | Status |
|:---|:---|:---|
| 1 | ✅ Can price any European option and compute all Greeks in Python | ☐ |
| 2 | ✅ Can load, interpolate, and visualize an implied vol surface | ☐ |
| 3 | ✅ Have a working backtesting engine that handles signals, costs, and metrics | ☐ |
| 4 | ✅ Have backtested at least one systematic options strategy end-to-end | ☐ |
| 5 | ✅ Can explain the vol smile, term structure, and why they matter for strategy design | ☐ |
| 6 | ✅ Can articulate what the STS desk strat **owns** vs **consumes** | ☐ |
| 7 | ✅ Have a clean project structure with tests | ☐ |
| 8 | ✅ Are comfortable using AI tools to accelerate coding and learning | ☐ |

---

## 8. Phase 1 → Phase 2 Transition

Once Phase 1 is complete, you have a **working skeleton**. Phase 2 will:

- Replace the simple BS pricer with **vol-surface-aware pricing**
- Add **realized vol estimators** and the **variance risk premium** signal
- Build the **multi-leg GSVIMLVL-style strategy** with conditional triggers
- Add **Greeks aggregation** and **P&L attribution**

> The skeleton you built in Phase 1 is the scaffolding. Phase 2 adds the walls and wiring.

---

## Appendix: Phase 1 Weekly Schedule

| Week | Focus | Deliverable |
|:---|:---|:---|
| 1 | BS pricing theory + code | `black_scholes.py` with tests passing |
| 2 | Greeks deep-dive + IV solver | `greeks.py`, `implied_vol.py`, Greeks notebook |
| 3 | Vol surface concepts + data loading | `loader.py`, sample CSV, 2D smile plots |
| 4 | Vol surface visualization | `plotter.py`, interactive 3D Plotly surface |
| 5 | Backtester architecture design | `engine.py`, `strategy.py` base classes |
| 6 | Backtester core implementation | Working engine with MA crossover test strategy |
| 7 | Metrics + reporting | `metrics.py`, `report.py`, equity curve plots |
| 8 | Backtester refinement + cost model | Transaction costs, drawdown analysis |
| 9 | Put-spread strategy design | Strategy class, strike selection logic |
| 10 | Put-spread implementation | Connected to pricer + vol surface |
| 11 | Full backtest run + analysis | Complete backtest with all metrics |
| 12 | Regime analysis + documentation | VIX regime splits, final Phase 1 report |
