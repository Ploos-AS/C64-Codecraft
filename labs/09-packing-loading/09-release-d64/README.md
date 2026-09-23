# Lab 09.09 — Release D64 qualification

## Goal
Turn a build into a reproducible release artifact.

The reference lab always assembles a boot PRG. A D64 target should be added only with a disk-image utility that has been qualified for the host/OCI environment.

## Release checklist
A release candidate must record:
- disk title and ID,
- boot filename,
- deterministic file order,
- every part/artifact included,
- disk-image command and tool version,
- emulator boot test,
- real-hardware test when available,
- PAL/NTSC assumptions,
- checksums for distributed artifacts.

Do not manually edit the final D64 after the reproducible build step.

**Why does a demo coder care?** The release artifact is what the audience and compo machine actually run; it deserves the same engineering discipline as the effects.
