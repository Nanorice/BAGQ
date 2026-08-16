# Section XII: Game Theory & Mechanism Design — Detailed Problem List

> *Foundation: Nash equilibrium, minimax theorem, auction theory*

Game theory models strategic interaction between rational agents — a natural framework for trading, market microstructure, auction design, and competitive decision-making. Quant interviews test your ability to reason about incentives, equilibria, and optimal strategies when your payoff depends on what others do.

---

## 1. Two-Player Zero-Sum Games

### Core Concepts

- **Zero-Sum Game:** One player's gain is the other's loss. Represented by a payoff matrix $A$ where player 1 wants to maximize and player 2 wants to minimize.
- **Minimax Theorem (von Neumann):** In any finite zero-sum game, $\max_x \min_y x^T A y = \min_y \max_x x^T A y = v^*$ (the value of the game). Both players have optimal mixed strategies.
- **Pure Strategy Nash Equilibrium:** A pair of strategies where neither player can improve by unilaterally deviating. Exists when there is a saddle point in the payoff matrix.
- **Mixed Strategy:** A probability distribution over pure strategies. Every finite game has at least one Nash equilibrium in mixed strategies.
- **Dominated Strategies:** A strategy is dominated if another strategy gives a weakly better payoff in every scenario. Iteratively eliminating dominated strategies can simplify the game.

### Key Problems and Questions

- **Rock-Paper-Scissors:** Write the $3 \times 3$ payoff matrix. Show there is no pure strategy NE. Derive the unique mixed strategy NE: $(1/3, 1/3, 1/3)$ for both players. Value of the game: 0.
- **Matching Pennies:** Player 1 wins if coins match, Player 2 wins if they differ. Write the $2 \times 2$ matrix. Derive the mixed NE: $(1/2, 1/2)$. Show any deviation from 50/50 is exploitable.
- **Colonel Blotto Game:** Two players allocate $N$ troops across $k$ battlefields. The player with more troops in a battlefield wins it. Find the equilibrium allocation for $k = 3$ and $N = 6$. Discuss the continuous version. Relate to resource allocation in multi-asset trading.
- **Minimax via Linear Programming:** Any zero-sum game can be solved as an LP. Formulate and solve a $3 \times 4$ game using `scipy.optimize.linprog`. Extract both players' optimal mixed strategies and the game value.
- **Simplified Poker (Kuhn Poker):** Three cards (K, Q, J), two players, one card each. One round of betting. Derive the Nash equilibrium (involves bluffing with J). Show the optimal bluffing frequency. Implement and verify by simulation.
- **Iterated Elimination of Dominated Strategies:** Given a $4 \times 4$ game, iteratively eliminate strictly dominated strategies. Show the remaining game has a clear NE. Does the order of elimination matter? (For strict dominance: no.)
- **Game of Chicken (Hawk-Dove):** Two traders race to execute a large order. If both rush (Hawk), both suffer impact costs. If one yields (Dove), the other profits. Write the payoff matrix. Find both pure and mixed NE. Compute the expected payoff under the mixed NE.
- **Penalty Kicks — Mixed Strategy Equilibrium:** A kicker chooses left/right, a goalie dives left/right. Payoffs are asymmetric (kicker is better on their strong side). Derive the mixed NE. Show the kicker mixes non-uniformly. Compare with empirical data from professional soccer.
- **Value of Information in a Zero-Sum Game:** In a $2 \times 2$ game, player 1 can "spy" and learn player 2's strategy before choosing. What is the value of this information? Compute the game value with and without information. Show the improvement equals the value of the spy.
- **Repeated Zero-Sum Games — Fictitious Play:** Two players repeatedly play a $3 \times 3$ game. Each plays the best response to the opponent's empirical frequency. Implement fictitious play. Show convergence to the NE mixed strategies (for zero-sum games, this is guaranteed).

---

## 2. Non-Zero-Sum Games & General Equilibria

### Core Concepts

- **Nash Equilibrium (General):** A strategy profile where no player can unilaterally improve. Every finite game has at least one NE (possibly mixed).
- **Prisoner's Dilemma:** Both players defecting is the unique NE, even though mutual cooperation is Pareto-superior. The tension between individual and collective rationality.
- **Coordination Games:** Multiple NE exist; the challenge is coordinating on one. Examples: battle of the sexes, stag hunt.
- **Correlated Equilibrium:** A generalization of NE where a mediator recommends strategies. Can achieve outcomes outside the convex hull of NE payoffs.
- **Evolutionary Game Theory:** Strategies evolve via replication dynamics. An Evolutionarily Stable Strategy (ESS) resists invasion by mutants.

### Key Problems and Questions

