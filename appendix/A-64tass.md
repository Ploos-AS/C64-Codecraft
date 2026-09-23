# Appendix A — 64tass

64tass is the initial reference assembler used by C64 Codecraft. It is a tool, not a Codecraft language.

## Core workflow

Typical course builds expose the real assembler invocation rather than hiding it behind a framework:

```sh
64tass --cbm-prg -o build/example.prg main.asm
```

Use the project's Makefile/build recipe when supplied, but learn to recognize the underlying command.

## What to learn
Be comfortable with source origins, labels, constants, data directives, binary inclusion, expressions, output selection and symbol/listing output used by the current project.

When a lesson needs assembler-specific syntax, it should identify it explicitly.

## Debugging
Generate useful labels/symbol information when the selected workflow supports it and carry those names into emulator debugging.

## Portability
Do not assume a 64tass directive is part of 6510 assembly itself. When reading ACME/KickAssembler source, translate the build-time concept while keeping the machine instructions separate.
