---
type: role
name: Market making and execution
tilt: hft
---

# Market making and execution

> Quote two-sided prices, manage inventory, get filled at good prices.

**Tilt:** `hft` — this is a *scheduling weight* for S23+, not a statement about which branch is
real. Every role below matters to both targets. See [[../../03_gated_progression|the fork]].

## Applications that feed it

```dataview
LIST FROM "vault/applications" WHERE contains(string(roles), "market-making")
```

## Stage coverage

```dataview
TABLE id AS Stage, status, sprint, actual_h AS Hours
FROM "stage_maps" WHERE contains(string(roles), "market-making")
```
