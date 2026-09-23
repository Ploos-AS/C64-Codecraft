# Lab 10.03 — Debugger workflow

## Goal
Debug from evidence instead of editing code until the symptom disappears.

The starter contains an intentional logic bug: it copies only seven of eight bytes.

## Workflow
1. State expected memory contents.
2. Reproduce the failure.
3. Break at the copy loop in VICE.
4. Inspect X, PC and destination memory.
5. Identify the first point where actual state diverges.
6. Fix the cause.
7. Re-run and verify all eight bytes.

**Why does a demo coder care?** Raster and memory bugs become tractable when you can locate the first incorrect machine state.
