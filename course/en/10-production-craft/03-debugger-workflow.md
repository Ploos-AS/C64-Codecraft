---
title: Debug with symbols and the VICE monitor
course: 10-production-craft
lesson: 03
level: advanced
prerequisites: [02-assembler-dialects]
labs: [debugger-workflow]
---
# Debug with symbols and the VICE monitor
Low-level debugging becomes much faster when addresses have names.

Generate or export labels/symbol information where the chosen assembler supports it. In the emulator monitor/debugger, use breakpoints, memory inspection, register state, disassembly and stepping to connect source intent with machine behaviour.

For timing bugs, combine debugger evidence with border probes and manual cycle reasoning.

## Tool qualification boundary
The course may use interactive VICE monitor workflows without claiming that the current reference container supports deterministic remote state assertions. Those are separate capabilities and must be qualified separately.

## Lab
Debug an intentionally broken teaching routine: stop at a named location, inspect registers/memory, identify the fault and verify the repair.

## Next
We bring graphics and music tools into the same reproducible workflow.
