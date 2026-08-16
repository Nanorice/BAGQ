---
type: concept
name: inclusion-exclusion
topics: ["[[I-1-combinatorics-and-counting]]"]
applications: ["[[signal-testing]]"]
---

# inclusion-exclusion

> Add the singles, subtract the pairs, add the triples. The signs alternate because an element in

**Arises in:** [[I-1-combinatorics-and-counting]]
**Feeds:** [[signal-testing]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

Add the singles, subtract the pairs, add the triples. The signs alternate because an element in
exactly m sets must end up counted once, and sum (-1)^(k+1) C(m,k) = 1.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "inclusion-exclusion")
```
