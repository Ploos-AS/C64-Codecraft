# C64 Codecraft

**From Zero to Demo Coder**

C64 Codecraft is a machine-code/assembly course for absolute beginners. It starts with zero assumed 6502/6510 experience and builds, step by step, toward competent C64 demoscene coding. The demoscene is not a late optional module: scene thinking, visual feedback, timing, cycles, bytes and hardware consequences give the entire course its flavour from the first assembly lessons.

## Core principles

- **6510 assembly is the focus.**
- **Hardware first:** understand the 6510, VIC-II, SID, CIA, memory system and timing.
- **Scene credible:** teach techniques, constraints and tools that transfer directly to real C64 demo development.
- **No Codecraft programming framework, runtime or private assembly dialect.**
- **Use real tools directly:** 64tass, ACME, KickAssembler, ca65, VICE and established scene utilities.
- **Cycles matter from the beginning.** Timing, code size, addressing choices and memory layout are introduced as the relevant concepts appear.
- **Markdown is the source of truth.**
- **Editor independent:** VSCodium is recommended, not required.
- **OCI is a reproducible toolbox, not an abstraction layer.**

No prior machine-code, assembly, hexadecimal or CPU-programming experience is required. The course must explain the fundamentals before relying on them. EduCPU may be used as an optional deeper dive into CPU design, but it is never a prerequisite.

## Course direction

The path starts with enough binary, hexadecimal and CPU vocabulary to write real code quickly, then develops through 6510 assembly, C64 memory, VIC-II graphics, raster timing, interrupts, SID integration and increasingly serious demo techniques.

By the advanced material, students should be comfortable reading and writing ordinary C64 assembly projects without depending on Codecraft-specific tooling.

## Toolchain

64tass is the initial canonical teaching assembler. ACME and KickAssembler are first-class scene-oriented alternatives, with ca65 also supported.

VICE/x64sc is the reference emulator for automated qualification. Native VICE monitor commands and workflows are part of the course.

## Reproducibility

The OCI images package known-good versions of command-line tools used by the course and CI. Students are always free to install and invoke those tools natively.

Generated GitHub Pages, PDF and EPUB editions are built from the same Markdown sources.

## Status

M0 — foundation and toolchain qualification in progress.
