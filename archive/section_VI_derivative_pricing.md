# Section VI: Derivative Pricing & Financial Mathematics — Detailed Problem List

> *Foundation: Risk-neutral valuation, no-arbitrage, fundamental theorems of asset pricing*

Derivative pricing is the crown jewel of quantitative finance. Every quant interview for a trading or structuring desk will touch this material. The core insight is the no-arbitrage principle: derivative prices are expectations under a risk-neutral measure. From binomial trees to Black-Scholes to Monte Carlo, these tools form the practical backbone of the industry.

---

## 1. Binomial Tree Models

### Core Concepts

- **One-Step Binomial Model:** Stock goes up by factor $u$ or down by $d$ in one period. A derivative can be replicated by a portfolio of stock and bond.
- **Risk-Neutral Probability:** $q = (e^{r\Delta t} - d) / (u - d)$. Under $q$, the expected return on the stock equals the risk-free rate.
- **Replicating Portfolio:** $\Delta$ shares of stock + $B$ dollars of bonds that exactly replicate the derivative payoff in both states.
- **Multi-Step Tree:** Chain one-step models together. Price by backward induction: at each node, $V = e^{-r\Delta t}[qV_u + (1-q)V_d]$.
- **CRR Parameters:** Cox-Ross-Rubinstein choice: $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$, ensuring the tree recombines and converges to GBM.

### Key Problems and Questions

- **One-Step Replication:** A stock is at $\$100$. In one period it goes to $\$110$ or $\$90$. Risk-free rate is 5%. Price a call with strike $\$105$ by constructing the replicating portfolio. Verify using risk-neutral pricing.
- **Two-Step European Call:** Extend to a 2-step tree with $u = 1.1$, $d = 0.9$, $r = 0.05$, $\Delta t = 0.5$. Price a European call with $K = 100$. Draw the full tree with stock prices, option values, and hedge ratios at each node.
- **American Put on a Binomial Tree:** Price an American put with $K = 100$ on a 3-step tree. At each node, compare the continuation value with the exercise value. Identify the early exercise boundary. Show the American put is worth strictly more than the European put.
- **Convergence to Black-Scholes:** Price a European call using CRR trees with $n = 10, 50, 100, 500, 1000$ steps. Plot the tree price vs. $n$ and overlay the Black-Scholes analytical price. Show oscillatory convergence and discuss even/odd effects.
- **Binomial Greeks:** Compute Delta, Gamma, and Theta from the binomial tree using finite differences between adjacent nodes. Compare with Black-Scholes Greeks as $n$ increases.
- **Dividend-Paying Stock:** Modify the binomial tree for a stock paying a known discrete dividend $D$ at time $t_d$. Show how the tree "jumps" at the ex-dividend date. Price an American call and show early exercise may be optimal just before the dividend.
- **Trinomial Tree:** Extend the model to three branches (up, middle, down). Derive the risk-neutral probabilities. Show the trinomial tree converges faster than the binomial tree. Implement and compare.
- **Arrow-Debreu Securities:** Compute the state prices (Arrow-Debreu prices) at each node of a binomial tree. Show they sum to the discount factor. Use them to price any derivative as a weighted sum.
- **Binomial Model — Put-Call Parity:** Verify put-call parity $C - P = S - Ke^{-rT}$ holds exactly on the binomial tree for European options. Show it fails for American options (American put-call inequality).
- **Exotic on a Tree — Barrier Option:** Price a down-and-out call on a binomial tree. The option is knocked out if the stock hits $\$80$ at any node. Compare with the analytical barrier option formula. Discuss the "barrier too close to a node" problem.

---

## 2. Black-Scholes-Merton Framework

### Core Concepts

