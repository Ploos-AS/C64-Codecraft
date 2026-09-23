---
title: Optimize the DYCP
course: 03-smooth-scrolling
lesson: 10
level: intermediate
prerequisites: [09-first-dycp]
labs: [03.10-dycp-optimization]
---
# Optimize the DYCP
Optimization starts with the measured bottleneck.

Useful options may include:

- move calculations to precalculated tables;
- arrange tables to remove wrap branches;
- use zero-page state where the savings matter;
- align data to avoid unwanted page-cross penalties;
- update only data that actually changed;
- move non-critical work out of the timed region;
- unroll a loop when the cycle saving justifies the bytes;
- use self-modifying code later where it is clear, controlled and worthwhile.

Do not apply every technique automatically. Each optimization spends something: memory, code size, complexity, flexibility or setup time.

## Prove the improvement
Keep before/after cycle counts and binary-size changes. An optimization without measurement is only a hypothesis.

## Scene connection
**Why does a demo coder care about this?**
Scene credibility comes from understanding trade-offs, not decorating code with obscure tricks. Fast code should have a reason for being fast.

## Lab
Choose the two largest measured costs in the DYCP, optimize them independently, and record cycles/bytes before and after.

## Checkpoint
You can build and measure a real table-driven scene effect and choose optimizations from evidence.

## Next
The next block introduces SID music, frame-rate playback and synchronization between sound and visual effects.
