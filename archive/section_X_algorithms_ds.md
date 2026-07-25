# Section X: Algorithms, Data Structures & Pseudo-Code — Detailed Problem List

> *Foundation: Computational complexity, algorithm design, numerical methods*

Algorithms and data structures are the implementation layer of quantitative finance. Every Monte Carlo engine, order book, risk system, and backtester is built on these primitives. Quant interviews — especially at firms with a technology focus — test your ability to design efficient solutions, analyze complexity, and translate mathematical ideas into working code. Numerical methods bridge the gap between analytical formulas and real-world computation.

---

## 1. Sorting & Searching

### Core Concepts

- **Binary Search:** Given a sorted array, find a target in $O(\log n)$ by halving the search space at each step. Generalizes to "binary search on the answer" for optimization problems.
- **Comparison-Based Sorting Lower Bound:** Any comparison-based sort requires $\Omega(n \log n)$ comparisons in the worst case (decision tree argument).
- **Merge Sort:** Divide-and-conquer, $O(n \log n)$ worst case, stable. Natural for external sorting (large datasets on disk).
- **Quicksort:** Divide-and-conquer with a pivot, $O(n \log n)$ average, $O(n^2)$ worst case. Randomized pivot selection avoids worst case in practice.
- **Heap Sort / Priority Queue:** A binary heap supports insert and extract-min in $O(\log n)$. Heap sort is $O(n \log n)$ in-place.
- **Hash Tables:** Average $O(1)$ lookup, insert, delete. Collision resolution: chaining or open addressing. Load factor determines performance.
- **Counting Sort / Radix Sort:** Non-comparison sorts achieving $O(n)$ for integer keys in a bounded range.

### Key Problems and Questions

