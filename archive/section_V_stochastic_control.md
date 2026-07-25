# Section V: Stochastic Control & Dynamic Programming — Detailed Problem List

> *Foundation: Bellman optimality, HJB equations, viscosity solutions*

Stochastic Control is the study of making optimal decisions over time in systems governed by uncertainty. In quantitative finance, this is the mathematical foundation for portfolio optimization, risk management, and derivative pricing. The three pillars — optimal stopping, Markov decision processes, and continuous-time control — each provide a different lens on the same fundamental question: how do you act optimally when the future is random?

---

## 1. Optimal Stopping Theory

Optimal Stopping is a subset of stochastic control concerned with choosing the exact time to take an action (e.g., "stop" or "exercise") to maximize an expected reward or minimize a cost.

### Core Concepts

- **Bellman Equation:** The recursive formula for the optimal value: $V_n(x) = \max\{g(x),\ E[V_{n+1}(X_{n+1}) \mid X_n = x]\}$ where $g(x)$ is the immediate reward and the expectation represents the value of continuing.
- **Backward Induction:** Solving a finite-horizon problem by starting from the terminal time and working toward the present, computing the optimal value at each step.
- **Snell Envelope:** The smallest supermartingale that dominates the reward process $\{g(X_n)\}$. It represents the value of the optimal stopping problem and the optimal stopping time is $\tau^* = \inf\{n : V_n = g(X_n)\}$.
- **Continuation Region vs. Stopping Region:** The state space partitions into a region where it is optimal to continue and a region where it is optimal to stop.
- **Smooth Pasting (High-Contact) Condition:** At the free boundary, the value function meets the payoff function with continuous first derivative — used to pin down the optimal exercise boundary.

### Key Problems and Questions

- **The Cayley-Moser Problem (Dice with $n$ Rolls):** You roll a fair die up to $n$ times. After each roll, you can keep the result or discard it and roll again. What is the optimal strategy? Solve by backward induction. Compute optimal thresholds and expected payoffs for $n = 1, \ldots, 10$. Generalize to an $m$-sided die.
- **The Secretary Problem (The $1/e$ Rule):** You interview $n$ candidates sequentially. After each interview you must immediately accept or reject. You can rank candidates relative to those seen so far. Maximize the probability of selecting the best overall candidate. Show the optimal strategy is: reject the first $n/e$ candidates, then accept the next one that is the best so far. Compute the probability of success for $n = 10, 50, 100$.
- **The House Selling Problem:** You receive i.i.d. offers $X_1, X_2, \ldots$ from a known distribution. Each day you don't sell costs $c$ (maintenance). What is the optimal selling rule? Derive the threshold: sell when $X_n \ge v^*$ where $v^*$ solves $E[\max(X - v^*, 0)] = c$. Implement for $X \sim \text{Uniform}(0,1)$ and $X \sim \text{LogNormal}$.
- **American Option Pricing (Discrete):** A stock follows a binomial tree. An American put option can be exercised at any node. Set up the backward induction on the tree. Compare the American put price with the European put. Compute the early exercise boundary at each time step.
- **The Parking Problem:** You drive down a one-way street toward your destination. Parking spots appear as i.i.d. Bernoulli (occupied/free). If you pass a free spot, you can't go back. You want to minimize the expected walking distance. Derive the optimal strategy using backward induction.
- **The Asset Selling Problem with Recall:** Same as the house selling problem, but you can return to any previous offer (with probability $p$ of it still being available). How does recall change the optimal threshold? Show that the threshold is lower with recall.
- **The Burglar Problem:** A burglar plans a series of heists. Each heist succeeds with probability $p$, yielding reward $r$. If caught (probability $1-p$), all accumulated rewards are lost. How many heists should the burglar attempt? Derive the optimal stopping rule.
- **The Googol Game:** A variant of the Secretary Problem where the number of candidates $N$ is itself random (e.g., $N \sim \text{Poisson}(\lambda)$). Derive the optimal strategy and compare with the classical $1/e$ rule.
- **Optimal Consumption-Investment (Discrete):** At each period, you choose how much to consume vs. invest. Investment returns are i.i.d. Maximize $E[\sum_{t=0}^{T} \beta^t u(c_t)]$ where $u$ is a CRRA utility. Solve by dynamic programming.
- **The Prophet Inequality:** A gambler sees values $X_1, \ldots, X_n$ sequentially (from known distributions). A "prophet" knows all values in advance. Show that there exists a stopping rule guaranteeing at least $E[\max X_i] / 2$ in expectation. Implement the threshold strategy.

---

## 2. Markov Decision Processes (MDP)

