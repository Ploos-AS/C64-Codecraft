---
title: Memory-safe depacking
course: 09-packing-loading
lesson: 03
level: advanced
prerequisites: [02-reproducible-packing]
labs: [09.03-memory-safe-depacking]
---
# Memory-safe depacking
A depacker reads compressed input, writes expanded output and executes code while both representations may temporarily coexist.

Before running it, map:
- packed source range;
- depacker code/state;
- output range;
- stack/zero-page needs;
- resident music/IRQ code;
- buffers;
- banking requirements.

Overlapping source and destination is safe only when the specific format/depacker explicitly supports that arrangement.

## Scene connection
**Why does a demo coder care about this?**
A perfect effect is useless if transition-time depacking overwrites the player, stack or the bytes it has not read yet.

## Lab
Draw the complete memory timeline for a packed asset from loaded bytes to final expanded placement.

## Next
We put multiple files into a reproducible disk image.
