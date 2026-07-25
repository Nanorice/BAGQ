# Section VIII: Calculus, Differential Equations & Analysis — Detailed Problem List

> *Foundation: Real analysis, ODEs, PDEs*

Calculus and differential equations are the analytical engine behind quantitative finance. The Black-Scholes PDE, the Feynman-Kac theorem linking expectations to PDEs, optimization of portfolios via Lagrange multipliers — all require fluency in continuous mathematics. Interview questions range from straightforward ODE solving to recognizing the heat equation inside a pricing problem.

---

## 1. Ordinary Differential Equations (ODEs)

### Core Concepts

- **First-Order Linear ODE:** $y' + p(x)y = q(x)$. Solved via the integrating factor $\mu(x) = e^{\int p(x)dx}$.
- **Separable ODEs:** $y' = f(x)g(y)$ → $\int dy/g(y) = \int f(x)dx$.
- **Second-Order Linear ODE (Constant Coefficients):** $ay'' + by' + cy = 0$. Characteristic equation $ar^2 + br + c = 0$ gives solutions as exponentials, sines/cosines, or their products depending on the discriminant.
- **Systems of ODEs:** $\mathbf{x}' = A\mathbf{x}$. Solution: $\mathbf{x}(t) = e^{At}\mathbf{x}_0$. Eigenvalues of $A$ determine stability (stable if all $\text{Re}(\lambda_i) < 0$).
- **Variation of Parameters:** General method for non-homogeneous ODEs. Find the homogeneous solution first, then vary the constants.

### Key Problems and Questions

- **Exponential Growth/Decay — Continuously Compounded Interest:** Solve $dV/dt = rV$ with $V(0) = V_0$. Derive $V(t) = V_0 e^{rt}$. Extend to time-varying rates $r(t)$: $V(t) = V_0 \exp(\int_0^t r(s)ds)$.
- **Mean-Reverting ODE (Deterministic OU):** Solve $dx/dt = \kappa(\theta - x)$ with $x(0) = x_0$. Show $x(t) = \theta + (x_0 - \theta)e^{-\kappa t}$. Plot for various $\kappa$. This is the deterministic skeleton of the Ornstein-Uhlenbeck process.
- **Logistic Growth — Population/Market Saturation:** Solve $dN/dt = rN(1 - N/K)$. Derive the logistic function $N(t) = K / (1 + (K/N_0 - 1)e^{-rt})$. Apply to modeling market adoption of a new product.
- **Second-Order ODE — Damped Oscillator:** Solve $x'' + 2\gamma x' + \omega_0^2 x = 0$. Classify the solutions: overdamped ($\gamma > \omega_0$), critically damped ($\gamma = \omega_0$), underdamped ($\gamma < \omega_0$). Plot all three cases. Relate to mean-reversion speed in finance.
- **Systems of ODEs — Two-Asset Portfolio:** A portfolio of two assets has values $V_1, V_2$ evolving as $\mathbf{V}' = A\mathbf{V}$ where $A$ captures growth and cross-effects. Solve via eigendecomposition of $A$. Determine when the system is stable.
- **The Perpetual Annuity ODE:** A perpetuity pays $c$ per unit time continuously. Its present value satisfies $rV = c$ (trivial) but for a growing perpetuity at rate $g$: $rV - gV = c$, so $V = c/(r-g)$. Derive from the ODE $V' = rV - c e^{gt}$.
- **Riccati Equation in Finance:** The bond pricing ODE under affine models is a Riccati equation: $B'(t) = 1 - \kappa B(t) + \frac{1}{2}\sigma^2 B(t)^2$. Solve for the Vasicek model ($\sigma$ coefficient of $B^2$ is 0) and the CIR model (full Riccati). Compare solutions.
- **Phase Portraits:** For the 2D system $x' = y$, $y' = -x - \epsilon y$, draw the phase portrait for $\epsilon = 0$ (center), $\epsilon = 0.5$ (stable spiral), $\epsilon = -0.5$ (unstable spiral). Relate to oscillatory vs. damped price behavior.
- **Green's Function for a First-Order ODE:** Solve $y' + ay = \delta(t - t_0)$ (impulse response). Show $y(t) = e^{-a(t-t_0)} H(t-t_0)$ where $H$ is the Heaviside function. Interpret as the response of a discounting process to a single cash flow.
- **Stability Analysis — Linearization:** Given a nonlinear ODE $x' = f(x)$, find equilibria ($f(x^*) = 0$), linearize ($x' \approx f'(x^*)(x - x^*)$), and determine stability. Apply to a simple model of supply-demand equilibrium.

---

## 2. Partial Differential Equations (PDEs)

