# Section IV: Continuous-Time Stochastic Processes — Detailed Problem List

> *Foundation: Brownian motion, filtrations, martingale theory, Itô calculus*

Continuous-time stochastic processes are the mathematical engine of modern quantitative finance. Brownian motion models asset price fluctuations, Itô calculus provides the tools to differentiate and integrate in the presence of randomness, and martingale theory underpins the no-arbitrage framework. Every derivatives pricer, risk model, and trading strategy rests on these foundations.

---

## 1. Brownian Motion (Wiener Process)

### Core Concepts

- **Definition:** A stochastic process $\{W_t\}_{t \ge 0}$ with: (i) $W_0 = 0$, (ii) independent increments, (iii) $W_t - W_s \sim N(0, t-s)$ for $t > s$, (iv) continuous paths a.s.
- **Properties:** $E[W_t] = 0$, $\text{Var}(W_t) = t$, $\text{Cov}(W_s, W_t) = \min(s,t)$.
- **Quadratic Variation:** $\langle W \rangle_t = t$. Over $[0,t]$, $\sum (W_{t_{i+1}} - W_{t_i})^2 \to t$ as the partition refines. This is why $dW^2 = dt$ in Itô calculus.
- **Non-Differentiability:** Brownian paths are continuous but nowhere differentiable a.s.
- **Reflection Principle:** $P(\max_{0 \le s \le t} W_s \ge a) = 2P(W_t \ge a)$ for $a > 0$. Used for barrier option pricing.
- **Geometric Brownian Motion (GBM):** $S_t = S_0 \exp((\mu - \sigma^2/2)t + \sigma W_t)$, the standard model for stock prices.
- **Donsker's Theorem (Functional CLT):** A scaled random walk converges in distribution to Brownian motion.

### Key Problems and Questions

- **Simulating Brownian Motion:** Generate and plot sample paths of $W_t$ on $[0,1]$ with $n = 100, 1000, 10000$ time steps. Verify that the variance of the endpoint grows linearly with $t$.
- **Quadratic Variation — Numerical Verification:** Simulate a Brownian path and compute $\sum_{i} (W_{t_{i+1}} - W_{t_i})^2$ for partitions of increasing fineness. Show it converges to $T$. Then compute the ordinary variation $\sum |W_{t_{i+1}} - W_{t_i}|$ — show it diverges.
- **Maximum of Brownian Motion:** Using the reflection principle, derive $P(\max_{0 \le s \le t} W_s \ge a) = 2\Phi(-a/\sqrt{t})$ where $\Phi$ is the standard normal CDF. Verify by simulation. What is $E[\max_{0 \le s \le t} W_s]$?
- **Brownian Bridge:** A Brownian bridge is $W_t$ conditioned on $W_T = 0$ (or some other value). Derive $B_t = W_t - (t/T)W_T$. Show $B_t \sim N(0, t(T-t)/T)$. Simulate and plot.
- **Geometric Brownian Motion — Stock Price Simulation:** Simulate GBM paths for $S_0 = 100$, $\mu = 0.1$, $\sigma = 0.3$ over 1 year. Plot 100 paths. Compute the distribution of $S_T$ and verify it matches the log-normal distribution.
- **GBM — The Log-Normal Trap:** The expected value of $S_T$ under GBM is $S_0 e^{\mu T}$, but the median is $S_0 e^{(\mu - \sigma^2/2)T}$. For what $\sigma$ does the median path decrease even when $\mu > 0$? Visualize.
- **Donsker's Theorem — Simulation:** Scale a simple random walk: $W_n^{(N)}(t) = \frac{1}{\sqrt{N}} S_{\lfloor Nt \rfloor}$ where $S_k = \sum_{i=1}^k X_i$ with $X_i = \pm 1$ equally likely. Simulate for $N = 10, 100, 1000$ and overlay with true Brownian paths.
- **First Passage Time of Brownian Motion:** For standard Brownian motion, derive the density of $\tau_a = \inf\{t \ge 0 : W_t = a\}$ for $a > 0$. (Answer: inverse Gaussian / Lévy distribution.) Show $E[\tau_a] = \infty$.
- **Brownian Motion with Drift — Hitting Probabilities:** For $X_t = \mu t + \sigma W_t$ with $\mu < 0$, what is $P(\max_{t \ge 0} X_t \ge a)$? Derive using the exponential martingale. Relate to ruin probability.
- **Brownian Scaling and Self-Similarity:** Prove that $\{c^{-1/2} W_{ct}\}_{t \ge 0}$ is also a standard Brownian motion. Use this to show that the distribution of $\max_{0 \le s \le t} W_s$ scales as $\sqrt{t}$.

