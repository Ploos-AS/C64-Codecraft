---
title: Side-border timing
course: 06-advanced-vicii
lesson: 06
level: advanced
prerequisites: [05-opening-borders]
labs: [side-border-timing]
---
# Side-border timing
A side-border effect requires register activity inside a narrow horizontal timing window. Raster-line synchronization alone is therefore insufficient: the critical write must occur at the intended cycle phase.

Everything learned earlier now matters together:
- IRQ jitter and stabilization;
- instruction-cycle accounting;
- page-cross behaviour;
- badlines;
- sprite DMA;
- deterministic code paths;
- VIC-II model differences.

## Engineer the path
Start from a stable entry point. Count forward to the critical write. Keep the path deterministic and prove the timing with instrumentation/debugger evidence.

Do not cargo-cult a chain of NOPs. A delay has meaning only relative to a known entry phase and target.

## Scene connection
**Why does a demo coder care about this?**
This is cycle-exact coding in its clearest form: a visible hardware result depends on a write landing inside a tiny timing window.

## Lab
Create a minimal target-specific side-border timing experiment and document the cycle path from stabilized entry to critical write.

## Next
We learn how to combine advanced tricks without destroying their timing assumptions.
