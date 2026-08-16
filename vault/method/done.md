# Deliverables Spec — "Definition of Done" per Stage

> A stage is `COMPLETE` **iff** all four deliverables below pass. No exceptions.

---

## The four deliverables (theory + code twin)

### D1 — Feynman note (theory)
- File: `progress/feynman_notes/<stage_id>_<slug>.md`
- Rubric: all 6 sections of the template in `feynman.md`, zero remaining `⚠️ GAP`.

### D2 — Problem set (application)
- **The stage map is the authority.** Problems live in `stage_maps/<stage_id>_<slug>.md`,
  tiered A/B/C and numbered `<STAGE>-<TIER><N>` (e.g. `F1.5-A2`).
- **Bar: Tier A is the floor (all of them, unhinted, on paper). Tier B is the target (≥3 of 5).**
  Tier C only if A+B ran short. This replaces the old fixed "N by tier" counts, which assumed
  section-sized stages — we study at day-stage granularity now.
- `inventory/section_*.md` is the **scope inventory, not an indexed problem bank.** Its problems are
  prose bullets with no IDs. Where a stage problem comes from there, cite it by name:
  `F1.1-A3 — MISSISSIPPI anagram (inventory/section_I §1)`. **Do not index all 13 files** — that is
  speculative work for stages months away.
- Solutions go on paper. Log which needed hints in the stage map's deliverables block.
  Hint use is fine; hiding it is not.

**Build the knowledge checklist from the source's actual section headings — then annotate.**
Not from what interviews tend to ask. Two passes: (1) read the real headings and derive the core
list from them, with section numbers attached; (2) mark anything interview-critical that is
*outside* the chapter as **stretch**.

*Why this is a rule: `F1.4`-A5 asked for MGF derivations that Ross Ch.4 does not cover, and the
same assumption then produced two out-of-chapter items in `F1.5`. A stage that claims "one
source" and then asks for things outside it silently recreates the multi-source problem that
cost `R.calculus` five hours.*

**Every stretch item resolves one of three ways, decided when it is written — never left as a
bare pointer:**

| Resolution | Use when | What the map contains |
|---|---|---|
| **Inline** | ≤1 page, uses only tools the stage already has | The material itself, in a `## Stretch notes` section |
| **Named source** | It is a real chapter in a book already owned | `Ross §7.7, pp. 354–360` — budgeted as a mini-block |
| **Deferred** | It genuinely needs machinery not yet held | Target stage **and the reason** — "needs joint dists → F1.6" |

A stretch item that says only "→ S1.8" is a to-do, not a learning path. **No new textbooks** —
"named source" means Ross, Green Book, Hull, or CLM.

### D3 — Code twin (computational)

- **Code problems are stated in the stage map**, in a `## Code problems` section. Specified up
  front like any other problem — never improvised at the close block.
- **Everything goes in `code/codify.ipynb`**, one `# Topic` markdown heading per topic, newest
  at the bottom. Standard library only.
- Each code problem is one cell containing:
  1. **Analytical / closed-form function**, if one exists
  2. **An independent verifier** converging to the same answer within tolerance
  3. **A docstring with time + space complexity** — interviewers grade Big-O explicitly
  4. **An `assert`** comparing the two. A cell that runs silently has passed.
- **Choosing the verifier:** exact enumeration when the state space is small enough to walk,
  Monte Carlo only when it isn't. When a cell has both, say which is which and why — that choice
  is the transferable skill. Monte Carlo needs a comment naming the trial count and why.
- For pure-algorithmic problems (Section X), the code twin is implementation + complexity
  comment + edge-case asserts.

