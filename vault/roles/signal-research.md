---
type: role
name: Signal research
tilt: qr
---

# Signal research

> Find something that predicts returns, and establish it is not noise.

**Tilt:** `qr` — this is a *scheduling weight* for S23+, not a statement about which branch is
real. Every role below matters to both targets. See [[../../03_gated_progression|the fork]].

## Applications that feed it

```dataview
LIST FROM "vault/applications" WHERE contains(string(roles), "signal-research")
```

## Stage coverage

```dataview
TABLE id AS Stage, status, sprint, actual_h AS Hours
FROM "stage_maps" WHERE contains(string(roles), "signal-research")
```
