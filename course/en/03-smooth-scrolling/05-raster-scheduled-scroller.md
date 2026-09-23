---
title: A raster-scheduled smooth scroller
course: 03-smooth-scrolling
lesson: 05
level: intermediate
prerequisites: [04-colour-scrolling]
labs: [03.05-raster-scheduled-state]
---
# A raster-scheduled smooth scroller
We now combine the previous blocks into one effect:

- raster IRQ chooses when the scroller region is serviced;
- $D016 supplies fine X movement;
- periodic coarse updates shift screen data;
- a text stream supplies incoming characters;
- colour logic supplies the visual palette.

Separate **critical** work from **deferred** work. Register changes that must happen at a precise raster position belong in the timed section. Message parsing or other non-critical preparation can often happen elsewhere in the frame.

## Frame thinking
Document the frame as a timeline. Mark IRQs, badlines, sprite DMA if active, coarse-update frames and spare time. The scroller is no longer an isolated routine; it is a scheduled subsystem of the demo part.

## Scene connection
**Why does a demo coder care about this?**
This is the transition from individual tricks to effect architecture. A real demo coordinates several jobs inside one frame budget.

## Lab
Build the complete one-line smooth scroller and document its frame schedule. Measure ordinary and coarse-update frames separately.

## Checkpoint
You can explain the whole pipeline from message byte to smooth visible motion and account for when the work happens.

## Next
We bend the straight scroller into per-character vertical motion: the conceptual road toward DYCP.
