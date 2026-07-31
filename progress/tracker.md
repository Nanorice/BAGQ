# Daily Tracker

> **The single artifact you open every morning.**
> Two purposes: (1) tell you what to do today, (2) capture what you actually did.
>
> Flexible time — pick blocks that fit the day. What matters is *contact ≥ 5 days/week* and *shipping the sprint deliverables by Day 14*.

---

## This week — Sprint 15 tail (2026-07-24 → 2026-08-02)

**Sprint 15 goal:** setup + baseline done ✅. Extended scope: knock out T0.C + T0.D refreshers so Sprint 16 opens with content, not setup.

**Blocks available:** Sat/Sun mornings (3h each), weekday evenings 60–90 min. Flex freely.

> ⚠️ **Re-planned 2026-07-29 (Day 10) against measured velocity.**
> First 7 days ran **5.0h** against ~13h planned = **38% of plan**. Calculus took 5h vs 4h budgeted,
> across six fragmented sittings — root cause was 7 sources across 3 media, not effort.
>
> **Fixes applied:** one source per stage (named chapter + page range, one video fallback max).
> Distributions split from a single 8h stage into two 3h day-stages, each self-contained on one
> Ross chapter — so a slipped Friday doesn't take Saturday with it.
>
> Remaining plan is **10h across 4 days** against a demonstrated ~0.7h/day. Still ambitious, and
> that is deliberate: the one-source change is untested, so this sprint measures whether it works.
> **If forced to cut, cut Continuous Distributions** (Sat) — it carries into S16 cleanly.
> Linear Algebra (Thu) is protected: it closes baseline red flags VII.1 + VII.2 and gates S1.6, S7, S9.3, S25.

### Schedule

| Date | Day | Plan | Est. | Done? |
|---|---|---|---|---|
| Fri 07-24 | 5 | T0.A/B verification ✅ · read `02_feynman_protocol.md` if not yet | 0.5h | ☐ |
| **Sat 07-25** | **6** | **T0.C Steps 1–2.** Input time-boxed 45 min (sources table in `problem_sets/T0C_calculus.md` — S2 + S5 are the non-negotiables). Then **close the source** and write §1 teach-back from memory. Then Tier-A problems A1–A6 on paper. | **3h** | ☐ |
| Sun 07-26 | 7 | **T0.C Steps 3–4.** Gap-hunt §1 (agent checks), fill gaps, write napkin + analogy + numerical anchor (verify `e¹≈2.71828`). Tier-B problems. Close the note. · **Weekly review 17:30** → `weekly_reviews/2026-W30.md` | 2.5h | ☐ |
| Mon 07-27 | 8 | **T0.D Steps 1–2.** 3B1B *Essence of LA* eps 1, 10, 11, 14. Cover: matrix mult, 2×2/3×3 determinants, eigenvalues by hand via characteristic polynomial, PSD + why covariance is PSD. Teach-back from memory. | 1.5h | ☐ |
| Tue 07-28 | 9 | **T0.D Steps 3–4.** Numerical anchor: eigenvalues of `[[2,1],[1,2]]` by hand → verify `np.linalg.eig`. *(This is baseline VII.1 — you had the definition, lost the computation.)* Close the note. | 1.5h | ☐ |
| Wed 07-29 | 10 | Rest / exercise. Scrap only: cheap-win Bayes vocabulary (30 min) — sensitivity/specificity/prevalence + the disease-test problem *(baseline I.2, scored 0)* | 0.5h scrap | ☐ |
| **Thu 07-30** | **11** | **Linear Algebra Refresher** `T0.D` — all 4 Feynman steps in one day. Green Book Ch.2 LA section, 40-min hard stop. Blocks: 08–09 read+teach-back · afternoon scrap Tier A · evening gap-hunt + Tier B + close. Set at `problem_sets/T0D_linear_algebra.md`. *If the day collapses: A1, A5, B1 only — B1 (why Σ is PSD) is the highest-value item in the stage.* | 3h | ☑ |
| Fri 07-31 | 12 | **Discrete Distributions** `S1.3` — Bernoulli, Binomial, Geometric, Poisson. **Ross 6th ed. Ch. 4**, 40-min hard stop. Each: PMF, E[X], Var, MGF, one classic problem. Poisson-as-limit-of-binomial. Set at `problem_sets/S1_3_discrete_distributions.md`. · Create `src/solvers/` (first real need) *If the day collapses: A1, A3, B1 only.* | 3h | ☐ |
| Sat 08-01 | 13 | **Continuous Distributions** `S1.5` — Uniform, Exponential, Normal. **Ross 6th ed. Ch. 5**, 40-min hard stop. Memorylessness of the exponential. Set at `problem_sets/S1_5_continuous_distributions.md`. MC verifier in `src/solvers/s1_probability/distributions_verify.py`. *(Exp is baseline I.3, scored 1 — mandatory-deep.)* *If the day collapses: A2, A3, B1 only.* | 3h | ☐ |
| Sun 08-02 | 14 | **Sprint 15 retro** (fill `sprints/S15.md` — velocity number sizes S16) · **Sprint 16 re-plan** · Weekly review · **T0.C +1wk review** (recall napkin cold) | 1.5h | ☐ |

