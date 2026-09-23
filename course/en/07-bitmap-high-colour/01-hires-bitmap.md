---
title: Hires bitmap mode
course: 07-bitmap-high-colour
lesson: 01
level: advanced
prerequisites: [06-advanced-vicii/07-composing-vicii-tricks]
labs: [hires-bitmap]
---
# Hires bitmap mode
Bitmap mode changes how VIC-II interprets display memory. Instead of selecting character glyphs for each screen cell, bitmap data supplies pixel patterns while screen memory contributes colour information.

A standard bitmap occupies 8000 bytes for the 320x200 pixel field. The organization is still strongly tied to 8x8 display cells rather than being a simple modern linear framebuffer.

That layout matters when plotting, converting images and scheduling updates.

## Scene connection
**Why does a demo coder care about this?**
Bitmap mode gives pixel-level artwork but costs much more memory than a charset. Understanding its cell-oriented layout is essential before using converters or advanced bitmap tricks.

## Lab
Create a tiny generated test pattern, locate its bytes in bitmap memory and verify how the corresponding screen-memory colour data affects it.

## Next
We trade horizontal resolution for more colour choices in multicolor bitmap mode.
