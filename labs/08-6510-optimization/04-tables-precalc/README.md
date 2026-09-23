# Lab 08.04 — Tables and precalculation

## Goal
Replace repeated runtime transformation with a lookup table.

The baseline computes a simple 4× transform with shifts. The table path reads the same result from prepared data. Both write results for inspection.

Measure both approaches and include the table's memory cost in the comparison.

**Why does a demo coder care?** Precalculation exchanges memory and preparation work for predictable runtime cost.
