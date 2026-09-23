---
title: Qualify the mini-demo part
course: 05-demo-architecture
lesson: 07
level: advanced
prerequisites: [06-transitions]
labs: [05.07-mini-demo-qualification]
---
# Qualify the mini-demo part
The integrated part now contains enough moving pieces that "it looked okay once" is not a useful acceptance test.

Qualification should cover:
- clean assembly from source;
- documented memory map with no unintended overlap;
- explicit target video model(s);
- stable raster regions over sustained execution;
- correct music cadence;
- coarse-scroll/DYCP worst-case frames;
- sprite movement and animation;
- cue transitions;
- entry/exit ownership;
- repeatable emulator test procedure;
- real hardware testing when available.

Automate deterministic checks where the current toolchain genuinely supports them. Do not claim emulator state verification that has not been qualified.

## Release evidence
Keep the PRG/binary reproducible from source. Record assembler/tool versions and any generated-data steps.

## Checkpoint
You have designed, integrated, measured and qualified a small scene-style demo part rather than merely collecting effects.

## Next
The next course moves into advanced VIC-II techniques: sprite multiplexing, FLD, open borders, line crunching and other timing-sensitive tricks.
