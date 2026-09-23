# Lab 01.10 — Sine-table sprite movement

## Goal
Drive a hardware coordinate from prepared motion data.

Each invocation advances a phase and writes the next table value to sprite 0 X. Repeated calls keep the data path visible before proper frame scheduling is introduced.

Inspect phase, table lookup and hardware write as three separate jobs.

**Why does a demo coder care?** Precalculated tables replace runtime maths with predictable indexed loads.
