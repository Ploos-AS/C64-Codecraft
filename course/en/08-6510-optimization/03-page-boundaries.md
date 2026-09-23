---
title: Page boundaries and deterministic timing
course: 08-6510-optimization
lesson: 03
level: advanced
prerequisites: [02-zero-page-strategy]
labs: [08.03-page-boundaries]
---
# Page boundaries and deterministic timing
Some indexed memory accesses can incur an extra cycle when the effective address crosses a page boundary. Branch timing also depends on whether a taken branch crosses a page.

In ordinary code this may be a small performance detail. In cycle-exact code it can become unwanted timing variation.

Alignment can therefore be a timing tool, not just an aesthetic linker choice.

## Prove the path
Do not add alignment directives blindly. Identify the exact access/branch whose timing matters, then arrange code/data so the relevant path has the required behaviour.

## Lab
Construct a small routine whose timing changes across a page boundary, observe it, then place code/data deliberately to make the critical path deterministic.

## Next
We optimize control flow and layout together.
