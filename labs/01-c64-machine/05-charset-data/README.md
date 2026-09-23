# Lab 01.05 — Custom charset data block

## Goal
Scale from one glyph to a deliberately aligned character-data block.

The program copies four 8-byte teaching glyphs to $c800. Inspect the 32 bytes and calculate each glyph's offset.

## Challenge
Add a fifth glyph and access it by `character_index * 8` during development.

**Why does a demo coder care?** Charset animation and scrollers depend on predictable glyph layout long before clever raster code begins.
