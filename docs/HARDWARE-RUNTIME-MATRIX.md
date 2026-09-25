# C64 Hardware/Emulator Runtime Qualification Matrix

This matrix is the M0.2 counterpart to `CPU-RUNTIME-MATRIX.md`.
`emulator_state: true` is reserved for machine-level assertions proven by a
qualified C64 emulator/hardware runner.

## Qualification classes

| Class | Scope | Initial examples |
|---|---|---|
| VIC-II state | register writes/readback and visible configuration | border/background, $D011/$D016/$D018 |
| Raster/timing | raster position, IRQ timing, badlines, cycle-sensitive effects | $D012 waits, rasterbars, stable raster |
| Color RAM | $D800-$DBFF C64 color RAM semantics | row fills, table-driven colors |
| SID | voice/register state and playback contracts | first voice, frame playback |
| CIA | timers, IRQ/NMI and I/O semantics | timer-driven examples |
| Banking | 6510 $0000/$0001 and ROM/I/O visibility | memory-map/banking labs |
| Disk/loader | drive, D64 and loading behavior | loader/release labs |

## Initial M0.2 queue

| Lab | Class | Status | Reason |
|---|---|---|---|
| 00.03 Subroutine/stack | VIC-II state | PASS | VICE 3.9 binary-monitor assertion of $D020/$D021 readback; non-cycle-exact |
| 00.08 Fill row | Color RAM | PASS | VICE 3.9 asserts screen RAM $0400/$0427 and masked 4-bit Color RAM $D800/$D827 after the 40-column fill |
| 00.09 Table-driven screen | Color RAM | PASS | VICE 3.9 asserts repeated 8-cell motif across screen RAM and masked 4-bit Color RAM, including final column |
| 07.02 Multicolor bitmap data | VIC-II + Color RAM | TODO | $D021 plus color RAM |
| 07.04 Bitmap raster splits | Raster/timing | TODO | waits on $D012 |
| 08.01 Measure first | VIC-II state | TODO | border instrumentation |
| 08.06 Self-modifying code | VIC-II state | TODO | observable result currently $D020 |
| 09.04 Disk image contract | VIC-II + disk | TODO | machine state plus disk contract |
| 09.09 Release D64 | VIC-II + Color RAM + disk | TODO | release artifact qualification |

## Gate

M0.2 is complete when at least one hardware-facing lab is qualified by a
reproducible machine runner with a machine-readable assertion, and an
intentional wrong expectation is proven to fail. Raster/timing, SID, CIA and
disk support remain independent follow-on capabilities and must not be implied
by the first VIC-II-state pass.
