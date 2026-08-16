---
type: concept
name: conditional information
topics: ["[[I-3-conditional-probability-and-bayes-theorem]]"]
applications: ["[[adverse-selection]]"]
---

# conditional information

> Being filled is itself information. P(price moves against me | I was filled) is not P(price moves

**Arises in:** [[I-3-conditional-probability-and-bayes-theorem]]
**Feeds:** [[adverse-selection]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

Being filled is itself information. P(price moves against me | I was filled) is not P(price moves
against me) - the same conditioning that makes Bayes non-obvious makes market making hard.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "conditional-information")
```
