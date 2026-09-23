---
title: Measure before optimizing
course: 08-6510-optimization
lesson: 01
level: advanced
prerequisites: [07-bitmap-high-colour/07-high-colour-integration]
labs: [08.01-measure-first]
---
# Measure before optimizing
Choose a real hot path from an earlier effect. Record its instruction path, cycles under relevant conditions, bytes of code/data, call frequency and timing deadline.

Average cost can hide the failure. For raster work, the worst relevant path often matters most.

Use border probes, debugger traces and manual cycle accounting as complementary evidence.

## Scene connection
**Why does a demo coder care about this?**
A routine that is 20% faster but was never on the critical path may improve nothing. Optimization starts by finding what actually limits the effect.

## Lab
Create a baseline report for one scroller, sprite or raster routine. No optimization is allowed until the baseline exists.

## Next
We spend scarce zero-page bytes where they produce measurable value.
