# Appendix K — VIC-II register quick reference

This is a navigation aid for registers used throughout the course.

## Frequently used registers
- $d000-$d00f — sprite X/Y coordinate pairs.
- $d010 — sprite X-coordinate high bits.
- $d011 — vertical control/scroll plus raster high-bit semantics.
- $d012 — raster register / low raster compare bits.
- $d015 — sprite enable.
- $d016 — horizontal control/scroll and multicolor-related display control.
- $d017 — sprite Y expansion.
- $d018 — screen/character/bitmap memory selection within the active VIC bank.
- $d019 — VIC interrupt status/acknowledge.
- $d01a — VIC interrupt mask.
- $d01b — sprite/background priority.
- $d01c — sprite multicolor enable.
- $d01d — sprite X expansion.
- $d020 — border colour.
- $d021 — background colour 0.
- $d025/$d026 — shared sprite multicolors.
- $d027-$d02e — individual sprite colours.

## Sprite pointers
For a selected screen base, sprite pointer bytes occupy the final eight bytes of its 1 KiB screen block. Pointer interpretation is relative to the active VIC bank in 64-byte sprite blocks.

## Timing warning
A register address does not tell you *when* it is safe/useful to write it. Raster, badline, sprite-DMA and border techniques require timing knowledge from the course and target-specific references.
