# Lab 01.04 — First custom character

## Goal
Build character bitmap data yourself and inspect its eight bytes.

This starter keeps the data at a simple RAM location for inspection before the next lab changes VIC-II charset selection.

## Expected result
No display takeover yet. The important result is that `glyph` assembles to eight rows representing an 8×8 pattern.

## Observe
Inspect the bytes and draw their bits as pixels.

**Why does a demo coder care?** Charset effects start as raw bytes; tools may later generate them, but the coder must understand the representation.
