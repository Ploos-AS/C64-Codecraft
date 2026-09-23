---
title: VIC-II 16 KiB banks
course: 01-c64-machine
lesson: 05
level: beginner
prerequisites: [04-meet-the-cias]
labs: [01.03-vic-bank-d018]
---

# VIC-II 16 KiB banks

The VIC-II does not simply see the CPU's whole 64 KiB address space. For graphics fetches it works inside one 16 KiB bank at a time.

CIA2 port A participates in selecting that bank. The four banks correspond to:

- $0000-$3fff
- $4000-$7fff
- $8000-$bfff
- $c000-$ffff

The CIA2 selection bits are active-low, so the bit pattern is easy to misread. Always derive the intended bank from a trusted reference and preserve unrelated port bits when modifying the register.

## CPU view versus VIC-II view

A CPU address and a VIC-II graphics address are related but not identical concepts. CPU ROM/I/O banking through $00/$01 and VIC-II bank selection solve different problems.

This distinction is essential before relocating screen or character data.

## Scene connection

**Why does a demo coder care about this?**

A VIC bank is a 16 KiB graphics workspace. Screen matrices, character sets, bitmap data and sprite data must be placed where the VIC-II can fetch them. Bank choice therefore constrains the memory layout of an effect or demo part.

## Lab

Draw all four 16 KiB VIC banks. Choose one and mark candidate locations for screen and character data. Do not write CIA2 blindly; first identify which bits must be preserved.

## Checkpoint

You understand that VIC-II sees one selected 16 KiB bank for graphics fetches and that CIA2 bank selection is distinct from CPU $00/$01 banking.

## Next

Inside the selected bank, $D018 tells VIC-II where important display data lives.
