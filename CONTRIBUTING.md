# Contributing

## Source of truth

Markdown and source files committed to this repository are authoritative.

**Generated HTML, GitHub Pages output, PDF and EPUB files must never be edited manually.**

## Course principles

1. Assembly is the focus.
2. Teach the C64 hardware, not a framework.
3. Use real scene tools and ordinary assembler source.
4. Do not introduce a Codecraft-specific runtime, assembly dialect or required programming API.
5. Teach cycles, bytes, memory layout and hardware consequences alongside the concepts that cause them.
6. Keep the command-line workflow canonical and editor-independent.
7. VSCodium is recommended; VS Code and other editors are welcome.
8. Examples shown in lessons should be buildable and testable.
9. Prefer deterministic qualification without hiding the native workflow from students.
10. Keep Norwegian and English tracks structurally aligned.

## Scene credibility

Course material should remain useful after the student leaves the course. A student should be able to open a normal C64 assembly project, recognize its tools and techniques, and continue without a Codecraft dependency.

Advanced material must not artificially avoid difficult subjects merely to keep examples simple. Timing, badlines, DMA, raster stability, memory constraints, self-modifying code, compression and undocumented opcodes should be taught when technically relevant and with appropriate context.

## Tooling

64tass is the initial canonical assembler. ACME and KickAssembler are first-class scene-oriented alternatives; ca65 is also supported.

VICE/x64sc is the reference emulator for automated qualification, and the native VICE monitor is a course tool in its own right.

Project scripts may automate CI, documentation and repetitive qualification. They must not become a student-facing programming framework.

## Generated content

Do not commit generated site/book output unless a release process explicitly requires it.
