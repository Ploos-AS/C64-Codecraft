# CPU/RAM Runtime Qualification Matrix

This file tracks the bulk audit for deterministic CPU/RAM qualification.
`cpu_state` means execution in the repository's deterministic 6502/6510 harness;
it does not imply VIC-II/SID/CIA/VICE qualification.

## Qualified

| Lab | Status | Notes |
|---|---|---|
| 08.02 Zero-page strategy | PASS | zero-page pointer/state and copied output asserted |
| 08.03 Page boundaries | PASS | indexed reads across page boundary asserted |
| 08.04 Tables and precalculation | PASS | RAM/ZP/table result asserted |
| 08.05 Loop unrolling | PASS | loop-generated output asserted |
| 08.08 Size vs speed | PASS | compact and expanded copies plus stack restoration asserted |
| 08.09 Measured optimization pass | PASS | arithmetic loop output asserted |
| 09.01 Why pack | PASS | payload read/write contract asserted |
| 09.02 Reproducible packing | PASS | deterministic output asserted |
| 09.03 Memory-safe depacking | PASS | depack-model output asserted |
| 09.05 Loader basics | PASS | request/destination/status and stack contract asserted |
| 09.06 Loading under effects | PASS | job state and RAM outputs asserted |
| 09.07 Part contracts | PASS | 16-byte contract table asserted |
| 09.08 Multipart demo | PASS | repeated-entry LOAD/INIT/RUN/EXIT state machine asserted |

## Deferred from CPU-only qualification

| Lab | Reason |
|---|---|
| 08.01 Measure first | writes VIC-II border register $D020 |
| 08.06 Self-modifying code | final observable effect is $D020; keep for hardware-aware path |
| 09.04 Disk image contract | writes VIC-II registers $D020/$D021 |
| 09.09 Release D64 | writes VIC-II/color RAM; release artifact also needs disk/emulator qualification |

The remaining courses are audited in batches. Labs touching VIC-II, SID, CIA, raster
timing, banking, loaders, or other C64 hardware are intentionally kept out of the
CPU-only gate rather than being falsely marked as emulator-qualified.