**Planned total: ~18h across 9 days.** Against ~13h prime + 3h scrap. Expect to land short — that's the data point.

**Scrap-time backlog (fill any 15–30 min slots this week):**
- [ ] Cheap-win: coupon collector formula (20 min → `feynman_notes/cheap_wins.md`) *(baseline II.3, scored 0)*
- [ ] Cheap-win: put-call parity direction (20 min) *(VI.4, scored 1)*
- [ ] Cheap-win: Vickrey auction (20 min) *(XII, scored 0)*
- [ ] Cheap-win: Shannon entropy formula (20 min) *(XI.1, scored 0)*
- [ ] LeetCode-easy warm-up: 2 array problems (any)

---

### Actuals log — fill after every session

One row per session. Raw honesty; a 0-hour day with a reason is more useful than a blank.
`Contact?` = any deliberate touch with study material, however brief (per contract §C invariant 1).

| Date | Planned | Hrs actual | Contact? | What actually got done / what blocked |
|---|---|---:|:---:|---|
| Wed 07-23 | (pre-sprint) | 0.5 | ✅ | Baseline / setup |
| Fri 07-24 | T0.A/B | 1.0 | ✅ | T0.A/B verified |
| Sat 07-25 | T0.C S1–2 | 0 | ☐ | No session logged |
| Sun 07-26 | T0.C S3–4 | 1.5 | ✅ | T0.C teach-back §1 drafted |
| Mon 07-27 | T0.D S1–2 | 0.5 | ✅ | T0.C revisions (T0.D not started) |
| Tue 07-28 | T0.D S3–4 | 0.75 | ✅ | T0.C §1(c)(d), §3, §4, §6 filled |
| Wed 07-29 | rest/scrap | 0.75 | ✅ | **T0.C CLOSED** (5.0h total). Euler `(1+dx)^(1/dx)` insight → §6(e). archive §VIII Q1+Q3 done; PDE/2nd-order/Kelly deferred to post-S4/S6 |
| Thu 07-30 | Linear Algebra | 3.5 | ✅ | **T0.D CLOSED** — all 4 Feynman steps in one day, on plan (3h budgeted). First stage to land at full allocation. |
| Fri 07-31 | Discrete Distributions | | | |
| Sat 08-01 | Continuous Distributions | | | |
| Sun 08-02 | Retro + S16 plan | | | |
| | **TOTAL** | **8.5 / 18h** (thru 07-30) | **7 / 8** | |

**Weekly invariants check (fill each Sunday):**
- Learning contact days: __ / 7 (target ≥ 5)
- Prime hours logged: __ / 11 target
- Entertainment hours: __ (flag if > 10)
- Quantamental hours: __ (cap 6; circuit breaker at >8 for 2 weeks)
- Mood 1–5: __

**Velocity readout (fill at retro, Day 14):**
- Planned 18h → actual __h = **__% of plan**. This number sizes Sprint 16, not the estimate.
- Stages closed: __ / 4 (Calculus ✅ · Linear Algebra · Discrete Dists · Continuous Dists)
- If <60% for 3 consecutive weeks → contract §F circuit breaker: renegotiate A.2, don't grind.

---

## Next week — Sprint 16 (2026-08-03 → 2026-08-16) — preview

Sprint 16 revised scope (T0.C/T0.D moved into Sprint 15 tail):
- Continue/complete T1.X Named Distributions if it slips from Sprint 15
- **S1.1 Combinatorics** — full stage (4 Feynman steps + 5 problems + 3 solvers + unlock test)
- **Start S1.2 Cond prob + Bayes** — Feynman Steps 1–2
- Scrap: 5 LeetCode-easy (arrays/hash pattern warm-up for S10.1 in S17)

Detailed day-by-day filled in Sun 08-02 after S15 retro.

---

## How to use this tracker

1. **Morning:** open this file, look at today's row. Adjust if life demands.
2. **After each session:** tick ☐ → ☑, add notes (e.g., "T0.C Step 2 done, GAP on Lagrange geometry, need to fill Sunday").
3. **Sunday:** fill weekly invariants, do 30-min review, roll over undone items to next week or next sprint.
4. **Sprint end (Day 14):** archive the completed sprint section, paste next sprint from `progress/sprints/S<NN+1>.md`.

**Rule:** if a row goes 3 days untouched without note, mark it a `⚠️ slippage` and either reschedule or explicitly drop. Never let items rot silently.

---

## Log of completed sprints

- **Sprint 15** (07-20 → 08-02): setup + baseline + T0 refreshers · retro pending Sun 08-02

---

*Tracker started: 2026-07-24*

<!-- NOTE: this file previously had the full AGENT_CONTEXT.md text pasted below this line
     by accident. Split out to ../AGENT_CONTEXT.md on 2026-07-25. -->