---

## 2. Martingale Theory

### Core Concepts

- **Martingale:** An adapted process $\{M_t\}$ with $E[|M_t|] < \infty$ and $E[M_t \mid \mathcal{F}_s] = M_s$ for $s \le t$. Intuitively: a "fair game."
- **Submartingale / Supermartingale:** Replace $=$ with $\ge$ (submartingale, tends to increase) or $\le$ (supermartingale, tends to decrease).
- **Optional Stopping Theorem (OST):** If $\tau$ is a bounded stopping time and $\{M_t\}$ is a martingale, then $E[M_\tau] = E[M_0]$. Fails if $\tau$ is unbounded without additional conditions (e.g., uniform integrability).
- **Doob's Maximal Inequality:** $P(\max_{0 \le k \le n} M_k \ge \lambda) \le E[M_n^+] / \lambda$ for a submartingale.
- **Martingale Convergence Theorem:** A non-negative supermartingale converges a.s. A uniformly integrable martingale converges a.s. and in $L^1$.
- **Martingale Representation Theorem:** Any martingale adapted to the Brownian filtration can be written as a stochastic integral: $M_t = M_0 + \int_0^t H_s \, dW_s$.

### Key Problems and Questions

- **Brownian Motion is a Martingale:** Prove that $W_t$ is a martingale w.r.t. its natural filtration. Also prove that $W_t^2 - t$ is a martingale.
- **Exponential Martingale:** Show that $M_t = \exp(\theta W_t - \theta^2 t / 2)$ is a martingale for any $\theta \in \mathbb{R}$. Use this to derive hitting probabilities for Brownian motion with drift.
- **Optional Stopping — Gambler's Ruin:** A gambler plays a fair game starting with $\$a$. Use the martingale $M_n = S_n$ (wealth) and OST to find the probability of reaching $\$N$ before $\$0$. Then use $M_n = S_n^2 - n$ to find the expected duration.
- **Optional Stopping — When It Fails:** Consider $W_t$ and $\tau = \inf\{t : W_t = 1\}$. We have $E[W_\tau] = 1 \neq 0 = E[W_0]$. Why doesn't OST apply? (Because $E[\tau] = \infty$ and the stopped martingale is not UI.)
- **Wald's Equation via Martingales:** If $\{X_i\}$ are i.i.d. with mean $\mu$ and $N$ is a stopping time with $E[N] < \infty$, prove $E[\sum_{i=1}^N X_i] = \mu \cdot E[N]$ using the martingale $M_n = S_n - n\mu$.
- **Doob's Decomposition:** Every submartingale $\{X_n\}$ can be uniquely decomposed as $X_n = M_n + A_n$ where $M_n$ is a martingale and $A_n$ is a predictable increasing process. Compute this decomposition for $X_n = W_n^2$.
- **Martingale Betting Strategy — The Doubling Strategy:** You double your bet after each loss. Show that the wealth process is a supermartingale (with a finite bankroll). Prove you can't beat a fair game in the long run.
- **Azuma-Hoeffding Inequality:** If $\{M_n\}$ is a martingale with bounded differences $|M_n - M_{n-1}| \le c$, then $P(M_n - M_0 \ge t) \le \exp(-t^2 / (2nc^2))$. Apply to bound the deviation of a random walk from its mean.
- **Martingale in Finance — Discounted Stock Price:** Under the risk-neutral measure, the discounted stock price $e^{-rt}S_t$ is a martingale. Verify this for GBM with drift $r$. Use this to price a European call option.
- **Lévy's Characterization:** Prove (or verify by simulation) that if $\{M_t\}$ is a continuous martingale with $\langle M \rangle_t = t$, then $M_t$ is a standard Brownian motion. This is the converse of "BM is a martingale."

---

## 3. Itô Calculus & Stochastic Differential Equations (SDEs)

### Core Concepts

