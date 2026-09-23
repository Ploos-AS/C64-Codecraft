---
title: Zero-page strategy
course: 08-6510-optimization
lesson: 02
level: advanced
prerequisites: [01-measure-first]
labs: [08.02-zero-page-strategy]
---
# Zero-page strategy
Zero page provides shorter and often faster addressing forms, and it is required for important indirect addressing modes. But zero-page space is shared, finite and may also be used by the operating environment or integrated players.

Treat it as a resource budget.

Good candidates include frequently accessed pointers, counters or state on a measured hot path. Cold data does not deserve zero page merely because space happens to be free today.

## Ownership
Document every reserved byte/range and its lifetime. Integration bugs from overlapping zero-page ownership can be far harder to diagnose than ordinary RAM overlap.

## Lab
Move selected hot state into zero page, measure the cycle/byte change, and update the part memory contract.

## Next
Memory placement also changes timing at page boundaries.
