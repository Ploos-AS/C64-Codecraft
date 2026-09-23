---
title: Raster splits and IRQ scheduling
course: 02-raster-timing
lesson: 10
level: intermediate
prerequisites: [09-first-rasterbar]
labs: [raster-splits]
---
# Raster splits and IRQ scheduling
A raster split changes display state at a chosen vertical position so different regions of one frame can use different settings.

A common architecture is an IRQ chain: each handler performs its work, programs the next raster line, acknowledges the current source and returns. The next IRQ then handles the next region.

Possible split work includes colours, scroll values, screen/charset pointers, sprite state and music scheduling.

## Budget every region
Each handler consumes cycles and may interact with badlines or sprite DMA. The split architecture therefore needs a frame plan, not just a list of raster lines.

Keep non-critical work outside the tightest sections whenever possible.

## Scene connection
**Why does a demo coder care about this?**
Raster splits let one physical C64 frame behave like several independently configured display zones. This is a foundation for scrollers, status areas, logos and multipart-looking effects.

## Lab
Build a two-region split that changes background colour at two scheduled lines. Then document the frame as a timeline with IRQ work and known VIC-II activity.

## Checkpoint
You can explain an IRQ chain, schedule multiple raster regions and reason about their cycle budgets.

## Next
The next block combines raster timing with $D016 fine scrolling to build a smooth character scroller.
