---
title: The 64 KiB memory map
course: 01-c64-machine
lesson: 01
level: beginner
prerequisites: [00-intro/18-table-driven-screen]
labs: [01.01-memory-map]
---

# The 64 KiB memory map

The 6510 can address $0000-$ffff: 65,536 CPU addresses. But an address does not always expose the same physical thing.

Important regions in the normal C64 configuration include:

- $0000-$00ff: zero page, with $00/$01 special on the C64
- $0100-$01ff: CPU stack page
- $0400 onward: default screen RAM
- $a000-$bfff: BASIC ROM normally visible
- $d000-$dfff: I/O normally visible, including VIC-II, SID, colour RAM and CIA
- $e000-$ffff: KERNAL ROM normally visible

RAM exists underneath ROM/I/O in important regions. What the CPU sees depends on memory configuration.

## Scene connection

**Why does a demo coder care about this?**

A demo needs deliberate homes for code, graphics, music, tables and buffers. Banking can expose RAM that appears hidden, while hardware I/O must be visible when you access registers.

Memory layout is therefore part of program architecture.

## Lab

Sketch the map and place the code/data used in earlier lessons. Mark $0400, $d020 and $d800. Then mark the ROM and I/O regions.

## Checkpoint

You understand that the CPU has a 64 KiB address space and that visible RAM/ROM/I/O depends on configuration.

## Next

We examine the special 6510 port at $00/$01 that helps control this visibility.