- **Itô Integral:** $\int_0^T f(t) \, dW_t$ — defined as a limit of sums $\sum f(t_i)(W_{t_{i+1}} - W_{t_i})$ where $f$ is evaluated at the left endpoint.
- **Itô Isometry:** $E\left[\left(\int_0^T f(t) \, dW_t\right)^2\right] = \int_0^T E[f(t)^2] \, dt$.
- **Itô's Lemma (Stochastic Chain Rule):** If $dX_t = \mu \, dt + \sigma \, dW_t$ and $f \in C^2$, then $df(X_t) = f'(X_t) dX_t + \frac{1}{2} f''(X_t) \sigma^2 dt$. The extra $\frac{1}{2} f'' \sigma^2 dt$ term is the Itô correction.
- **Itô vs. Stratonovich:** Itô uses left-endpoint evaluation; Stratonovich uses midpoint. They give different results. Finance uses Itô; physics often uses Stratonovich.
- **Key SDEs:**
  - *GBM:* $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, solution $S_t = S_0 e^{(\mu - \sigma^2/2)t + \sigma W_t}$.
  - *Ornstein-Uhlenbeck:* $dX_t = \theta(\mu - X_t) dt + \sigma \, dW_t$, mean-reverting.
  - *CIR (Cox-Ingersoll-Ross):* $dX_t = \kappa(\theta - X_t) dt + \sigma \sqrt{X_t} \, dW_t$, non-negative.

### Key Problems and Questions

- **Itô's Lemma — Deriving the GBM Solution:** Starting from $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, apply Itô's lemma to $f(S) = \ln S$ to derive the explicit solution $S_t = S_0 \exp((\mu - \sigma^2/2)t + \sigma W_t)$.
- **Itô's Lemma — $W_t^2$:** Apply Itô's lemma to $f(x) = x^2$ with $X_t = W_t$. Show $d(W_t^2) = 2W_t \, dW_t + dt$. Integrate to get $W_t^2 = 2\int_0^t W_s \, dW_s + t$. Verify this implies $\int_0^t W_s \, dW_s = \frac{1}{2}(W_t^2 - t)$.
- **Itô's Lemma — Product Rule:** If $dX = \mu_X dt + \sigma_X dW$ and $dY = \mu_Y dt + \sigma_Y dW$ (same Brownian motion), derive $d(XY)$ using Itô's lemma. Show the extra cross-term $\sigma_X \sigma_Y dt$ (the "Itô product rule").
- **Ornstein-Uhlenbeck Process — Solution and Moments:** Solve $dX_t = \theta(\mu - X_t) dt + \sigma dW_t$ explicitly using the integrating factor $e^{\theta t}$. Compute $E[X_t]$ and $\text{Var}(X_t)$. Show mean-reversion: $E[X_t] \to \mu$ as $t \to \infty$. Simulate and overlay with the theoretical mean ± 2 s.d.
- **CIR Process — Non-Negativity:** Show that the CIR process $dX_t = \kappa(\theta - X_t)dt + \sigma\sqrt{X_t} \, dW_t$ stays non-negative if the Feller condition $2\kappa\theta \ge \sigma^2$ holds. Simulate paths for parameters satisfying and violating the condition.
- **Simulating SDEs — Euler-Maruyama Method:** Implement the Euler-Maruyama discretization for GBM, OU, and CIR. Compare with exact solutions (where available). Measure strong and weak convergence rates.
- **Milstein Scheme:** Implement the Milstein discretization for GBM: $S_{n+1} = S_n + \mu S_n \Delta t + \sigma S_n \Delta W_n + \frac{1}{2}\sigma^2 S_n((\Delta W_n)^2 - \Delta t)$. Show it achieves strong order 1.0 convergence vs. Euler's 0.5.
- **Itô Isometry — Verification:** Simulate $\int_0^1 W_t \, dW_t$ using Riemann-sum approximations. Verify $E\left[\left(\int_0^1 W_t \, dW_t\right)^2\right] = \int_0^1 E[W_t^2] \, dt = 1/2$.
- **Stochastic Exponential (Doléans-Dade):** Define $\mathcal{E}(M)_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$ for a continuous local martingale $M_t$. Show $d\mathcal{E}(M)_t = \mathcal{E}(M)_t \, dM_t$. Apply to $M_t = \sigma W_t$ to recover GBM.
- **Black-Scholes PDE via Itô:** Form a self-financing portfolio $\Pi = V - \Delta S$ (option minus delta shares). Apply Itô's lemma to make $\Pi$ riskless. Derive the Black-Scholes PDE: $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$.

