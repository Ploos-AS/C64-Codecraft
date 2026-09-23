---
title: Entry, exit and transitions
course: 05-demo-architecture
lesson: 06
level: advanced
prerequisites: [05-part-state-and-cues]
labs: [part-transitions]
---
# Entry, exit and transitions
A demo part needs defined boundaries.

On entry, establish only the machine state the part owns: memory configuration, VIC-II state, IRQ policy, required CIA state, music relationship and effect data.

On exit, either restore the agreed environment or hand a documented state directly to the next part.

A transition may fade colours, move sprites, switch screens or prepare data for the next part while the current effect still runs.

## Ownership contract
Write down what the part assumes, changes and guarantees on exit. This becomes essential when parts are assembled by a loader or linked into a larger production.

## Scene connection
**Why does a demo coder care about this?**
A spectacular isolated effect is not yet a demo. Parts must start, coexist and hand control onward reliably.

## Lab
Implement entry, a cue-triggered transition and exit to a simple successor state.

## Next
We qualify the complete mini-demo part under emulator/debugger observation.
