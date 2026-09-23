---
title: Badlines and VIC-II bus time
course: 02-raster-timing
lesson: 05
level: intermediate
prerequisites: [04-cycle-budgets]
labs: [02.05-badline-observation]
---
# Badlines and VIC-II bus time
In normal character display modes, VIC-II periodically performs extra memory fetches for display data. These **badlines** reduce CPU time on those raster lines.

The exact condition depends on display state and vertical fine-scroll/raster conditions; we derive it when manipulating $D011. Sprite DMA can also consume bus time.

**The CPU does not own every bus cycle.**

## Scene connection
**Why does a demo coder care about this?**
Badlines are part of the machine you compose with. Advanced effects schedule around, move, suppress or exploit VIC-II fetch behaviour.

## Lab
On an explicit PAL or NTSC model, identify candidate badlines from reference material and verify reduced CPU availability experimentally.

## Next
We use the border as an oscilloscope and start removing timing uncertainty.
