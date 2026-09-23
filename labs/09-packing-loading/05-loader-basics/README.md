# Lab 09.05 — Loader state contract

## Goal
Separate loader responsibilities from effect responsibilities before implementing a fastloader.

A software model records a request, destination and completion state. No disk protocol is hidden in the starter.

## Contract
A real loader integration must document:
- device/protocol assumptions,
- destination ownership,
- IRQ/NMI/CIA usage,
- banking state,
- error path,
- restoration requirements.

**Why does a demo coder care?** Loaders are system code. They share interrupts, memory and timing with the demo and must have explicit boundaries.
