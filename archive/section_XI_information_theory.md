# Section XI: Information Theory & Entropy — Detailed Problem List

> *Foundation: Shannon entropy, KL-divergence, mutual information*

Information theory, originally developed for communication systems, has deep connections to statistics, machine learning, and finance. Entropy quantifies uncertainty, KL-divergence measures the "cost" of using the wrong model, and the Kelly criterion — derived from information-theoretic principles — is the optimal betting strategy. These concepts appear in quant interviews at the intersection of probability, estimation, and decision-making.

---

## 1. Entropy & Information Content

### Core Concepts

- **Shannon Entropy:** $H(X) = -\sum_{x} p(x) \log_2 p(x)$ (bits) or $-\sum p(x) \ln p(x)$ (nats). Measures the average "surprise" or uncertainty of a random variable.
- **Properties of Entropy:**
  - $H(X) \ge 0$, with equality iff $X$ is deterministic.
  - $H(X) \le \log |\mathcal{X}|$, with equality iff $X$ is uniform (maximum entropy).
  - Adding constraints reduces entropy.
- **Joint Entropy:** $H(X, Y) = -\sum_{x,y} p(x,y) \log p(x,y)$.
- **Conditional Entropy:** $H(Y|X) = H(X,Y) - H(X)$. The remaining uncertainty in $Y$ after observing $X$.
- **Chain Rule:** $H(X,Y) = H(X) + H(Y|X)$.
- **Differential Entropy:** For continuous r.v.s: $h(X) = -\int f(x) \ln f(x) dx$. Can be negative. The normal distribution maximizes differential entropy for a given variance.

### Key Problems and Questions