### Core Concepts

- **Heat Equation:** $\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}$. Describes diffusion. The Black-Scholes PDE transforms into the heat equation under a change of variables.
- **Black-Scholes PDE:** $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$. Backward in time, second-order, parabolic.
- **Feynman-Kac Formula:** If $u(t,x)$ satisfies $u_t + \mu u_x + \frac{1}{2}\sigma^2 u_{xx} - ru = 0$ with terminal condition $u(T,x) = g(x)$, then $u(t,x) = E^Q[e^{-r(T-t)} g(X_T) \mid X_t = x]$ where $dX = \mu dt + \sigma dW$. The bridge between PDEs and expectations.
- **Separation of Variables:** Assume $u(x,t) = X(x)T(t)$ and reduce the PDE to two ODEs. Works for simple geometries and boundary conditions.
- **Fourier Transform Methods:** Transform the PDE in $x$ to an ODE in $t$ (in Fourier space), solve, then inverse-transform. Powerful for infinite domains.
- **Green's Function for the Heat Equation:** $G(x,t) = \frac{1}{\sqrt{4\pi Dt}} \exp\left(-\frac{x^2}{4Dt}\right)$. The solution is $u(x,t) = \int G(x-y, t) u_0(y) dy$ — convolution with the initial condition.

### Key Problems and Questions

- **Heat Equation — Fundamental Solution:** Verify that $G(x,t) = \frac{1}{\sqrt{4\pi Dt}} e^{-x^2/(4Dt)}$ satisfies the heat equation. Show $\int_{-\infty}^{\infty} G(x,t) dx = 1$ for all $t > 0$. Interpret as a spreading Gaussian.
- **BS PDE → Heat Equation Transformation:** Starting from the Black-Scholes PDE, apply the substitutions $x = \ln(S/K)$, $\tau = \frac{1}{2}\sigma^2(T-t)$, $u = e^{r(T-t)} V / K$. Show the PDE reduces to the standard heat equation $u_\tau = u_{xx}$ (up to a drift term). This is how the BS formula is derived analytically.
- **Feynman-Kac — Verification:** Consider the PDE $u_t + \frac{1}{2}\sigma^2 u_{xx} = 0$ with $u(T,x) = x^2$. Solve analytically ($u(t,x) = x^2 + \sigma^2(T-t)$). Verify by computing $E[W_T^2 \mid W_t = x] = x^2 + (T-t)$ (with $\sigma = 1$).
- **Separation of Variables — Vibrating String:** Solve the wave equation $u_{tt} = c^2 u_{xx}$ on $[0, L]$ with $u(0,t) = u(L,t) = 0$. Find the normal modes. While not directly financial, this builds PDE intuition.
- **Fourier Transform — Option Pricing (Carr-Madan):** Use the Fourier transform to price a European call: $C = \frac{e^{-\alpha \ln K}}{\pi} \int_0^\infty e^{-iv\ln K} \psi(v) dv$ where $\psi$ is the characteristic function of $\ln S_T$. Implement via FFT. Price under Black-Scholes and Heston models.
- **Black-Scholes PDE — Boundary Conditions:** For a European call, specify boundary conditions: $V(0,t) = 0$, $V(S,t) \to S - Ke^{-r(T-t)}$ as $S \to \infty$, $V(S,T) = \max(S-K, 0)$. Show these are consistent with the BS formula.
- **American Option PDE — Free Boundary:** The American put satisfies the BS PDE in the continuation region $S > S^*(t)$ with the constraint $V \ge (K-S)^+$. At the free boundary: $V(S^*,t) = K - S^*$ (value matching) and $V_S(S^*, t) = -1$ (smooth pasting). Explain why these two conditions are needed and what they mean.
- **Maximum Principle:** For the heat equation, the maximum of $u$ on a bounded domain is attained on the boundary (initial or spatial boundary), not in the interior. Prove for a simple case. Apply to show that an option price is bounded by its boundary values.
- **PDE for a Barrier Option:** Modify the BS PDE for a down-and-out call: solve on $S > B$ with $V(B,t) = 0$. Implement a finite difference solver and compare with the analytical formula (images method).
- **Multi-Dimensional PDE — Basket Option:** The 2-asset BS PDE: $V_t + \frac{1}{2}\sigma_1^2 S_1^2 V_{S_1 S_1} + \rho \sigma_1 \sigma_2 S_1 S_2 V_{S_1 S_2} + \frac{1}{2}\sigma_2^2 S_2^2 V_{S_2 S_2} + rS_1 V_{S_1} + rS_2 V_{S_2} - rV = 0$. Discuss the curse of dimensionality. Why do practitioners prefer Monte Carlo for $d > 3$?

