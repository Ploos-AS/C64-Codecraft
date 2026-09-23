---
title: Debug med symbols og VICE monitor
course: 10-production-craft
lesson: 03
level: advanced
prerequisites: [02-assembler-dialects]
labs: [debugger-workflow]
---
# Debug med symbols og VICE monitor
Low-level debugging blir mye raskere når addresses har navn.

Generer eller eksporter labels/symbol-information der valgt assembler støtter det. I emulator monitor/debugger brukes breakpoints, memory inspection, register state, disassembly og stepping for å koble source intent til machine behaviour.

For timing bugs kombineres debugger evidence med border probes og manuell cycle reasoning.

## Tool qualification boundary
Kurset kan bruke interactive VICE monitor workflows uten å hevde at dagens reference-container støtter deterministic remote state assertions. Det er separate capabilities som må kvalifiseres separat.

## Lab
Debug en intentionally broken teaching routine: stopp på named location, inspiser registers/memory, finn feilen og verifiser reparasjonen.

## Neste
Vi tar graphics- og music-tools inn i samme reproducible workflow.