- **Black-Scholes PDE:** $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$.
- **Black-Scholes Formula (Call):** $C = S_0 \Phi(d_1) - Ke^{-rT}\Phi(d_2)$ where $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$, $d_2 = d_1 - \sigma\sqrt{T}$.
- **Risk-Neutral Derivation:** $C = e^{-rT} E^Q[\max(S_T - K, 0)]$ where under $Q$, $S_T = S_0 e^{(r-\sigma^2/2)T + \sigma\sqrt{T}Z}$, $Z \sim N(0,1)$.
- **Greeks:** Sensitivities of the option price to model parameters — the language of risk management.
  - *Delta ($\Delta$):* $\partial V / \partial S$ — hedge ratio.
  - *Gamma ($\Gamma$):* $\partial^2 V / \partial S^2$ — convexity / Delta sensitivity.
  - *Vega ($\mathcal{V}$):* $\partial V / \partial \sigma$ — volatility sensitivity.
  - *Theta ($\Theta$):* $\partial V / \partial t$ — time decay.
  - *Rho ($\rho$):* $\partial V / \partial r$ — interest rate sensitivity.
- **Implied Volatility:** The $\sigma$ that, when plugged into Black-Scholes, reproduces the market price. The "language" traders use to quote options.

### Key Problems and Questions

- **Derive Black-Scholes via Replication:** Form a self-financing portfolio $\Pi = V - \Delta S$. Apply Itô's lemma to make $\Pi$ riskless. Derive the PDE. Then solve it for a European call using the heat equation transformation.
- **Derive Black-Scholes via Risk-Neutral Expectation:** Compute $C = e^{-rT}E^Q[\max(S_T - K, 0)]$ directly by integrating the log-normal distribution. Show every step of the algebra.
- **Implement a Full BS Pricer:** Build a Python class that computes call/put prices, all five Greeks (analytically), and implied volatility (via Newton-Raphson). Validate against known test cases.
- **Put-Call Parity — Proof and Arbitrage:** Prove $C - P = S - Ke^{-rT}$ using no-arbitrage. Given market prices where parity is violated, construct the arbitrage strategy. Compute the profit.
- **Greeks Visualization:** Plot Delta, Gamma, Vega, Theta as functions of (a) spot price, (b) time to expiry, (c) volatility. Show how Greeks behave for ATM, ITM, and OTM options. Explain "Gamma scalping."
- **Delta Hedging Simulation:** Simulate GBM paths. At each rebalance point, delta-hedge a short call position. Track the P&L. Show that hedging error decreases with rebalancing frequency. Compute the hedging error distribution.
- **Implied Volatility — Newton-Raphson:** Given a market price, extract implied vol by solving $\text{BS}(\sigma) = V_{\text{market}}$ using Newton-Raphson with Vega as the derivative. Handle edge cases (deep ITM/OTM). Compare with Brent's method.
- **Volatility Smile and Surface:** Given market option prices across strikes and maturities, compute the implied volatility surface. Plot the smile for a single expiry. Discuss why Black-Scholes produces a flat smile but markets don't.
- **Black-Scholes with Dividends:** Modify the formula for a stock paying continuous dividend yield $q$: replace $S$ with $Se^{-qT}$. Price options on a dividend-paying stock. Show the early exercise boundary for American calls.
- **Limitations of Black-Scholes:** List and explain the key assumptions (constant vol, no jumps, continuous trading, no transaction costs). For each assumption, name the model that relaxes it (local vol, jump-diffusion, discrete hedging, transaction cost models).

---

## 3. Exotic Option Pricing

### Core Concepts

- **Path-Dependent Options:** Payoff depends on the entire path of the underlying, not just the terminal value.
- **Barrier Options:** Activated (knock-in) or extinguished (knock-out) when the underlying hits a barrier level.
- **Asian Options:** Payoff depends on the average price over a period. Arithmetic average has no closed form; geometric average does.
- **Lookback Options:** Payoff depends on the maximum or minimum of the underlying over the life of the option.
- **Digital (Binary) Options:** Pay a fixed amount if the underlying is above/below a strike at expiry. The building blocks of more complex structures.

### Key Problems and Questions

