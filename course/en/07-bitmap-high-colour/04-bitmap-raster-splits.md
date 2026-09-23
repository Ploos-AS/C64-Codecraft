---
title: Raster splits inside bitmap graphics
course: 07-bitmap-high-colour
lesson: 04
level: advanced
prerequisites: [03-asset-pipeline]
labs: [bitmap-raster-splits]
---
# Raster splits inside bitmap graphics
A bitmap does not force one display state for the entire frame. Raster-scheduled writes can change selected VIC-II state between regions.

Start with a simple shared-colour change at a known line. Then reason about more ambitious splits only after accounting for badlines, bitmap fetch activity and the exact registers being changed.

The frame plan from earlier courses still applies.

## Scene connection
**Why does a demo coder care about this?**
Raster splits let limited per-cell colour information be supplemented by changes over vertical position. This is the conceptual bridge toward high-colour display techniques.

## Lab
Create a bitmap with two raster regions using a documented register change. Measure the IRQ/timing cost and mark affected lines.

## Next
We study the idea behind FLI rather than starting with a copied FLI routine.