---

## 3. Optimization & Calculus of Variations

### Core Concepts

- **Unconstrained Optimization:** $\nabla f(x^*) = 0$ (first-order condition). $\nabla^2 f(x^*)$ positive definite (second-order sufficient condition for a minimum).
- **Lagrange Multipliers:** Optimize $f(x)$ subject to $g(x) = 0$: solve $\nabla f = \lambda \nabla g$ and $g(x) = 0$. The multiplier $\lambda$ is the shadow price of the constraint.
- **KKT Conditions:** For inequality-constrained optimization $\min f(x)$ s.t. $g_i(x) \le 0$: stationarity, primal feasibility, dual feasibility ($\lambda_i \ge 0$), complementary slackness ($\lambda_i g_i = 0$).
- **Convex Optimization:** If $f$ is convex and the constraints define a convex set, every local minimum is global. Many financial optimization problems (mean-variance, risk budgeting) are convex.
- **Euler-Lagrange Equation:** For functionals $J[y] = \int_a^b L(x, y, y') dx$, the minimizer satisfies $\frac{\partial L}{\partial y} - \frac{d}{dx}\frac{\partial L}{\partial y'} = 0$. The continuous-time analogue of "set the derivative to zero."

### Key Problems and Questions

- **Markowitz Optimization — Lagrange Multipliers:** Minimize $\frac{1}{2}w^T \Sigma w$ subject to $w^T \mu = \mu_p$ and $w^T \mathbf{1} = 1$. Set up the Lagrangian. Derive the closed-form solution using matrix algebra. Compute the efficient frontier.
- **Maximum Entropy Distribution:** Find the distribution on $\{1, \ldots, n\}$ that maximizes Shannon entropy $H = -\sum p_i \ln p_i$ subject to $\sum p_i = 1$ and a mean constraint $\sum x_i p_i = \mu$. Solve using Lagrange multipliers. Show the solution is an exponential (Boltzmann) distribution.
- **Log-Utility Portfolio — Kelly Criterion:** Maximize $E[\ln(1 + f \cdot R)]$ where $f$ is the fraction bet and $R$ is the return. Derive the optimal Kelly fraction for a binary bet. Extend to continuous returns. Show the connection to information theory.
- **KKT — Portfolio with No Short Sales:** Minimize $\frac{1}{2}w^T \Sigma w$ subject to $w^T \mu \ge \mu_p$, $w \ge 0$, $w^T \mathbf{1} = 1$. Write the KKT conditions. Show that some weights will be exactly 0 (the KKT complementary slackness condition). Solve numerically with `cvxpy`.
- **Convexity Proof — Variance is Convex:** Prove that $f(w) = w^T \Sigma w$ is convex for PSD $\Sigma$. Show the Hessian is $2\Sigma \succeq 0$. Why does this guarantee a unique minimum-variance portfolio?
- **Newton's Method for Optimization:** Implement Newton's method: $x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$. Apply to minimizing $f(x,y) = (x-1)^2 + 10(y-x^2)^2$ (Rosenbrock). Compare convergence with gradient descent.
- **Euler-Lagrange — Brachistochrone:** Find the curve connecting $(0,0)$ to $(x_1, y_1)$ along which a bead slides fastest under gravity. Set up the functional and derive the Euler-Lagrange equation. Show the solution is a cycloid. This builds intuition for calculus of variations in control theory.
- **Optimal Consumption — Euler Equation:** An agent maximizes $\int_0^T e^{-\rho t} u(c_t) dt$ subject to the budget constraint $dW = (rW - c)dt$. Derive the Euler equation $u'(c_t) = e^{-(\rho - r)t} u'(c_0)$ using calculus of variations. For CRRA utility, solve for the optimal consumption path.
- **Duality in Linear Programming:** Formulate a simple portfolio allocation as an LP. Write the dual problem. Verify strong duality (primal optimal = dual optimal). Interpret the dual variables as shadow prices of constraints.
- **Gradient Descent — Convergence Rates:** Implement gradient descent for a quadratic $f(x) = \frac{1}{2}x^T A x - b^T x$. Show the convergence rate depends on the condition number $\kappa(A)$. Compare standard gradient descent, gradient descent with momentum, and conjugate gradient. Relate to optimizing portfolio risk.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive closed-form results by hand (Lagrangians, Euler-Lagrange, KKT conditions).
> 2. **Numerical implementation** — build solvers using `scipy.optimize`, `cvxpy`, or hand-coded Newton/gradient methods.
> 3. **Visualization** — plot solution surfaces, convergence trajectories, efficient frontiers, and phase portraits.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

