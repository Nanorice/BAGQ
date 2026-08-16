# BAGQ — Vault Home

> Start here in Obsidian. Requires the **Dataview** plugin (Settings → Community plugins).
> If you see code blocks instead of tables, Dataview isn't enabled.

**The chain:** `stage → topic → concept → application → role`

Feynman notes and stage maps are the things you write. Everything in `vault/` is structure —
stubs you fill in as you go, never during a study block.

---

## ☀️ Open this first, every morning

**Active sprint:** [[../progress/sprints/S16|S16]] · Week 1 of 2 · ends 2026-08-16

Today's row is in the sprint file. This page tells you everything around it — what's in flight,
what's overdue, and whether anything closed is quietly untested.

## Stages in flight

```dataview
TABLE WITHOUT ID id AS Stage, name, status, sprint, budget_h AS Budget, actual_h AS Actual
FROM "stage_maps" WHERE type = "stage" SORT status ASC, id ASC
```

## ⚠️ Closed but never tested

These passed their deliverables and are waiting on a D4 unlock test. **This is the gap the old
system had no artifact for** — a stage could sit here indefinitely and nothing would say so.

```dataview
TABLE WITHOUT ID id AS Stage, name, d4_due AS "D4 due", actual_h AS Hours
FROM "stage_maps" WHERE status = "ready-for-test" SORT d4_due ASC
```

## Velocity

```dataview
TABLE WITHOUT ID
  rows.file.link[0] AS Sprint,
  sum(rows.h) AS "Hours logged",
  length(filter(rows.h, (x) => x > 0)) AS "Contact days"
FROM "progress/sprints"
FLATTEN number(hours) AS h
GROUP BY file.link
```

---

## The six roles

```dataview
TABLE WITHOUT ID file.link AS Role, tilt AS Tilt FROM "vault/roles" SORT file.name ASC
```

## Topic coverage

```dataview
TABLE WITHOUT ID id AS Topic, name, coverage, covered_by AS "Stages"
FROM "vault/topics" WHERE coverage != "none" SORT id ASC
```

## Concepts installed so far

```dataview
TABLE WITHOUT ID file.link AS Concept, topics AS "Arises in", applications AS Feeds
FROM "vault/concepts" SORT file.name ASC
```

---

## Where things live

| | |
|---|---|
| **What to do** for a stage | `stage_maps/<id>_<slug>.md` |
| **What I understood** | `progress/feynman_notes/<id>_<slug>.md` |
| Schedule, actuals, retro | `progress/sprints/S<NN>.md` — *not in the graph, by design* |
| Sequencing (what unlocks what) | [Gated Progression](../vault/method/progression.md) — **owns study order** |
| Why a stage matters | [Capability Map](../CAPABILITY_MAP.md) — GitHub-readable schematic |
| Problem inventory | `inventory/` — **excluded from the vault**, 911 problems, would swamp the graph |

**Sequencing lives in the DAG, not here.** This vault records relationships; it never decides
what to study next.
