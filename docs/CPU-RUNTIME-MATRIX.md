# CPU/RAM Runtime Qualification Matrix

This file tracks the bulk audit for deterministic CPU/RAM qualification.
`cpu_state` means execution in the repository's deterministic 6502/6510 harness;
it does not imply VIC-II/SID/CIA/VICE qualification.

## Qualified

| Lab | Status | Notes |
|---|---|---|
| 08.04 Tables and precalculation | PASS | RAM/ZP/table result asserted |
| 08.09 Measured optimization pass | PASS | arithmetic loop output asserted |
| 09.07 Part contracts | PASS | 16-byte contract table asserted |

## Next CPU/RAM batch

| Lab | Classification | Required harness work |
|---|---|---|
| 08.02 Zero-page strategy | CPU/RAM | LDY, LDA (zp),Y, STA abs,Y, INY, CPY, INC zp |
| 08.03 Page boundaries | CPU/RAM | existing LDX/LDA abs,X plus STA abs |
| 08.05 Loop unrolling | CPU/RAM | existing loop opcodes plus LDA abs |
| 08.08 Size vs speed | CPU/RAM | JSR/RTS, DEX, BPL, LDA abs |
| 09.01 Why pack | CPU/RAM | LDA abs plus STA abs |
| 09.02 Reproducible packing | CPU/RAM | existing indexed-copy subset |
| 09.03 Memory-safe depacking | CPU/RAM | existing indexed-copy subset |

## Deferred from CPU-only qualification

| Lab | Reason |
|---|---|
| 08.01 Measure first | writes VIC-II border register $D020 |
| 08.06 Self-modifying code | final observable effect is $D020; keep for hardware-aware path |
| 09.08 Multipart demo | state-machine semantics need repeated entry calls; qualify after call/entry contract is generalized |

The remaining courses are audited in batches. Labs touching VIC-II, SID, CIA, raster
timing, banking, loaders, or other C64 hardware are intentionally kept out of the
CPU-only gate rather than being falsely marked as emulator-qualified.
