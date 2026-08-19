---
type: prep-list
name: Citadel — LeetCode Close List
status: active
opened: 2026-08-19
target: HackerRank screen + CoderPad round
---

# LeetCode — the close list

**Format:** 30-minute scrap slots. **One problem per slot**, Python, no exceptions.
**20 minutes stuck = open the solution**, read it, close it, retype from memory. Staring is not
studying — same rule as the stage-map drift move.

**Every solution states its complexity before you write it** *(baseline X.1: correct answer, wrong
Big-O — interviewers grade this explicitly)*.

**Not a list of 150.** These are 42 problems chosen because they are the *patterns*; the HackerRank
screen samples from this space, it does not sample from a longer list you did not finish.

**Log:** tick the box, and put the date + minutes in the margin. Wrong-first-attempt earns a `↻` —
those get a second pass a week later.

---

## Tier 0 — the baseline zeros ⚠️ do these first

> Three baseline questions scored 0–2 and every one of them is here. `X.4` is flagged in
> `CLAUDE.md` as a screen *blocker*.

- [ ] **Two Sum** *(easy)* — hash map. **Baseline X.1 scored 2: you wrote O(n²).** Write the O(n)
      one-pass version and say why the dict is the whole trick.
- [ ] **Number of Islands** *(medium)* — BFS/DFS on a grid. **Baseline X.4: "don't know what BFS
      is".** This single problem closes the blocker. Do it twice, once each way.
- [ ] **Binary Tree Level Order Traversal** *(medium)* — BFS with a queue, the canonical shape.
      `collections.deque`.
- [ ] **Coin Change** *(medium)* — **Baseline X.3 scored 0: "not familiar with DP".** The DP
      "hello world". Write the recurrence in a comment before the loop.
- [ ] **Climbing Stairs** *(easy)* — do this *before* Coin Change if DP feels alien. It is
      Fibonacci wearing a hat.
- [ ] **Longest Palindromic Substring** *(medium)* — **baseline X.2 scored 3 at O(n³)**. Redo at
      O(n²) expand-around-centre. You already have the logic; this is a complexity upgrade.

---

## Tier 1 — arrays, hashing, two pointers

> The highest-frequency screen bucket. If the HackerRank lands next week, this tier plus Tier 0
> is the whole prep.

- [ ] Contains Duplicate *(easy)* — set, one line
- [ ] Valid Anagram *(easy)* — `Counter`
- [ ] Group Anagrams *(medium)* — `defaultdict(list)`, sorted-tuple key
- [ ] Top K Frequent Elements *(medium)* — `Counter` + `heapq.nlargest`; know the bucket-sort O(n)
      alternative
- [ ] Product of Array Except Self *(medium)* — prefix/suffix, no division
- [ ] Maximum Subarray *(easy/medium)* — **Kadane.** Also the "max drawdown" question in disguise;
      say that out loud if asked
- [ ] Best Time to Buy and Sell Stock *(easy)* — running min. **Expect a finance-flavoured variant**
- [ ] Two Sum II — sorted input *(medium)* — two pointers, contrast with the hash version
- [ ] 3Sum *(medium)* — sort + two pointers + the duplicate-skip. The classic screen filter
- [ ] Container With Most Water *(medium)* — two pointers, and *why* moving the shorter side is safe

## Tier 2 — sliding window, stack, binary search

- [ ] Best Time to Buy and Sell Stock II *(medium)* — greedy
- [ ] Longest Substring Without Repeating Characters *(medium)* — the canonical window
- [ ] Minimum Window Substring *(hard)* — the window boss fight; do it once, do it late
- [ ] Valid Parentheses *(easy)* — stack
- [ ] Daily Temperatures *(medium)* — **monotonic stack.** Rolling-max-over-window pattern shows up
      constantly in market data
- [ ] Binary Search *(easy)* — write it bug-free from memory. `bisect` in real code; by hand here
- [ ] Search in Rotated Sorted Array *(medium)*
- [ ] Find Minimum in Rotated Sorted Array *(medium)*
- [ ] Koko Eating Bananas *(medium)* — **binary search on the answer.** A pattern, not a problem

