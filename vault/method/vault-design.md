# Obsidian Vault — Design Proposal

> **Status: DESIGN ONLY. Nothing has moved.** Review, then I build.
> **Date:** 2026-08-09

---

## 1. What problem this solves

Today the relationships between things live in **hand-maintained prose**: `CAPABILITY_MAP.md`
holds a Mermaid block I edit by hand, `TOPIC_MAP.md` holds a table I edit by hand, status counts
(1/10, 0/8) are counted by hand, and velocity is summed by hand.

All four drift. The DAG's traversal table already did.

In a vault, the relationships live in **links and frontmatter on the notes themselves**, and the
maps become *queries*. A stage that links to a topic cannot disagree with a table about which
topic it covers, because there is no table.

**What does not change:** you still write two files per stage (map + Feynman note), still in
markdown, still in git.

---

## 2. Entity types

Six. Only the first two are things you write during a study block.

| Entity | Count | You write | Purpose |
|---|---:|---|---|
| **Stage map** | ~30 | ✍️ before a block | What to do: checklist, source, problems, code, deliverables |
| **Feynman note** | ~30 | ✍️ during/after | What you understood |
| **Topic** | 59 | stub, once | `inventory/` subsection — the intuitive middle layer |
| **Concept** | ~12 | stub, once | The named idea that carries explanatory weight |
| **Application** | ~14 | stub, once | The concrete thing a quant builds |
| **Role** | 6 | stub, once | What a quant is hired to do |
| **Sprint** | ~13 | ✍️ at planning/retro | Schedule, actuals, retro — **excluded from the graph** |

### The chain

```
Feynman note ─┐
              ├─► STAGE ─► TOPIC ─► CONCEPT ─► APPLICATION ─► ROLE
stage map ────┘
```

**Topics are the new layer, and they are the reason this works.** `inventory/section_*.md` already
has 59 numbered subsections with canonical names — "I.5 Continuous Random Variables &
Distributions", "X.3 Graph Algorithms". They are the natural granularity between a stage and a
concept, they are more intuitive than concept names, and **you did not have to invent any of
them.**

This replaces the earlier sub-topic idea (separate `exponential` / `normal` / `uniform` notes).
One `I.5` note covers all three, and the stage map already handles per-distribution detail.

---

## 3. ⚠️ Two errors this surfaced

**A. `F1.4b` is misnamed. It should be `F1.5`.**

`inventory/section_I` §4 is *Discrete* RVs; §5 is *Continuous* RVs. They are **different
subsections**. On 08-04 I verified §3 was Bayes but assumed both distribution stages sat in §4.

| Now | Correct | Why |
|---|---|---|
| `F1.4a` Discrete | **`F1.4`** | §4 Discrete RVs & Distributions |
| `F1.4b` Continuous | **`F1.5`** | §5 Continuous RVs & Distributions |

They were never a split of one subsection — that premise was wrong. Renaming makes stage↔topic
a clean 1:1 and removes the `a`/`b` split letters entirely.

**Cost:** third rename this week; `F1.4a`/`F1.4b` appear in commits, notes, S15 retro, S16 plan.
**Recommendation: do it**, and treat "check the heading in `inventory/` before assigning" as a rule
that has now been violated twice.

**B. `TOPIC_MAP.md` dissolves.** Its whole job — stage ↔ topic mapping, what's covered, what's
deferred — becomes frontmatter on the topic notes plus one Dataview query. Content is preserved
in the migration, the file goes.

---

## 4. Folder layout

```
BAGQ/
├── stage_maps/          F1_5_continuous_distributions.md      ← unchanged, wikilinks added
├── progress/
│   ├── feynman_notes/   F1_5_continuous_distributions.md      ← unchanged
│   └── sprints/         S16.md                                ← inline fields for velocity
├── vault/                                                     ← NEW, all stubs
│   ├── inventory/          I-5-continuous-rvs.md         (59)
│   ├── concepts/        memorylessness.md             (12)
│   ├── applications/    var-tail-risk.md              (14)
│   └── roles/           market-making.md              (6)
├── inventory/                                            ← EXCLUDED from vault (.obsidianignore)
└── CAPABILITY_MAP.md    hand-maintained Mermaid, stays for GitHub
```

**91 new stub files.** Written upfront, 3–6 lines each, no prose.

**`inventory/` is excluded** — 3,440 lines of problem inventory would swamp the graph. The 59 topic
*notes* in `vault/topics/` link back to it by markdown path, so nothing is lost.

**Sprints stay standalone but out of the graph** — per your call, they are artifacts, not mind-map
material. Sprint↔stage lives in frontmatter only (`sprint: S16`), queryable but not drawn.

---

## 5. Frontmatter schemas

### Stage map
```yaml
---
type: stage
id: F1.5
name: Continuous Distributions
kind: foundation          # refresher | foundation | deepen
multiplier: 2.0
topic: "[[I-5-continuous-rvs]]"
sprint: S16
status: in-progress       # locked | unlocked | in-progress | ready-for-test | complete
budget_h: 6
actual_h:
d4_due: 2026-08-15
baseline_closes: [I.3]
---
```

