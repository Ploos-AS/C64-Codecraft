# CPU/RAM Runtime Qualification Matrix

This file tracks the bulk audit for deterministic CPU/RAM qualification.
`cpu_state` means execution in the repository's deterministic 6502/6510 harness;
it does not imply VIC-II/SID/CIA/VICE qualification.

## Qualified

| Lab | Status | Notes |
|---|---|---|
| 00.05 Zero-page pointer | PASS | zero-page pointer and 16-byte indirect-indexed fill asserted |
| 00.06 Indirect indexed | PASS | source pointer and 16-byte indirect-indexed copy asserted |
| 01.04 Custom character | PASS | 8-byte glyph copy asserted |
| 01.05 Charset data | PASS | 32-byte charset data block asserted |
| 01.06 Character animation | PASS | all four animation frames and frame advance asserted |
| 01.07 Character scroll data | PASS | 39-byte overlapping row shift and tail byte asserted |
| 03.03 Text stream | PASS | stream byte and text index advance asserted |
| 03.06 Phase-shifted sine | PASS | generated 8-byte sine output and phase advance asserted |
| 03.08 Shifted glyphs | PASS | both 8-byte glyph variants asserted |
| 04.05 Playback-rate model | PASS | three playback scheduling policy cases asserted |
| 07.01 Hires bitmap layout | PASS | bitmap tile and screen byte asserted |
| 07.03 Asset pipeline | PASS | bitmap and screen asset blocks asserted |
| 07.05 FLI concept | PASS | screen-state and colour-state model blocks asserted |
| 07.06 FLI family | PASS | all four three-byte family descriptors asserted |
| 07.07 High-colour integration | PASS | job state, RAM outputs, and stack restoration asserted |
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
| 10.03 Debugger workflow | PASS | complete 8-byte data block asserted |
| 10.04 Scene tools | PASS | generated 8-byte asset asserted |
| 10.06 Release craft | PASS | release signature asserted |
| 10.07 Production review | PASS | seven-byte review gate state asserted |
| 11.02 Technical design | PASS | eight-byte design-state contract asserted |
| 11.07 Qualification | PASS | deterministic qualification state asserted |
| 11.09 Postmortem | PASS | three-byte postmortem marker asserted |

## Deferred from CPU-only qualification

| Lab | Reason |
|---|---|
| 00.08 Fill row | writes color RAM at $D800 |
| 00.09 Table-driven screen | writes color RAM at $D800 |
| 07.02 Multicolor bitmap data | writes color RAM $D800 and VIC-II $D021 |
| 07.04 Bitmap raster splits | synchronizes on $D012 and writes $D020 |
| 08.01 Measure first | writes VIC-II border register $D020 |
| 08.06 Self-modifying code | final observable effect is $D020; keep for hardware-aware path |
| 09.04 Disk image contract | writes VIC-II registers $D020/$D021 |
| 09.09 Release D64 | writes VIC-II/color RAM; release artifact also needs disk/emulator qualification |

Other labs touching VIC-II, SID, CIA, raster timing, banking, loaders, or other C64
hardware are intentionally kept out of the CPU-only gate rather than being falsely
marked as emulator-qualified. Pure sub-contracts may still be qualified separately
later when doing so does not imply qualification of the hardware-facing lab.
