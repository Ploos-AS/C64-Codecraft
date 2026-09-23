---
title: Build vertically shifted glyphs
course: 03-smooth-scrolling
lesson: 08
level: intermediate
prerequisites: [07-dycp-concept]
labs: [03.08-shifted-glyphs]
---
# Build vertically shifted glyphs
An 8x8 glyph is eight row bytes. Moving its visible pixels vertically means choosing where those source rows appear in a larger destination window.

For teaching, start with an offline transformation: take one source glyph and generate variants for vertical offsets. Inspect every output byte.

This makes the representation concrete before we optimize it.

## Precompute or rebuild?
Two broad choices appear:

- precompute shifted variants and select them at runtime;
- generate/rebuild destination character data while the demo runs.

Precomputation costs memory. Runtime generation costs cycles and writes to VIC-visible memory. Hybrid designs are possible.

## Scene connection
**Why does a demo coder care about this?**
The important skill is not memorizing one DYCP routine. It is transforming graphics into a representation that makes the runtime effect affordable.

## Lab
Generate vertical variants of several glyphs for a small offset range. Verify the bytes visually and calculate the memory cost.

## Next
We connect shifted glyph selection to the moving text stream.
