# C64 Codecraft

**From Zero to Demo Coder**

C64 Codecraft is an assembly-first course for learning the Commodore 64 from the hardware up and progressing toward competent demoscene coding.

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

No prior machine-code experience is required. Fundamental concepts are introduced briefly and practically; deeper CPU-computer fundamentals belong in projects such as EduCPU rather than being duplicated here.

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
