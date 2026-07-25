# Section IX: Statistics & Estimation — Detailed Problem List

> *Foundation: Statistical inference, likelihood theory, hypothesis testing*

Statistics is the bridge between theory and data. In quant finance, every model must be calibrated, every strategy backtested, every risk metric estimated from noisy observations. Interview questions test your ability to derive estimators, assess their quality, fit models to time series, and reason about uncertainty — all skills that separate a theorist from a practitioner.

---

## 1. Estimation Theory

### Core Concepts

- **Estimator:** A function of the data $\hat{\theta}(X_1, \ldots, X_n)$ used to infer an unknown parameter $\theta$.
- **Bias:** $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$. An estimator is unbiased if $\text{Bias} = 0$.
- **Variance:** $\text{Var}(\hat{\theta})$ measures the spread of the estimator across samples.
- **Mean Squared Error:** $\text{MSE} = \text{Bias}^2 + \text{Variance}$. The fundamental bias-variance tradeoff.
- **Consistency:** $\hat{\theta}_n \xrightarrow{P} \theta$ as $n \to \infty$.
- **Maximum Likelihood Estimation (MLE):** $\hat{\theta}_{\text{MLE}} = \arg\max_\theta \prod_{i=1}^n f(x_i; \theta)$. Asymptotically efficient (achieves the Cramér-Rao bound).
- **Fisher Information:** $I(\theta) = -E\left[\frac{\partial^2}{\partial \theta^2} \ln f(X;\theta)\right]$. Measures the "information" a sample carries about $\theta$.
- **Cramér-Rao Lower Bound:** $\text{Var}(\hat{\theta}) \ge 1 / (nI(\theta))$ for any unbiased estimator. The MLE achieves this asymptotically.
- **Method of Moments (MoM):** Set sample moments equal to population moments and solve for parameters. Simpler than MLE but generally less efficient.

### Key Problems and Questions

- **MLE for Normal Distribution:** Given $X_1, \ldots, X_n \sim N(\mu, \sigma^2)$, derive the MLE for $\mu$ and $\sigma^2$. Show $\hat{\mu} = \bar{X}$ is unbiased but $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i - \bar{X})^2$ is biased. Compute the bias and the unbiased corrected estimator.
- **MLE for Exponential Distribution:** Given $X_1, \ldots, X_n \sim \text{Exp}(\lambda)$, derive $\hat{\lambda}_{\text{MLE}} = 1/\bar{X}$. Compute its bias, variance, and MSE. Show it is consistent. Compare with the MoM estimator.
- **Fisher Information — Normal Mean:** Compute $I(\mu)$ for $X \sim N(\mu, \sigma^2)$ with known $\sigma^2$. Verify the Cramér-Rao bound: $\text{Var}(\bar{X}) = \sigma^2/n = 1/(nI(\mu))$. The sample mean is efficient.
- **Fisher Information — Bernoulli:** Compute $I(p)$ for $X \sim \text{Bernoulli}(p)$. Show $I(p) = 1/(p(1-p))$. Why is estimation hardest when $p$ is near 0 or 1? Relate to the width of confidence intervals for rare events.
- **Method of Moments — Gamma Distribution:** Given data from $\text{Gamma}(\alpha, \beta)$, estimate $\alpha$ and $\beta$ by matching the first two sample moments to the population moments $E[X] = \alpha/\beta$, $\text{Var}(X) = \alpha/\beta^2$. Compare with MLE (which requires numerical optimization).
- **Bias-Variance Tradeoff — Ridge Regression:** In linear regression with many predictors, OLS has low bias but high variance. Ridge regression adds $\lambda \|w\|^2$ penalty, introducing bias but reducing variance. Simulate data, compute MSE for various $\lambda$, and plot the U-shaped bias-variance curve.
- **Sufficient Statistics:** Show that $\bar{X}$ is a sufficient statistic for $\mu$ in the normal model (by the factorization theorem). Why does sufficiency matter? (Any estimator based on a sufficient statistic loses no information.)
- **MLE for Log-Normal — Calibrating GBM:** Given daily stock prices, compute log returns. Show log returns are approximately $N((\mu-\sigma^2/2)\Delta t, \sigma^2 \Delta t)$. Estimate $\mu$ and $\sigma$ by MLE. Compute standard errors and confidence intervals.
- **Asymptotic Normality of MLE:** State and illustrate the result: $\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta) \xrightarrow{d} N(0, 1/I(\theta))$. Simulate 10,000 MLEs from Poisson samples of size $n = 10, 50, 200$. Plot the histograms and overlay the asymptotic normal.
- **James-Stein Estimator — Shrinkage:** For $X_i \sim N(\mu_i, 1)$ with $p \ge 3$ independent means, the James-Stein estimator $\hat{\mu}_i^{JS} = (1 - (p-2)/\|X\|^2) X_i$ dominates the MLE in total MSE. Simulate and verify. Discuss implications for estimating expected returns of many assets.

