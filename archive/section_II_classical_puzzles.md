# Section II: Classical Probability Puzzles & Brain Teasers — Detailed Problem List

> *Foundation: Discrete probability, conditional expectation, symmetry arguments*

Classical probability puzzles are the bread and butter of quant interviews. They test your ability to model a problem precisely, identify the right conditioning variable, and compute expectations under pressure. These problems appear deceptively simple but require careful reasoning — and every one of them can be verified by simulation.

---

## 1. Dice Problems

Dice problems test combinatorial thinking, conditional expectation, and optimal decision-making under uncertainty.

### Core Concepts

- **Fair Die Distribution:** Each face has probability $1/6$; the expected value of a single roll is $3.5$.
- **Max/Min of Multiple Dice:** The CDF of the maximum of $n$ i.i.d. dice is $P(\max \le k) = (k/6)^n$. The minimum uses the complementary approach.
- **Optimal Stopping with Dice:** When offered sequential rolls with the option to stop, the decision rule compares the current roll to the expected value of continuing.
- **Non-Transitive Relations:** A set of dice where A beats B, B beats C, but C beats A — violating transitivity.

### Key Problems and Questions

- **Expected Maximum of $n$ Dice:** Roll $n$ fair dice. What is $E[\max(X_1, \ldots, X_n)]$? Derive the closed-form using $E[\max] = \sum_{k=1}^{6} [1 - (k/6)^n + ((k-1)/6)^n] \cdot k$. Compute for $n = 2, 3, 5, 10$.
- **Expected Minimum of $n$ Dice:** Roll $n$ fair dice. What is $E[\min(X_1, \ldots, X_n)]$? Show the symmetry with the max problem.
- **The Cayley-Moser Dice Problem:** You can roll a die up to $n$ times. After each roll, you can either keep the result or roll again (forfeiting the current value). What is the optimal strategy and expected payoff? Solve by backward induction for $n = 1, 2, 3, \ldots, 10$.
- **Sum of Two Dice — All Possible Totals:** What is the most likely sum of two dice? Compute the full PMF. Extend to 3, 4, 5 dice and visualize convergence to a bell curve (CLT in action).
- **Conditional Dice:** You roll two dice. Given that the sum is 9, what is the probability that one die shows a 6? Generalize: given sum $= s$, probability of at least one $k$.
- **Non-Transitive Dice (Efron's Dice):** Construct three dice A, B, C such that A beats B with probability > 1/2, B beats C with probability > 1/2, but C beats A with probability > 1/2. Verify by enumeration and simulation.
- **Sicherman Dice:** Find the unique pair of non-standard dice (with positive integer faces) that produce the same sum distribution as two standard dice. Prove uniqueness using generating functions.
- **Dice Doubling Game:** Roll a die repeatedly. After each roll, you can either collect the sum so far or double your total and roll again (but if you roll a 1, you lose everything). What is the optimal strategy?
- **Expected Rolls Until a Repeat:** Roll a fair die repeatedly. What is the expected number of rolls until you see a face you've already seen? (Birthday problem variant with 6 "days".)
- **Chuck-a-Luck:** You bet on a number 1–6. Three dice are rolled. You win $k$ dollars if your number appears on exactly $k$ dice, and lose $1$ if it appears on none. What is the expected value of this game? Is it fair?

---

## 2. Coin-Flipping Problems

Coin problems test geometric/negative binomial reasoning, pattern recognition in sequences, and clever uses of symmetry and conditioning.

### Core Concepts

- **Geometric Waiting Time:** The expected number of flips to get the first head with a fair coin is $1/p = 2$.
- **Runs and Patterns:** The expected waiting time for a specific pattern (e.g., HHH) depends on the pattern's internal structure (overlaps).
- **Symmetry and Exchangeability:** Many coin problems simplify dramatically when you notice that certain outcomes are equally likely by symmetry.
- **Von Neumann's Trick:** Extract fair bits from a biased coin by looking at pairs: HT → 0, TH → 1, discard HH and TT.

### Key Problems and Questions

- **Expected Flips to $k$ Consecutive Heads:** What is the expected number of flips of a fair coin to get $k$ heads in a row? Derive the recursion $E_k = 2E_{k-1} + 2$ with $E_1 = 2$. Solve for $k = 1, \ldots, 10$.
- **Penney's Game:** Player A chooses a 3-flip pattern (e.g., HHH). Player B then chooses a different pattern (e.g., THH). A fair coin is flipped repeatedly; the player whose pattern appears first wins. Show that B always has a winning counter-strategy. Compute the optimal response for each of A's choices.
- **Fair Coin from Biased Coin (Von Neumann):** Given a coin with $P(H) = p \neq 1/2$, generate fair coin flips. Implement and measure the expected number of biased flips per fair flip ($1/(2p(1-p))$).
- **Gambler's Ruin via Coin Flips:** A gambler starts with $a$ dollars, bets $1$ per round on a fair coin. They stop when they reach $N$ or $0$. What is the probability of reaching $N$? What is the expected duration? Solve for fair and biased coins.
- **The Ballot Problem (Coin Version):** In an election, candidate A gets $a$ votes and B gets $b$ votes ($a > b$). If votes are counted in random order, what is the probability A is strictly ahead after every vote? (Answer: $(a-b)/(a+b)$.)
- **Waiting for HT vs. HH:** Flip a fair coin repeatedly. What is the expected number of flips to see HT? To see HH? Why is HT faster (8 vs. 6 flips for HH vs. HT — wait, verify!) Resolve using Markov chains.
- **Three-Way Coin Duel (Truel):** Three players A, B, C take turns shooting (flipping coins with different success probabilities). The weakest shoots first. What is the optimal strategy for the weakest player? (Sometimes it's best to intentionally miss.)
- **Random Walk Returns:** A symmetric random walk starts at 0 with $\pm 1$ steps. What is the probability of returning to 0? What is the expected number of returns in $2n$ steps? (Answer: the walk returns with probability 1 but the expected return time is $\infty$.)
- **Matching Pennies:** Two players simultaneously show H or T. Player 1 wins if they match; Player 2 wins if they differ. What is the Nash equilibrium mixed strategy? What is the expected payoff?
- **The Coin-Tossing Martingale:** You start with $1$ and double your money on heads, lose everything on tails. Prove that $X_n = $ wealth after $n$ flips is a martingale (for a fair coin). What does optional stopping say about your expected final wealth?

---

## 3. Card & Poker Problems

Card problems test combinatorial counting with constraints, conditional probability given partial information, and the ability to handle large sample spaces systematically.

### Core Concepts

- **Standard Deck:** 52 cards, 4 suits × 13 ranks. Total 5-card hands: $\binom{52}{5} = 2{,}598{,}960$.
- **Poker Hand Rankings:** Royal Flush > Straight Flush > Four of a Kind > Full House > Flush > Straight > Three of a Kind > Two Pair > One Pair > High Card.
- **Hypergeometric Sampling:** Drawing without replacement from a finite population — the natural model for card games.
- **Conditional Probability in Card Games:** As cards are revealed, the sample space shrinks and probabilities update.

### Key Problems and Questions

- **Poker Hand Probabilities:** Compute the exact probability of each poker hand ranking (Royal Flush through High Card). Verify they sum to 1. Implement as a combinatorial calculator.
- **Texas Hold'em — Pocket Aces:** What is the probability of being dealt two aces in Texas Hold'em? Given pocket aces, what is the probability at least one more ace appears in the 5 community cards?
- **The Birthday Card Problem:** You draw cards one at a time (with replacement). What is the expected number of draws until you see a repeated rank? Compare with the birthday problem ($n = 13$ "days").
- **Expected Cards to Complete a Set:** Draw cards from a shuffled deck. How many cards must you draw (on average) to get at least one card of every suit? (Coupon collector with 4 coupons.)
- **Blackjack — Probability of Bust:** In Blackjack, you have a hand totaling 12. What is the probability of busting if you hit (draw one card)? What about a hand totaling 16? Compute for a full shoe vs. a depleted shoe.
- **Bridge — Suit Splits:** In Bridge, 13 cards are dealt to each of 4 players. Given that your partnership holds 8 cards in a suit, what is the probability the remaining 5 split 3-2 between the opponents? 4-1? 5-0?
- **The Dropped Card Problem:** A standard deck is shuffled and one card is secretly removed. You then draw cards one at a time. How many draws do you need (on average) to determine which card is missing?
- **Shuffling — Riffle Shuffle Analysis:** The Gilbert-Shannon-Reeds model: how many riffle shuffles are needed to "randomize" a deck? (Answer: ~7 for 52 cards.) Implement the model and measure total variation distance from uniform.
- **Card Counting in Blackjack:** Implement the Hi-Lo counting system. Simulate a shoe and compute the true count at each point. Show that a positive true count shifts the edge to the player.
- **The Problem of Points (Pascal & Fermat):** Two players are playing a best-of-$n$ game of cards. The game is interrupted when Player A needs $a$ more wins and Player B needs $b$ more wins. How should the stakes be divided fairly? Solve using combinations.

---

## 4. Urn & Ball Problems

Urn problems are the probabilist's laboratory — simple setups that illustrate deep concepts like exchangeability, reinforcement, and convergence.

### Core Concepts

- **Urn Model:** A container with colored balls. Balls are drawn (with or without replacement), and the composition may change dynamically.
- **Pólya Urn Scheme:** Draw a ball, note its color, return it along with $c$ additional balls of the same color. This creates reinforcement (rich-get-richer dynamics).
- **Exchangeability:** A sequence of random variables is exchangeable if its joint distribution is invariant under permutations. Pólya urn draws are exchangeable but not independent.
- **Coupon Collector Framework:** Drawing with replacement from $n$ types until all types are seen.

### Key Problems and Questions

- **Pólya Urn — Limiting Proportion:** An urn starts with 1 red and 1 blue ball. At each step, draw a ball and return it with one extra of the same color. After $n$ draws, what is $E[\text{fraction red}]$? What is the distribution of the limiting fraction? (Answer: $\text{Uniform}(0,1)$.) Simulate and plot the trajectory.
- **Coupon Collector's Problem:** There are $n$ distinct coupon types, each equally likely. What is the expected number of coupons you must collect to get all $n$? Derive $E[T] = n H_n = n \sum_{k=1}^n 1/k$. Compute the variance. Simulate for $n = 10, 50, 100$.
- **Birthday Problem:** What is the minimum number of people in a room so that the probability of a shared birthday exceeds 50%? Derive the exact formula. Generalize to $n$ possible "birthdays." Compute the expected number of people until the first match.
- **Birthday Problem — Near Matches:** What is the probability that in a group of $n$ people, at least two have birthdays within 1 day of each other? Generalize to within $k$ days.
- **Ehrenfest Diffusion Model:** $2N$ particles are divided between two containers. At each step, a particle is chosen uniformly at random and moved to the other container. Model as a Markov chain. Find the stationary distribution (Binomial). Compute expected return time to the initial state.
- **The Ballot Urn Problem:** An urn has $a$ red and $b$ blue balls ($a > b$). Balls are drawn one at a time without replacement. What is the probability that the count of red always exceeds the count of blue throughout the process?
- **Hypergeometric Urn — Quality Control:** A lot of $N$ items contains $D$ defectives. An inspector draws $n$ items. What is the probability of finding exactly $k$ defectives? What sample size is needed to detect at least one defective with 95% confidence?
- **The Banach Match Problem:** A mathematician has two matchboxes, each initially with $n$ matches. Each time he needs a match, he picks a box at random. What is the probability that when he first finds an empty box, the other contains exactly $k$ matches?
- **Two-Color Urn — Martingale:** An urn has $r$ red and $b$ blue balls. You draw without replacement. Let $M_k = $ (fraction of red among first $k$ draws). Is $\{M_k\}$ a martingale? Prove or disprove.
- **The Hopping Rabbit:** An urn has $n$ balls numbered $1$ to $n$. You draw balls one at a time without replacement. What is the expected number of "records" (draws where the number is larger than all previously drawn numbers)? (Answer: $H_n$.) Prove using indicator variables.

---

## 5. Geometric & Spatial Probability

Geometric probability problems require you to define a probability measure on continuous spaces (lengths, areas, volumes) and reason about random points, lines, and shapes.

### Core Concepts

- **Uniform Distribution on a Region:** If a point is uniformly distributed in a region $R$, then $P(\text{point} \in A) = \text{Area}(A) / \text{Area}(R)$.
- **Geometric Probability Formula:** Probability = (favorable measure) / (total measure), where "measure" can be length, area, volume, or angle.
- **Buffon's Needle:** The classic connection between geometry and probability — dropping a needle on parallel lines to estimate $\pi$.
- **Bertrand's Paradox:** The probability of a "random chord" being longer than the side of an inscribed equilateral triangle depends on how you define "random chord" — illustrating that a uniform distribution on a continuous space requires a precise specification.

### Key Problems and Questions

- **Buffon's Needle:** A needle of length $l$ is dropped on a floor with parallel lines spaced $d$ apart ($l \le d$). Derive $P(\text{crossing}) = 2l / (\pi d)$. Simulate to estimate $\pi$. Extend to $l > d$ (Buffon-Laplace).
- **Bertrand's Paradox — Three Solutions:** A chord is drawn "at random" on a unit circle. What is the probability it is longer than $\sqrt{3}$ (side of inscribed equilateral triangle)? Show three methods give three answers ($1/3$, $1/2$, $1/4$) and explain why.
- **The Broken Stick Problem:** A stick of length 1 is broken at two points chosen uniformly at random. What is the probability the three pieces can form a triangle? (Answer: $1/4$.) Solve analytically (geometric region) and verify by simulation.
- **Random Points on a Circle — Acute Triangle:** Three points are chosen uniformly on a circle. What is the probability they form an acute triangle? (Answer: $1/4$.) What about an obtuse triangle?
- **Random Points in a Square — Distance:** Two points are chosen uniformly in the unit square $[0,1]^2$. What is the expected distance between them? (Requires a 4D integral; answer $\approx 0.5214$.) Simulate to verify.
- **Meeting Problem (Rendezvous):** Two people agree to meet at a café between 12:00 and 1:00. Each arrives at a uniform random time and waits for 15 minutes. What is the probability they meet? (Answer: $7/16$.) Solve geometrically and generalize to waiting time $w$.
- **Random Triangle Area:** Three points are chosen uniformly in the unit square. What is the expected area of the triangle they form? (Answer: $11/144$.) Simulate and verify.
- **The Sylvester-Gallai Problem:** Four points are chosen uniformly in a convex region. What is the probability that one point lies inside the triangle formed by the other three? For a circle: $1 - 35/(12\pi^2)$.
- **Uniform Points on a Sphere:** Generate $n$ points uniformly on the surface of a unit sphere. What is the expected distance between two random points? (Answer: $4/3$.) Why does naïve latitude-longitude sampling fail?
- **Random Line Through a Convex Body (Cauchy's Formula):** A line is drawn uniformly at random intersecting a convex body. What is the expected length of the intersection (chord length)? Relate to Cauchy's formula: $E[\text{chord}] = \pi \cdot \text{Area} / \text{Perimeter}$.

---

> **Implementation Note:** Each problem above is designed to be codifiable in Python. Recommended approach:
> 1. **Analytical solution** — derive the answer by hand (pen-and-paper).
> 2. **Simulation** — verify via Monte Carlo simulation.
> 3. **Visualization** — plot distributions, convergence, or sensitivity to parameters.
>
> This mirrors the workflow in `src/pricer/` and `notebooks/` already established in this project.