## Tier 3 — heaps, intervals, sorting

> Interval and heap problems are the most finance-adjacent bucket on the whole list.

- [ ] Kth Largest Element in an Array *(medium)* — heap; know quickselect exists
- [ ] Merge Intervals *(medium)* — sort by start. Trade/position aggregation in disguise
- [ ] Insert Interval *(medium)*
- [ ] Non-overlapping Intervals *(medium)* — greedy by end time
- [ ] Meeting Rooms II *(medium)* — min-heap of end times. **The concurrent-exposure problem**
- [ ] Find Median from Data Stream *(hard)* — two heaps. **Streaming quantiles = streaming VaR.**
      Worth it for the analogy alone
- [ ] Merge k Sorted Lists *(hard)* — `heapq.merge` in practice; by hand here

## Tier 4 — DP

> Baseline scored 0 here. Six problems is enough to stop being empty; it is not enough to be good,
> and that is the right trade for August.

- [ ] House Robber *(medium)* — the second DP after Climbing Stairs
- [ ] Longest Increasing Subsequence *(medium)* — O(n²) first, then the `bisect` O(n log n)
- [ ] Unique Paths *(medium)* — grid DP
- [ ] Word Break *(medium)*
- [ ] Maximum Product Subarray *(medium)* — Kadane with a sign twist
- [ ] Longest Common Subsequence *(medium)* — the 2-D table

## Tier 5 — graphs

> Beyond the Tier 0 blocker. Thin on purpose — central risk is not a graph-heavy seat.

- [ ] Clone Graph *(medium)* — hash map + traversal
- [ ] Course Schedule *(medium)* — **cycle detection / topological sort.** The dependency-DAG
      problem; you already think in DAGs
- [ ] Rotting Oranges *(medium)* — multi-source BFS
- [ ] Pacific Atlantic Water Flow *(medium)* — reverse traversal

## Tier 6 — quant-flavoured, for the CoderPad round

> Not LeetCode-standard. CoderPad at a fund is more likely to look like these than like Tier 5.
> **Each one goes in `code/codify.ipynb` under `# Citadel`** with a verifier and an assert, per
> the repo convention.

- [ ] Rolling mean and rolling std over a stream, O(1) per update (Welford). *Then say why the
      naive two-pass version is numerically worse*
- [ ] EWMA volatility, `λ = 0.94` — write it, then vectorise it
- [ ] Historical VaR and Expected Shortfall from a return series, with a comment on why `sorted`
      is fine at this size
- [ ] Max drawdown in one pass. *(Kadane's cousin — notice that)*
- [ ] Portfolio variance `wᵀΣw` two ways: loops, then numpy. Assert they agree
- [ ] Cholesky by hand for 2×2, then correlated normal sampling from it. Verify the empirical
      correlation matches *(this is `R.linalg` B5, cashed in)*
- [ ] Simulate a fair 7-sided die from a fair 5-sided die *(**baseline X.5 scored 1** — you had
      the rejection-sampling idea and stalled. Expected ≈ 2.38 calls; verify empirically)*

---

## The 30-minute protocol

1. Read, restate the problem in one sentence, out loud
2. **State the target complexity before writing** — this is the graded habit
3. Brute force in comments if the optimal is not obvious
4. Code it. Stuck at 20 min: open the solution, close it, retype from memory
5. Tick the box, note date + minutes, `↻` if the first attempt was wrong

**If a slot is under 15 minutes**, do not start a medium. Retype a solved one from memory instead —
that is the retention half, and it is the half you are currently missing across the whole system.

---

## Order of attack

**Tier 0 → Tier 1 → Tier 6 → Tier 2 → Tier 3 → Tier 4 → Tier 5.**

Tier 6 is third because the CoderPad round is where domain knowledge stops being invisible, and
because those problems double as `code/codify.ipynb` cells for the curriculum. Tier 0 and 1 are
what a screen next week actually tests.
