# Toolchain policy

## Assemblers

C64 Codecraft deliberately supports multiple assemblers.

### Canonical beginner path

**64tass** is the initial canonical syntax used to introduce 6510 assembly.

### Scene paths

**ACME** and **KickAssembler** are first-class targets because students should encounter tooling used in real C64 development and demo workflows.

### Additional path

**ca65** is supported for students interested in the cc65 ecosystem and more general 6502-family development.

Lessons should distinguish CPU concepts from assembler-specific syntax.

## Emulator

VICE/x64sc is the reference emulator for automated course qualification.

The project will use VICE monitor automation for deterministic tests where practical.

## Editors

The course is editor-independent.

- VSCodium: recommended
- VS Code: supported
- Vim/Neovim/Emacs/other editors: usable through the CLI workflow

No lesson may require an editor extension to build the canonical exercise.

## GUI scene tools

Real scene tools should be introduced where they improve the workflow. GUI-only applications may remain host-installed rather than being forced into the OCI environment.

## Codecraft tooling

c64cc provides a stable teaching interface while preserving access to native commands. It must not become a private assembler, emulator or opaque build system.
