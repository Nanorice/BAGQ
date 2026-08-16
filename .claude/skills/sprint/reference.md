# Sprint file template

Reference model: `progress/sprints/S16_v2.md`.

## Shape

```markdown
# Sprint 18 — Bayes + Tower Property

**Dates:** 2026-09-14 → 2026-09-27

---

## Topics this sprint
## Backlog
## Log
## Code problems
## Unlock tests
## Retro
```

Nothing else. No sprint-number-of-13 line, no capacity line, no re-scope blockquotes, no
"not in scope" section, no provenance footer.

## Topics this sprint

One block per topic: bold plain-English name, wikilink to the stage map, then 2–4 bullet lines
of the concepts it carries. Concepts only — no formulas beyond naming them, no rationale.

```markdown
**Conditional Probability and Bayes** — [[F1_2_conditional_probability_bayes]]
- Law of total probability · Bayes' rule · posterior odds form
- Base rates · sensitivity vs specificity · the disease-test trap
- Independence vs conditional independence
```

If a topic has natural parts, they stay inside the stage map — the sprint file does not list them.

## Backlog

Bare heading, ranked numbered list, wikilinks, no gloss. Last item can group scrap-sized work.

```markdown
## Backlog

1. Joint distributions — [[F1_6_joint_distributions]]
2. Generating functions — [[F1_8_mgf]]
3. Scrap-size: coupon collector · put-call parity direction · LeetCode-easy × 2
```

## Log

One table for the whole sprint, every date pre-filled, `[hours:: 0]` as the default. Three
columns: Date, Hrs, and free prose.

```markdown
| Date      | Hrs         | What I studied / what blocked |
| --------- | ----------- | ----------------------------- |
| Mon 09-14 | [hours:: 0] | |
```

Then the Dataview block, with `file.name` matching the actual filename:

````markdown
```dataview
TABLE WITHOUT ID
  sum(rows.h) AS "Hours logged",
  length(filter(rows.h, (x) => x > 0)) AS "Contact days"
FROM "progress/sprints" WHERE file.name = "S18"
FLATTEN number(hours) AS h
WHERE h != null
GROUP BY true
```
````

Then the one warning worth keeping:
> Keep `|` out of every cell — including aliased wikilinks. It splits the row.

**The prose column stays prose.** It is where cause gets recorded, and one sentence there has
produced more insight than any metric in the file. Never replace it with a dropdown or a code.
A zero-hour day with a reason beats a blank.

## Code problems

Names only, grouped by target file, one line pointing at the maps.

```markdown
## Code problems

Specs live in the stage maps — inputs, method, verifier, and the complexity to state.

**`src/solvers/s1_probability/bayes_verify.py`**
- Base-rate simulation against the closed-form posterior
- Sequential updating, checked against a single batch update
```

## Unlock tests

Run `reviews_due.py` first. **Overdue and due get separate subsections** — never merge them.

```markdown
## Unlock tests

> Closed-book except your own note. Pass ≥ 80%. Write on paper before opening the answer block.
> Grade the day after. Say the napkin version aloud once — incoherent in 90 seconds counts as a
> gap regardless of the written score.
>
> **A score below 80% resets that topic to the start of the ladder**, and it comes back next
> sprint as a full paper.

### Overdue — no retrieval evidence yet

#### Discrete Distributions — 5 questions
...

### Due this sprint

#### Combinatorics — 3 questions
...
```

Heading per topic is its **plain English name**, never a stage ID. State the question count.

### Question shape

R1 (5 questions): 2 conceptual, 2 numerical, 1 twist.
R2 and R3 (3 questions): 1 conceptual, 1 numerical, 1 twist.

- **Conceptual** — "explain why X requires Y but Z does not". Probes whether a right answer has
  a right justification, which is the thing an interviewer actually chases.
- **Numerical** — a clean number the user can check, small enough for paper.
- **Twist** — the same machinery one step past where it was taught: a case where the shortcut
  fails and the user must notice. This is the question that distinguishes recall from
  understanding, and it must be new, not a restatement of a Tier B problem.

**Never reuse a problem from the stage map.** The user has the answer key. A test built from
seen problems measures nothing.

Each topic's questions are followed immediately by a `<details><summary>Answers — <topic name>
</summary>` block with fully worked solutions — derivation and number, plus one line on what the
question was really testing.

## Retro

Two parts, both knowledge-focused. **No process questions, no velocity arithmetic, no invariant
counters, no circuit-breaker checks.**

### Flashcard pass

Topic names only, one block per topic, `·`-separated. Say each aloud, tick what comes cold.
Pull the terms from each stage map's knowledge checklist. Include topics carried from earlier
sprints that were reviewed this sprint.

### Questions

Four, and they are about knowledge:

```markdown
1. **Unlock test scores:** <topic> __% · <topic> __%
   For each one that lost marks — was it a formula, a derivation, or a concept? _____
2. Which topics from this sprint would not survive an interview question tomorrow? _____
3. What went into the note but never into the hand? _____
4. Topics to carry into the next sprint, and topics to push back to the backlog: _____
```

Question 3 exists because of a finding worth preserving: recall errors came from unworked
problems, not from unread pages. Keep testing whether that holds.

## After writing

Record any review that passed by updating the stage map's frontmatter (`review:` and
`reviewed:`), so the next sprint's ladder calculation is correct. If a review failed, set
`review: R1` and clear `reviewed:` — that is the reset.
