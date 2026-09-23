---
title: Sprite multiplexing
course: 06-advanced-vicii
lesson: 01
level: advanced
prerequisites: [05-demo-architecture/07-mini-demo-qualification]
labs: [06.01-sprite-multiplex-model]
---
# Sprite multiplexing
The VIC-II exposes eight hardware sprites, but those sprite units can be reused at different vertical positions during one frame.

A sprite multiplexer maintains a larger logical sprite list, determines which objects must be visible next, and rewrites hardware-sprite state after earlier uses are safely finished.

The first version should prioritize correctness:
- sort or otherwise schedule logical sprites by Y;
- assign hardware sprite slots;
- update position, pointer, colour and mode state;
- schedule updates before each reuse point;
- define what happens when demand exceeds available time/slots.

## Scene connection
**Why does a demo coder care about this?**
Multiplexing converts timing knowledge into an apparent hardware expansion. It is a classic example of doing more with the machine by scheduling resources.

## Lab
Display more than eight logical sprites at separated Y positions. Instrument each reuse point with the border/debugger.

## Next
We study why sprite DMA changes the cycle budget around those reuse points.
