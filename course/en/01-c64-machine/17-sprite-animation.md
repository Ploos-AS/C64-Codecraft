---
title: Sprite animation as data
course: 01-c64-machine
lesson: 17
level: beginner
prerequisites: [16-multicolor-sprites]
labs: [sprite-animation]
---

# Sprite animation as data

A sprite pointer selects a 64-byte slot. That makes frame animation straightforward: place several sprite frames in suitable slots and change the pointer byte rather than copying 63 bytes every frame.

Conceptually:

```asm
    ldx anim_phase
    lda frame_pointers,x
    sta screen_base + $03f8
```

For sprite 0, its pointer is at screen_base + $03f8. The exact pointer values depend on frame placement within the active VIC bank.

## Copy or switch?

Two useful strategies now appear:

- copy new bitmap bytes into one sprite slot;
- keep several frames and switch the pointer.

Pointer switching spends more memory but much less CPU time per frame. Copying can conserve VIC-visible memory but costs bandwidth.

## Scene connection

**Why does a demo coder care about this?**

This is the same memory-versus-time decision seen with character animation, now tied directly to VIC-II object hardware. Scene code repeatedly wins by choosing the right representation before optimizing instructions.

## Lab

Place two or more sprite frames in aligned slots. Build a pointer table and animate sprite 0 by changing its pointer. Combine this with the sine movement table from the previous lesson.

## Checkpoint

You can calculate sprite pointer values and animate by switching frames rather than blindly copying bitmap data.

## Next

The graphics fundamentals are now strong enough for the next major subject: raster timing, interrupts and smooth hardware-synchronized effects.
