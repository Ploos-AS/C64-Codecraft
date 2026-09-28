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
- [ ] Run first automated VICE execution/state smoke test (M0.1; CI implementation added, qualification pending green run)
- [x] Add direct ACME example and byte-equivalence CI gate
- [x] Add direct KickAssembler example
- [ ] Qualify pinned/reproducible KickAssembler distribution in OCI/CI
- [x] Define SceneASM as a first-class optional modern scene assembler without making Codecraft depend on it
- [ ] Add SceneASM example/qualification when the assembler interface is stable enough for the course gate
- [ ] Documentation validation
- [ ] GitHub Pages build
- [ ] PDF/EPUB build
- [x] Foundation CI/OCI gates green

## M1 — 6510 Machine Code Foundations

This milestone assumes **no previous machine-code or assembly experience**. Teach binary and hexadecimal, bits/bytes/words, addresses and memory, the CPU execution model, registers, flags and addressing modes before depending on them. Then progress through real 6510 ASM: loads/stores, arithmetic and logic, branches, loops, tables, pointers, subroutines, stack and zero page.

Every topic should have an immediate C64/scene connection. Early examples should manipulate visible hardware where practical; loops lead toward animation, tables toward colour/sine tables, branches toward timing, and zero page toward real performance trade-offs. Introduce cycles, bytes and memory cost from the beginning without requiring students to master raster timing yet.

SceneASM examples may accompany canonical lessons where useful, but the concepts and machine code remain assembler-independent.

## M2 — The C64 as a Machine

Memory map, banking, KERNAL/BASIC interaction, VIC-II, CIA and the practical hardware model a demo coder needs.

## M3 — VIC-II Graphics

Screen/color RAM, character modes, VIC banks, custom character sets, sprites, bitmap, scrolling and graphics memory organization.

## M4 — Interrupts and Timing

IRQ/NMI, raster interrupts, cycle counting, badlines, bus contention, sprite DMA, PAL/NTSC and stable raster. Timing is a continuation of earlier lessons, not a new concept introduced here.

## M5 — SID and Demo Architecture

SID fundamentals, real music init/play routines, IRQ playback, memory placement, synchronization, loaders and multi-part organization.

## M6 — Demo Effects

Raster bars, scrollers, sine effects, sprite multiplexing, FLD and progressively more demanding VIC-II techniques. C64Scene SDK may be introduced here as an optional productivity layer after the underlying techniques have been implemented directly.

## M7 — Advanced Scene Coding

Cycle-exact programming, stable raster techniques, open borders, advanced VIC-II behavior, self-modifying code, undocumented opcodes where appropriate, precalculation, compression and size/speed/memory trade-offs. SceneASM and C64Scene SDK can be used for advanced production workflows while direct hardware understanding remains mandatory.

## M8 — Final Demo

Design, implement, debug, optimize, package and release a complete C64 demo using ordinary scene-compatible tooling and workflows. Students may choose qualified assemblers and may optionally use C64Scene SDK; no Codecraft-specific runtime is required.
