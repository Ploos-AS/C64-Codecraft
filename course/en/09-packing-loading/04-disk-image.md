---
title: Build a reproducible disk image
course: 09-packing-loading
lesson: 04
level: advanced
prerequisites: [03-memory-safe-depacking]
labs: [d64-build]
---
# Build a reproducible disk image
A disk image is a build artifact, not a manually curated mystery file.

The source tree should describe which files enter the image, their C64-visible names/order where relevant, and how the image is generated. A clean build should recreate the release image from source assets and tools.

Do not commit copyrighted system ROMs merely to make emulator startup convenient.

## Inspect the result
Automated checks can verify expected directory entries and payload hashes/sizes where tooling supports it. Emulator qualification is a separate concern.

## Lab
Generate a .d64 containing a boot/entry program plus at least two part/data files and verify its directory from the build.

## Next
We separate ordinary file loading from a demo loader architecture.
