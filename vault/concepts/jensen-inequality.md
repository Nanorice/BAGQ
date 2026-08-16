---
type: concept
name: Jensen's inequality
topics: ["[[I-7-expectation-variance-and-moments]]"]
applications: ["[[kelly-sizing]]", "[[black-scholes-pricer]]"]
---

# Jensen's inequality

> E[f(X)] >= f(E[X]) for convex f. Why an option on the average is not the average of options, and

**Arises in:** [[I-7-expectation-variance-and-moments]]
**Feeds:** [[kelly-sizing]] · [[black-scholes-pricer]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

E[f(X)] >= f(E[X]) for convex f. Why an option on the average is not the average of options, and
why volatility drag makes geometric returns lag arithmetic ones.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "jensen-inequality")
```
