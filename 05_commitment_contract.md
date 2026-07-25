# Commitment Contract — With Yourself

> Fill this in during **Week 1**. Renegotiate at the end of **each month**.
> Save signed versions as `progress/contracts/contract_YYYY-MM-DD.md`.

---

## Section A — Time audit (do this before signing)

### A.0 Time-shape principle (read first)

**Not all hours are equal.** Two activities have opposite cognitive profiles:

| Activity | Mode | Preferred time-shape |
|---|---|---|
| **Learning** (Feynman notes, derivations, problems) | Deep, continuous, holds state in working memory | **Prime blocks** ≥ 60 min, low-fatigue |
| **Quantamental / vibe-coding** | Shallow, interruptible, LLM caches state for you | **Scrap slots** 15–45 min, any energy level |

**Allocation rules:**

1. **Learning gets prime slots. Quantamental gets scraps.** Never invert.
2. **Minimum viable learning block = 60 min.** Below that, use the slot for one of:
   - Reviewing an old Feynman note (spaced repetition)
   - Passive reading (Hull / Shreve / a paper) — input only, Step 1 of Feynman
   - LeetCode-easy from Section X
   - Weekly review logging
3. **Weekly quota, not daily quota, for learning.** Any given weekday may be zero if the weekly total is protected.
4. **Cap quantamental with a weekly ceiling** (e.g., ≤ 6 h/week) — vibe-coding expands to eat prime slots because it feels productive without being tiring. Don't let it.
5. **One-block-per-topic rule.** A stage's *learning phase* (Feynman Steps 1–2) should fit in one 90-min block. If it doesn't, the stage is scoped too big — split it.
6. **Cold-start tax hack.** Start every deep block by re-reading the last 5 lines of your previous Feynman note out loud. 90 seconds to reload state vs. 20 minutes cold.

### A.1 Weekly fixed / semi-fixed hours

| Bucket | Hours / week | Notes |
|---|---:|---|
| Sleep | 56 | 8 h/night × 7 — non-negotiable |
| Work + commute | 45 | 9:30–18:30 × 5 days |
| Meals + chores + admin | 12 | Dinner ~1.25 h × 7 + chore ~0.5 h × 7 (lunch inside work block) |
| Exercise | 4.5 | 60 min × 4–5 days |
| Relationships / social | 1 | ~4 h / month, non-routine |
| Entertainment (gaming, movies, dessert/screen time while eating) | 7 | Fuzzy floor, not ceiling — the most elastic bucket; monitor in weekly review |
| Quantamental project | 6 | See A.1a for how these 6 h are shaped |
| **Subtotal fixed** | **131.5** | |
| **Discretionary = 168 − 131.5** | **36.5** | pool for learning + slack |

#### A.1a — Quantamental operating mode (locked in)

Quantamental runs in **agent-driven scrap mode**, not deep-work mode:

- **Slot shape:** 2–3 × 15 min slots per weekday (~5 h/week) + one 1–2 h planning/scheduling block on the weekend (~1–2 h). Total cap: **6 h/week**.
- **Weekday mechanics:** prompt-and-leave. Write the prompt, hand it to the agent, close the laptop. Multiple sessions can run in parallel as long as the *prompts* were planned in advance.
- **Weekend mechanics:** batch-plan the coming week's prompts, review agent output, prune backlog, commit merged work. This is the only "prime-ish" quantamental time and it stays under 2 h.
- **Overlap credit:** work that touches Section IX (regression, time-series, GARCH) or Section X (numerical methods, backtesting infra) can be *dual-counted* as code-twin deliverables — log it in the relevant stage's `progress/` folder to claim credit.
- **Hard rule:** no quantamental in weekday morning slots. Those belong to learning.

### A.2 Discretionary split (36.5 h)

| Bucket | Prime hours (≥60 min blocks) | Scrap hours (<60 min) | Total |
|---|---:|---:|---:|
| Learning system | 11 | 3 (reviews / LeetCode / passive reading) | 14 |
| Slack / rest / spontaneous | — | — | ~10 |
| **Sub-allocated** | **11** | **3** | **24** |
| **Remaining buffer** (life, unplanned, entertainment overflow) | — | — | **~12.5** |

**Sanity check:** 11 prime learning hours ≥ 8 → passes the Q1-2027 reality-check threshold ✓.
The ~12.5 h buffer absorbs travel, sickness, mood dips, social overflow, and entertainment creep without triggering circuit breakers.

---

## Section B — Goal declaration

- **Target first interview date:** **2027-01-15** (25-week runway from 2026-07-23)
- **Target roles:** **Buy-side QR / systematic PM** (primary) + **HFT / market-making** (secondary). Excludes: sell-side structuring, sales-strat, pure risk roles.
- **Definition of success:**
  - *External:* pass ≥ 1 onsite loop; secure ≥ 2 first-round interviews.
  - *Internal (the real one):* **walk into any interview room with quiet confidence** — no impostor spiral, no bluffing, able to say "I don't know" without shame because I know what I *do* know is solid. Confidence sourced from *demonstrated* mastery (Feynman notes + working solvers + passed unlock tests), not from cramming the night before.
- **Definition of acceptable failure:** complete Tier 1 + Tier 2 stages of the DAG (S1–S4, S7–S10 core) with passing unlock tests, even if no offer materialises. Re-interview cycle in Q3-2027 with a stronger portfolio.

---

## Section C — Weekly cadence

**Design principle:** pair back-to-back weekday prime blocks + one long weekend block. Do NOT scatter single 90-min blocks across all 7 days — half of each would be spent on cold-start reload.

### Reference template (adjust hours to your chronotype; keep the SHAPE)

