---
name: sprint
description: Assemble a sprint file from a list of topics — topic overview, backlog, log table, code problem names, unlock tests for whatever is due for review, and a knowledge-focused retro. Use when the user names topics for a sprint ("/sprint Bayes and tower property", "plan S18"), or asks to revise an existing sprint file.
---

# Assembling a sprint

A sprint file is an **overview plus a log**. Detail lives in the stage maps; the sprint file
never repeats it. Output goes to `progress/sprints/S<NN>.md`.

Reference model: `progress/sprints/S16_v2.md`. Full template in [reference.md](reference.md).

## The rules that matter most

**No schedule.** No per-day plan, no week split, no hour budgets per topic, no capacity line.
The user studies when they have time; a day-by-day plan they can't follow is worse than none.
One flat log table covering the sprint's dates is the whole time structure.

**Overview only.** A topic gets a wikilink to its stage map and 2–4 lines of concepts. If you
find yourself explaining a formula, that belongs in the stage map.

**A backlog, not a commitment.** Ranked list of what to pull if the sprint's topics close early.
No estimates, no gloss.

**Code problems by name only** — grouped by the file they live in. The specs are in the stage
maps; repeating them here is the duplication that made sprint files unreadable.

**No project vocabulary.** No stage IDs in prose or headings, no baseline question numbers, no
sizing multipliers, no adjustment numbers, no `D4` label — write "unlock tests".

## Steps

1. **Read `BACKLOG.md`** — every topic, its status, estimate, what it pays into, and what blocks
   it. When the user asks for a sprint plan without naming topics, **propose from here**: pick
   topics that are unblocked (`Blocked by` is `—`), prefer ones paying into the roles they are
   targeting, and total ~18–20h against the ~22h a sprint holds. Present the shortlist with
   estimates and let them adjust before writing anything.
2. **Get the sprint number and dates.** Two weeks, Monday to Sunday. Read the previous sprint
   file if one exists.
3. **Read each named topic's stage map** for its `name`, `est_h`, concept list, and code-problem
   titles. If a topic has no stage map, say so — offer to write one with the `stage-map` skill
   rather than inventing scope here.
4. **Compute reviews due:**
   ```
   python .claude/skills/sprint/scripts/reviews_due.py S<NN> <end-date>
   ```
   Prints OVERDUE (no retrieval evidence), DUE, and not-yet-due. **Keep overdue separate from
   due in the file** — "never tested" and "due for R2" are different states.
5. **Write unlock tests** for everything overdue or due. See reference.md for the question shape.
   Fresh questions, never reused from the stage map's problem tiers.
6. **Write the file** per reference.md.
7. **Regenerate the backlog:** `python vault/build_backlog.py`.
8. **Report** the topics included, total estimated hours against the ~22h the user has in a
   sprint, and which reviews are carried.

## The review ladder

Spaced retrieval, not Feynman — Feynman is the encoding method, this is the schedule.

| Rung | Gap since last pass | Test length |
|---|---|---|
| **R1** | +1 week | 5 questions, 45 min |
| **R2** | +1 month | 3 questions, 15 min |
| **R3** | +3 months | 3 questions, 15 min |
| Final | interview prep, S26–27 | everything |

**A failed review (<80%) resets the topic to R1.** That reset is what makes spacing work and is
the part most people skip. Record a passed review in the stage map's frontmatter — `review: R1`
and `reviewed: <ISO date>` — so the next sprint's calculation picks it up.

R2 and R3 are short on purpose: they test whether the summary table survived, not whether the
user can rederive everything. Only R1 is a full paper.
