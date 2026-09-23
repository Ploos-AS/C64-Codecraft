# Appendix P — Cycle-counting checklist

Cycle counting is a reasoning tool, not a ritual.

## Start with the path
1. Identify entry phase/condition.
2. List instructions actually executed.
3. Include branch outcomes.
4. Include relevant page-cross effects.
5. Account for interrupts or other asynchronous work.
6. Account for VIC-II bus stealing where it affects CPU availability.
7. Compare the result with the deadline/window.
8. Measure in emulator/debugger and, when appropriate, hardware.

## Determinism
For cycle-exact code, ask whether data values can select a different path. A fast average path is irrelevant if a slower legal path misses the raster window.

## Border probe
A border-colour change is a useful visual instrument for coarse timing and jitter. It is not a replacement for instruction-level reasoning.

## Optimization log
Record baseline, proposed change, expected saving, measured result and regressions. Keep/revert from evidence.
