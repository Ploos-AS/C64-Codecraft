---
title: Loop unrolling
course: 08-6510-optimization
lesson: 05
level: advanced
prerequisites: [04-tables-and-precalculation]
labs: [08.05-loop-unrolling]
---
# Loop unrolling
A loop spends time on control: index updates, comparisons and branches. Unrolling duplicates the body so fewer control operations execute.

Full unrolling can produce a large straight-line routine. Partial unrolling can retain flexibility while reducing overhead.

The trade is explicit: more code bytes for fewer runtime cycles and often more deterministic timing.

## Generated assembly
For large repetitive routines, consider generating assembly source/data rather than maintaining hundreds of hand-copied lines. The generated result must remain inspectable and reproducible.

## Lab
Measure rolled, partially unrolled and fully unrolled versions of one fixed-size operation. Record cycles and code bytes.

## Next
We let code modify carefully chosen operands at runtime.
