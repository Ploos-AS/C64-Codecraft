---
title: Your first instruction — LDA
course: 00-intro
lesson: 05
level: absolute-beginner
prerequisites: [04-meet-the-6510]
labs: []
---

# Your first instruction — LDA

## What you will learn

You will learn what `LDA` does and what **immediate addressing** means.

## Why this matters on the C64

The accumulator is a common route for getting a value from one place to another. Loading A is therefore one of the first building blocks for controlling C64 memory and hardware.

## The idea

`LDA` means **LoaD Accumulator**.

```asm
lda #$06
```

The `#` says that `$06` is the value itself. This is called **immediate addressing**.

So:

`lda #$06` -> put the value `$06` into A.

Contrast that idea with an address: without immediate syntax, an operand can instead refer to a memory location. We will introduce those forms carefully rather than mixing them together now.

## What the machine does

Before:

`A = $00`

Execute:

```asm
lda #$06
```

After:

`A = $06`

For this value the zero flag is clear because the result is not zero. `LDA` also updates the negative flag according to bit 7. We will give flags their own practical exercises later.

## Bytes and cycles

On the 6510, immediate `LDA` uses **2 bytes** and **2 cycles**.

Its machine-code bytes for this example are:

```text
A9 06
```

`A9` is the opcode for LDA immediate; `06` is the operand.

You have now connected assembly syntax directly to actual machine code.

## Scene connection

**Why does a demo coder care about this?**

Before you can write a colour, sprite coordinate or control value to hardware, that value often has to be prepared in a CPU register. Immediate loads are also common when initializing effects and hardware registers.

## Lab

### Observe

Assemble or inspect `lda #$06` and find the bytes `A9 06`.

### Modify

Change it to `lda #$0e`. Predict both A and the two machine-code bytes before assembling.

### Break

Compare `#$06` with `$06`. Explain why the `#` must not be treated as decoration.

### Debug

If the assembler produces `A9 0E`, explain what each byte represents.

### Optimize

Write down the instruction's size and cycle count. We are measuring, not optimizing yet.

### Challenge

Choose four C64 colour values from `$00` through `$0f` and write four immediate LDA instructions that would load them one at a time.

## Checkpoint

You should be able to read `lda #$06`, explain immediate addressing, predict A afterward, and recognize `A9 06` as the resulting machine-code bytes.

## Next

A value sitting in A is invisible. Next we learn `STA` and send that value to the VIC-II border-colour register.
