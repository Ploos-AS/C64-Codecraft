---
title: PAL, NTSC and playback cadence
course: 04-sid-music
lesson: 05
level: intermediate
prerequisites: [04-irq-playback]
labs: [04.05-playback-rate-model]
---
# PAL, NTSC and playback cadence
A tune may expect calls tied to a particular video/frame rate or another timing source. PAL and NTSC machines do not provide identical frame timing.

Therefore, "call play once per frame" is not automatically portable.

The correct strategy depends on the player and tune: use the cadence it declares, adapt scheduling when appropriate, or explicitly target one standard.

## State the target
A demo may legitimately be PAL-only. It may support both standards. What matters is that the decision is explicit and tested rather than accidental.

## Scene connection
**Why does a demo coder care about this?**
Wrong cadence changes musical tempo and can break synchronization between audio and effects.

## Lab
Run the documented test tune under explicit PAL and NTSC emulator models. Compare frame-driven playback and record the observed consequence.

## Next
We create synchronization state that visual code can consume.