- **Prisoner's Dilemma — Single and Repeated:** Write the payoff matrix. Show (Defect, Defect) is the unique NE. In the infinitely repeated game with discount factor $\delta$, show that cooperation is sustainable via tit-for-tat if $\delta$ is large enough. Derive the threshold $\delta^*$.
- **Battle of the Sexes — Multiple Equilibria:** Two traders must coordinate on a trading venue (exchange A or B). Each prefers a different one, but both prefer coordination over miscoordination. Find all three NE (two pure, one mixed). Compute expected payoffs.
- **Cournot Duopoly — Quantity Competition:** Two firms choose quantities $q_1, q_2$. Price $P = a - b(q_1 + q_2)$. Cost $c$ per unit. Derive the best-response functions $q_i^*(q_j) = (a - c - bq_j) / (2b)$. Find the NE. Compare with monopoly and perfect competition.
- **Bertrand Competition — Price War:** Two firms choose prices. Consumers buy from the cheapest. Show the NE is $p_1 = p_2 = c$ (marginal cost), yielding zero profit — the "Bertrand paradox." How do product differentiation or capacity constraints resolve it?
- **Stackelberg Leadership — First-Mover Advantage:** In Cournot, firm 1 moves first (commits to $q_1$), then firm 2 responds. Solve by backward induction. Show the leader produces more and earns more than in the simultaneous game.
- **Correlated Equilibrium — Traffic Game:** Two drivers choose routes. A traffic light (mediator) sends private signals. Show a correlated equilibrium that achieves higher total payoff than any NE. Implement and compute the optimal correlation device via LP.
- **Stag Hunt — Risk Dominance vs. Payoff Dominance:** Two hunters can hunt a stag (cooperative, high payoff) or a hare (safe, low payoff). Stag hunt requires coordination. Find both pure NE and the mixed NE. Discuss risk dominance (which NE is "safer"?) vs. payoff dominance.
- **Market Entry Game:** $n$ firms simultaneously decide whether to enter a market. If $k$ firms enter, each earns $\pi(k)$ (decreasing in $k$). What is the symmetric mixed NE? Compute the expected number of entrants and the probability of each outcome.
- **Replicator Dynamics — Hawk-Dove Revisited:** Model a population where strategies evolve. Hawks fight and share; Doves yield. Write the replicator equation $\dot{x} = x(f_H - \bar{f})$. Find the ESS. Show it corresponds to the mixed NE. Simulate the dynamics.
- **Mechanism Design — Revelation Principle:** Design a trading mechanism where agents truthfully reveal their valuations. State the revelation principle: any mechanism can be replicated by a direct mechanism where truth-telling is optimal. Illustrate with a simple bilateral trade example.

---

## 3. Auction Theory

### Core Concepts

- **First-Price Sealed-Bid Auction:** Highest bidder wins, pays their bid. Bidders shade their bids below their valuations.
- **Second-Price Sealed-Bid (Vickrey) Auction:** Highest bidder wins, pays the second-highest bid. Dominant strategy: bid your true valuation.
- **English Auction (Ascending):** Price rises until one bidder remains. Strategically equivalent to Vickrey auction.
- **Dutch Auction (Descending):** Price drops until someone claims. Strategically equivalent to first-price sealed-bid.
- **Revenue Equivalence Theorem:** Under standard assumptions (risk-neutral bidders, independent private values, symmetric), all four standard auctions yield the same expected revenue to the seller.
- **Winner's Curse:** In common-value auctions, winning implies you likely overestimated the value. Rational bidders shade their bids to account for this.
- **Optimal Auction (Myerson):** The seller can maximize expected revenue by setting a reserve price. Myerson's theorem gives the optimal mechanism.

### Key Problems and Questions

- **Vickrey Auction — Dominant Strategy:** Prove that in a second-price auction, bidding your true value is a dominant strategy regardless of what others do. Show the proof by considering the cases where you win and lose.
- **First-Price Auction — Equilibrium Bidding:** $n$ bidders with i.i.d. values $\sim \text{Uniform}(0,1)$. Derive the symmetric BNE bid function $b(v) = v \cdot (n-1)/n$. Verify: with 2 bidders, you bid half your value. With 10 bidders, you bid 90% of your value. Simulate and verify.
- **Revenue Equivalence — Verification:** Simulate 10,000 instances of both first-price and second-price auctions with $n = 5$ bidders, values $\sim \text{Uniform}(0,1)$. Compute expected revenue for each. Verify they are approximately equal ($E[\text{revenue}] = (n-1)/(n+1)$).
- **Reserve Price — Optimal Auction:** A seller faces 2 bidders with values $\sim \text{Uniform}(0,1)$. Show the optimal reserve price is $r = 1/2$ (Myerson). Compute the expected revenue with and without the reserve. The reserve increases revenue despite sometimes resulting in no sale.
- **Winner's Curse — Common Value Auction:** Two bidders estimate the value of an oil field. True value $V = (s_1 + s_2)/2$ where $s_i \sim \text{Uniform}(V - \epsilon, V + \epsilon)$. A naïve bidder bids $s_i$ — show this leads to a loss on average (winner's curse). Derive the equilibrium bid function that accounts for the curse.
- **All-Pay Auction — Lobbying Model:** All bidders pay their bid, but only the highest bidder wins. Derive the symmetric BNE for 2 bidders with values $\sim \text{Uniform}(0,1)$: $b(v) = v^2 / 2$. Expected revenue equals the expected value of the highest bidder (same as other auctions by revenue equivalence!).
- **Multi-Unit Auction — Discriminatory vs. Uniform Price:** A seller has $k$ identical units. Bidders submit demand curves. Compare discriminatory pricing (each winner pays their bid) vs. uniform pricing (all winners pay the clearing price). Which yields more revenue? Simulate for $k = 5$, $n = 20$.
- **Auction with Risk-Averse Bidders:** Bidders have CRRA utility $u(x) = x^{1-\gamma}/(1-\gamma)$. Show that first-price auction revenue exceeds second-price when bidders are risk-averse (revenue equivalence breaks). Derive the equilibrium bid function and compare.
- **Double Auction — Bilateral Trade:** A buyer values a good at $v_B \sim \text{Uniform}(0,1)$ and a seller at $v_S \sim \text{Uniform}(0,1)$. They simultaneously submit bids. Trade occurs if $b_B \ge b_S$ at price $(b_B + b_S)/2$. Derive the linear BNE. Show that not all efficient trades occur (Myerson-Satterthwaite theorem).
- **Auction Design for Treasury Bonds:** The US Treasury uses a uniform-price auction for bonds. Model with 10 bidders submitting demand schedules. Simulate the auction. Compare revenue with a discriminatory auction. Discuss strategic demand reduction.