---

## 4. Poisson Processes & Jump Processes

### Core Concepts

- **Poisson Process:** A counting process $\{N_t\}_{t \ge 0}$ with: (i) $N_0 = 0$, (ii) independent increments, (iii) $N_t - N_s \sim \text{Poisson}(\lambda(t-s))$ for a homogeneous process.
- **Inter-Arrival Times:** The times between events are i.i.d. $\text{Exp}(\lambda)$.
- **Inhomogeneous Poisson Process:** Rate $\lambda(t)$ varies with time. $N_t - N_s \sim \text{Poisson}(\int_s^t \lambda(u) du)$.
- **Compound Poisson Process:** $X_t = \sum_{i=1}^{N_t} Y_i$ where $\{Y_i\}$ are i.i.d. jump sizes. Models aggregate claims (insurance) or aggregate jumps (asset prices).
- **Jump-Diffusion (Merton):** $dS_t / S_t = (\mu - \lambda k) dt + \sigma dW_t + J_t dN_t$ where $J_t$ is a random jump size. Combines continuous GBM with discrete jumps.
- **Lévy Process:** A process with stationary, independent increments and càdlàg paths. Generalizes both Brownian motion and Poisson processes.

### Key Problems and Questions

- **Simulating a Poisson Process:** Implement two methods: (1) generate inter-arrival times as $\text{Exp}(\lambda)$, (2) on a grid of width $\Delta t$, flip Bernoulli($\lambda \Delta t$) coins. Compare. Plot $N_t$ vs. $t$.
- **Superposition and Thinning:** Two independent Poisson processes with rates $\lambda_1, \lambda_2$: show their superposition is Poisson with rate $\lambda_1 + \lambda_2$. Conversely, thin a rate-$\lambda$ process: each event is kept with probability $p$. Show the result is Poisson with rate $\lambda p$.
- **Conditional Distribution of Arrival Times:** Given $N_T = n$ events in $[0, T]$, show that the event times $(T_1, \ldots, T_n)$ are distributed as the order statistics of $n$ i.i.d. $\text{Uniform}(0, T)$ random variables. Simulate and verify.
- **Compound Poisson — Insurance Claims:** Claims arrive as a Poisson process with rate $\lambda = 10$/year. Claim sizes are i.i.d. $\text{LogNormal}(\mu, \sigma^2)$. Simulate total claims over 1 year. Compute the probability of exceeding a threshold (ruin probability approximation).
- **Inhomogeneous Poisson — Time-Varying Intensity:** Model customer arrivals at a store with rate $\lambda(t) = 5 + 3\sin(2\pi t / 24)$ (peak at hour 6). Simulate using thinning (Lewis-Shedler algorithm). Plot arrival rate vs. time.
- **Merton's Jump-Diffusion Model:** Simulate stock price paths under Merton's jump-diffusion: $dS/S = \mu dt + \sigma dW + J dN$ with $\ln(1+J) \sim N(\mu_J, \sigma_J^2)$. Compare path behavior with pure GBM. Price a European call option by Monte Carlo.
- **Jump-Diffusion — Implied Volatility Smile:** Price European options at multiple strikes using Merton's model. Compute the implied volatility for each strike. Show that the model produces a volatility smile, unlike pure Black-Scholes.
- **Compensated Poisson Process:** Define $\tilde{N}_t = N_t - \lambda t$. Prove this is a martingale. Show it has quadratic variation $\langle \tilde{N} \rangle_t = \lambda t$. This is the jump analogue of Brownian motion.
- **Kou's Double-Exponential Jump-Diffusion:** Model jump sizes as double-exponential (asymmetric up/down jumps). Derive the characteristic function. Price barrier options using this model (semi-analytical via Laplace transforms).
- **Lévy-Itô Decomposition (Conceptual):** Every Lévy process can be decomposed into a deterministic drift, a Brownian component, and a pure jump component (compound Poisson for large jumps + compensated small jumps). Simulate a Variance Gamma process ($\Gamma$-subordinated Brownian motion) and visualize its path vs. Brownian motion.

---

## 5. Stopping Times & First-Passage Problems (Continuous)

