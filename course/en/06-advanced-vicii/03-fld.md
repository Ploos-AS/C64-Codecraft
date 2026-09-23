---
title: FLD — flexible line distance
course: 06-advanced-vicii
lesson: 03
level: advanced
prerequisites: [02-sprite-dma]
labs: [06.03-fld-observation]
---
# FLD — flexible line distance
FLD (*Flexible Line Distance*) manipulates VIC-II vertical display timing so character rows can appear displaced, creating controllable vertical gaps/movement.

The effect is tied to the relationship between raster position, $D011 vertical scroll state and when VIC-II performs character-row fetch activity. This is exactly the territory where an unexplained delay loop is dangerous.

We first model the relevant raster/badline behaviour, then implement a target-specific timed sequence.

## Scene connection
**Why does a demo coder care about this?**
FLD turns knowledge of display fetch timing into vertical motion without redrawing an entire bitmap. It also prepares the reasoning needed for more aggressive VIC-II tricks.

## Lab
On the documented target model, create a controlled vertical displacement and annotate every timing-critical register write.

## Next
We examine the more aggressive family of line-crunch techniques.
