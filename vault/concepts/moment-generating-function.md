---
type: concept
name: moment generating function
topics: ["[[I-8-generating-functions-and-transforms]]"]
applications: ["[[var-tail-risk]]"]
---

# moment generating function

> M(t) = E[e^tX]: differentiate at zero to get moments, multiply to get sums of independents. The

**Arises in:** [[I-8-generating-functions-and-transforms]]
**Feeds:** [[var-tail-risk]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

M(t) = E[e^tX]: differentiate at zero to get moments, multiply to get sums of independents. The
engine behind Chernoff bounds and the cleanest proof of the CLT.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "moment-generating-function")
```
