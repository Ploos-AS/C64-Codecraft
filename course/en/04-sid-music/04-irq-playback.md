---
title: Schedule music playback
course: 04-sid-music
lesson: 04
level: intermediate
prerequisites: [03-init-and-play]
labs: [irq-music-playback]
---
# Schedule music playback
A music play routine needs a reliable cadence. A raster IRQ can provide that cadence while also participating in the visual frame schedule.

Where the play call belongs depends on its cycle cost and the effect layout. Do not put it inside the most timing-critical section merely because an IRQ is convenient.

Measure the player call with the same tools used for visual routines.

## Preserve the contract
If the player clobbers registers or zero-page locations, the surrounding code must account for that. If visual code and music both want the same memory, redesign the layout rather than relying on luck.

## Scene connection
**Why does a demo coder care about this?**
Music is another scheduled workload. Once its cost is known, it becomes part of the same engineering problem as scrollers, sprites and raster effects.

## Lab
Call the documented test player from a raster-scheduled frame and measure its execution window with a border probe/debugger.

## Next
Playback cadence is where PAL/NTSC differences become especially visible.
