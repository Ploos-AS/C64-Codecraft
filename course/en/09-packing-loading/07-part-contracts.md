---
title: Contracts between demo parts
course: 09-packing-loading
lesson: 07
level: advanced
prerequisites: [06-loading-under-effects]
labs: [multipart-contracts]
---
# Contracts between demo parts
Each part should declare what it needs on entry and what it guarantees on exit.

Useful contract fields include:
- entry address;
- loaded memory ranges;
- zero-page/stack ownership;
- VIC-II bank/display assumptions;
- IRQ/NMI/CIA state;
- music/player state;
- resident loader buffers;
- exit reason/next-part request.

The contract is not a Codecraft runtime API. It is documentation and ordinary assembly-level agreement between components.

## Scene connection
**Why does a demo coder care about this?**
Parts can be developed and optimized independently only when their boundaries are explicit.

## Lab
Write contracts for two existing teaching parts and resolve every conflicting memory/state assumption before linking the transition.

## Next
We assemble a complete multipart flow.