| Day | Prime block (Learning) | Scrap time |
|---|---|---|
| Mon | 90 min — new topic input (Feynman Step 1) | 3 × 15 min quantamental prompts · lunch 20 min: LeetCode-easy |
| Tue | 90 min — Feynman note draft (Steps 2–3) | 3 × 15 min quantamental prompts |
| Wed | — (rest / life / exercise) | 2 × 15 min quantamental prompts |
| Thu | 90 min — problems + code twin solvers | 3 × 15 min quantamental prompts · lunch 20 min: spaced-rep review |
| Fri | — (rest / life) | 2 × 15 min quantamental prompts |
| Sat | 3 h — unlock-test prep or capstone push | 1–2 h quantamental planning + review |
| Sun AM | 2 h — unlock test + spaced-rep reviews | — |
| **Sun 17:30–18:00** | — | **WEEKLY REVIEW ritual (mandatory)** — see Section D |

**Totals:** ~11 h/week learning-prime + ~3 h/week learning-scrap + ~6 h/week quantamental-scrap + built-in slack (Wed/Fri evenings, most of Sun).

### Two invariants (do not violate)

1. **Learning contact ≥ 5 days/week.**
   *Definition:* "learning contact" = **any deliberate touch with study material that day**, however brief. A 90-min derivation counts. A 10-min re-read of last week's Feynman note counts. Answering one spaced-rep question counts. The point is *habit continuity* — preventing the cold-start decay that follows a 2–3 day gap.
2. **Sunday review, 30 min, non-negotiable.**

### Sprint cadence (2-week sprints, aligned with your existing agile system)

Learning is scheduled in **2-week sprints** that align 1:1 with your existing personal-agile cadence. Each sprint owns a slice of the traversal in `03_gated_progression.md`.

**Sprint anatomy (14 days):**

| Day | Activity |
|---|---|
| Mon (Day 1) — Sprint planning | 30 min: pick stages, define "done" per stage, write sprint goal in `progress/sprints/S<NN>.md` |
| Days 1–13 | Execute per the weekly cadence table above |
| Sun of week 1 (Day 6) | Weekly review (Section D) — mid-sprint temperature check |
| Sat/Sun of week 2 (Days 13–14) | Unlock tests + sprint demo (see below) |
| Sun of week 2 (Day 14) — Sprint retro + next planning | 60 min: retro on this sprint, plan next |

**Sprint deliverables (the "demo" at Day 13–14):**
- Every stage marked COMPLETE this sprint must have D1–D4 passed (per `04_deliverables_spec.md`)
- Sprint goal in `progress/sprints/S<NN>.md` is closed with a ✅ or ❌ and a one-paragraph retro
- If a capstone project shipped, tag the commit

**Sprint sizing rules of thumb (calibrate over first 3 sprints, then trust the number):**
- 1 sprint = ~22 h learning capacity (2 × 11 h prime + 2 × 3 h scrap, minus buffer usage)
- 1 stage ≈ 8–12 h of learning capacity (Tier 0: 4–6 h; Tier 1: 8–12 h; Tier 2/3: 12–18 h; capstone: full sprint)
- **Realistic load: 2 stages per sprint**, or 1 stage + 1 capstone if the capstone is small
- **Never plan more than 3 stages in a sprint** — velocity will collapse and you'll fail the retro

**Sprint retro (60 min, Day 14):**
1. Sprint goal: hit / missed / partial? Why?
2. Velocity: how many stages actually closed vs. planned? Update your capacity estimate.
3. What blocked or slowed you? Root cause, not symptom.
4. What worked well? Codify it into the next sprint plan.
5. Any Section F circuit breaker triggered?
6. **Plan next sprint** in `progress/sprints/S<NN+1>.md` — commit to stage list before the sprint starts.

---

## Section D — Weekly review ritual (30 min, every Sunday)

Answer these in `progress/weekly_reviews/YYYY-WW.md`:

1. **What stage(s) advanced this week?** (LOCKED → UNLOCKED → IN_PROGRESS → COMPLETE)
2. **What stalled and why?** (fatigue? unclear topic? distraction? ambiguous next step?)
3. **Hours logged vs. plan** — learning-prime, learning-scrap, quantamental. Raw honesty.
4. **The ONE thing to change next week** (single lever, not a list).
5. **Mood / energy 1–5** + any life-context for next week.
6. **Entertainment hours this week: __** (7 h floor; flag if > 10).
7. **Learning contact days this week: __/7** (target ≥ 5).

---

## Section E — Monthly review (60 min, first Sunday of each month)

1. Retake **one** unlock test from a stage completed 3+ weeks ago. Did it stick?
2. Re-audit Section A time buckets — has real life shifted?
3. Are you on track for the Q1 traversal in `03_gated_progression.md`?
   - If **> 2 weeks behind**: cut scope (defer more advanced stages) or push target date.
   - If **> 1 week ahead**: pull in one deferred stage from Tier 4.
4. Update this contract's numbers in place; snapshot to `progress/contracts/contract_YYYY-MM-DD.md`.

---

## Section F — Circuit breakers

If any of these happens, **pause and diagnose** instead of grinding:

- 3 consecutive weeks under 60% of committed learning-prime hours → time budget is wrong; renegotiate A.2.
- 2 consecutive stages fail unlock test → Feynman Step 3 is being skipped; refresh protocol.
- Mood ≤ 2 for 2 weeks → take a full week off, no guilt.
- Sunday review skipped 3× in a row → autopilot; do a full monthly review.
- Quantamental hours > 8 for 2 weeks running → scope creep; hard-reset to 6 h cap.
- Entertainment hours > 12 for 2 weeks running → territorial encroachment on prime slots; apply physical separation (blockers, different device).

---

*Version: 0.2 | Last updated: 2026-07-23*