- **Entropy of a Coin Flip:** Compute $H(X)$ for a Bernoulli($p$) random variable. Plot $H(p)$ vs. $p$. Show the maximum is at $p = 1/2$ (1 bit). What is the entropy of a biased coin with $p = 0.99$?
- **Entropy of a Die Roll:** Compute the entropy of a fair 6-sided die ($\log_2 6 \approx 2.585$ bits). Compute for a loaded die with $P(6) = 1/2$, others $= 1/10$. Which has higher entropy? Why?
- **Maximum Entropy Distribution — Given Mean:** Find the distribution on $\{1, 2, \ldots, n\}$ that maximizes entropy subject to $\sum p_i x_i = \mu$ and $\sum p_i = 1$. Solve using Lagrange multipliers. Show it is an exponential (Boltzmann) distribution.
- **Maximum Entropy — Continuous, Given Mean and Variance:** Show that the continuous distribution maximizing $h(X)$ subject to $E[X] = \mu$ and $\text{Var}(X) = \sigma^2$ is the Gaussian $N(\mu, \sigma^2)$. This is why the normal distribution is the "default" model when you only know the first two moments.
- **Entropy Rate of a Markov Chain:** For an ergodic Markov chain with stationary distribution $\pi$ and transition matrix $P$, the entropy rate is $H_{\text{rate}} = -\sum_i \pi_i \sum_j p_{ij} \log p_{ij}$. Compute for a 2-state weather chain. Interpret: how many bits per step does the chain generate?
- **Joint and Conditional Entropy — Two Dice:** Roll two fair dice. Compute $H(X)$, $H(Y)$, $H(X,Y)$, $H(Y|X)$, and $H(X|Y)$. Verify the chain rule. What if $Y = X$ (perfectly correlated)?
- **Entropy of a Portfolio Return:** Model a portfolio return as a mixture of two normals (bull/bear regimes). Compute the differential entropy numerically. Compare with the entropy of a single normal with the same variance. The mixture has higher entropy due to the regime uncertainty.
- **Source Coding Theorem (Shannon's First Theorem):** $N$ i.i.d. draws from a distribution with entropy $H$ can be compressed to $\approx NH$ bits. Simulate: generate a sequence from a biased coin ($p = 0.9$), compress with Huffman coding, and verify the compressed length approaches $NH$.
- **Huffman Coding — Optimal Prefix Codes:** Construct a Huffman code for a distribution over 5 symbols. Compute the expected code length. Show it satisfies $H(X) \le E[\text{length}] < H(X) + 1$.
- **Entropy and Estimation — Sample Entropy:** Given $n$ samples from an unknown distribution, estimate the entropy using the plug-in estimator $\hat{H} = -\sum \hat{p}_i \log \hat{p}_i$. Show it is biased downward ($E[\hat{H}] < H$). Implement the Miller-Madow bias correction: $\hat{H}_{\text{corrected}} = \hat{H} + (k-1)/(2n)$ where $k$ is the number of bins with positive count.

---

## 2. KL-Divergence & Cross-Entropy

### Core Concepts

- **Kullback-Leibler Divergence:** $D_{\text{KL}}(P \| Q) = \sum_x p(x) \log \frac{p(x)}{q(x)} = E_P\left[\log \frac{p(X)}{q(X)}\right]$. Measures the information "lost" when $Q$ is used to approximate $P$.
- **Properties:**
  - $D_{\text{KL}}(P \| Q) \ge 0$ (Gibbs' inequality), with equality iff $P = Q$.
  - Not symmetric: $D_{\text{KL}}(P \| Q) \neq D_{\text{KL}}(Q \| P)$ in general.
  - Not a metric (violates triangle inequality and symmetry).
- **Cross-Entropy:** $H(P, Q) = -\sum p(x) \log q(x) = H(P) + D_{\text{KL}}(P \| Q)$. Minimizing cross-entropy w.r.t. $Q$ is equivalent to minimizing KL-divergence.
- **MLE and KL-Divergence:** MLE minimizes the KL-divergence between the empirical distribution and the model family. This is the information-theoretic justification for MLE.
- **Relative Entropy in Finance:** Change of measure (risk-neutral vs. physical) can be viewed through the lens of KL-divergence. The minimal entropy martingale measure minimizes $D_{\text{KL}}(Q \| P)$ over all risk-neutral measures $Q$.

### Key Problems and Questions

- **KL-Divergence Between Two Normals:** Derive $D_{\text{KL}}(N(\mu_1, \sigma_1^2) \| N(\mu_2, \sigma_2^2)) = \log \frac{\sigma_2}{\sigma_1} + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2}$. Compute for (a) same mean, different variance, (b) different mean, same variance. Plot.
- **KL-Divergence — Asymmetry Demonstration:** Compute $D_{\text{KL}}(P \| Q)$ and $D_{\text{KL}}(Q \| P)$ for $P = \text{Bernoulli}(0.3)$ and $Q = \text{Bernoulli}(0.7)$. Show they differ. Visualize: $D_{\text{KL}}(P \| Q)$ penalizes $Q$ being near zero where $P$ is positive ("zero-avoiding"), while $D_{\text{KL}}(Q \| P)$ is "zero-forcing."
- **Cross-Entropy Loss in Classification:** In logistic regression, the loss function is cross-entropy: $L = -\sum [y_i \log \hat{p}_i + (1 - y_i) \log(1 - \hat{p}_i)]$. Show this is equivalent to minimizing $D_{\text{KL}}(\text{empirical} \| \text{model})$. Implement for a simple classification task.
- **Model Selection via KL-Divergence:** Fit two models to financial returns: (a) Normal, (b) Student-$t$. Estimate $D_{\text{KL}}(\hat{P}_{\text{empirical}} \| Q_{\text{model}})$ for each using the plug-in estimator. Which model is closer to the data? Compare with AIC.
- **AIC and Information Theory:** Akaike's Information Criterion $\text{AIC} = -2\ell + 2k$ is an estimate of $2n \cdot D_{\text{KL}}(\text{truth} \| \text{model})$ plus a constant. Derive the connection. Fit ARMA models of various orders and select via AIC. Compare with BIC.
- **Jensen-Shannon Divergence:** $\text{JSD}(P \| Q) = \frac{1}{2}D_{\text{KL}}(P \| M) + \frac{1}{2}D_{\text{KL}}(Q \| M)$ where $M = \frac{1}{2}(P + Q)$. Show JSD is symmetric and bounded: $0 \le \text{JSD} \le \log 2$. Compute for two return distributions.
- **KL-Divergence and Change of Measure:** For a one-period model, the physical measure $P$ assigns probabilities $(p, 1-p)$ to up/down, and the risk-neutral measure $Q$ assigns $(q, 1-q)$. Compute $D_{\text{KL}}(Q \| P)$. Interpret: the "cost" of risk-neutral pricing in information-theoretic terms.
- **Variational Inference — ELBO:** In Bayesian inference, approximate the posterior $p(\theta | \text{data})$ with a simpler $q(\theta)$ by minimizing $D_{\text{KL}}(q \| p)$. Show this is equivalent to maximizing the Evidence Lower Bound (ELBO). Implement for a simple conjugate model and compare with exact posterior.
- **Relative Entropy Pricing:** In incomplete markets, there are infinitely many risk-neutral measures. The minimal entropy martingale measure $Q^*$ minimizes $D_{\text{KL}}(Q \| P)$ over all $Q$ such that discounted prices are martingales. Implement for a trinomial model. Compare with other criteria (variance-optimal, Esscher).
- **KL Divergence — Hypothesis Testing Connection:** The likelihood ratio test statistic is $\Lambda = 2n \cdot D_{\text{KL}}(\hat{P} \| Q_{H_0})$. Show this converges to $\chi^2_k$ under $H_0$ (Wilks' theorem). Implement for testing normality of returns.

---

## 3. Mutual Information

### Core Concepts

- **Mutual Information:** $I(X; Y) = H(X) + H(Y) - H(X, Y) = D_{\text{KL}}(P_{XY} \| P_X \otimes P_Y)$. Measures the total dependence between $X$ and $Y$ — both linear and nonlinear.
- **Properties:**
  - $I(X; Y) \ge 0$, with equality iff $X$ and $Y$ are independent.
  - $I(X; Y) = I(Y; X)$ (symmetric).
  - $I(X; Y) = H(X) - H(X|Y)$: mutual information is the reduction in uncertainty about $X$ from knowing $Y$.
- **Conditional Mutual Information:** $I(X; Y | Z) = H(X|Z) - H(X|Y,Z)$.
- **Data Processing Inequality:** If $X \to Y \to Z$ forms a Markov chain, then $I(X; Z) \le I(X; Y)$. Processing data cannot increase information.

### Key Problems and Questions

- **Mutual Information — Correlated Normals:** For $(X, Y) \sim N(0, 0, 1, 1, \rho)$, derive $I(X; Y) = -\frac{1}{2}\ln(1 - \rho^2)$. Plot vs. $\rho$. Compare with $|\rho|$ — MI captures the same relationship but on a different scale.
- **MI vs. Correlation — Nonlinear Dependence:** Generate $X \sim \text{Uniform}(-1,1)$ and $Y = X^2$. Compute $\text{Corr}(X,Y) = 0$ but $I(X;Y) > 0$. MI detects the nonlinear relationship that correlation misses. Estimate MI using a KNN estimator.
- **Feature Selection via MI:** Given a dataset of financial features (momentum, volatility, value, etc.) and a binary target (up/down), compute $I(\text{feature}; \text{target})$ for each feature. Rank features by MI. Compare with correlation-based ranking.
- **Mutual Information — Time Series Dependence:** Compute MI between $X_t$ and $X_{t-k}$ for various lags $k$ in a financial time series. Compare with the autocorrelation function (ACF). MI can detect nonlinear serial dependence that ACF misses.
- **Data Processing Inequality — Signal Degradation:** A signal $X$ is corrupted by noise to produce $Y$, then further processed to produce $Z$. Verify $I(X; Z) \le I(X; Y)$ by simulation. Interpret: each processing step can only lose information.
- **Channel Capacity — Binary Symmetric Channel:** A binary channel flips each bit with probability $\epsilon$. The capacity is $C = 1 - H(\epsilon)$ bits. Compute and plot vs. $\epsilon$. At $\epsilon = 1/2$, capacity is 0 (no information gets through).
- **MI for Portfolio Construction:** Compute the pairwise MI matrix for 20 stocks. Cluster stocks by MI (instead of correlation). Does MI-based clustering differ from correlation-based clustering? Build a diversified portfolio using MI.
- **Transfer Entropy — Directed Information Flow:** Transfer entropy $T_{X \to Y} = I(Y_{t+1}; X_t | Y_t)$ measures directed information flow from $X$ to $Y$. Compute transfer entropy between two financial time series. Which one "leads" the other?
- **Conditional MI — Confounding:** $X$ and $Y$ appear dependent ($I(X;Y) > 0$), but after conditioning on $Z$, $I(X; Y | Z) = 0$. Construct an example with financial data (e.g., two stocks appear correlated but are both driven by a common factor).
- **MI and Optimal Quantization:** Quantize a continuous r.v. $X$ into $k$ bins to maximize $I(X_{\text{quantized}}; Y)$. This is the optimal discretization for prediction. Implement for a regression problem and compare with equal-width and equal-frequency binning.

---

## 4. Kelly Criterion & Applications

### Core Concepts

- **Kelly Criterion:** The optimal fraction $f^*$ to bet to maximize expected log wealth (equivalently, long-run geometric growth rate): $f^* = \arg\max_f E[\ln(1 + fR)]$.
- **Binary Bet:** Win $b$ with probability $p$, lose 1 with probability $q = 1-p$. Kelly fraction: $f^* = p/1 - q/b = (pb - q)/b$.
- **Continuous Version:** For a normally distributed return $R \sim N(\mu, \sigma^2)$, the Kelly leverage is $f^* = \mu / \sigma^2$.
- **Connection to Entropy:** Maximizing $E[\ln W]$ is equivalent to maximizing the growth rate $g = E[\ln(1 + fR)]$, which is related to the mutual information between the strategy and the market.
- **Fractional Kelly:** In practice, full Kelly is aggressive (high variance of wealth). Using $f = \alpha f^*$ with $\alpha \in (0, 1)$ reduces variance at the cost of growth rate. $\alpha = 1/2$ (half-Kelly) is a common choice.

### Key Problems and Questions

- **Kelly for a Coin Flip:** A biased coin has $P(H) = 0.6$. You bet fraction $f$ of your wealth; win $f$ (1:1 odds) on H, lose $f$ on T. Derive $f^* = 2p - 1 = 0.2$. Plot the growth rate $g(f) = p \ln(1+f) + q \ln(1-f)$ vs. $f$. Show that $f > 2f^*$ leads to negative growth.
- **Kelly with Asymmetric Payoffs:** You can bet on a horse with odds $b:1$ and $P(\text{win}) = p$. Derive $f^* = (bp - q)/b$. Compute for $p = 0.3$, $b = 4$. What if $bp < q$ (negative edge)?
- **Multi-Asset Kelly:** Two independent bets with edges $\mu_1, \mu_2$ and variances $\sigma_1^2, \sigma_2^2$. Derive the Kelly allocations $f_i^* = \mu_i / \sigma_i^2$. With correlation $\rho$, the vector Kelly is $f^* = \Sigma^{-1} \mu$. Implement and compare with Markowitz.
- **Kelly vs. Mean-Variance:** Show that the Kelly portfolio $f^* = \Sigma^{-1}\mu$ is the same as the Markowitz tangency portfolio (up to a scaling). The difference: Kelly maximizes growth rate, Markowitz maximizes Sharpe ratio. They agree on the direction but differ on leverage.
- **Fractional Kelly — Simulation:** Simulate 10,000 paths of wealth under full Kelly, half-Kelly, and quarter-Kelly for a strategy with Sharpe 1. Plot the distribution of terminal wealth. Show that half-Kelly dramatically reduces the probability of large drawdowns.
- **Overbetting Disaster:** Simulate a Kelly strategy where the bettor overestimates the edge ($\hat{p} > p_{\text{true}}$). Show that the resulting overbetting leads to ruin. Quantify: by what factor can you overestimate the edge before growth turns negative?
- **Kelly and the Growth-Optimal Portfolio:** Prove that the Kelly portfolio maximizes $E[\ln W_T]$ and that no other strategy can beat it in the long run (almost surely). This is the foundation of the Growth-Optimal Portfolio theory.
- **Kelly for a Trading Strategy:** A strategy has daily returns with mean $\mu = 0.05\%$ and std $\sigma = 1\%$. Compute the Kelly leverage $f^* = \mu/\sigma^2 = 5$. Is this realistic? Discuss the impact of estimation error, fat tails, and serial correlation.
- **Kelly with Transaction Costs:** Modify the Kelly criterion to account for proportional transaction costs $c$. Show that the optimal rebalancing frequency decreases with $c$. Simulate and compare wealth paths with and without costs.
- **Information-Theoretic Interpretation:** Show that the growth rate $g = E[\ln(1+fR)]$ can be decomposed as $g = H(\text{market}) - H(\text{market} | \text{strategy})$ (loosely: how much information the strategy extracts from the market). Discuss the analogy with channel capacity.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive formulas for entropy, KL-divergence, MI, and Kelly fractions by hand.
> 2. **Numerical estimation** — implement plug-in, KNN, and kernel estimators for information-theoretic quantities.
> 3. **Simulation** — verify theoretical results via Monte Carlo, simulate wealth paths under Kelly strategies.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