- **Down-and-Out Call — Analytical Formula:** Derive the price of a down-and-out call using the reflection principle for GBM. Show $C_{\text{do}} = C_{\text{BS}} - (S/B)^{1-2r/\sigma^2} C_{\text{BS}}(\text{reflected})$. Implement and verify against Monte Carlo.
- **Knock-In / Knock-Out Parity:** Prove $V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}$. Use this to price a down-and-in put from a vanilla put and a down-and-out put.
- **Asian Option — Geometric Average:** Derive the closed-form price for a geometric average Asian call. Show that the geometric average of a log-normal is log-normal. Use this as a control variate for pricing arithmetic average Asians by Monte Carlo.
- **Asian Option — Monte Carlo with Control Variate:** Price an arithmetic average Asian call by Monte Carlo. Use the geometric average Asian as a control variate. Show the variance reduction factor.
- **Lookback Call — Floating Strike:** The payoff is $S_T - \min_{0 \le t \le T} S_t$. Derive the closed-form price using the joint distribution of $(S_T, \min S_t)$. Implement and verify.
- **Digital Option — Pricing and Hedging:** Price a cash-or-nothing call ($\$1$ if $S_T > K$). Show $V = e^{-rT}\Phi(d_2)$. Compute its Delta — show it approaches a Dirac delta near expiry for ATM options. Discuss the hedging nightmare.
- **Compound Option (Option on an Option):** Price a call on a call using Geske's formula (bivariate normal). Implement and compute the critical stock price at the first expiry.
- **Chooser Option:** At time $t_1$, the holder chooses whether the option is a call or a put (both with the same strike and expiry $T$). Use put-call parity to show this is equivalent to a call plus a put with modified parameters.
- **Rainbow Option — Best of Two Assets:** Payoff is $\max(S_1^T, S_2^T) - K$. Price using the Margrabe/Stulz formula involving the bivariate normal. How does correlation affect the price?
- **Cliquet (Ratchet) Option:** A series of forward-starting at-the-money options. At each reset date, the strike is reset to the current spot. Price by Monte Carlo. Show the sensitivity to the volatility surface (not just a single $\sigma$).

---

## 4. Interest Rate Models

### Core Concepts

- **Short Rate Models:** Model the instantaneous risk-free rate $r_t$ as a stochastic process. Bond prices are $P(t,T) = E^Q[e^{-\int_t^T r_s ds} \mid \mathcal{F}_t]$.
- **Vasicek Model:** $dr_t = \kappa(\theta - r_t)dt + \sigma dW_t$. Mean-reverting, Gaussian, allows negative rates. Bond prices and yields are affine in $r_t$.
- **CIR Model:** $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t} dW_t$. Mean-reverting, non-negative (if Feller condition holds). Also affine.
- **Hull-White Model:** $dr_t = (\theta(t) - \kappa r_t)dt + \sigma dW_t$. Time-dependent $\theta(t)$ allows exact calibration to the initial yield curve.
- **HJM Framework:** Models the entire forward rate curve $f(t,T)$ directly: $df(t,T) = \alpha(t,T)dt + \sigma(t,T)dW_t$. The no-arbitrage drift restriction links $\alpha$ to $\sigma$.
- **LIBOR Market Model (BGM):** Models discrete forward rates $L_i(t)$ (LIBOR rates) directly under their own forward measure. Industry standard for pricing caps, floors, swaptions.

### Key Problems and Questions

- **Vasicek Bond Pricing:** Derive the zero-coupon bond price $P(t,T) = A(t,T)e^{-B(t,T)r_t}$ under the Vasicek model by solving the bond pricing PDE (or using the affine structure). Compute $A$ and $B$ explicitly. Plot the yield curve for different $r_0$.
- **Vasicek — Yield Curve Shapes:** Show that the Vasicek model can produce normal (upward-sloping), inverted, and humped yield curves depending on the parameters. Plot examples of each.
- **CIR Bond Pricing:** Derive the analogous affine bond price for the CIR model. Compare with Vasicek. Show that CIR produces non-negative rates when $2\kappa\theta \ge \sigma^2$.
- **Simulating Short Rate Paths:** Implement Euler-Maruyama simulation for Vasicek and CIR. For CIR, handle the square-root process carefully (truncation or exact simulation via non-central chi-squared). Plot paths and verify the mean-reversion.
- **Hull-White Calibration:** Given a market yield curve (e.g., from Treasury data), calibrate $\theta(t)$ so that the model exactly matches observed zero-coupon bond prices. Implement the calibration and price a European swaption.
- **HJM Drift Restriction:** Derive the HJM no-arbitrage drift condition: $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,s)ds$. Show that Vasicek and CIR are special cases of HJM with specific volatility functions.
- **Cap and Floor Pricing:** A caplet pays $\max(L - K, 0) \cdot \tau$ on a single LIBOR period. Price a caplet under the Vasicek and Black models. Assemble caplets into a cap. Derive the cap-floor parity.
- **Swaption Pricing — Black's Formula:** Price a European payer swaption using Black's formula on the swap rate. Define the annuity measure. Implement and compute the swaption price for given market data.
- **Term Structure of Volatility:** From market cap/swaption prices, extract the term structure of implied volatilities. Plot the vol surface (strike × expiry). Discuss the smile/skew in interest rate markets.
- **Negative Rates and Shifted Models:** When rates go negative (post-2008 world), standard log-normal models break. Implement the shifted Black model: $L_{\text{shifted}} = L + s$ where $s$ is a shift parameter. Reprice caps and compare.

