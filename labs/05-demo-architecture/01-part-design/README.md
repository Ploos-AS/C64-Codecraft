# Lab 05.01 — Part lifecycle

## Goal
Give a demo part an explicit lifecycle without inventing a Codecraft runtime.

The program calls ordinary 6510 subroutines: `part_init`, `part_update`, `part_render`, and `part_shutdown`. The interface is a teaching convention inside this lab, not a required framework.

Inspect which state each routine owns.

**Why does a demo coder care?** Clear lifecycle boundaries make effects easier to integrate, replace and debug.
