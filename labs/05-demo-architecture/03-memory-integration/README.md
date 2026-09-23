# Lab 05.03 — Memory ownership map

## Goal
Integrate independent data blocks by assigning explicit addresses and checking their boundaries at assembly time.

The example places effect tables at $c000 and sprite data at $2000. Symbols describe ownership; the assembler layout is the source of truth.

## Challenge
Add a music region and document every overlap risk, including zero-page bytes.

**Why does a demo coder care?** Most multi-effect failures are easier to prevent with a memory map than to debug after integration.
