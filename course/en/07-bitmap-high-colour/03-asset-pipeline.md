---
title: A reproducible graphics pipeline
course: 07-bitmap-high-colour
lesson: 03
level: advanced
prerequisites: [02-multicolor-bitmap]
labs: [bitmap-pipeline]
---
# A reproducible graphics pipeline
Real productions rarely type thousands of bitmap bytes by hand. Artwork is created or converted with external tools, then assembled into the production.

A good pipeline records:
- source asset;
- converter/tool and version;
- command/options;
- target C64 format;
- generated bitmap/screen/colour data;
- load addresses or linker placement;
- any palette/dithering assumptions.

Generated output is replaceable; the recipe and legal source asset are the important reproducible inputs.

## No opaque magic
Inspect small generated samples and compare them with the format learned in the previous lessons. A converter saves labour; it does not replace understanding.

## Lab
Convert or generate a small legal course-owned image and reproduce identical C64 data from a clean checkout.

## Next
We change display state during the bitmap itself.
