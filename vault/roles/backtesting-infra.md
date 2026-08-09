---
type: role
name: Backtesting and infrastructure
tilt: both
---

# Backtesting and infrastructure

> Simulate a strategy on history without lying to yourself.

**Tilt:** `both` — this is a *scheduling weight* for S23+, not a statement about which branch is
real. Every role below matters to both targets. See [[../../03_gated_progression|the fork]].

## Applications that feed it

```dataview
LIST FROM "vault/applications" WHERE contains(string(roles), "backtesting-infra")
```

## Stage coverage

```dataview
TABLE id AS Stage, status, sprint, actual_h AS Hours
FROM "stage_maps" WHERE contains(string(roles), "backtesting-infra")
```
