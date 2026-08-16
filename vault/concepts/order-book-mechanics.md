---
type: concept
name: order book mechanics
topics: ["[[IV-4-poisson-processes-and-jump-processes]]"]
applications: ["[[market-structure]]"]
---

# order book mechanics

> Price-time priority: at a given price, the order that arrived first is filled first. Your position in

**Arises in:** [[IV-4-poisson-processes-and-jump-processes]]
**Feeds:** [[market-structure]]

## In my own words
<!-- fill this when a stage first teaches it - one paragraph, no jargon -->

Price-time priority: at a given price, the order that arrived first is filled first. Your position in
that queue, not just your price, decides whether you trade.

## Stages that install it

```dataview
TABLE id AS Stage, status, sprint FROM "stage_maps" WHERE contains(string(concepts), "order-book-mechanics")
```
