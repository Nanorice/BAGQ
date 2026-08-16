---
type: concept
name: mean reversion
topics: ["[[IV-1-brownian-motion]]"]
applications: ["[[inventory-management]]", "[[execution-tca]]"]
---

# mean reversion

> dx/dt = kappa(theta - x): the further from the level, the harder the pull back. Ornstein-Uhlenbeck is

**Arises in:** [[IV-1-brownian-motion]]
**Feeds:** [[inventory-management]] · [[execution-tca]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

dx/dt = kappa(theta - x): the further from the level, the harder the pull back. Ornstein-Uhlenbeck is
the continuous version, and it is the model behind both inventory skew and impact decay.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "mean-reversion")
```
