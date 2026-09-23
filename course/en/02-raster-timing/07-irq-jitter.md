---
title: IRQ jitter
course: 02-raster-timing
lesson: 07
level: intermediate
prerequisites: [06-border-timing-probe]
labs: [02.07-irq-jitter-probe]
---
# IRQ jitter
A raster IRQ requests service at a defined video position, but the CPU does not necessarily begin your first handler instruction on one invariant cycle.

The CPU may be finishing an instruction when the request becomes serviceable. Interrupt entry itself has defined CPU behaviour, and other machine activity must also be controlled or understood.

The result is **jitter**: the handler can arrive with a small timing uncertainty even though the raster line is correct.

## Why line accuracy is not cycle accuracy
For many jobs, line-level scheduling is enough. For a colour transition or trick that must occur at a precise horizontal position, it is not.

Stable raster techniques deliberately remove this uncertainty before entering cycle-critical code.

## Scene connection
**Why does a demo coder care about this?**
A one- or few-cycle variation can move a visible register change horizontally. Stability is therefore an engineering problem, not just "set an IRQ and hope".

## Lab
Use the border timing probe at IRQ entry and observe variation across frames in a controlled environment.

## Next
We build a stabilization stage before the effect.