---

## 5. Monte Carlo Methods for Pricing

### Core Concepts

- **Basic Monte Carlo:** Generate $N$ i.i.d. paths of the underlying, compute the payoff on each, and average: $\hat{V} = e^{-rT} \frac{1}{N}\sum_{i=1}^N g(S_T^{(i)})$. Standard error $\propto 1/\sqrt{N}$.
- **Variance Reduction:** Techniques to reduce the standard error without increasing $N$:
  - *Antithetic Variates:* For each path using $Z$, also use $-Z$. Reduces variance when the payoff is monotone in $Z$.
  - *Control Variates:* Use a correlated variable with known expectation to adjust the estimate.
  - *Importance Sampling:* Change the probability measure to sample rare events more frequently.
  - *Stratified Sampling:* Partition the probability space and sample from each stratum.
- **Quasi-Monte Carlo (QMC):** Replace pseudo-random numbers with low-discrepancy sequences (Sobol, Halton). Convergence rate improves to $O(1/N)$ (up from $O(1/\sqrt{N})$).
- **Least-Squares Monte Carlo (LSM):** Longstaff-Schwartz algorithm for American options: at each exercise date, regress continuation value on basis functions of the state. Exercise if payoff > fitted continuation value.

### Key Problems and Questions

- **European Call — Plain Monte Carlo:** Price a European call by simulating $N = 10^3, 10^4, 10^5, 10^6$ GBM paths. Plot the estimate and 95% confidence interval vs. $N$. Compare with the Black-Scholes closed form. Show the $1/\sqrt{N}$ convergence.
- **Antithetic Variates — Variance Reduction:** Implement antithetic variates for a European call. Measure the variance reduction factor. For which payoff shapes (call, put, digital, straddle) is the reduction largest?
- **Control Variate — Geometric Asian:** Price an arithmetic Asian call by Monte Carlo. Use the geometric Asian (closed-form) as a control variate. Implement the optimal control variate coefficient $\beta^*$. Measure the variance reduction (often 10–100×).
- **Importance Sampling — Deep OTM Options:** A European call with $K = 200$, $S_0 = 100$ is deep OTM. Standard Monte Carlo gives huge variance. Implement importance sampling by shifting the drift. Compare the standard error.
- **Quasi-Monte Carlo — Sobol Sequences:** Replace `np.random.normal` with Sobol sequences (via `scipy.stats.qmc`). Price a European call and an Asian option. Show the improved convergence rate vs. pseudo-random Monte Carlo.
- **Longstaff-Schwartz — American Put:** Implement the LSM algorithm for an American put. Use Laguerre polynomials (or simple polynomials) as basis functions. Compare with the binomial tree price. Visualize the estimated exercise boundary.
- **Multi-Asset Monte Carlo — Basket Option:** Price a call on the equally-weighted average of 5 correlated stocks. Generate correlated GBM paths using Cholesky decomposition on the correlation matrix. Compute the price and Greeks by finite differences.
- **Greeks by Monte Carlo:** Compute Delta and Gamma by (a) finite differences (bump-and-reprice), (b) pathwise (IPA) method, (c) likelihood ratio method. Compare bias and variance for each approach.
- **Path-Dependent Exotic — Lookback:** Price a floating-strike lookback put by Monte Carlo. Discuss the discretization bias (monitoring frequency). Show the price converges as monitoring frequency increases.
- **Nested Monte Carlo — CVA/XVA:** Price a portfolio of derivatives and compute the Credit Valuation Adjustment (CVA). This requires "simulation within simulation" — simulate counterparty default times, and at each default time, simulate the portfolio value. Implement a simplified version.

