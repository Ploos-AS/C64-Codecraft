---
title: Sprite movement and 9-bit X
course: 01-c64-machine
lesson: 13
level: beginner
prerequisites: [12-first-sprite]
labs: [01.09-sprite-9bit-x]
---

# Sprite movement and 9-bit X

Sprite Y positions fit in one byte. X positions need nine bits because the visible coordinate range extends beyond 255.

For sprite 0, the low eight X bits are written to $d000. The ninth X bit is bit 0 of $d010. The other bits of $d010 belong to the other sprites, so code must preserve them.

```asm
; low eight bits
lda sprite_x_lo
sta $d000

; set or clear bit 0 of $d010 according to the high bit
```

This is our first strong reason to learn read-modify-write bit operations rather than overwriting a whole hardware register blindly.

## Scene connection

**Why does a demo coder care about this?**

Sprite movement routinely crosses the 255 boundary. Shared bit registers such as $d010 also teach a crucial hardware habit: change only the bits you own.

## Lab

Move sprite 0 across positions below and above 255. Observe the discontinuity when the ninth bit is omitted, then implement correct high-bit handling while preserving the other sprite bits.

## Checkpoint

You understand why sprite X is 9-bit and why $d010 must be modified carefully.

## Next

We drive X/Y from tables instead of calculating every position in the hot path.
