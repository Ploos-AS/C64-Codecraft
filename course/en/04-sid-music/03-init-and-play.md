---
title: Music init and play routines
course: 04-sid-music
lesson: 03
level: intermediate
prerequisites: [02-first-voice]
labs: [04.03-init-play-contract]
---
# Music init and play routines
Many C64 music players expose a small machine-code interface: an initialization entry point called once and a play entry point called repeatedly at the required rate.

The exact calling convention, subtune selection, clobbered registers, memory range and playback rate belong to the specific music/player. Read its documentation or exported metadata; do not assume a universal contract.

Conceptually:

```asm
    ; select/init tune according to player contract
    jsr music_init

frame:
    ; at the required cadence
    jsr music_play
```

Codecraft does not wrap this in its own API.

## Scene connection
**Why does a demo coder care about this?**
Real productions integrate code and music from different tools/authors. Respecting a player's memory and calling contract is part of demo architecture.

## Lab
Integrate a redistributable/open test tune or course-owned test player whose exact contract is documented. Mark its occupied memory on the demo memory map.

## Next
We schedule play calls from the frame/IRQ structure.
