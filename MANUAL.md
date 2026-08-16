# BAGQ — The Manual

> How to run this system. Everything else in the repo is reference; this is the operating
> procedure. If you read one file after a long gap, read this one.
>
> **Last updated:** 2026-08-09

---

## 0. Setup, once

1. Open this repo folder as a vault in Obsidian.
2. Settings → Community plugins → Browse → install and enable **Dataview**.
3. Open `vault/HOME.md`. If you see code blocks instead of tables, Dataview isn't on.

`inventory/`, `pine_scripts/`, `.claude/`, `src/`, `tests/` are excluded from the vault by
`.obsidianignore` — deliberately. `inventory/` alone is 3,440 lines and would swamp the graph.

---

## 1. The four files that matter

| File | What it is | Who writes it |
|---|---|---|
| `vault/HOME.md` | Morning dashboard — in flight, overdue, untested | Dataview, automatically |
| `progress/sprints/S<NN>.md` | Schedule, actuals log, retro | You + agent at planning |
| `stage_maps/<id>_<slug>.md` | **What to do** — checklist, source, problems, code, deliverables | Agent, before the block |
| `progress/feynman_notes/<id>_<slug>.md` | **What you understood** | **You, always. Never the agent.** |

Everything else — `vault/method/progression.md`, `CAPABILITY_MAP.md`, `vault/**` — is reference you
consult, not paperwork you maintain.

**Working mode is "I study, you check."** You read the source and write the teach-back from
memory. The agent hunts gaps and grades. If the agent drafts the teach-back, the whole theory of
change is dead.

---

## 2. A day

### Start (2 minutes)

1. Open `vault/HOME.md` → glance at what's in flight and what's overdue.
2. Open the active sprint file → find today's row.
3. Open the two files it names: the **stage map** and the **Feynman note**.

No decisions to make. The plan already exists.

### The block

| Block | Duration | Do |
|---|---|---|
| **1 — Read** | 40 min **hard stop** | One source, named sections from the map. Then close it. |
| **2 — Teach back** | ~45 min | §1 from memory, source closed. Mark every hand-wave `⚠️ GAP:` |
| **3 — Problems** | ~60 min | Tier A on paper, closed-book |

**New material gets two passes on separate days.** Pass 2 opens on your `⚠️ GAP` list, not on
page 1. One pass does not install machinery you have never held — that is the measured S15
finding, not an opinion.

### 🔴 The drift move — the single most important rule here

**When it gets hard and your attention scatters:**

> **Stop reading. Write the sentence you cannot finish into §2 as a `⚠️ GAP`. Switch to Tier A
> on paper.**

Paper problems survive low focus; re-reading the same paragraph does not. **Drifting means input
is exhausted for this sitting — not that you need more discipline.** This is a designated
action, not a fallback.

### If the day collapses

Every stage map names a **collapse subset** — e.g. *"if a pass collapses: A2, A3, B1 only."*
Do those three. That is a successful day, not a failed one.

### Wrap up (1 minute)

One line in the sprint actuals table:

```
| Wed 08-05 | `F1.5` Pass 1 | [hours:: 2.5] | Ross §5.1–5.3. Gap on the Jacobian. Tail formula clicked. |
```

- **Square-bracket inline field in the Hrs column** (see the code block above). Dataview sums
  it and derives contact days from hours > 0.
- **Notes column is prose, and stays prose.** "Scattered sittings; difficulty → distraction" is
  what produced the entire S15 finding. Dataview can sum hours; it cannot notice a cause.
- **A 0-hour day with a reason beats a blank.**

### ⚠️ Four things that silently corrupt the actuals table

Each of these has already happened once. None of them error — they just produce wrong numbers.

1. **Never put a `|` inside a table cell** — including an aliased wikilink `[[note|F1.5]]` or a
   maths expression like `|dx/dy|`. Markdown reads it as a column separator: the row gains a
   column, every cell after it shifts right, and notes land on the wrong day. **Use
   `` `F1.5` `` in tables**, and link properly in prose outside the table.
2. **"Format table" in an editor reflows rows** and can re-split on those pipes. If a note shows
   up on the wrong date, that is what happened — `git diff` will show it.
3. **Numbers must be bare.** A value like `2.5` sums; `2.5h` is a string, and `sum()` silently
   concatenates into nonsense like `N0100000000000000` instead of erroring.
4. **Never write a live inline field in prose or guidance text.** Dataview parses inline fields
   *anywhere in the file*, including inside blockquotes and instructions — not just in tables.
   An example written in explanatory text gets counted as real data. Put examples inside fenced
   code blocks (Dataview skips those), which is why the sample row above is fenced.

---

## 3. A stage

### Start

The map already exists. Skim three things:

1. **Why this stage exists** — which baseline gap it closes
2. **The knowledge checklist** — the scope, built from the source's real section headings
3. **The collapse subset** — your bad-day plan, decided in advance

Set frontmatter `status: in-progress`.

### Close

- [ ] Gap-hunt §1 — every `⚠️ GAP` filled or explicitly deferred with a reason
- [ ] Tier B, ≥3 of 5
- [ ] Napkin ≤200 words, **said out loud once** — record it, listen back
- [ ] Summary table **from memory**, then verified
- [ ] Code problems run and assert
- [ ] **Two sentences per concept note** in `vault/concepts/` *(D3.5 — see below)*
- [ ] Frontmatter: `status: ready-for-test`, `actual_h: N`

**The stage is not COMPLETE here.** It sits at `ready-for-test` for a week, visible in HOME. That
is a real state, not a failure.

