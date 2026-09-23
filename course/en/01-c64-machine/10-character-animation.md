---
title: Character animation
course: 01-c64-machine
lesson: 10
level: beginner
prerequisites: [09-custom-charset]
labs: [character-animation]
---

# Character animation

If several screen cells use the same screen code, they all refer to the same character shape. Change that shape and all those cells can appear to change together.

One simple strategy is to prepare several eight-byte frames and copy the selected frame into the active character slot.

```asm
    ldx #$07
copy_frame:
    lda frame1,x
    sta charset_base + 8,x
    dex
    bpl copy_frame
```

This introduces `BPL`: branch while the negative flag is clear. Starting at 7 and decrementing lets us copy exactly eight bytes.

## Data versus bandwidth

Animation is not free. Updating character RAM consumes CPU cycles and memory bandwidth. Pre-storing multiple characters and changing screen codes can sometimes be cheaper than copying bitmap bytes; other effects benefit from modifying the charset itself.

## Scene connection

**Why does a demo coder care about this?**

Demos constantly trade memory against CPU time. Character animation makes that trade visible very early: store more frames, copy data, modify data in place, or change references.

## Lab

Animate one character between two 8-byte frames. Then place the same screen code in several cells and observe how one charset update affects them all.

## Checkpoint

You understand character reuse, frame data and the memory-versus-CPU trade-off.

## Next

Before smooth pixel scrolling, we first learn coarse character scrolling.
