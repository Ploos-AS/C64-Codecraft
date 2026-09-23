---
title: The FLI concept
course: 07-bitmap-high-colour
lesson: 05
level: advanced
prerequisites: [04-bitmap-raster-splits]
labs: [fli-model]
---
# The FLI concept
FLI (*Flexible Line Interpretation*) is a family-defining idea: carefully timed VIC-II register changes alter display-fetch behaviour so colour/display information can be refreshed more frequently than in an ordinary bitmap setup.

That extra flexibility is not free. It introduces strict raster timing, substantial data requirements and characteristic display constraints/artifacts depending on the implementation.

Before code, model:
- which display data VIC-II normally fetches;
- when those fetches occur;
- which register changes influence the fetch sequence;
- what extra colour freedom is gained;
- what CPU/memory/display cost is paid.

## Scene connection
**Why does a demo coder care about this?**
FLI is a landmark example of exploiting hardware sequencing to create a graphics mode the machine was not designed to expose as a simple mode bit.

## Lab
Draw a line-by-line conceptual fetch/state diagram comparing ordinary multicolor bitmap with the FLI strategy used by the later target-specific lab.

## Next
We compare FLI-family variants and choose by constraints rather than prestige.
