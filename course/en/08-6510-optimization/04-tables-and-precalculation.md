---
title: Tables and precalculation
course: 08-6510-optimization
lesson: 04
level: advanced
prerequisites: [03-page-boundaries]
labs: [precalculation-tradeoffs]
---
# Tables and precalculation
The 6510 is often fastest when expensive decisions have already been made.

Tables can replace arithmetic, wrapping logic, address calculation, colour generation, animation decisions or other repeated work. Host-side generation can move still more computation out of runtime.

But tables consume memory and may create cache-like locality concerns in the human sense: placement, page crossing and indexing become part of the design.

## Scene connection
**Why does a demo coder care about this?**
Precalculation is one of the defining ways demo code trades abundant offline computation and memory for scarce runtime cycles.

## Lab
Replace one measured runtime calculation with generated lookup data. Compare runtime cycles, total bytes and build complexity.

## Next
We trade code size for speed with loop unrolling.
