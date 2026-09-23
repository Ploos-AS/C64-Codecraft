# Contributing

## Source of truth

Markdown and source files committed to this repository are authoritative.

**Generated HTML, GitHub Pages output, PDF and EPUB files must never be edited manually.**

The publishing pipeline must be reproducible from repository sources.

## Course principles

1. Teach the machine, not a framework.
2. Use real scene tools.
3. Keep the command-line workflow canonical and editor-independent.
4. VSCodium is the recommended editor; VS Code and other editors are welcome.
5. Examples shown in lessons should be buildable and testable.
6. Prefer deterministic labs and automated validation.
7. Introduce abstraction only after the student understands what it abstracts.
8. Keep Norwegian and English tracks structurally aligned.

## Tooling

64tass is the initial canonical assembler. ACME, KickAssembler and ca65 are first-class supported targets as the course matures.

VICE/x64sc is the reference emulator for automated qualification.

The c64cc CLI may simplify workflows, but advanced lessons must expose the underlying assembler/emulator commands.

## Generated content

Do not commit generated site/book output unless a release process explicitly requires it.
