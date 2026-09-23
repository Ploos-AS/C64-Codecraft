---
title: Build a small custom charset
course: 01-c64-machine
lesson: 09
level: beginner
prerequisites: [08-first-custom-character]
labs: [small-custom-charset]
---

# Build a small custom charset

A monochrome C64 character consumes eight bytes. A complete 256-character set therefore occupies 2048 bytes, and character N begins at charset_base + N*8.

That arithmetic matters.

```text
character 0 -> base + 0*8
character 1 -> base + 1*8
character 2 -> base + 2*8
...
```

A small effect does not have to use every possible character, but the VIC-II addressing structure still reserves positions in the character set.

## From one glyph to assets

Define several related shapes: perhaps animation frames, logo tiles or pieces of a pattern. Put their screen codes into screen RAM to compose a larger image.

Keep source data understandable first. Asset converters can later generate the same byte representation from image-oriented workflows.

## Scene connection

**Why does a demo coder care about this?**

Character mode trades flexibility for compact data. Reusing 8-byte tiles can produce much larger graphics, and modifying character data can animate every screen cell that references that character.

## Lab

Create four custom characters and arrange their screen codes into a small 2x2 graphic. Calculate each character's byte offset before assembling.

## Checkpoint

You can calculate character offsets and use multiple custom characters as reusable graphics assets.

## Next

We exploit reuse directly by animating character data.