### Topic
```yaml
---
type: topic
id: I.5
name: Continuous Random Variables & Distributions
section: I
source: "../../inventory/section_I_probability_combinatorics.md#5-continuous-random-variables--distributions"
concepts: ["[[memorylessness]]", "[[standardisation]]", "[[change-of-variables]]"]
covered_by: ["[[F1.5]]"]
coverage: partial         # none | partial | full
deferred: "log-normal → S6 · χ² → S9.2 · Gamma/Beta"
---
```
`coverage` + `deferred` are what `TOPIC_MAP.md` used to hold.

### Concept
```yaml
---
type: concept
name: memorylessness
topics: ["[[I-4-discrete-rvs]]", "[[I-5-continuous-rvs]]"]
applications: ["[[time-to-fill]]"]
one_liner: A quote that has waited 10s is no more due a fill than a fresh one.
---
```

### Application
```yaml
---
type: application
name: VaR / tail risk
concepts: ["[[standardisation]]", "[[fat-tails]]"]
roles: ["[[risk-management]]"]
interview_form: "Compute 99% 1-day VaR. Why is VaR not coherent?"
---
```

### Role
```yaml
---
type: role
name: Market making and execution
tilt: hft                 # qr | hft | both — scheduling weight only
---
```

### Sprint session rows (inline fields, option A-ii)
```markdown
| Date | Planned | Hrs | Contact | Notes |
|---|---|---|---|---|
| Wed 08-05 | [[F1.5]] Pass 1 | (hours:: 2.5) | (contact:: true) | Ross §5.1–5.3 · gap on inverse transform |
```
Dataview reads `(field:: value)` inline. **The Notes column stays free prose** — that is where
"scattered sittings; difficulty → distraction" got written, and that sentence produced the entire
S15 finding. Arithmetic is automated; cause is not.

---

## 6. What becomes automatic

| Today (hand-maintained) | Becomes |
|---|---|
| Capability status counts `1/10`, `0/8` | Dataview over `status` + `roles` |
| `TOPIC_MAP.md` coverage table | Dataview over topic `coverage` |
| Velocity `14.5/18h = 81%` | `sum(hours)` over the sprint's rows |
| Contact days `10/11` | `count(contact = true)` |
| "What's due for D4 review?" | Query on `d4_due <= today` |
| "Which closed stages never got tested?" | `status = ready-for-test` |

That last one is worth the whole exercise — it is the gap I flagged in the progress review, and
it currently has no artifact that surfaces it.

Example, in the S16 note:
````
```dataview
TABLE sum(rows.hours) AS Hours, length(filter(rows.contact, (c) => c)) AS Contact
FROM "progress/sprints" WHERE sprint = "S16" GROUP BY week
```
````

---

## 7. Plugins

| Plugin | Need | Why |
|---|---|---|
| **Dataview** | **required** | Every query above. Without it you see code blocks, not tables |
| Breadcrumbs | optional | Hierarchical up/down navigation along the chain |
| Excalidraw | optional | If you ever want to draw the capability map by hand |

Settings → Community plugins → Browse → install → enable.

---

## 8. Skills — genuinely minimal

1. **`[[` autocompletes.** That is the whole link syntax.
2. **Frontmatter is YAML between `---` fences.** You already write `stage:` lines informally.
3. **Dataview blocks: read, don't write.** I write them.
4. **One habit change:** hours as `(hours:: 2.5)` instead of a plain cell.

**GitHub tradeoff, accepted:** wikilinks render as literal `[[text]]` on GitHub and Dataview
blocks show as code. You are the only audience; `CAPABILITY_MAP.md` stays hand-maintained as the
GitHub-readable schematic.

---

## 9. Build order

| # | Step | Files | Reversible |
|---|---|---|---|
| 1 | `.obsidian/` config + `.obsidianignore` for `inventory/` | 2 new | trivially |
| 2 | Create 59 topic stubs | 59 new | delete folder |
| 3 | Create 12 concept + 14 application + 6 role stubs | 32 new | delete folder |
| 4 | Wire concept→topic, app→concept, role links | edits to stubs | git |
| 5 | **Rename `F1.4a`→`F1.4`, `F1.4b`→`F1.5`** | 4 renames + refs | git |
| 6 | Add frontmatter to 4 stage maps + 4 Feynman notes | 8 edits | git |
| 7 | Convert S16 actuals to inline fields + Dataview | 1 edit | git |
| 8 | Migrate `TOPIC_MAP.md` content → topic notes, delete file | 1 delete | git |
| 9 | Verify: every stage reaches a role; no orphan concepts | — | — |

Steps 1–4 are additive and touch nothing existing. **Step 5 is the only destructive one** and it
is the one to confirm before I run it.

---

## 10. Open questions

1. **`F1.4b` → `F1.5` — confirmed?** Fixes a real error; third rename this week.
2. **Vault root — repo root or `vault/` subfolder?** Repo root means Obsidian sees everything
   including `.claude/` and `pine_scripts/`; a subfolder means stage maps and Feynman notes sit
   *outside* the vault and cannot be linked. **Recommend repo root + `.obsidianignore`.**
3. **59 topic stubs, or only the ~25 for non-deferred sections?** You said all upfront; flagging
   that ~20 are for sections (measure theory, game theory, stochastic control) that may never be
   studied. They cost ~4 lines each and complete the map.
4. **Does `syllabus.md` survive?** It overlaps the sprint notes and would be a third place the
   calendar can drift. Suggest folding it into a Dataview query over stages.
