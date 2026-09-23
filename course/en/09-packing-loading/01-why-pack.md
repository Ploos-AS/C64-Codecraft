---
title: Why pack demo data?
course: 09-packing-loading
lesson: 01
level: advanced
prerequisites: [08-6510-optimization/09-optimization-pass]
labs: [packing-baseline]
---
# Why pack demo data?
Packing reduces stored size by transforming code or assets into a compressed representation plus a depacking step.

That can improve disk usage and transfer/load time, but it costs something elsewhere: depacker code, CPU time, temporary memory, destination constraints and build complexity.

Always keep the original generated asset/code as the conceptual input. Packed bytes are a delivery representation.

## Scene connection
**Why does a demo coder care about this?**
Packing can make a larger production practical, but only when depacking fits the memory and transition plan.

## Lab
Measure the uncompressed sizes of one part and its major assets. Define which constraint packing is intended to improve before selecting a tool.

## Next
We make the packing step reproducible and replaceable.
