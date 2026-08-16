---
type: role
name: Portfolio construction
tilt: qr
---

# Portfolio construction

> Turn return forecasts and a covariance estimate into position sizes.

**Tilt:** `qr` — this is a *scheduling weight* for S23+, not a statement about which branch is
real. Every role below matters to both targets. See [[../method/progression|the fork]].

## Applications that feed it

```dataview
LIST FROM "vault/applications" WHERE contains(string(roles), "portfolio-construction")
```

## Stage coverage

```dataview
TABLE id AS Stage, status, sprint, actual_h AS Hours
FROM "stage_maps" WHERE contains(string(roles), "portfolio-construction")
```
