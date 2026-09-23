---
title: Build the first DYCP
course: 03-smooth-scrolling
lesson: 09
level: intermediate
prerequisites: [08-shifted-glyphs]
labs: [first-dycp]
---
# Build the first DYCP
Now combine four systems already learned:

1. the smooth horizontal text stream;
2. a phase value for each visible character position;
3. a sine-derived vertical offset;
4. shifted glyph data or another explicit vertical-placement representation.

The first version should prioritize traceability over cleverness. A student must be able to point from a message byte to its source glyph, selected offset and final visible data.

## Keep timing visible
Instrument the update with the border. Separate work that must happen in the raster-critical region from data preparation that can run elsewhere.

If the first implementation exceeds its budget, that is useful evidence. Measure before optimizing.

## Scene connection
**Why does a demo coder care about this?**
This is now unmistakably a demo effect: text, tables, generated graphics, raster scheduling and cycle budgeting all interact.

## Lab
Build a short DYCP with a small alphabet/message and modest wave. Record ordinary-frame and coarse-update costs.

## Next
We optimize from measurements rather than folklore.
