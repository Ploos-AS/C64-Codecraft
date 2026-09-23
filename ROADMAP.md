# C64 Codecraft Roadmap

## M0 — Foundation

- [x] Project identity and mission
- [x] Markdown source-of-truth policy
- [x] Editor-independent architecture
- [x] ASM-first / hardware-first / scene-credible policy
- [x] Explicit no-framework/no-private-dialect policy
- [x] Multi-assembler policy
- [x] VICE reference-emulator policy
- [x] Qualify OCI base: Alpine first, Debian slim fallback
- [x] Build minimal and full OCI toolboxes
- [x] Assemble first 64tass example
- [ ] Run first automated VICE execution/state smoke test (M0.1; packaged VICE interface still to qualify)
- [ ] Add direct ACME and KickAssembler examples/qualification
- [ ] Documentation validation
- [ ] GitHub Pages build
- [ ] PDF/EPUB build
- [x] Foundation CI/OCI gates green

## M1 — 6510 Machine Code Foundations

Only the fundamentals needed to become productive are repeated here: binary/hex, registers, flags and addressing. Move quickly into real 6510 ASM, loads/stores, arithmetic, branches, loops, subroutines, stack and zero page. Introduce cycles, bytes and trade-offs from the start.

## M2 — The C64 as a Machine

Memory map, banking, KERNAL/BASIC interaction, VIC-II, CIA and the practical hardware model a demo coder needs.

## M3 — VIC-II Graphics

Screen/color RAM, character modes, VIC banks, custom character sets, sprites, bitmap, scrolling and graphics memory organization.

## M4 — Interrupts and Timing

IRQ/NMI, raster interrupts, cycle counting, badlines, bus contention, sprite DMA, PAL/NTSC and stable raster. Timing is a continuation of earlier lessons, not a new concept introduced here.

## M5 — SID and Demo Architecture

SID fundamentals, real music init/play routines, IRQ playback, memory placement, synchronization, loaders and multi-part organization.

## M6 — Demo Effects

Raster bars, scrollers, sine effects, sprite multiplexing, FLD and progressively more demanding VIC-II techniques.

## M7 — Advanced Scene Coding

Cycle-exact programming, stable raster techniques, open borders, advanced VIC-II behavior, self-modifying code, undocumented opcodes where appropriate, precalculation, compression and size/speed/memory trade-offs.

## M8 — Final Demo

Design, implement, debug, optimize, package and release a complete C64 demo using ordinary scene-compatible tooling and workflows.
