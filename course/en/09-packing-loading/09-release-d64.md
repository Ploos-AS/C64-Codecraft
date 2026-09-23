---
title: Qualify the release disk
course: 09-packing-loading
lesson: 09
level: advanced
prerequisites: [08-multipart-demo]
labs: [release-d64]
---
# Qualify the release disk
A release image should be reproducible and testable from the repository.

Qualification includes:
- clean build of every part;
- deterministic asset generation where feasible;
- documented packer/loader versions;
- generated disk directory verification;
- no unintended memory overlap;
- every part transition exercised;
- target PAL/NTSC policy stated;
- sustained music/effect operation where required;
- emulator test procedure;
- real-hardware test record when available;
- release file hashes recorded by CI/build tooling when practical.

Do not put proprietary ROMs or unlicensed third-party music/art into the repository to make qualification convenient.

## Checkpoint
You can construct a multipart C64 production whose storage, packing, loading, depacking and part boundaries are engineered rather than improvised.

## Next
The next block is production craft: scene tooling, source/data organization, credits, release metadata, debugging workflows and preparing the final capstone demo.