---

## 2. Hypothesis Testing & Confidence Intervals

### Core Concepts

- **Null and Alternative Hypothesis:** $H_0$ (status quo) vs. $H_1$ (what you want to show). The test decides between them based on data.
- **Type I Error ($\alpha$):** Rejecting $H_0$ when it is true (false positive). The significance level.
- **Type II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is true (false negative). Power $= 1 - \beta$.
- **p-Value:** The probability of observing data as extreme as (or more extreme than) the observed data, assuming $H_0$ is true. Reject $H_0$ if $p < \alpha$.
- **Neyman-Pearson Lemma:** The most powerful test of $H_0: \theta = \theta_0$ vs. $H_1: \theta = \theta_1$ is the likelihood ratio test: reject when $\Lambda = L(\theta_1)/L(\theta_0) > c$.
- **Confidence Interval:** A random interval $[\hat{\theta}_L, \hat{\theta}_U]$ such that $P(\theta \in [\hat{\theta}_L, \hat{\theta}_U]) = 1 - \alpha$.

### Key Problems and Questions

- **Z-Test for a Mean:** A trading strategy claims an annual Sharpe ratio of 2. You observe 52 weekly returns with sample Sharpe $\hat{S} = 1.5$. Test $H_0: S = 2$ vs. $H_1: S < 2$ at the 5% level. Compute the z-statistic and p-value. (Use the result $\text{SE}(\hat{S}) \approx 1/\sqrt{n}$.)
- **t-Test for Two Means:** Compare the mean returns of two strategies over 100 days. Implement both the equal-variance and Welch's (unequal-variance) t-test. When does the choice matter?
- **Chi-Squared Goodness of Fit:** Test whether daily stock returns follow a normal distribution. Bin the returns, compute expected frequencies under normality, and compute the chi-squared statistic. Also apply the Jarque-Bera test (based on skewness and kurtosis).
- **Likelihood Ratio Test — Nested Models:** Model 1: returns are $N(\mu, \sigma^2)$. Model 2: returns are a mixture of two normals. Compute the log-likelihood ratio statistic $\Lambda = -2(\ell_1 - \ell_2)$. Use Wilks' theorem ($\Lambda \sim \chi^2_{df}$) to test whether the mixture model is significantly better.
- **Multiple Testing — Bonferroni and FDR:** You test 100 trading strategies for significance at $\alpha = 0.05$. Even if none are truly profitable, you expect 5 false positives. Implement Bonferroni correction ($\alpha / 100$) and Benjamini-Hochberg FDR control. Simulate and compare.
- **Power Analysis — Sample Size Determination:** You want to detect a Sharpe ratio of 0.5 with power 0.8 at significance level 0.05. How many months of data do you need? Derive the formula and plot power vs. sample size.
- **Bootstrap Confidence Intervals:** Given 250 daily returns, compute a 95% confidence interval for the Sharpe ratio using (a) the normal approximation, (b) percentile bootstrap (10,000 resamples), (c) BCa bootstrap. Compare the three intervals.
- **Permutation Test — Strategy Comparison:** Test whether Strategy A outperforms Strategy B without assuming normality. Pool the returns, randomly reassign to A and B, compute the difference in means. Repeat 10,000 times. Compute the permutation p-value.
- **Kolmogorov-Smirnov Test:** Test whether two samples of returns come from the same distribution using the KS test (based on the maximum difference between empirical CDFs). Apply to comparing pre-crisis and post-crisis return distributions.
- **Backtest Overfitting — Deflated Sharpe Ratio:** When you test many strategies and report the best one, the reported Sharpe is inflated. Implement the Bailey-López de Prado deflated Sharpe ratio, which adjusts for the number of strategies tested. Show that a "Sharpe 2" strategy can be statistically insignificant after correction.

---

## 3. Regression & Time Series

### Core Concepts

