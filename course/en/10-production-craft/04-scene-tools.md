---
title: Work with scene tools
course: 10-production-craft
lesson: 04
level: advanced
prerequisites: [03-debugger-workflow]
labs: [10.04-scene-tools]
---
# Work with scene tools
A production can combine command-line assemblers with specialized graphics, music and debugging tools.

Examples of tool categories include:
- sprite/charset/bitmap editors and converters;
- SID trackers/composers such as GoatTracker workflows;
- emulator/debuggers;
- packers and disk-image tools;
- host-side generators for tables and assembly data.

GUI tools may run natively on the host while the reproducible build remains command-line driven.

## Preserve the source
Store legal editable source assets where licensing permits, plus enough metadata to reproduce exported C64 data. Do not treat a binary export as the only surviving master.

## Lab
Take one editable graphics or music test asset through its documented export/import pipeline and reproduce the bytes consumed by the assembly build.

## Next
We make provenance and credits first-class production data.