**Minimum coverage:** every stage ships at least one runnable check. Interview favourites
(expected-flips-to-HH, gambler's ruin, coupon collector) are mandatory.

**One notebook until it hurts.** No `src/` package, no pytest. Both were specced in July,
neither got written in three sprints, and the whole deliverable is one function plus one
verifier plus one assert — that is a cell, not a package. Split a topic into
`code/<topic>.ipynb` only when a section genuinely needs importing somewhere else.

### D3.5 — Concept notes (2 min each, at stage close)

For every concept in the stage's `concepts:` frontmatter, write **two sentences in your own
words** into `vault/concepts/<name>.md` under `## In my own words`.

- This is the **only** vault file touched during a stage. Everything else there is structure.
- Concept notes **accumulate across stages** — `F1.4` starts `memorylessness` from the geometric,
  `F1.5` extends it with the exponential and the "only two memoryless distributions" fact. A
  per-stage Feynman note cannot do this, because it is per-stage.
- Also set `status: ready-for-test` and `actual_h:` in the stage map frontmatter. That is what
  makes the stage appear in HOME's untested list.

*Without this step the vault is write-only — links flow in, nothing flows back — and a
reporting layer nobody reads is a reporting layer that rots.*

### D4 — Unlock test (proof of retention) — **at the +1 week review, not stage close**
**When:** at the stage's **+1 week review**, not on the day it closes. Retrieval practice works
on a delay; a same-day test measures short-term memory, which is not what has to survive until
January. Between close and +1wk the stage sits at `READY_FOR_TEST` — a real state, not a failure.

- **Fresh** questions you have not seen (from `inventory/section_*.md`, or generated with the prompt
  template below).
- Format: 3–5 questions, 45–60 min, closed-book (only your Feynman note allowed).
- **Pass threshold: ≥ 80%** (graded against a rubric — write the rubric *before* you start).
- **Oral component:** record yourself delivering the napkin version out loud. Listen back once.
  If it isn't coherent in 90s, redo Feynman step 4. *Incoherence is invisible on the page and
  obvious on playback — this is the cheapest quality check in the system.*
- Grade the **day after**, not the same day. Fresh eyes catch bluffing.
- **Sprint retro ≠ unlock test.** The retro reviews the *process* (velocity, blockers, what to
  change). D4 tests the *knowledge*, per stage, on its own clock. Keep them separate or the
  retro tries to be both and does neither.

**AI prompt template for generating fresh unlock-test questions:**
```
You are an interviewer at a top quant firm.
I just finished studying <topic>. My reference notes cover <bullet the subtopics>.
Give me 5 questions I have NOT seen before:
- 2 conceptual (verbal answer)
- 2 numerical (compute a value)
- 1 twist / follow-up (edge case, adversarial variant)
Difficulty: mid-level quant interview (Optiver / JS / SIG onsite phase 1).
Provide the rubric answers in a separate section I can hide.
```

---

## Capstone project deliverables (P1, P16, P18 for the 5-month plan)

A capstone additionally requires:
- All contained stages' D1–D4 passed
- Runnable end-to-end demo notebook
- README with: motivation, math summary, code layout, results, "where it breaks"
- **Peer/AI code review pass** (paste to Claude/GPT with: *"review this like a senior desk strat; find bugs, weak tests, and unclear naming"*)

---

## Grading rubrics (keep them honest)

Unlock tests are written into the sprint file (`progress/sprints/S<NN>.md`) for whatever is
due that sprint, with the attempt and grade logged in the same place. Rubric skeleton:

```markdown
# Unlock test rubric — <stage_id>

| Q# | Points | Key requirements for full credit |
|---|---|---|
| Q1 | 20 | State assumption X; derive step Y; final answer Z within tolerance |
| Q2 | 20 | ... |
| Q3 | 20 | ... |
| Q4 | 20 | ... |
| Q5 (twist) | 20 | Identify that the standard method fails because ...; propose fix |
| **Total** | 100 | Pass ≥ 80 |
```

**Grade yourself the day AFTER the test**, not the same day. Fresh eyes catch bluffing.

---

## Directory layout

```
code/codify.ipynb        every code deliverable, one heading per topic
inventory/               the 911-problem scope inventory
stage_maps/              what to do, per topic
progress/
  baseline_scores.md
  sprints/S<NN>.md       log + retro, one per sprint
  feynman_notes/         what was understood, one per topic
vault/                   the Obsidian graph — method/, topics/, concepts/, applications/, roles/
```

---

*Version: 0.1 | Created: 2026-07-23*

