---
title: Toward a stable raster
course: 02-raster-timing
lesson: 08
level: intermediate
prerequisites: [07-irq-jitter]
labs: [stable-raster]
---
# Toward a stable raster
A stable raster routine separates two jobs:

1. get close to the desired raster position;
2. remove the remaining cycle uncertainty before executing the critical sequence.

Classic C64 code uses carefully designed synchronization techniques, often involving a first interrupt and a precisely arranged second stage. The exact instruction sequence depends on the VIC-II model, surrounding interrupt policy and effect requirements.

Codecraft will not present a copied delay sequence as magic. Every stabilization sequence must come with a cycle explanation and an explicit target model.

## Engineering rule
Once stabilized, the critical path must remain deterministic. Avoid unexpected branches, page crossings, interrupts or VIC-II DMA effects unless they are part of the timing design.

## Scene connection
**Why does a demo coder care about this?**
Stable timing is the gateway to horizontal raster positioning, reliable splits and many VIC-II tricks.

## Lab
Build the documented model-specific two-stage synchronization lab, annotate each instruction with cycles, and verify repeatability using border/debugger observations.

## Next
We spend that stability on the first controlled rasterbar.
