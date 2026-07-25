# Feynman Protocol — The Study Loop

> **Root cause of "I learned this before but forgot":** you completed steps 1–2 (read, take notes) but skipped 3–4 (explain, identify gaps, simplify). The gaps you didn't find are exactly where the memory decays first.

---

## The 4 Steps (do all four, in order, every time)

### Step 1 — Learn (input)
- Source: textbook chapter, paper, AI explanation, video, lecture notes.
- Time-box it. Rule of thumb: **≤ 40% of the topic's total time** should be pure input.
- Take *sparse* notes — bullet points, key formulas, one worked example. Not a transcription.

### Step 2 — Teach back (output, from memory)
- Open a fresh file: `progress/feynman_notes/<stage_id>.md`.
- **Close the source.** Write an explanation as if teaching a smart 15-year-old (or your past self before you started).
- **Ban jargon shortcuts.** If you use a term, define it in the same paragraph. "Martingale" is not an explanation; "a process whose expected future value, given everything you know now, equals its current value" is.

### Step 3 — Identify gaps (the crucial step everyone skips)
- Read your Step-2 write-up. Every place you handwaved, wrote "obviously," "by symmetry," "it follows that," or couldn't produce a concrete number → mark it `⚠️ GAP: …`.
- Go back to the source (or ask AI) to fill *only those gaps*.
- Update your Feynman note in place.

### Step 4 — Simplify + analogize + numerical anchor
- Add three final sections to the note:
  - **Napkin version** — ≤ 200 words, could be spoken in 90 seconds in an interview.
  - **Analogy** — one non-math analogy. ("Delta is the hedge ratio, like the tilt of a see-saw when you add weight.")
  - **Worked numerical example** — one concrete calculation, ideally verified by code.
  - **Where this breaks** — assumptions + failure modes (Black-Scholes assumes constant vol; real markets have skew).

---

## The Feynman Note Template

Save at `progress/feynman_notes/<stage_id>_<slug>.md`. Copy this template:

```markdown
# <Stage ID> — <Topic Name>

**Stage:** S1.7 Expectation & Variance
**Started:** YYYY-MM-DD    **Completed:** YYYY-MM-DD
**Time spent:** _h    **Source(s):** Hull Ch.X; MIT 6.041 L9; Claude session <link>

---

## 1. Teach-back (Step 2 output)
<Your from-memory explanation. No jargon shortcuts.>

## 2. Gaps identified & filled (Step 3)
- ⚠️ GAP: I said "by linearity of expectation" without proving it → filled: it holds even for dependent RVs because integration is linear; proof: E[X+Y] = ∫∫(x+y)f(x,y)dxdy = ∫xf_X(x)dx + ∫yf_Y(y)dy.
- ⚠️ GAP: ...

## 3. Napkin version (≤200 words)
<The 90-second interview answer.>

## 4. Analogy
<One non-math analogy.>

## 5. Worked numerical example
<Concrete numbers. Include a code snippet or link to solver in `src/solvers/…`.>

## 6. Where this breaks
- Assumption 1: ...
- Failure mode: ...

## 7. Links
- Related stages: <prereqs / dependents>
- Solvers: `src/solvers/<path>.py`
- Problems solved: [list problem IDs from `section_*.md`]
```

---

## Completion checklist (must all pass to unlock the stage)

- [ ] All 6 sections of the template have real content (not "TODO")
- [ ] Zero remaining `⚠️ GAP` markers
- [ ] Napkin version is ≤ 200 words AND has been said out loud once (yes, really)
- [ ] Analogy is non-mathematical
- [ ] Numerical example runs and produces the claimed number
- [ ] "Where this breaks" lists ≥ 2 items

If any box is unchecked, the stage is *not* complete, no matter how many problems you solved.

---

## Anti-patterns to avoid

| Anti-pattern | Fix |
|---|---|
| Copying formulas from the textbook into your note | Close the book first. From memory only. |
| "It's obvious" | It's a GAP. Mark it. |
| Skipping Step 4 because "I get it" | Then the 200-word version should take 10 minutes. Do it. |
| Note is 3000 words | You're transcribing, not teaching. Cut it. |
| Never re-reading old notes | Schedule: re-read each note at +1 week, +1 month, +3 months (spaced repetition). |

---

## Spaced repetition schedule (lightweight, no Anki required)

At the top of each Feynman note, add a `## Review log` section:

```markdown
## Review log
- [ ] +1 week  (YYYY-MM-DD): recall napkin version without opening file → pass/fail + notes
- [ ] +1 month (YYYY-MM-DD): re-solve worked example from scratch → pass/fail
- [ ] +3 months (YYYY-MM-DD): re-take one unlock-test question → pass/fail
```

A missed review = the stage regresses one level in `progress/stage_log.md`. This is fine; it's data.

---

*Version: 0.1 | Created: 2026-07-23*

