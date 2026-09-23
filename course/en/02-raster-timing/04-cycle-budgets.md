---
title: Cycle budgets
course: 02-raster-timing
lesson: 04
level: intermediate
prerequisites: [03-first-raster-irq]
labs: [cycle-budget]
---
# Cycle budgets
Instruction-cycle counts now become a budget. For a specific VIC-II model a raster line has a fixed timing structure, while VIC-II can also take bus time from the CPU.

Count execution paths, not just mnemonics. Conditional branches, page crossings, interrupt entry/exit and data-dependent paths change timing.

```text
LDA #imm       2
STA abs        4
BNE taken      3
BNE not taken  2
```

Never quote a line-cycle constant without naming the target video standard/model.

## Scene connection
**Why does a demo coder care about this?**
Cycle budgeting turns "fast enough" into schedulable engineering.

## Lab
Count a short border routine by hand and compare it with debugger observations on the selected model.

## Next
VIC-II sometimes takes a large structured part of that budget: badlines.