- **Ordinary Least Squares (OLS):** $\hat{\beta} = (X^T X)^{-1} X^T y$. Minimizes $\|y - X\beta\|^2$. BLUE (Best Linear Unbiased Estimator) under Gauss-Markov assumptions.
- **Gauss-Markov Assumptions:** Linearity, full rank, exogeneity ($E[\epsilon|X] = 0$), homoscedasticity ($\text{Var}(\epsilon|X) = \sigma^2 I$), no autocorrelation.
- **Logistic Regression:** For binary outcomes, model $P(Y=1|X) = 1/(1 + e^{-X\beta})$. Fit by MLE (no closed form). Decision boundary is linear.
- **AR(p) Model:** $X_t = \phi_1 X_{t-1} + \cdots + \phi_p X_{t-p} + \epsilon_t$. Stationarity requires roots of the characteristic polynomial outside the unit circle.
- **MA(q) Model:** $X_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \cdots + \theta_q \epsilon_{t-q}$. Always stationary.
- **ARMA(p,q) / ARIMA(p,d,q):** Combines AR and MA. ARIMA includes differencing for non-stationary series.
- **GARCH(1,1):** $\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$. Models volatility clustering. $\alpha + \beta < 1$ for stationarity.
- **Cointegration:** Two non-stationary series $X_t, Y_t$ are cointegrated if a linear combination $Y_t - \beta X_t$ is stationary. Basis for pairs trading.

### Key Problems and Questions