- **Binary Search — Implied Volatility:** Given a monotone function $f(\sigma) = \text{BS}(\sigma) - V_{\text{market}}$, find the root using bisection. Implement with tolerance $10^{-8}$. Compare iterations with Newton-Raphson. Why is bisection more robust?
- **Binary Search on the Answer — Optimal Threshold:** A trading strategy has a parameter $\theta$. Profit is unimodal in $\theta$. Use ternary search (or golden section) to find the optimal $\theta$. Implement and count function evaluations.
- **Merge Sort — Counting Inversions:** The number of inversions in a permutation measures "unsortedness." Modify merge sort to count inversions in $O(n \log n)$. Apply to rank correlation (Kendall's tau) between two return series.
- **Quicksort — Randomized Pivot Analysis:** Implement quicksort with random pivot selection. Prove the expected number of comparisons is $2n \ln n$. Measure empirically for $n = 10^3, 10^4, 10^5$.
- **Priority Queue — Event-Driven Simulation:** Simulate an order book where orders arrive and are executed by price-time priority. Use a min-heap for asks and a max-heap for bids. Process $10^6$ events and measure throughput.
- **Hash Table — Frequency Counting:** Given a stream of trade ticks (symbol, price, size), count the number of trades per symbol using a hash map. Handle hash collisions. What is the expected number of collisions for $n$ keys in a table of size $m$?
- **Median Maintenance:** A stream of numbers arrives one at a time. Maintain the running median using two heaps (max-heap for lower half, min-heap for upper half). Apply to computing the running median of a price series in $O(\log n)$ per update.
- **K-th Largest Element — Quickselect:** Find the $k$-th largest element in an unsorted array in $O(n)$ expected time using quickselect (partition-based). Apply to finding VaR as a percentile of simulated P&L.
- **Sorting Stability — Portfolio Rebalancing:** You have a list of trades to execute, each with priority and timestamp. Sort by priority (primary) and timestamp (secondary). Show why a stable sort preserves the timestamp order within equal priorities.
- **External Sorting — Large Dataset:** You have $10^9$ trade records that don't fit in memory. Design an external merge sort using $k$-way merge with a heap. Analyze I/O complexity.

---

## 2. Dynamic Programming (Algorithmic)

### Core Concepts

- **Optimal Substructure:** The optimal solution contains optimal solutions to subproblems.
- **Overlapping Subproblems:** The same subproblems are solved multiple times → memoize or tabulate.
- **Memoization (Top-Down):** Recursive + cache. Natural but may hit recursion depth limits.
- **Tabulation (Bottom-Up):** Iterative, fill a table. Often more efficient in practice.
- **State Space Design:** The key challenge is defining the "state" — what information do you need to make optimal decisions?
- **Connection to Finance:** The Bellman equation in stochastic control is dynamic programming. Binomial tree pricing is backward induction. LSM for American options uses regression as a DP approximation.

### Key Problems and Questions

- **Fibonacci — Memoization vs. Tabulation:** Compute $F_n$ using (a) naive recursion ($O(2^n)$), (b) memoization ($O(n)$), (c) tabulation ($O(n)$, $O(1)$ space), (d) matrix exponentiation ($O(\log n)$). Implement all four and benchmark.
- **Longest Common Subsequence (LCS):** Given two strings, find the LCS. Build the DP table, trace back the solution. Apply to comparing two time series for common patterns.
- **0/1 Knapsack — Capital Allocation:** You have $n$ investment opportunities, each with a cost $c_i$ and expected return $r_i$. Total budget is $W$. Maximize total return. Formulate as a knapsack problem. Solve by DP. Compare with the continuous relaxation (greedy by return/cost ratio).
- **Coin Change — Minimum Denominations:** Given denominations $\{d_1, \ldots, d_k\}$ and a target $T$, find the minimum number of coins. Classic DP. Extend: count the number of ways to make change.
- **Edit Distance — String Similarity:** Compute the Levenshtein distance between two strings. Apply to fuzzy matching of ticker symbols or company names in a financial database.
- **Matrix Chain Multiplication — Optimal Parenthesization:** Given matrices $A_1, \ldots, A_n$ with dimensions $p_0 \times p_1, p_1 \times p_2, \ldots$, find the parenthesization that minimizes the number of scalar multiplications. Solve by DP in $O(n^3)$.
- **Longest Increasing Subsequence (LIS):** Find the LIS of a sequence in $O(n \log n)$ using patience sorting. Apply to finding the longest upward trend in a price series.
- **Optimal BST — Weighted Search:** Given keys with known access frequencies, construct the BST that minimizes expected search time. Solve by DP (Knuth's optimization gives $O(n^2)$).
- **Binomial Option Pricing as DP:** Frame the CRR binomial tree as a DP problem. State = (time step, number of up moves). Transition: option value = discounted expected value under risk-neutral probabilities. Implement and show it's identical to backward induction on the tree.
- **Sequence Alignment — Pairs Trading Signal:** Align two price series using dynamic time warping (DTW), which is solved by DP. Compute the DTW distance. Use it as a similarity metric for pairs trading candidate selection.

---

## 3. Graph Algorithms

### Core Concepts

- **Graph Representation:** Adjacency list ($O(V + E)$ space) vs. adjacency matrix ($O(V^2)$ space). Directed vs. undirected. Weighted vs. unweighted.
- **BFS (Breadth-First Search):** Explores level by level. Shortest path in unweighted graphs. $O(V + E)$.
- **DFS (Depth-First Search):** Explores depth-first. Detects cycles, topological sort, connected components. $O(V + E)$.
- **Topological Sort:** Linear ordering of vertices in a DAG such that for every edge $(u, v)$, $u$ comes before $v$. Used for dependency resolution.
- **Shortest Path:**
  - *Dijkstra:* Non-negative weights, $O((V + E) \log V)$ with a binary heap.
  - *Bellman-Ford:* Allows negative weights, detects negative cycles, $O(VE)$.
  - *Floyd-Warshall:* All-pairs shortest path, $O(V^3)$.
- **Minimum Spanning Tree (MST):**
  - *Kruskal:* Sort edges, greedily add if no cycle (union-find). $O(E \log E)$.
  - *Prim:* Grow tree from a vertex using a priority queue. $O((V + E) \log V)$.
- **Network Flow:** Max-flow min-cut theorem. Ford-Fulkerson / Edmonds-Karp algorithms.

### Key Problems and Questions

- **BFS — Shortest Path in a Grid:** A robot navigates a grid with obstacles. Find the shortest path from start to goal using BFS. Extend to weighted grids (Dijkstra). Visualize the exploration.
- **DFS — Cycle Detection in Dependencies:** A portfolio of derivatives has dependencies (e.g., a swaption depends on a swap rate, which depends on discount factors). Model as a DAG. Use DFS to detect circular dependencies. Topologically sort to determine the computation order.
- **Dijkstra — Optimal Routing:** Model a network of financial centers (nodes) with transaction costs (edge weights). Find the cheapest route to transfer funds. Implement Dijkstra with a priority queue.
- **Bellman-Ford — Negative Cycles as Arbitrage:** Model currencies as nodes and exchange rates as edge weights ($-\log(\text{rate})$). A negative cycle in this graph corresponds to a triangular arbitrage. Implement Bellman-Ford to detect and extract the arbitrage path.
- **MST — Minimum Cost Network:** A firm wants to connect $n$ offices with communication links. Each link has a cost. Find the minimum spanning tree using Kruskal's algorithm. What is the total cost?
- **Topological Sort — Task Scheduling:** A quantitative research pipeline has tasks with dependencies (data download → cleaning → feature engineering → model training → backtesting). Model as a DAG and topologically sort. Compute the critical path (longest path = minimum completion time).
- **Max-Flow — Portfolio Allocation:** Model a portfolio allocation problem as a network flow: source = cash, sink = target return, nodes = asset classes, edges = allocation limits. Find the maximum return subject to constraints using Ford-Fulkerson.
- **Connected Components — Correlation Clusters:** Build a graph where stocks are nodes and edges connect stocks with correlation > 0.7. Find connected components — each is a "correlation cluster." Compare with hierarchical clustering.
- **Bipartite Matching — Order Assignment:** Match $n$ buy orders to $n$ sell orders to maximize total surplus (buyer's price - seller's price). Model as a bipartite matching problem. Solve using the Hungarian algorithm.
- **PageRank on a Financial Network:** Model a network of banks with interbank lending as a directed graph. Compute PageRank to identify systemically important institutions. Compare with degree centrality and betweenness centrality.

---

## 4. Numerical Methods & Simulation

### Core Concepts

- **Root Finding:**
  - *Bisection:* Bracket a root, halve the interval. Convergence: linear, $O(\log(1/\epsilon))$ iterations. Robust.
  - *Newton-Raphson:* $x_{n+1} = x_n - f(x_n)/f'(x_n)$. Quadratic convergence near the root. Requires $f'$.
  - *Secant Method:* Like Newton but approximates $f'$ with a finite difference. Superlinear convergence.
- **Numerical Integration:**
  - *Trapezoidal Rule:* $\int_a^b f \approx \frac{h}{2}\sum(f(x_i) + f(x_{i+1}))$. Error $O(h^2)$.
  - *Simpson's Rule:* Uses quadratic interpolation. Error $O(h^4)$.
  - *Gaussian Quadrature:* Optimal node placement for polynomial exactness. Very efficient for smooth integrands.
- **Random Number Generation:**
  - *Linear Congruential Generator (LCG):* $X_{n+1} = (aX_n + c) \mod m$. Simple but has known flaws (hyperplane structure).
  - *Mersenne Twister:* Period $2^{19937} - 1$. The standard PRNG in most languages.
- **Inverse Transform Sampling:** If $U \sim \text{Uniform}(0,1)$, then $X = F^{-1}(U)$ has CDF $F$.
- **Acceptance-Rejection Method:** Sample from a proposal distribution and accept/reject based on the target density ratio.

### Key Problems and Questions

- **Newton-Raphson — Implied Volatility:** Implement Newton-Raphson to solve $\text{BS}(\sigma) = V_{\text{market}}$ for $\sigma$. Use Vega as the derivative. Handle convergence failures (negative vol, non-convergence). Compare with Brent's method for robustness.
- **Bisection — Bond Yield:** Given a bond price, find the yield-to-maturity by bisecting on the discount rate $y$ in $P = \sum c_i / (1+y)^{t_i}$. Implement with tolerance $10^{-10}$.
- **Secant Method — Rate Calibration:** Calibrate a Hull-White short rate model parameter by matching a market swaption price. Use the secant method (no analytical derivative of swaption price w.r.t. parameter).
- **Trapezoidal vs. Simpson's — Option Pricing Integral:** Price a European call using numerical integration of the risk-neutral expectation: $C = e^{-rT}\int_K^\infty (S - K) f(S) dS$. Compare trapezoidal and Simpson's for accuracy. How many points are needed for 4-digit accuracy?
- **Gaussian Quadrature — Characteristic Function Pricing:** Implement Gauss-Legendre quadrature for the Carr-Madan FFT pricing integral. Compare accuracy with trapezoidal rule for the same number of function evaluations.
- **LCG Implementation — Pitfalls:** Implement a simple LCG with parameters $a = 1103515245$, $c = 12345$, $m = 2^{31}$. Generate 10,000 "random" numbers. Plot pairs $(X_n, X_{n+1})$ and observe the hyperplane structure. Compare with Mersenne Twister.
- **Inverse Transform Sampling — Exponential:** Generate $\text{Exp}(\lambda)$ samples from $U \sim \text{Uniform}(0,1)$ via $X = -\ln(U)/\lambda$. Verify the sample mean and variance. Extend to generating normal samples via Box-Muller.
- **Acceptance-Rejection — Gamma Distribution:** Generate $\text{Gamma}(\alpha, 1)$ samples for non-integer $\alpha$ using acceptance-rejection with an exponential proposal. Compute the acceptance rate. Compare efficiency with inverse CDF (which requires numerical inversion).
- **Finite Differences — Greeks Computation:** Compute Delta by $\Delta \approx (V(S+h) - V(S-h))/(2h)$ and Gamma by $\Gamma \approx (V(S+h) - 2V(S) + V(S-h))/h^2$. Study the tradeoff: smaller $h$ reduces truncation error but increases rounding error. Find the optimal $h$.
- **Richardson Extrapolation — Accelerating Convergence:** If a numerical method has error $O(h^p)$, combine two estimates at step sizes $h$ and $h/2$ to cancel the leading error term: $\hat{V} = (2^p V_{h/2} - V_h)/(2^p - 1)$. Apply to accelerating convergence of binomial tree prices.

---

## 5. Complexity & Big-O Analysis

### Core Concepts

- **Big-O Notation:** $f(n) = O(g(n))$ if $f(n) \le c \cdot g(n)$ for large $n$. Describes the worst-case growth rate.
- **Common Complexities:** $O(1)$ (constant) < $O(\log n)$ < $O(n)$ < $O(n \log n)$ < $O(n^2)$ < $O(n^3)$ < $O(2^n)$ < $O(n!)$.
- **Time vs. Space Complexity:** Time = number of operations. Space = memory used. Often a tradeoff between the two.
- **Amortized Analysis:** The average cost per operation over a worst-case sequence of operations. Example: dynamic array resizing is $O(1)$ amortized per append, even though individual appends are occasionally $O(n)$.
- **NP-Completeness:** A class of problems where no polynomial-time algorithm is known. Important for recognizing when a problem is "hard" and heuristics/approximations are needed.

### Key Problems and Questions

- **Complexity Classification:** For each operation, state the time complexity: (a) binary search in a sorted array, (b) inserting into a balanced BST, (c) matrix multiplication ($n \times n$), (d) computing the determinant, (e) solving a tridiagonal system, (f) FFT of length $n$.
- **Monte Carlo Complexity:** Monte Carlo convergence is $O(1/\sqrt{N})$ in standard error. How many paths to achieve $10^{-4}$ accuracy? With a variance reduction that halves the variance, how does the required $N$ change?
- **Curse of Dimensionality:** PDE methods for option pricing on $d$ assets require $O(n^d)$ grid points. For $n = 100$ and $d = 5$, how many points? At what $d$ does Monte Carlo become preferable? (Answer: roughly $d \ge 3$–$4$.)
- **Amortized Analysis — Dynamic Array:** A dynamic array doubles in size when full. Show that $n$ appends cost $O(n)$ total, so each append is $O(1)$ amortized, using the accounting or potential method.
- **Space-Time Tradeoff — Memoization:** Computing Fibonacci naively is $O(2^n)$ time, $O(n)$ space. Memoization is $O(n)$ time, $O(n)$ space. Bottom-up with rolling variables is $O(n)$ time, $O(1)$ space. Implement all three and benchmark.
- **Complexity of Financial Algorithms:** State the complexity of: (a) binomial tree pricing ($O(n^2)$ for $n$ steps), (b) Monte Carlo pricing ($O(N \cdot M)$ for $N$ paths, $M$ time steps), (c) Crank-Nicolson FDM ($O(n_S \cdot n_t)$), (d) LU decomposition ($O(n^3)$), (e) Cholesky ($O(n^3/3)$).
- **NP-Hard in Finance — Portfolio Optimization with Cardinality Constraints:** Mean-variance optimization is convex ($O(n^3)$). Adding the constraint "hold at most $k$ assets" makes it NP-hard (combinatorial). Implement a greedy heuristic and compare with brute-force for small $n$.
- **Parallelism and Amdahl's Law:** A Monte Carlo simulation takes 100 seconds on 1 core. The path generation (90%) is parallelizable; aggregation (10%) is serial. With $p$ cores, the speedup is $1/(0.1 + 0.9/p)$. Plot speedup vs. $p$. What is the maximum speedup?
- **Streaming Algorithms — Online Variance:** Compute the mean and variance of a data stream in one pass using Welford's online algorithm. Show it is numerically stable (unlike the naive two-pass formula). Implement and test on $10^7$ values.
- **Profiling and Optimization:** Write a naive Monte Carlo pricer. Profile it (`cProfile`). Identify the bottleneck. Optimize using vectorization (`numpy`), then further with `numba` JIT. Measure speedup at each stage.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Algorithm design** — pseudocode and complexity analysis first.
> 2. **Implementation** — build using core Python, `numpy`, `scipy`, `heapq`, `collections`.
> 3. **Benchmarking** — measure runtime vs. input size, verify theoretical complexity, profile bottlenecks.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

