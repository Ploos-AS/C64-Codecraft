# Lab 10.06 — Release-candidate craft

## Goal
Treat release creation as a qualification gate, not as “copy the latest build”.

Build a release candidate from known sources and record:
- commit/revision,
- assembler/tool versions,
- generated artifact names,
- sizes and checksums,
- target video-standard assumptions,
- emulator tests,
- real-hardware tests when available,
- credits/provenance,
- known limitations.

The starter writes a small signature block to RAM so a debugger can confirm exactly which candidate is running.

**Why does a demo coder care?** A compo or public release must be identifiable, rebuildable and testable under pressure.