- **OLS Regression — CAPM Beta:** Regress stock returns on market returns: $R_i = \alpha + \beta R_m + \epsilon$. Estimate $\alpha$ (Jensen's alpha) and $\beta$ (market sensitivity). Compute standard errors, $t$-statistics, $R^2$. Test $H_0: \alpha = 0$.
- **Gauss-Markov Violations — Heteroscedasticity:** Simulate data where $\text{Var}(\epsilon_i) \propto x_i^2$. Show OLS estimates are still unbiased but standard errors are wrong. Implement White's heteroscedasticity-consistent standard errors (HC0). Compare.
- **Fama-MacBeth Regression:** Implement the two-pass Fama-MacBeth procedure for testing asset pricing models: (1) time-series regression of each asset on factors to get betas, (2) cross-sectional regression of average returns on betas at each time point. Compute Shanken-corrected standard errors.
- **Logistic Regression — Default Prediction:** Given financial ratios (leverage, profitability, size) for 500 firms, predict default (binary). Fit logistic regression. Compute AUC-ROC. Compare with a probit model.
- **AR(1) Model — Estimation and Forecasting:** Fit an AR(1) model to a mean-reverting financial series (e.g., interest rate spread). Estimate $\phi$ by OLS. Test for stationarity ($|\phi| < 1$). Forecast $h$ steps ahead and plot the forecast with confidence bands that widen with horizon.
- **ARIMA — Box-Jenkins Methodology:** For a non-stationary time series (e.g., log GDP), apply the Box-Jenkins method: (1) test for stationarity (ADF test), (2) difference if needed, (3) identify $p, q$ from ACF/PACF, (4) fit ARIMA, (5) diagnostic checking (Ljung-Box test on residuals). Implement end-to-end.
- **GARCH(1,1) — Volatility Modeling:** Fit GARCH(1,1) to daily S&P 500 returns. Estimate $\omega, \alpha, \beta$ by MLE. Plot the conditional volatility $\sigma_t$ over time. Show it captures volatility clustering. Compute VaR forecasts using the GARCH volatility.
- **Cointegration — Pairs Trading:** Test for cointegration between two stock prices using the Engle-Granger two-step method (or Johansen test). If cointegrated, construct the spread $Z_t = Y_t - \hat{\beta} X_t$. Trade the mean-reversion: go long/short when the spread deviates by $\pm 2\sigma$. Backtest.
- **Regime-Switching Model (Markov-Switching):** Fit a 2-regime model to stock returns: regime 1 (bull: high mean, low vol) and regime 2 (bear: low mean, high vol). Estimate transition probabilities by MLE/EM. Plot the smoothed regime probabilities over time.
- **Vector Autoregression (VAR):** Fit a VAR(1) model to a system of 3 macro variables (e.g., GDP growth, inflation, interest rate). Compute impulse response functions: how does a shock to one variable propagate through the system? Plot impulse responses over 20 periods.

---

## 4. Bayesian Inference

### Core Concepts

- **Bayes' Theorem (Parameter Version):** $p(\theta | \text{data}) \propto p(\text{data} | \theta) \cdot p(\theta)$. Posterior $\propto$ Likelihood $\times$ Prior.
- **Prior:** Encodes beliefs about $\theta$ before seeing data. Can be informative or non-informative (e.g., Jeffreys prior).
- **Conjugate Prior:** A prior that, combined with a particular likelihood, produces a posterior of the same family. Makes computation tractable.
  - *Beta-Binomial:* Prior $p \sim \text{Beta}(\alpha,\beta)$, data $k$ successes in $n$ trials → posterior $p \sim \text{Beta}(\alpha+k, \beta+n-k)$.
  - *Normal-Normal:* Prior $\mu \sim N(\mu_0, \sigma_0^2)$, data $\bar{X}$ with known $\sigma$ → posterior is normal (precision-weighted average).
  - *Gamma-Poisson:* Prior $\lambda \sim \text{Gamma}(\alpha,\beta)$, data $\sum x_i$ from $n$ observations → posterior $\lambda \sim \text{Gamma}(\alpha + \sum x_i, \beta + n)$.
- **Posterior Predictive Distribution:** $p(x_{\text{new}} | \text{data}) = \int p(x_{\text{new}} | \theta) p(\theta | \text{data}) d\theta$. Integrates over parameter uncertainty.
- **Credible Interval:** Bayesian analogue of a confidence interval. The 95% credible interval contains $\theta$ with posterior probability 0.95.
- **Bayesian Model Comparison:** Compare models using the marginal likelihood (Bayes factor): $\text{BF}_{12} = p(\text{data} | M_1) / p(\text{data} | M_2)$.

### Key Problems and Questions

- **Beta-Binomial — Coin Bias Estimation:** Prior: $p \sim \text{Beta}(1,1)$ (uniform). You observe 7 heads in 10 flips. Compute the posterior $\text{Beta}(8,4)$. Plot prior, likelihood, and posterior. Compute the posterior mean, MAP, and 95% credible interval. Compare with the frequentist MLE and confidence interval.
- **Normal-Normal — Estimating a Mean:** Prior: $\mu \sim N(0, 10^2)$. Data: $n = 25$ observations with $\bar{X} = 3$, known $\sigma = 5$. Derive the posterior. Show how the posterior mean is a weighted average of the prior mean and the sample mean. Plot how the posterior evolves as $n$ increases.
- **Sequential Bayesian Updating:** Data arrives one observation at a time. Update the posterior after each observation (today's posterior becomes tomorrow's prior). Implement for the Beta-Binomial model. Animate the posterior as data accumulates. Show convergence to the true parameter.
- **Bayesian Linear Regression:** Prior: $\beta \sim N(0, \sigma_\beta^2 I)$. Derive the posterior $\beta | y, X \sim N(\hat{\beta}_{\text{Bayes}}, \Sigma_{\text{post}})$. Show the posterior mean is a ridge regression estimate. Plot posterior predictive bands.
- **Conjugate Priors — Poisson-Gamma:** Model event counts as $X_i \sim \text{Poisson}(\lambda)$ with prior $\lambda \sim \text{Gamma}(2, 1)$. Observe $n = 20$ events with $\sum x_i = 50$. Compute the posterior. Derive the posterior predictive distribution (negative binomial).
- **Jeffreys Prior — Non-Informative:** Derive the Jeffreys prior for (a) the Bernoulli parameter $p$, (b) the normal mean $\mu$, (c) the normal variance $\sigma^2$. Show Jeffreys prior is $p(\sigma^2) \propto 1/\sigma^2$ (not uniform!). Discuss why it's "non-informative."
- **Bayesian A/B Testing:** Two trading strategies are tested over 30 days. Strategy A: mean return 0.5%, std 2%. Strategy B: mean return 0.8%, std 3%. Use a Bayesian approach to compute $P(\mu_B > \mu_A | \text{data})$. Compare with a frequentist t-test.
- **Posterior Predictive Checks:** Fit a normal model to stock returns. Generate simulated datasets from the posterior predictive distribution. Compare summary statistics (mean, variance, skewness, kurtosis) of simulated data with the observed data. Does the model fit well?
- **Bayesian Volatility Estimation — Stochastic Volatility:** Model log-returns as $r_t \sim N(0, e^{h_t})$ with $h_t = \phi h_{t-1} + \sigma_\eta \eta_t$. This is a state-space model. Implement a simple MCMC sampler (Gibbs or MH) to estimate the posterior of $(\phi, \sigma_\eta, h_{1:T})$. Plot the estimated volatility path.
- **Model Comparison — Bayes Factors:** Compare two models for stock returns: $M_1$: Normal, $M_2$: Student-$t$ (heavier tails). Compute the marginal likelihood for each (via harmonic mean estimator or bridge sampling). Compute the Bayes factor. Which model does the data prefer?

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive estimators, test statistics, and posteriors by hand.
> 2. **Numerical implementation** — build using `scipy.stats`, `statsmodels`, `arch` (for GARCH), `pymc` or custom MCMC.
> 3. **Visualization** — plot posterior distributions, ACF/PACF, regression diagnostics, volatility paths, and ROC curves.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

