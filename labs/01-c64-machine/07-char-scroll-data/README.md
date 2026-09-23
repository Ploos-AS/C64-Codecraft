# Lab 01.07 — Character scroll data movement

## Goal
Practice the coarse data movement behind a character scroller.

The routine shifts the first 40-column screen row one cell left and inserts screen code 1 at the right edge.

Inspect $0400-$0427 before and after. This is coarse movement only; smooth pixel scrolling belongs to Course 03.

**Why does a demo coder care?** Smooth scrollers combine VIC-II fine scroll with periodic coarse updates like this.
