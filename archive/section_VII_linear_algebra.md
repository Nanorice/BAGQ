# Section VII: Linear Algebra & Matrix Theory — Detailed Problem List

> *Foundation: Vector spaces, eigendecomposition, positive-definite matrices*

Linear algebra is the computational backbone of quantitative finance. Covariance matrices, PCA on yield curves, Markov chain analysis, portfolio optimization — all reduce to matrix operations. Interview questions test both theoretical understanding (eigenvalues, decompositions, definiteness) and practical fluency (can you set up and solve the system?).

---

## 1. Core Linear Algebra

### Core Concepts

- **Vector Spaces:** A set closed under addition and scalar multiplication. Basis, dimension, span, linear independence.
- **Linear Transformations & Matrices:** Every linear map between finite-dimensional spaces can be represented as a matrix. Rank = dimension of the image.
- **Systems of Linear Equations:** $Ax = b$. Solvable iff $b \in \text{Col}(A)$. Unique solution iff $A$ is full rank.
- **Gaussian Elimination / LU Decomposition:** $A = LU$ where $L$ is lower-triangular and $U$ is upper-triangular. $O(n^3)$ for an $n \times n$ system.
- **Eigenvalues and Eigenvectors:** $Av = \lambda v$. The characteristic polynomial $\det(A - \lambda I) = 0$ gives eigenvalues. Diagonalization: $A = PDP^{-1}$ when $A$ has $n$ linearly independent eigenvectors.
- **Symmetric Matrices:** Real symmetric matrices have real eigenvalues and orthogonal eigenvectors. Spectral theorem: $A = Q\Lambda Q^T$.
- **Positive Definite (PD) / Positive Semi-Definite (PSD):** $A$ is PD if $x^T A x > 0$ for all $x \neq 0$. Equivalently: all eigenvalues > 0, or all leading minors > 0 (Sylvester's criterion), or $A = B^T B$ for some full-rank $B$.
- **Matrix Decompositions:**
  - *QR:* $A = QR$ with $Q$ orthogonal, $R$ upper-triangular. Used for least squares and eigenvalue algorithms.
  - *SVD:* $A = U\Sigma V^T$. The most general decomposition. Singular values $\sigma_i$ are the square roots of eigenvalues of $A^T A$.
  - *Cholesky:* $A = LL^T$ for PD matrices. Half the cost of LU. Used to generate correlated random variables.

### Key Problems and Questions

- **Solving a System — Gaussian Elimination:** Implement Gaussian elimination with partial pivoting. Solve $Ax = b$ for a $5 \times 5$ system. Compare with `numpy.linalg.solve`. Measure the impact of pivoting on numerical stability.
- **LU Decomposition — Implementation:** Implement LU decomposition (Doolittle's method). Factor a given matrix $A$. Use the factorization to solve $Ax = b$ for multiple right-hand sides efficiently.
- **Eigenvalue Computation — Power Iteration:** Implement the power iteration method to find the largest eigenvalue and corresponding eigenvector of a matrix. Apply to a $10 \times 10$ correlation matrix. How many iterations until convergence to 6 decimal places?
- **Spectral Theorem — Verification:** For a random $5 \times 5$ symmetric matrix, compute the eigendecomposition $A = Q\Lambda Q^T$. Verify $Q$ is orthogonal ($Q^T Q = I$) and reconstruct $A$ from the decomposition. Verify numerically.
- **SVD — Low-Rank Approximation:** Compute the SVD of a $100 \times 50$ data matrix. Reconstruct the matrix using only the top $k$ singular values for $k = 1, 5, 10, 25$. Plot the Frobenius norm error vs. $k$ (Eckart-Young theorem).
- **Cholesky Decomposition — Correlated Samples:** Given a correlation matrix $\Sigma$ for 5 assets, compute the Cholesky factor $L$. Generate $n$ i.i.d. standard normals $Z$ and compute $X = LZ$ to get correlated samples. Verify the sample correlation matches $\Sigma$.
- **Condition Number and Numerical Stability:** Compute the condition number $\kappa(A) = \|A\| \cdot \|A^{-1}\|$ for several matrices. Show that solving $Ax = b$ with a large $\kappa$ amplifies errors. Construct an ill-conditioned Hilbert matrix and demonstrate.
- **Matrix Exponential — Markov Chain:** For a continuous-time Markov chain with generator matrix $Q$, the transition matrix is $P(t) = e^{Qt}$. Compute $e^{Qt}$ using eigendecomposition: $e^{Qt} = V e^{\Lambda t} V^{-1}$. Apply to a 3-state credit migration model.
- **Rank and Null Space:** Given a matrix $A$, find its rank, column space, and null space. Interpret geometrically. Show that $\text{rank}(A) + \dim(\text{null}(A)) = n$ (rank-nullity theorem).
- **Sherman-Morrison Formula:** If $A^{-1}$ is known and $A$ is updated to $A + uv^T$ (rank-1 update), the inverse is $(A + uv^T)^{-1} = A^{-1} - \frac{A^{-1}uv^T A^{-1}}{1 + v^T A^{-1}u}$. Implement and apply to efficiently updating a covariance matrix when one observation is added.

---

## 2. Applications in Quant Finance

### Core Concepts

- **Covariance Matrix:** $\Sigma_{ij} = \text{Cov}(R_i, R_j)$. Must be PSD. Estimated from data as $\hat{\Sigma} = \frac{1}{n-1}(X - \bar{X})^T(X - \bar{X})$.
- **Correlation Matrix:** $\rho_{ij} = \Sigma_{ij} / (\sigma_i \sigma_j)$. Diagonal entries are 1. Must be PSD with all entries in $[-1,1]$.
- **Principal Component Analysis (PCA):** Eigendecomposition of the covariance matrix: $\Sigma = V\Lambda V^T$. The $k$-th principal component is $V_k^T(X - \bar{X})$. Explained variance ratio: $\lambda_k / \sum \lambda_i$.
- **Mean-Variance Optimization (Markowitz):** Minimize $w^T \Sigma w$ subject to $w^T \mu = \mu_p$ and $w^T \mathbf{1} = 1$. The efficient frontier is a hyperbola in $(\sigma, \mu)$ space.
- **Factor Models:** $R_i = \alpha_i + \sum_{k=1}^K \beta_{ik} F_k + \epsilon_i$. Reduces the dimensionality of the covariance matrix from $O(n^2)$ to $O(nK)$.

### Key Problems and Questions

- **Covariance Matrix Estimation:** Download 1 year of daily returns for 10 stocks. Estimate the sample covariance matrix $\hat{\Sigma}$. Check if it's PSD (all eigenvalues $\ge 0$). What happens when $n < p$ (more assets than observations)?
- **Shrinkage Estimator (Ledoit-Wolf):** The sample covariance matrix is noisy when $p/n$ is not small. Implement the Ledoit-Wolf shrinkage estimator: $\hat{\Sigma}_{\text{shrunk}} = \alpha \hat{\Sigma} + (1-\alpha) \cdot \text{diag}(\hat{\Sigma})$. Compare the eigenvalue spectrum before and after shrinkage.
- **PCA on Yield Curves:** Obtain historical US Treasury yield curve data (2Y, 5Y, 10Y, 30Y). Compute the covariance matrix of yield changes. Run PCA. Show that the first 3 components explain >95% of variance and correspond to level, slope, and curvature.
- **PCA on Equity Returns:** Run PCA on daily returns of 50 S&P 500 stocks. How many components explain 80% of variance? Interpret the first component (market factor). Reconstruct the covariance matrix using only the top 5 PCs.
- **Markowitz Mean-Variance Optimization:** Given expected returns $\mu$ and covariance matrix $\Sigma$ for 5 assets, compute the efficient frontier. Plot it in $(\sigma, \mu)$ space. Find the minimum-variance portfolio and the tangency portfolio (maximum Sharpe ratio).
- **Portfolio Optimization with Constraints:** Add constraints: no short selling ($w_i \ge 0$), position limits ($w_i \le 0.3$), sector exposure limits. Solve using quadratic programming (`cvxpy` or `scipy.optimize`). Compare the constrained frontier with the unconstrained one.
- **Risk Parity Portfolio:** Instead of mean-variance, construct a risk parity portfolio where each asset contributes equally to total portfolio risk: $w_i (\Sigma w)_i = \frac{1}{n} w^T \Sigma w$ for all $i$. Implement using numerical optimization.
- **Random Matrix Theory — Marchenko-Pastur:** Generate a $500 \times 200$ random matrix (i.i.d. normals). Compute the sample covariance matrix and its eigenvalues. Plot the eigenvalue distribution and overlay the Marchenko-Pastur theoretical density. Identify eigenvalues that contain "signal" vs. "noise."
- **Cholesky for Monte Carlo Simulation:** Simulate 10,000 scenarios of daily returns for a 20-asset portfolio using the Cholesky decomposition of the correlation matrix. Compute portfolio VaR at the 99% level. Compare with the parametric (variance-covariance) VaR.
- **Factor Model — Covariance Decomposition:** Fit a 3-factor model (market, size, value) to 30 stock returns via OLS. Decompose the covariance matrix into $\Sigma = B F B^T + D$ where $F$ is the factor covariance and $D$ is the diagonal idiosyncratic variance. Compare with the full sample covariance matrix.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive results by hand where possible (eigendecompositions, optimization conditions, matrix identities).
> 2. **Numerical implementation** — build using `numpy`, `scipy.linalg`, `cvxpy` for optimization.
> 3. **Visualization** — plot eigenvalue spectra, efficient frontiers, PCA loadings, correlation heatmaps.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

