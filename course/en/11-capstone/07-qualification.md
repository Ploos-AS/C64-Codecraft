---
title: Qualification
course: 11-capstone
lesson: 07
level: capstone
prerequisites: [06-optimize-and-integrate]
labs: [11.07-qualification]
---
# Qualification
State what the release supports.

If PAL is the primary target, say so explicitly. If NTSC is supported, test it rather than inferring support from a PAL run. Timing-sensitive code must identify the relevant VIC-II/video assumptions.

Qualification should cover:
- clean build;
- complete run from boot to ending;
- sustained raster stability;
- music cadence and sync;
- loader/depacker transitions;
- worst-case effect paths;
- generated asset reproduction;
- disk contents;
- emulator procedure;
- real C64 testing when hardware is available.

A manual test is not an automated assertion. Record each honestly.

## Gate
No known blocker remains against the declared target policy.

## Next
Freeze the candidate and prepare the public release.
