---
type: prep-route
name: Route 3 — Coding and problem solving
status: active
opened: 2026-08-19
gates: [hackerrank, coderpad]
---

# Route 3 — Coding and problem solving

**Two gates, two different skills. Do not train them the same way.**

| | HackerRank | CoderPad |
|---|---|---|
| Format | Take-home, timed, alone | **Live, watched, talking** |
| Fails you by | Not finishing, wrong complexity | Silence, freezing, not explaining |
| Trains by | Volume — `leetcode_list.md` | **Talking out loud while typing** |
| Weight | The filter | **The main dish** |

**You already identified the asymmetry correctly.** The take-home is a volume problem. The live
round is a *performance* problem, and performance does not come from more LeetCode — it comes from
practising the performance.

---

## 3A. HackerRank — the take-home

**Drill list:** [`leetcode_list.md`](leetcode_list.md). 30-minute scrap slots, one problem each.

**Tier 0 first, always** — those six close your literal baseline zeros (Two Sum at O(n²), BFS
unknown, DP unknown). **Tier 0 + Tier 1 = 16 problems ≈ 8h**, and that is the whole HackerRank prep
if it lands next week.

### HackerRank-specific, beyond the drill list
- [ ] **Practise in the actual editor.** No autocomplete, no linter, no debugger. Do three
      problems in a plain text editor before test day — the interface *is* part of the test
- [ ] Read the input format carefully; HackerRank often supplies a stub with parsing done. Losing
      time to I/O is the most common avoidable failure
- [ ] **Manage the clock:** if a problem is not falling in the allotted slice, write the brute
      force, get partial credit, move on. A brute force scoring 60% beats an unfinished optimum
- [ ] Test on edge cases before submitting: empty, single element, all-equal, negatives, overflow
- [ ] Expect **quant-flavoured variants** — running statistics, a trading-P&L simulation, a
      matrix/portfolio computation. Tier 6 of the drill list is exactly this

---

## 3B. CoderPad — the main dish ⭐⭐

> **This is where you win or lose, and it is the least trainable by silent practice.**
> A correct silent solution loses to a clear narrated near-solution. That is not a cliché — it
> is what the interviewer is scoring.

### The protocol — run it every single time, including alone

1. **Restate the problem in one sentence.** Ask one clarifying question, even if you do not need
   to — input size, duplicates, empty case, return-or-mutate
2. **Say the brute force out loud, with its complexity.** *"Naively this is O(n²) because…"* —
   this alone banks credit before you write anything
3. **State the target complexity and the idea before typing.** *"I think we can get O(n) with a
   hash map, because…"* — the interviewer can now correct you *cheaply*, which is a good outcome
4. **Type, narrating.** Say what each block does as you write it. Silence over 15 seconds is the
   failure mode
5. **Walk a small example through the finished code, out loud, by hand.** Catches most bugs and
   demonstrates the skill they are actually testing
6. **State final complexity, time and space.** Then say one limitation and one improvement

> **The graded habit from your own baseline:** X.1 was a correct answer at the wrong complexity.
> Step 3 is the fix, and it is a *speech* habit, not a coding one.

### Training the performance, not the problem
- [ ] **Talk out loud, alone, every session.** Feels absurd. It is the entire intervention. The
      failure mode is that your first-ever narrated solution happens in front of the interviewer
- [ ] **Record one session a week** (phone, 20 min). Watch it back once. You will hear the silences
- [ ] **Re-solve an already-solved problem while narrating.** The point is the narration, not the
      problem — a known problem is *better* for this, because attention goes to the talking
- [ ] Practise being wrong on purpose: state an approach, have it not work, say *"that does not
      handle X, let me adjust"* out loud. **Recovering visibly is a scored behaviour**
- [ ] Practise typing without running: write 20 lines, then predict the output before executing

### Live-round specifics
- [ ] No autocomplete. Know `collections`, `heapq`, `bisect`, `itertools` by memory
- [ ] Sane naming under pressure — `left/right`, `seen`, `count`, not `a/b/tmp`
- [ ] If stuck: **say what you are stuck on.** *"I need a way to look this up in O(1) — a set?"*
      Interviewers hint when they can hear the problem. They cannot hint at silence
- [ ] Expect a **follow-up extension** — "now what if the data is streaming / too big for memory /
      needs to be online". Tier 6's streaming problems are the preparation for this
- [ ] They may ask you to **write a test.** Have a habit: one normal case, one edge, one degenerate

---

## 3C. Python fluency — the substrate

> Gap (b), from your own list. Slang is fine at GS and worth nothing here.

- [ ] `Counter`, `defaultdict`, `deque`, `heapq`, `bisect`, `itertools` — from memory, no lookup
- [ ] Comprehensions, unpacking, `enumerate`, `zip`, `sorted(key=)`, slicing
- [ ] numpy: vectorised ops, broadcasting, `@`, axis semantics, `np.linalg.{cholesky,eig,inv}`
- [ ] pandas: `groupby`, `rolling`, `merge`, `pct_change`, `shift` *(and why `shift` is the
      look-ahead-bias guard — a risk answer disguised as a pandas answer)*
- [ ] **The one habit to build:** reach for a `dict`/`set` before a nested loop. Baseline X.1 is
      exactly this reflex missing

**Cheapest fix available to you:** write your GS work in Python. Any small analysis you would do in
Slang, do twice. Real problems build fluency faster than exercises, and you have a supply of them.

---

## 3D. Quant coding — where the two routes meet

Tier 6 of `leetcode_list.md`, and the Unit A code problems from Route 2. **Every one lands in
`code/codify.ipynb` under `# Citadel`** — closed form, independent verifier, complexity docstring,
`assert`. Repo convention, and it doubles as curriculum output so the fork is not lost work.

**The highest-value single artifact in this whole prep:** rebuild your VaR surface in Python.
Small `Σ`, a grid of `(x, y)` position additions, the what-if VaR in each cell, component VaR
summing to the total as the verifier. It is your story, in their language, runnable. If a CoderPad
round goes well and there is time at the end, it is also the thing you mention having built.

---

## Weekly shape

| | HackerRank track | CoderPad track |
|---|---|---|
| Volume | 4–5 problems/week, scrap slots | 1–2 narrated sessions/week, prime |
| Focus | Tier 0 → 1 → 6 → 2 → 3 → 4 → 5 | Re-solve solved problems, out loud |
| Check | Box ticked, complexity stated | One recording watched back per week |

**If the process moves fast, drop the HackerRank track's later tiers before dropping the narration
practice.** Tiers 4–5 are insurance; the narration is the main dish.
