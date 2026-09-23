---
title: Loop unrolling
course: 08-6510-optimization
lesson: 05
level: advanced
prerequisites: [04-tables-og-precalculation]
labs: [08.05-loop-unrolling]
---
# Loop unrolling
En loop bruker tid på control: index updates, comparisons og branches. Unrolling dupliserer body slik at færre control operations kjøres.

Full unrolling kan gi en stor straight-line routine. Partial unrolling kan beholde flexibility samtidig som overhead reduseres.

Trade-off er eksplisitt: flere code bytes mot færre runtime cycles og ofte mer deterministic timing.

## Generated assembly
For store repetitive routines bør assembly source/data kunne genereres fremfor å vedlikeholde hundrevis av håndkopierte linjer. Generated result skal fortsatt være inspectable og reproducible.

## Lab
Mål rolled, partially unrolled og fully unrolled variant av én fixed-size operation. Noter cycles og code bytes.

## Neste
Vi lar code endre nøye valgte operands ved runtime.
