# Lab 03.01 — $D016 fine X scroll

## Goal
Change only the XSCROLL field in $D016 while preserving the other VIC-II control bits.

Each invocation advances a 0–7 phase and merges it into bits 0–2 of $D016.

Inspect $D016 before/after and verify that unrelated bits survive.

**Why does a demo coder care?** Hardware effects should modify owned bitfields, not casually overwrite shared control registers.
