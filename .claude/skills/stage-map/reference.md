# Stage map template and rules

Reference model: `stage_maps/F1_1_combinatorics_v2.md`.

## Frontmatter

```yaml
---
type: stage
id: F1.1                    # <TYPE><section>.<sub> — see naming below
name: Combinatorics         # plain English, the graph node label
topic: "[[I-1-combinatorics-and-counting]]"
concepts: ["[[ordered-vs-unordered]]", "[[bijection-proof]]"]
roles: ["[[signal-research]]", "[[market-making]]"]
sprint: S16
status: unlocked            # unlocked | in-progress | ready-for-test | closed
est_h: 6.5
actual_h:
---
```

**`concepts:` and `roles:` are the graph edges.** They are the whole reason the file wires into
`CAPABILITY_MAP.md`. Pick them deliberately: a concept belongs here if this stage is where the
idea gets installed, not merely mentioned. Role slugs are exactly the six in `vault/roles/` —
`signal-research`, `market-making`, `options-pricing`, `portfolio-construction`,
`risk-management`, `backtesting-infra`. There is no `quant-research`.

**Naming.** `R` refresher · `F` foundation · `D` deepen, then the section number (1 = `section_I`,
7 = `section_VII`, …) and the `##` sub-heading number *inside* that topic file. **Open the file
and read the heading before assigning — this has been got wrong twice.** Refreshers are
`R.<name>`. The ID lives in frontmatter only; it never appears in prose.

## Body sections, in order

### Title and source

```markdown
# Combinatorics

**Source:** Ross, *A First Course in Probability* 6th ed. — Ch. 1 §1.1–§1.6, then **Ch. 2 §2.5**.

**Estimated: 6.5h** — roughly 1.5h for counting rules, 2.5h each for the other two parts.
```

Source at the top, where you look when printing. If it crosses chapters, a blockquote right here
says which, and why — including any material that is a worked example rather than a headed
section, and where the user should expect the title to look unfamiliar.

### What this covers

Prose, not a bullet dump. Say what the topic *is for* in one or two sentences, then the parts.

If the topic needs more than one session, name **parts** and add:
> **Three natural pauses.** Stop at a part boundary if the session ends; don't stop mid-part.

Each part gets a paragraph: what it contains, and the one transferable move it installs. If two
parts join at a specific problem, say which problem and why — that join is usually the point.

End with **Not here:** — what a reader might expect and won't find, each with its reason
(deferred, no closed form, belongs to another topic). Never leave a deferral unexplained.

### Knowledge checklist

Grouped by the source's real section numbers, one `- [ ]` per checkable item. Tick marks are
real state; preserve them when revising a file.

Add the *why* inline where a formula alone would be memorisation:
`- [ ] C(n,k) = n!/(k!(n−k)!), and **why the k! divides out**`

### Problems

One `## Problems` heading, three tiers as `###` subheadings, numbered continuously across the
whole file (`A1…A11`, `B1…B8`, `C1…C3`) — not restarted per part.

- **Tier A — the floor.** All of them, unhinted, on paper. The things that must be automatic.
- **Tier B — the target.** A stated minimum ("at least four"). Where the topic gets interesting.
- **Tier C — only if A and B ran short.**

Most problems carry an *italic note* after them saying what the problem is really testing, or
naming the standard wrong answer. That note is the highest-value part of the file — it is the
interviewer's follow-up, written down in advance.

### Code problems

Only when a verifier earns its keep. **Do not write a solver for something the standard library
already does** — `math.comb` needs no reimplementation. Say so plainly when skipping.

LeetCode-shaped, one numbered subsection each, with the spec as a blockquote:

```markdown
### 1 · Stars and bars, checked by brute force

Count the ways to place `n` **identical** balls into `k` **labelled** bins.

> **Input:** `n ≥ 0` balls, `k ≥ 1` bins
> **Output:** the number of distinct distributions
> **Closed form:** `stars_and_bars(n, k)` returning `math.comb(n+k-1, k-1)`
> **Verify:** `brute_force(n, k)` enumerates via `itertools.product` and counts those summing to
> `n`. Assert both agree for every `n ≤ 8`, `k ≤ 4`.

**Complexity:** closed form `O(k)`; brute force `O((n+1)^k · k)`. State both in the docstring,
**and why the brute force is acceptable as a test and unacceptable as an implementation.**
```

Every code problem: one function computing the answer, one verifying it independently, an
`assert` in `__main__`, a docstring with time and space complexity. Standard library only.

**Choosing the verifier** — exact enumeration when the state space is small enough to walk;
Monte Carlo only when it isn't. When a file has both, say which is which and why: that choice is
the transferable skill. For Monte Carlo, require a comment naming the trial count and why — a
flaky assert is worse than none.

Path: `src/solvers/s1_probability/<name>_verify.py`. Prefer one file per topic over one per
problem.

### Deliverables

Plain headings — **Feynman note**, **Problems**, **Code**, **Unlock test**. No `D1`/`D2` labels.
Checkboxes for what "done" means. The note path is
`progress/feynman_notes/<id>_<slug>.md`; one note per topic, and say so if the topic has parts.

### Closing guidance

Two short paragraphs, unlabelled, after a `---`:

- **The drift move.** "When it gets hard and you start drifting: stop reading, write the sentence
  you can't finish into the note as a `⚠️ GAP`, and switch to Tier A on paper." Add the
  topic-specific version — for combinatorics, "draw `n=4, k=3` and enumerate". Drift means input
  is exhausted for this sitting, not that the user needs more discipline.
- **The collapse subset.** "If a session collapses: Part 1 → A2 and A4." Two problems per part,
  the ones that carry the transferable move.

### Answer key

After `---\n---`, a `# ANSWER KEY — do not read until you have attempted` heading, then
`<details>` blocks — one per tier, or per part when the key is long enough that one block would
be unnavigable.

**Work every answer properly.** Show the derivation, not just the number. Where there is a
classic wrong answer, give it and explain the error — that is often worth more than the right
answer. Close with the transferable statement where there is one ("overcounting is the failure
mode of counting, and the cure is always to partition into disjoint cases first").

## Creating vault stubs

Any `[[link]]` in frontmatter with no note behind it breaks the graph silently. Create it.

**Concept** → `vault/concepts/<slug>.md`:

```markdown
---
type: concept
name: proof by bijection
topics: ["[[I-1-combinatorics-and-counting]]"]
applications: ["[[signal-testing]]"]
---

# proof by bijection

> One-sentence plain-English statement of the idea.

**Arises in:** [[I-1-combinatorics-and-counting]]
**Feeds:** [[signal-testing]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

Two or three lines on what the idea actually says and where it bites.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "<slug>")
```
```

**Application** → `vault/applications/<slug>.md`: same shape with `type: application`,
`concepts:` and `roles:`, an `**Interview form:**` line phrased as a question someone would
actually ask, and a `## Notes` section on what you'd have to build and what breaks.

When you add a concept that an existing concept or application should feed, update *that* note's
`applications:` list and its `**Feeds:**` line too — edges are declared on both ends.

## Finish

```
python vault/build_capability_map.py
```

Regenerates the diagram and coverage table, and prints dangling links. **Zero dangling links
before you report done.**
