---
title: Binary and hexadecimal without the mystery
course: 00-intro
lesson: 02
level: absolute-beginner
prerequisites: [01-machine-code-and-assembly]
labs: []
---

# Binary and hexadecimal without the mystery

## What you will learn

You will learn why computers use binary, why C64 programmers usually write values in hexadecimal, and how to recognize and convert the small values we need first.

## Why this matters on the C64

C64 code constantly uses values such as `$00`, `$06`, `$ff`, `$d020` and `$0400`. Hexadecimal is not an advanced trick: it is a compact way to write binary values and addresses.

## The idea

Binary has two digits, 0 and 1. A single binary digit is a **bit**.

Eight bits form a **byte**. A byte can represent 256 different patterns, from binary `00000000` through `11111111`.

Hexadecimal uses sixteen digits:

`0 1 2 3 4 5 6 7 8 9 A B C D E F`

One hexadecimal digit represents exactly four bits, so two hex digits represent one byte. In this course, a leading `$` means hexadecimal:

- `$00` = binary `00000000`
- `$06` = binary `00000110`
- `$0f` = binary `00001111`
- `$ff` = binary `11111111`

You do not need to become a mental base-conversion calculator. Learn to recognize the patterns and become comfortable through use.

## What the machine does

The 6510 ultimately sees bit patterns. Hex is simply a convenient notation for us.

When you later write:

```asm
lda #$06
```

the `$06` is one byte-sized hexadecimal value. We will learn what `LDA` and `#` mean soon.

## Bytes and cycles

Binary and hexadecimal do not make code faster by themselves. They let us see values, masks, addresses and machine-code bytes in a form that maps cleanly to the hardware.

## Scene connection

**Why does a demo coder care about this?**

Demo code constantly manipulates hardware registers and individual bits. Colours, sprite controls, VIC-II modes, interrupt flags and memory layouts become much easier to reason about when hex and binary feel natural.

## Lab

### Observe

Write the binary form of `$00`, `$01`, `$0f`, `$10` and `$ff`.

### Modify

Change one bit in `00000110`. Which hexadecimal value does it become?

### Break

Deliberately write a nine-bit value. Explain why it no longer fits in one byte.

### Debug

Given `11110000`, split it into two groups of four bits and recover the hexadecimal value.

### Optimize

Compare writing `1101000000100000` with `$d020`. Which is easier to read as a C64 address?

### Challenge

Without memorizing the answer, work out the binary patterns for the sixteen single hexadecimal digits `0` through `F`.

## Checkpoint

You should understand bit, byte, binary, hexadecimal, `$` notation, and why two hex digits map neatly to one byte.

## Next

Next we turn bits and bytes into **values, words and addresses**, so numbers such as `$d020` start to mean something concrete.
