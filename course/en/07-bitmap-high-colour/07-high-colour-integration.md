---
title: Integrate high-colour graphics
course: 07-bitmap-high-colour
lesson: 07
level: advanced
prerequisites: [06-fli-family]
labs: [07.07-high-colour-integration]
---
# Integrate high-colour graphics
A high-colour raster routine may consume much of the frame and impose strong memory placement rules. Integration therefore begins with the timing and memory contracts, not with adding features until something breaks.

Place music playback, transitions, sprite work and decompression/preparation into windows the graphics routine genuinely leaves available.

If an asset must be converted or precomputed, keep that build step reproducible.

## Qualification
Test sustained raster stability, worst-case music/effect paths, memory overlap, target VIC-II model and clean regeneration of graphics data.

Real hardware testing is especially valuable for model-sensitive display tricks when hardware is available.

## Checkpoint
You can explain bitmap representations, build reproducible assets, reason about FLI-family mechanisms and integrate a high-colour display as part of a constrained production.

## Next
The next block focuses on advanced 6510 optimization: zero-page strategy, page boundaries, unrolling, self-modifying code and carefully justified undocumented opcodes.
