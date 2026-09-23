# C64 Codecraft Roadmap

## M0 — Foundation

- [x] Project identity and mission
- [x] Markdown source-of-truth policy
- [x] Editor-independent architecture
- [x] Multi-assembler policy
- [x] VICE reference-emulator policy
- [ ] Qualify OCI base: Alpine first, Debian slim fallback
- [ ] Build minimal and full OCI images
- [ ] Implement c64cc skeleton
- [ ] Assemble first 64tass example
- [ ] Run first automated VICE smoke test
- [ ] Documentation validation
- [ ] GitHub Pages build
- [ ] PDF/EPUB build
- [ ] CI green

## M1 — Machine Code Foundations

Binary/hex, C64 memory map, 6510 registers and flags, addressing modes, loads/stores, arithmetic, branches, loops, subroutines, stack and zero page.

## M2 — VIC-II Foundations

Screen/color RAM, character modes, VIC banks, custom character sets, sprites, bitmap and scrolling.

## M3 — Interrupts and Timing

IRQ/NMI, raster interrupts, cycle counting, badlines, sprite DMA, PAL/NTSC and stable raster foundations.

## M4 — SID and Demo Architecture

SID fundamentals, music init/play, IRQ playback, memory layout, synchronization and multi-part architecture.

## M5 — Demo Effects

Raster bars, scrollers, multiplexers, sine tables, FLD and progressively more timing-sensitive effects.

## M6 — Advanced Demo Coding

Cycle-exact programming, open borders, advanced VIC-II techniques, self-modifying code, undocumented opcodes where appropriate, compression and size/speed optimization.

## M7 — Final Demo

Design, implement, debug, optimize, package and release a complete C64 demo.
