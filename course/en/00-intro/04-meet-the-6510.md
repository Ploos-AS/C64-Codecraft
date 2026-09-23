---
title: Meet the 6510
course: 00-intro
lesson: 04
level: absolute-beginner
prerequisites: [03-bytes-words-addresses]
labs: []
---

# Meet the 6510

## What you will learn

You will learn the simple fetch/decode/execute model and meet the 6510 registers: A, X, Y, PC, SP and the processor status flags.

## Why this matters on the C64

The 6510 is the CPU at the centre of the C64. Assembly becomes much less mysterious once you can picture where the CPU keeps its immediate working state.

## The idea

Very roughly, the CPU repeats:

1. **Fetch** the next instruction byte from memory.
2. **Decode** what that instruction means.
3. **Execute** it.
4. Continue with the next instruction, unless execution changes the flow.

The **program counter (PC)** identifies where execution continues.

The registers you will use most are:

- **A — accumulator:** central to loads, stores, arithmetic and logic.
- **X and Y — index registers:** useful for counting, indexing and addressing data.
- **SP — stack pointer:** tracks the CPU stack.
- **PC — program counter:** tracks execution.
- **P/status:** flags recording conditions such as zero, negative and carry.

Do not memorize every flag today. We will introduce each one when an instruction gives it a purpose.

## Smallest useful 6510 example

```asm
lda #$06
```

Read it for now as: **load the value $06 into A**.

After this instruction, A contains `$06`. Nothing visible has to change on the screen yet.

## What the machine does

The CPU fetches the opcode and operand bytes, decodes the instruction, places `$06` in A, updates the relevant status flags, and continues.

This distinction is important: CPU state can change even when the screen does not.

## Bytes and cycles

`LDA #value` is encoded as two bytes and takes two CPU cycles on the 6502/6510.

You do not need to optimize this. Start building the habit of noticing that instructions consume both **memory** and **time**.

## Scene connection

**Why does a demo coder care about this?**

Demo effects are ultimately sequences of CPU operations scheduled against hardware. A, X and Y become the working hands of routines that move sprites, index tables, update colours and feed effects. Later, knowing exactly what state an instruction changes becomes essential for tight timing.

## Lab

### Observe

Imagine A initially contains `$00`. Execute `lda #$06` on paper. What does A contain afterward?

### Modify

Change the operand to `#$0e`. Predict A.

### Break

Remove the `#` mentally. Do not guess what happens; note that this changes the addressing mode and therefore the meaning. We will teach addressing modes explicitly.

### Debug

If A contains `$06` after the instruction but the border has not changed, explain why this is not a bug.

### Optimize

Record the two facts for this instruction: two bytes, two cycles.

### Challenge

Describe, without code, why a demo routine might use X or Y as a counter while A carries values being written to hardware.

## Checkpoint

You should know the purpose of A, X, Y, PC, SP and status flags at a beginner level, and be able to describe fetch/decode/execute.

## Next

Next we study `LDA` carefully, including what the `#` means, before using `STA` to make our first visible hardware change.