### D3.5 — the two sentences that keep the vault alive

For each concept in the map's `concepts:` frontmatter, write two sentences in your own words into
`vault/concepts/<name>.md`.

This is **the only vault file you touch during a stage**, and it is what makes the vault a system
rather than a diagram. Concept notes **accumulate across stages**: `F1.4` starts
`memorylessness` from the geometric, `F1.5` extends it with the exponential and "the only two
memoryless distributions." A per-stage Feynman note structurally cannot do that.

### +1 week — D4 unlock test

- 5 fresh questions you have not seen, 45 min, closed-book (Feynman note allowed)
- Record the napkin aloud; listen back once
- **Grade the day after.** Fresh eyes catch bluffing.
- ≥80% → `status: complete`. Below → `in-progress`, redo Feynman step 3.

**Why the delay:** retrieval practice works on a delay. A same-day test measures short-term
memory, which is not what has to survive until January.

### Later reviews

`+1 month` and `+3 months` are logged at the top of each Feynman note. A failed review drops the
stage back to `in-progress`. **That is data, not failure.**

---

## 4. A sprint

### Day 1 — planning (~45 min)

1. **Read the previous retro's velocity first.** Not your gut.
2. Size with the measured multipliers:
   - **Refresher ×1.2** · **New material ×2.0**
   - Ceiling ≈ **11h/week prime**
   - **Two new-material stages per sprint. Not three.**
3. Write the day-by-day and the actuals skeleton.
4. Don't gold-plate it. 45 minutes.

### Mid-sprint Sunday — weekly review (~30 min)

- Invariants: contact ≥5/7 · prime hours · entertainment (flag >10) · quantamental (cap 6) · mood
- **Write next week's stage maps** — just-in-time, never upfront
- The one thing to change next week. One lever, not a list.

### Day 14 — retro (~60 min), two separate things

**1. Flashcard pass.** Say the sprint's topic names aloud, tick what comes cold. This is a
temperature check on the *process*, not a test. If most are cold, don't trust the conclusions below.

**2. Process retro.** Velocity (Dataview computes it) · blockers by **root cause, not symptom** ·
what worked, codified into the next sprint · circuit breakers · adjustments.

**Retro ≠ unlock test.** The retro reviews the process; D4 tests the knowledge, per stage, on its
own clock. Tangling them is what made the S15 retro try to be both and do neither well.

### Circuit breakers (contract §F) — pause and diagnose, don't grind

| Trigger | Response |
|---|---|
| <60% of prime hours, 3 weeks running | Time budget is wrong. Renegotiate, don't grind. |
| 2 stages fail D4 in a row | Feynman step 3 is being skipped. |
| Mood ≤2 for 2 weeks | Take a full week off. No guilt. |
| Quantamental >8h for 2 weeks | Scope creep. Hard reset to the 6h cap. |

---

## 5. Where everything lives

```
vault/HOME.md              ← morning dashboard
progress/sprints/S16.md    ← today's row, actuals, retro
stage_maps/                ← what to do, per stage
progress/feynman_notes/    ← what you understood (yours)
vault/topics|concepts|applications|roles/   ← the mind map
vault/method/progression.md    ← what unlocks what. OWNS STUDY ORDER.
CAPABILITY_MAP.md          ← why a stage matters (GitHub-readable)
vault/method/done.md    ← definition of done, D1–D4
vault/method/contract.md  ← time budget, invariants, circuit breakers
inventory/                    ← 911-problem inventory. Excluded from vault.
```

**Only `vault/method/progression.md` decides study order.** The capability map and the vault are
reference. Two competing calendars is exactly what made the DAG's traversal table go stale.

---

## 6. The rules that were paid for

Each of these came from something going wrong. They are not preferences.

| Rule | Cost of learning it |
|---|---|
| **One source per stage**, named chapter + page range | `R.calculus` ran 5h on 7 sources — time spent *choosing*, not studying |
| **Refresher ×1.2, new material ×2.0** | `F1.4` budgeted 3h, took 6h. The 40-min cap was calibrated on a refresher. |
| **Two passes on separate days** for new material | `F1.4`'s second pass happened anyway — unplanned, unbudgeted, across 3 days |
| **Name the drift move** | Difficulty scattered attention and there was no designated next action |
| **Build checklists from the source's real headings** | `F1.4`-A5 asked for MGFs that Ross Ch.4 doesn't cover |
| **Every stretch item resolves** — inline, named source, or deferred *with a reason* | A bare "→ S1.8" is a to-do, not a learning path |
| **Read the `inventory/` heading before assigning a stage ID** | Got wrong twice: `S1.3`, then `F1.4a`/`F1.4b` |
| **Small stages localise overrun** | `F1.4` blew its budget; `F1.5` carried cleanly because they were separate |
| **D4 at +1 week, not at close** | Four stages closed, zero tested — the gap that had no artifact |
| **No new textbooks** | Ross, Green Book, Hull, CLM. Over-collecting is procrastination. |

---

## 7. The one thing to watch

**Four stages are closed. Zero have been tested.**

The write-side of the loop works — your `R.linalg` note struck out a stalled derivation and
rebuilt it a better way, which is the Feynman method doing exactly its job. The **retrieval**
side has never run.

`vault/HOME.md` now surfaces this permanently under *"Closed but never tested."*

**Sat 08-15 carries all four D4 tests.** That is the first real evidence about whether these
notes produce retention or just produce notes. Everything else in this manual is scaffolding
around that question.

**If a day gets tight, cut Tier B before you cut the test.**
