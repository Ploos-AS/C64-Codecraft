---
title: Think in raster lines
course: 02-raster-timing
lesson: 01
level: intermediate
prerequisites: [01-c64-machine/17-sprite-animation]
labs: [raster-observation]
---
# Think in raster lines
VIC-II builds the video image over time. Raster position advances through scan lines and then starts a new frame. A register write can therefore affect different parts of one frame depending on when it occurs.

## PAL and NTSC
Different VIC-II/video standards have different frame structures and timing. Never silently apply one model's constants everywhere; timing values must name their target.

## Scene connection
**Why does a demo coder care about this?**
A C64 demo is often choreography between the 6510 and VIC-II. Code can synchronize directly with video hardware.

## Lab
Observe raster/debug information in VICE on an explicitly selected model and record that model with your observations.

## Next
We read and program raster position through $D011/$D012.