---

## 6. Numerical PDE Methods

### Core Concepts

- **Finite Difference Methods (FDM):** Discretize the Black-Scholes PDE on a grid $(S_i, t_j)$ and approximate derivatives with finite differences.
  - *Explicit:* $V_i^{j} = f(V_{i-1}^{j+1}, V_i^{j+1}, V_{i+1}^{j+1})$. Simple but requires $\Delta t \le \Delta S^2 / (2\sigma^2 S_{\max}^2)$ for stability (CFL condition).
  - *Implicit:* $V_i^{j+1} = f(V_{i-1}^{j}, V_i^{j}, V_{i+1}^{j})$. Unconditionally stable. Requires solving a tridiagonal system at each time step.
  - *Crank-Nicolson:* Average of explicit and implicit. Second-order in time, unconditionally stable. Industry standard.
- **Boundary Conditions:** At $S = 0$: put payoff, call worthless. At $S = S_{\max}$: call $\approx S - Ke^{-r\tau}$, put $\approx 0$. At $t = T$: payoff function.
- **Free-Boundary Problems:** For American options, the PDE becomes a variational inequality: $\max(V_t + \mathcal{L}V, g(S) - V) = 0$ where $g$ is the payoff. The free boundary $S^*(t)$ separates the continuation and exercise regions.

### Key Problems and Questions

- **Explicit FDM — European Call:** Implement the explicit finite difference scheme for the Black-Scholes PDE. Price a European call. Show that it blows up when the CFL condition is violated. Plot the solution surface $V(S, t)$.
- **Implicit FDM — Tridiagonal Solver:** Implement the implicit scheme. At each time step, solve the tridiagonal system using the Thomas algorithm. Compare stability with the explicit scheme. Price European calls and puts.
- **Crank-Nicolson — European Options:** Implement Crank-Nicolson. Show second-order convergence in $\Delta t$. Compare accuracy with explicit and implicit for the same grid size. Price calls, puts, and digitals.
- **American Put — PSOR Method:** Price an American put using Crank-Nicolson with Projected Successive Over-Relaxation (PSOR) to handle the early exercise constraint. Extract the free boundary $S^*(t)$. Plot the exercise boundary and compare with known approximations.
- **Grid Design — Non-Uniform Grids:** Use a sinh or log transformation to concentrate grid points near the strike (where Gamma is largest). Show improved accuracy vs. a uniform grid with the same number of points.
- **Convergence Study:** For a European call, compute the FDM price on grids of increasing refinement. Compute the error vs. Black-Scholes. Verify the convergence order (1st for explicit/implicit, 2nd for Crank-Nicolson in time).
- **Barrier Option — PDE with Absorbing Boundary:** Price a down-and-out call by solving the BS PDE with $V(B, t) = 0$ at the barrier. Compare with the analytical formula. Discuss the difficulty of placing the barrier exactly on a grid point.
- **Two-Asset PDE — ADI Method:** Price a 2D option (e.g., spread option on two assets) by solving the 2D Black-Scholes PDE using Alternating Direction Implicit (ADI) splitting. Discuss the curse of dimensionality.
- **Finite Element Method (FEM) — Basics:** Implement a simple 1D FEM for the Black-Scholes PDE using linear basis functions. Compare with FDM. Discuss advantages (natural handling of irregular domains, adaptivity).
- **Comparison: Tree vs. FDM vs. Monte Carlo:** For the same American put, compute the price using a binomial tree (500 steps), Crank-Nicolson FDM (500 × 500 grid), and LSM Monte Carlo (100,000 paths). Compare accuracy, speed, and ease of computing Greeks.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive closed-form results where they exist (Black-Scholes, barrier formulas, affine bond prices).
> 2. **Numerical implementation** — build pricers using trees, FDM, and Monte Carlo.
> 3. **Visualization** — plot option price surfaces, Greeks, yield curves, convergence studies, and exercise boundaries.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

