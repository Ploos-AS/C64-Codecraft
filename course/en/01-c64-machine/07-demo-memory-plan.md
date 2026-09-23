---
title: Plan memory before the effect
course: 01-c64-machine
lesson: 07
level: beginner
prerequisites: [06-d018-screen-and-charset]
labs: [memory-plan]
---

# Plan memory before the effect

A demo part is easier to build when major memory users are planned before they collide.

A simple plan might reserve regions for:

- program code;
- zero-page variables/pointers;
- stack;
- screen matrix;
- custom charset;
- sprite data;
- music and player;
- effect tables;
- temporary buffers.

The exact addresses depend on the part, toolchain, loader and hardware configuration. There is no universal Codecraft layout.

## Constraints matter

Ask for every region:

1. Does the CPU need to read/write it?
2. Does VIC-II need to fetch it?
3. Must ROM or I/O be visible at the same time?
4. Does it need alignment?
5. Can it cross a page without hurting timing?
6. Can data be reused or discarded after initialization?

## Scene connection

**Why does a demo coder care about this?**

Memory planning is optimization before instruction optimization. A good layout can make graphics reachable, free RAM under ROM, simplify pointers and remove timing penalties. A bad layout can make an otherwise good effect awkward or impossible.

## Lab

Create a memory-map document for a hypothetical one-part demo with one screen, one 2 KiB charset, sprite data, music, code and tables. Mark CPU and VIC-II requirements separately.

## Checkpoint

You can reason about memory placement as a set of hardware and software constraints rather than copying fixed addresses.

## Next

We now create character data ourselves and point VIC-II at it.
