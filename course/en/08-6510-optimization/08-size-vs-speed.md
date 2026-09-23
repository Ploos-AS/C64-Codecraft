---
title: Size, speed and production constraints
course: 08-6510-optimization
lesson: 08
level: advanced
prerequisites: [07-undocumented-opcodes]
labs: [08.08-size-vs-speed]
---
# Size, speed and production constraints
Fastest is not always best. A 4K intro, a one-file demo part and a disk-loaded multipart production can have very different constraints.

Possible objectives include:
- minimum cycles in a raster window;
- minimum code/data bytes;
- minimum load time;
- enough free memory for graphics/music;
- predictable timing;
- maintainable iteration before release.

Optimizing for one metric can damage another.

## Sizecoding mindset
Sizecoding encourages reuse, computed data, overlapping roles and compact instruction choices. Speed coding may instead spend memory on tables and unrolled code. Both are valid when the production goal demands them.

## Lab
Take one routine and produce two variants: one optimized primarily for cycles and one primarily for bytes. Document the different decisions without declaring a universal winner.

## Next
We finish with an evidence-driven optimization pass on a real effect.