### Core Concepts

- **Stopping Time:** A random variable $\tau$ such that $\{\tau \le t\} \in \mathcal{F}_t$ for all $t$ — the decision to stop depends only on information available up to time $t$.
- **First-Passage Time:** $\tau_a = \inf\{t \ge 0 : X_t = a\}$ — the first time a process hits level $a$.
- **Distribution of $\tau_a$ for BM:** For standard BM, $\tau_a$ has an inverse Gaussian (Lévy) distribution with density $f(t) = \frac{|a|}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right)$ for $t > 0$.
- **BM with Drift:** For $X_t = \mu t + W_t$, the Laplace transform of $\tau_a$ is $E[e^{-s\tau_a}] = \exp(a\mu - a\sqrt{\mu^2 + 2s})$ for $a > 0$ and $\mu^2 + 2s > 0$.
- **Connection to Barrier Options:** The price of a knock-out barrier option depends on $P(\max_{0 \le s \le T} S_s \ge B)$, which is a first-passage problem under GBM.

### Key Problems and Questions

- **First-Passage Time of Standard BM:** Derive the density of $\tau_a = \inf\{t : W_t = a\}$ using the reflection principle. Verify by simulation: generate many BM paths and record the first time each crosses $a = 1$. Plot the histogram vs. the theoretical density.
- **Expected First-Passage Time — BM with Drift:** For $X_t = \mu t + W_t$ with $\mu > 0$, derive $E[\tau_a] = a/\mu$ for $a > 0$. What happens when $\mu \le 0$? Verify by simulation.
- **Two-Sided Barrier — Exit Time:** For standard BM starting at $x \in (0, L)$, what is $E[\tau]$ where $\tau = \inf\{t : W_t \notin (0, L)\}$? What is the probability of exiting at $L$ vs. $0$? Solve the BVP $\frac{1}{2}u''(x) = -1$ with $u(0) = u(L) = 0$.
- **Barrier Option Pricing — Knock-Out Call:** Price a European up-and-out call option with strike $K$ and barrier $B > K$ using the reflection principle. Compare with Monte Carlo simulation. How sensitive is the price to the barrier level?
- **Inverse Gaussian Distribution — Properties:** Show that the first-passage time $\tau_a$ for BM with drift $\mu > 0$ follows the Inverse Gaussian distribution $IG(a/\mu, a^2)$. Compute its mean, variance, and MGF. Fit to simulated data.
- **Double Barrier — Range of BM:** For BM starting at 0, compute $P(L \le W_t \le U \text{ for all } t \in [0,T])$ for barriers $L < 0 < U$. This requires an infinite series (images method). Implement and compare with simulation.
- **Hitting Time of GBM:** For $S_t = S_0 e^{(\mu-\sigma^2/2)t + \sigma W_t}$, the first time $S_t$ hits level $B$ reduces to a first-passage problem for BM with drift. Derive and simulate.
- **Optimal Stopping and Free Boundaries:** The American put option defines a free boundary $S^*(t)$ below which it is optimal to exercise. Set up the free-boundary ODE for the perpetual American put: $\frac{1}{2}\sigma^2 S^2 V'' + rSV' - rV = 0$ for $S > S^*$, with value matching and smooth pasting at $S^*$. Solve for $S^*$ and the option price.
- **Occupation Times — Time Spent Above Zero:** For standard BM on $[0,T]$, the fraction of time spent above zero follows the arcsine distribution: $P(\text{fraction} \le x) = \frac{2}{\pi}\arcsin(\sqrt{x})$. Simulate and verify. Explain why BM spends most of its time on one side (despite being symmetric).
- **Drawdown and Running Maximum:** Define the drawdown $D_t = \max_{0 \le s \le t} X_s - X_t$ for BM with drift. Compute $P(\max_{t \ge 0} D_t > d)$ for $\mu > 0$. This is the ruin probability for a trader whose strategy follows a drifted BM. Simulate and relate to maximum drawdown in trading.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive closed-form results where possible (Itô's lemma, reflection principle, Laplace transforms).
> 2. **Simulation** — verify via Monte Carlo simulation of paths (Euler-Maruyama, exact methods).
> 3. **Visualization** — plot sample paths, histograms of first-passage times, convergence of discretization schemes, or implied volatility surfaces.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

