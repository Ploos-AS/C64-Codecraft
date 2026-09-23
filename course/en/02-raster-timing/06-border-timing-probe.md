---
title: The border as a timing probe
course: 02-raster-timing
lesson: 06
level: intermediate
prerequisites: [05-badlines]
labs: [02.06-border-timing-probe]
---
# The border as a timing probe
A border-colour write gives a visible marker for when code executes relative to the raster.

```asm
    inc $d020
    ; code being measured
    dec $d020
```

This is not a precision instrument by itself, but it is an excellent first visualization of CPU time. A wider coloured region means more time elapsed between the writes.

## Measure deliberately
Keep the target machine model fixed. Know whether interrupts, badlines or sprite DMA can occur during the measured region. For exact work, combine visual probes with emulator/debugger cycle information.

## Scene connection
**Why does a demo coder care about this?**
Border timing turns invisible execution cost into something you can see. Scene programmers have long used the border as a practical timing/debug surface.

## Lab
Wrap two routines with border writes and compare their visible widths. Predict the faster routine from cycle counts before running.

## Next
We use the probe to see IRQ entry jitter.
