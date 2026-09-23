---
title: Bytes, words, memory and addresses
course: 00-intro
lesson: 03
level: absolute-beginner
prerequisites: [02-binary-and-hex]
labs: []
---

# Bytes, words, memory and addresses

## What you will learn

You will learn what a byte is, what C64 programmers mean by a word, how memory can be pictured as numbered storage locations, and what an address such as `$d020` means.

## Why this matters on the C64

Assembly programming is full of addresses because the C64 exposes both RAM and hardware through the CPU's address space. Writing to the right address can change something you can immediately see or hear.

## The idea

Imagine memory as a long row of numbered boxes. Each box has an **address** and can hold one byte.

The 6510 has a 16-bit address space. That gives 65,536 possible addresses, conventionally written from `$0000` through `$ffff`.

A **word** in normal 6502/6510 usage is 16 bits, or two bytes. A word is large enough to represent an address in this 16-bit address space.

Not every address always means ordinary RAM. The C64 can map ROM and I/O hardware into parts of the same address space. We will learn that mapping gradually.

## A first important address

`$d020` is associated with the VIC-II border-colour register in the normal C64 I/O configuration.

Later, when we execute:

```asm
sta $d020
```

we are not asking a graphics library to change the border. The CPU writes directly to an address through which the VIC-II is controlled.

## What the machine does

For a memory operation the CPU needs to know both **what operation** to perform and **which address/value** it concerns. Assembly gives us a readable notation for both.

## Bytes and cycles

Addresses also influence instruction encoding, size and timing. Some especially useful addresses in the first 256 bytes form the **zero page** and can be accessed efficiently by many 6502/6510 instructions. We will earn that optimization later rather than treating it as magic now.

## Scene connection

**Why does a demo coder care about this?**

A C64 demo is built around deliberate use of the machine's address space: screen data, colour data, graphics, music, code, tables, stacks and hardware registers all need a home. Eventually memory layout itself becomes part of effect design.

## Lab

### Observe

Identify the lowest and highest addresses in a 16-bit address space.

### Modify

If an address increases from `$0400` to `$0401`, describe what changed.

### Break

Try to represent `$10000` with only four hexadecimal digits. Explain why it lies beyond a 16-bit address.

### Debug

Explain the difference between the **address** `$d020` and a **value** such as `$06` that might be written there.

### Optimize

Compare the size of the address ranges `$0000-$00ff` and `$0000-$ffff`. Notice why zero page is a particularly small resource.

### Challenge

Draw a tiny memory map with separate labelled regions for code, data and one hardware-register address. It does not need to match the real C64 map yet.

## Checkpoint

You should be able to explain byte, word, address, 16-bit address space, and the difference between an address and the value stored or written there.

## Next

Next we meet the 6510 CPU itself: its registers and the fetch/decode/execute loop that turns our bytes into activity.
