# Daily Tracker

> **The single artifact you open every morning.**
> Two purposes: (1) tell you what to do today, (2) capture what you actually did.
>
> Flexible time — pick blocks that fit the day. What matters is *contact ≥ 5 days/week* and *shipping the sprint deliverables by Day 14*.

---

## This week — Sprint 15 tail (2026-07-24 → 2026-08-02)

**Sprint 15 goal:** setup + baseline done ✅. Extended scope: knock out T0.C + T0.D refreshers so Sprint 16 opens with content, not setup.

**Blocks available:** Sat/Sun mornings (3h each), weekday evenings 60–90 min. Flex freely.

> ⚠️ **This sprint is knowingly over-committed.** T0.C (~4h) + T0.D (~4h) + T1.X (~8h) ≈ 16h against ~13h prime remaining.
> Decision 2026-07-25: plan it full and let the retro record the truth. There is no velocity data yet — the overrun *is* the measurement.
> **If forced to cut, cut T1.X**, not the T0 stages. T0.C/T0.D close baseline red flags (VIII.1, VII.1) and gate everything downstream. S16 already lists T1.X as carryover.

### Schedule

| Date | Day | Plan | Est. | Done? |
|---|---|---|---|---|
| Fri 07-24 | 5 | T0.A/B verification ✅ · read `02_feynman_protocol.md` if not yet | 0.5h | ☐ |
| **Sat 07-25** | **6** | **T0.C Steps 1–2.** Input time-boxed 45 min (sources table in `problem_sets/T0C_calculus.md` — S2 + S5 are the non-negotiables). Then **close the source** and write §1 teach-back from memory. Then Tier-A problems A1–A6 on paper. | **3h** | ☐ |
| Sun 07-26 | 7 | **T0.C Steps 3–4.** Gap-hunt §1 (agent checks), fill gaps, write napkin + analogy + numerical anchor (verify `e¹≈2.71828`). Tier-B problems. Close the note. · **Weekly review 17:30** → `weekly_reviews/2026-W30.md` | 2.5h | ☐ |
| Mon 07-27 | 8 | **T0.D Steps 1–2.** 3B1B *Essence of LA* eps 1, 10, 11, 14. Cover: matrix mult, 2×2/3×3 determinants, eigenvalues by hand via characteristic polynomial, PSD + why covariance is PSD. Teach-back from memory. | 1.5h | ☐ |
| Tue 07-28 | 9 | **T0.D Steps 3–4.** Numerical anchor: eigenvalues of `[[2,1],[1,2]]` by hand → verify `np.linalg.eig`. *(This is baseline VII.1 — you had the definition, lost the computation.)* Close the note. | 1.5h | ☐ |
| Wed 07-29 | 10 | Rest / exercise. Scrap only: cheap-win Bayes vocabulary (30 min) — sensitivity/specificity/prevalence + the disease-test problem *(baseline I.2, scored 0)* | 0.5h scrap | ☐ |
| Thu 07-30 | 11 | **T1.X Step 1** — first 5 of 9: Bernoulli, Binomial, Geometric, Poisson, Uniform. Ross Ch. 4. · Create `src/solvers/` (first real need) | 1.5h | ☐ |
| Fri 07-31 | 12 | **T1.X Step 2** — teach-back for those 5 in `feynman_notes/T1X_named_distributions.md`. Each: PMF/PDF, E[X], Var, MGF, one classic problem. | 1.5h | ☐ |
| Sat 08-01 | 13 | **T1.X** — Steps 1–2 for last 4: Exponential, Normal, Log-normal, χ². Start MC verifiers in `src/solvers/s1_probability/distributions_verify.py`. *(Exp is baseline I.3, χ² is I.4 — both scored 1.)* | 3h | ☐ |
| Sun 08-02 | 14 | **T1.X** Steps 3–4 · **Sprint 15 retro** (fill `sprints/S15.md`) · **Sprint 16 re-plan using this sprint's actual velocity** · Weekly review | 2.5h | ☐ |

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
| Fri 07-24 | T0.A/B | | | |
| Sat 07-25 | T0.C S1–2 | | | |
| Sun 07-26 | T0.C S3–4 | | | |
| Mon 07-27 | T0.D S1–2 | | | |
| Tue 07-28 | T0.D S3–4 | | | |
| Wed 07-29 | rest/scrap | | | |
| Thu 07-30 | T1.X S1 | | | |
| Fri 07-31 | T1.X S2 | | | |
| Sat 08-01 | T1.X last 4 | | | |
| Sun 08-02 | T1.X S3–4 + retro | | | |
| | **TOTAL** | **__ / 18h** | **__ / 10** | |

**Weekly invariants check (fill each Sunday):**
- Learning contact days: __ / 7 (target ≥ 5)
- Prime hours logged: __ / 11 target
- Entertainment hours: __ (flag if > 10)
- Quantamental hours: __ (cap 6; circuit breaker at >8 for 2 weeks)
- Mood 1–5: __

**Velocity readout (fill at retro, Day 14):**
- Planned 18h → actual __h = **__% of plan**. This number sizes Sprint 16, not the estimate.
- Stages closed: __ / 3 (T0.C, T0.D, T1.X)
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