---

## 4. Cooperative Games & Fair Division

### Core Concepts

- **Characteristic Function Form:** A cooperative game is defined by a value function $v(S)$ for each coalition $S \subseteq N$. The question: how should the total value $v(N)$ be divided?
- **Shapley Value:** $\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(n-|S|-1)!}{n!} [v(S \cup \{i\}) - v(S)]$. The unique fair allocation satisfying efficiency, symmetry, dummy player, and additivity axioms.
- **Core:** The set of allocations $(x_1, \ldots, x_n)$ with $\sum x_i = v(N)$ and $\sum_{i \in S} x_i \ge v(S)$ for all coalitions $S$. No coalition has an incentive to break away. The core may be empty.
- **Nucleolus:** The allocation that lexicographically minimizes the maximum "unhappiness" (excess) of any coalition. Always unique and in the core (when the core is non-empty).

### Key Problems and Questions

- **Shapley Value — Airport Cost Sharing:** Three airlines use a runway. Airline A needs 1 km, B needs 2 km, C needs 3 km. The runway costs $v(\{C\}) = 3$M. Compute the Shapley value for each airline. Show it's "fair": each pays their marginal contribution averaged over all orderings.
- **Shapley Value — Voting Power:** A weighted voting game: player weights $(4, 3, 2, 1)$, quota $= 6$. Compute the Shapley-Shubik power index for each player. Show that player 4 (weight 1) has zero power (dummy player). Compare with the Banzhaf power index.
- **Cost Allocation in a Supply Chain:** Three firms share a warehouse. Costs: $v(\{1\}) = 10$, $v(\{2\}) = 12$, $v(\{3\}) = 15$, $v(\{1,2\}) = 18$, $v(\{1,3\}) = 20$, $v(\{2,3\}) = 22$, $v(\{1,2,3\}) = 25$. Compute the Shapley value. Check if it's in the core.
- **Core — Existence and Emptiness:** Construct a 3-player game where the core is empty (e.g., a majority voting game). Show that no allocation satisfies all coalition constraints simultaneously. What does this mean practically?
- **Shapley Value for Feature Attribution (SHAP):** In machine learning, SHAP values attribute a model's prediction to each feature using the Shapley value framework. Implement for a simple 3-feature linear model. Verify that SHAP values sum to the prediction minus the baseline.
- **Profit Allocation in a Trading Desk:** A trading desk has three traders. Profits: trader 1 alone = \$2M, trader 2 alone = \$3M, trader 3 alone = \$1M. Pairs: {1,2} = \$7M, {1,3} = \$4M, {2,3} = \$5M. All three: \$10M. Compute the Shapley value bonus for each trader.
- **Nash Bargaining Solution:** Two players bargain over splitting \$1. Disagreement payoffs $(d_1, d_2)$. The Nash bargaining solution maximizes $(u_1 - d_1)(u_2 - d_2)$. Derive the solution for linear utilities. What if utilities are concave (risk-averse)?
- **Fair Division — Cake Cutting:** Divide a heterogeneous resource (a "cake") among $n$ players with different valuations. Implement the "I cut, you choose" protocol for 2 players. For $n > 2$, implement the Selfridge-Conway protocol. Is the allocation envy-free?
- **Nucleolus — Computation:** For the 3-player game above, compute the nucleolus by solving a sequence of LPs. Compare with the Shapley value. When do they coincide?
- **Coalition Formation — Hedging Consortium:** $n$ firms each have risk exposures. By forming coalitions, they can hedge more efficiently (diversification). Define $v(S)$ as the reduction in VaR from joint hedging. Compute the Shapley value to allocate the hedging benefit. Show larger firms contribute more to diversification.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive equilibria, bid functions, and Shapley values by hand.
> 2. **Numerical implementation** — solve games via LP (`scipy.optimize.linprog`), simulate auctions, compute power indices.
> 3. **Simulation** — verify theoretical predictions (revenue equivalence, equilibrium convergence, winner's curse) via Monte Carlo.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