MDPs provide a mathematical framework for modeling decision-making where outcomes are partly random and partly under the control of a decision-maker.

### Core Concepts

- **Markov Property:** The future state depends only on the current state and action, not on the history: $P(X_{n+1} \mid X_n, a_n, X_{n-1}, \ldots) = P(X_{n+1} \mid X_n, a_n)$.
- **Components:** States $\mathcal{S}$, actions $\mathcal{A}$, transition probabilities $P(s' | s, a)$, rewards $R(s, a)$, discount factor $\gamma$.
- **Policy ($\pi$):** A mapping from states to actions (deterministic) or to distributions over actions (stochastic).
- **Value Function:** $V^\pi(s) = E^\pi[\sum_{t=0}^{\infty} \gamma^t R(S_t, A_t) \mid S_0 = s]$.
- **Bellman Optimality Equation:** $V^*(s) = \max_a \{R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\}$.
- **Policy Iteration:** Alternate between policy evaluation ($V^\pi$) and policy improvement (greedy w.r.t. $V^\pi$). Converges in finite steps.
- **Value Iteration:** Repeatedly apply the Bellman operator: $V_{k+1}(s) = \max_a \{R(s,a) + \gamma \sum_{s'} P(s'|s,a) V_k(s')\}$.

### Key Problems and Questions

- **The Gambler's Ruin (MDP Formulation):** A gambler can bet any integer amount up to current wealth. $P(\text{win}) = p$. Goal: reach $\$N$. Formulate as an MDP. Use value iteration to find the optimal betting policy for $p = 0.4$ and $p = 0.55$. Visualize the policy.
- **The Ant on a Cube:** An ant at vertex $A$ of a cube moves to a uniformly random adjacent vertex each step. What is the expected number of steps to reach the opposite vertex $G$? Solve by setting up the system of linear equations (exploit symmetry to reduce from 8 states to 4). Verify by simulation.
- **Inventory Control (s, S Policy):** A retailer faces random demand $D \sim \text{Poisson}(\lambda)$ each period. Ordering costs: fixed $K$ + per-unit $c$. Holding cost $h$ per unit per period. Stockout cost $p$ per unit. Formulate as an MDP. Show the optimal policy has the $(s, S)$ form: order up to $S$ when inventory drops below $s$.
- **Grid World Navigation:** A robot on a $5 \times 5$ grid. Each action (N/S/E/W) succeeds with probability 0.8 and moves to a random adjacent cell with probability 0.2. Goal cell gives reward +1, trap cell gives -1. Implement value iteration and policy iteration. Visualize the optimal policy as arrows.
- **Multi-Armed Bandit Problem:** $k$ slot machines with unknown reward distributions. Balance exploration (learning) and exploitation (earning). Implement $\epsilon$-greedy, UCB1, and Thompson Sampling. Compare regret curves over 10,000 rounds.
- **The Coupon Collector as an MDP:** States = number of distinct coupons collected. Action = "draw" (no choice, but formulate as an MDP to practice). Recover $E[T] = nH_n$ via the value function. Compute the variance of the collection time.
- **Mean-Reverting Trading Strategy:** An asset price follows a discrete-time OU process. States = current price level (discretized). Actions = buy/hold/sell. Formulate as an MDP with transaction costs. Use value iteration to find the optimal trading strategy. Backtest on simulated data.
- **Credit Risk Migration:** Moody's/S&P credit rating transition matrix (AAA → AA → A → BBB → ... → Default). Model as an absorbing Markov chain. Compute the probability of default within 5 years from each rating. Price a credit-risky bond.
- **The Knight's Tour on a Chessboard:** A knight starts at a corner of a chessboard and performs a random walk (uniform over legal moves). What is the expected number of moves to return to the starting square? Set up the transition matrix (exploit symmetry) and compute the mean return time from the stationary distribution.
- **Queueing Theory (M/M/1 Queue):** Arrivals: Poisson($\lambda$). Service: Exponential($\mu$). States = number of customers in system. Formulate the optimal admission control problem: reject customers if the queue is too long (each waiting customer costs $c$ per unit time, each served customer earns $r$). Find the optimal threshold.

---

## 3. Continuous-Time Stochastic Control (HJB)

When decisions are made continuously, the discrete Bellman equation evolves into a Partial Differential Equation — the Hamilton-Jacobi-Bellman (HJB) equation.

### Core Concepts

- **Hamilton-Jacobi-Bellman (HJB) Equation:** For a controlled diffusion $dX_t = \mu(X_t, u_t) dt + \sigma(X_t, u_t) dW_t$ with objective $\sup_u E[\int_0^T f(X_t, u_t) dt + g(X_T)]$, the value function $V(t,x)$ satisfies:
  $$\frac{\partial V}{\partial t} + \sup_u \left\{ \mu(x,u) \frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2(x,u) \frac{\partial^2 V}{\partial x^2} + f(x,u) \right\} = 0$$
  with terminal condition $V(T,x) = g(x)$.
- **Verification Theorem:** If a smooth solution to the HJB equation exists and satisfies certain growth conditions, it equals the value function and the maximizing control is optimal.
- **Itô's Lemma:** The "chain rule" for stochastic calculus, essential for deriving the HJB from the dynamic programming principle.
- **Free-Boundary Problems:** Problems where the optimal control involves a boundary between "action" and "no-action" regions, and this boundary is unknown and must be solved as part of the problem.
- **Viscosity Solutions:** When the HJB equation doesn't have a classical (smooth) solution, the correct notion of solution is a viscosity solution. Important for problems with constraints or degenerate diffusions.

### Key Problems and Questions

- **Merton's Portfolio Problem:** An investor allocates wealth between a risk-free asset ($r$) and a risky asset (GBM with drift $\mu$, vol $\sigma$). Maximize $E[u(W_T)]$ with CRRA utility $u(w) = w^{1-\gamma}/(1-\gamma)$. Derive the HJB equation. Show the optimal allocation is constant: $\pi^* = (\mu - r)/(\gamma \sigma^2)$. Verify by simulation.
- **Optimal Execution (Almgren-Chriss):** Liquidate $Q$ shares over time $[0,T]$. Price impact: temporary $\eta \dot{q}$ and permanent $\gamma q$. Minimize $E[\text{cost}] + \lambda \cdot \text{Var}[\text{cost}]$. Derive the optimal trajectory (TWAP-like with risk aversion). Implement and visualize for different $\lambda$ values.
- **Market Making (Avellaneda-Stoikov):** A market maker sets bid/ask quotes. Inventory $q$ follows a jump process driven by order arrivals. The mid-price follows BM. Derive the HJB equation for the market maker's value function. Show the optimal spread depends on inventory and time-to-horizon. Simulate the P&L.
- **Passport Option Pricing:** The holder can trade the underlying freely; at expiry, receives $\max(\text{trading account}, 0)$. The value satisfies a nonlinear PDE. Show that the optimal strategy is "bang-bang" (always fully long or short). Solve numerically.
- **Uncertain Volatility Model:** Volatility is unknown but bounded: $\sigma \in [\sigma_{\min}, \sigma_{\max}]$. A worst-case (robust) pricing approach leads to the Black-Scholes-Barenblatt equation: choose $\sigma$ to maximize/minimize the option value at each point. Implement and compare with standard BS.
- **Stochastic Volatility Control (Heston + Hedging):** Under the Heston model $dS = \mu S dt + \sqrt{v} S dW_1$, $dv = \kappa(\theta - v)dt + \xi\sqrt{v}dW_2$, derive the optimal hedging strategy that accounts for volatility risk. Solve the 2D HJB equation numerically.
- **Optimal Switching (Real Options):** A power plant can be on (earning revenue) or off (saving fuel costs). Switching has a fixed cost $K$. Electricity prices follow an OU process. Formulate as a system of two variational inequalities. Find the optimal switching boundaries $p_{\text{on}}$ and $p_{\text{off}}$.
- **Quickest Disorder Detection (CUSUM):** A process initially has drift $\mu_0$. At an unknown time $\tau$, the drift changes to $\mu_1 > \mu_0$. Detect $\tau$ as quickly as possible while minimizing false alarms. Derive the CUSUM statistic and the optimal threshold. Apply to detecting regime changes in financial time series.
- **Boundary Crossing Probabilities (Barrier Options):** For GBM, compute the probability of hitting a barrier $B$ before expiry $T$ using the reflection principle and Girsanov's theorem. Price a down-and-out call and verify with finite differences.
- **Singular Stochastic Control (Transaction Costs):** An investor rebalances a two-asset portfolio. Each trade incurs proportional transaction costs $\lambda$. The optimal strategy is a "no-trade region" — do nothing while the portfolio weight is within $(l^*, u^*)$ and trade to the boundary when it exits. Derive the free-boundary ODE and solve numerically.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive the answer by hand (Bellman equation, HJB, dynamic programming).
> 2. **Simulation** — verify optimal policies via Monte Carlo simulation of the controlled process.
> 3. **Visualization** — plot value functions, optimal policies/boundaries, convergence of iteration schemes, or P&L distributions.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

