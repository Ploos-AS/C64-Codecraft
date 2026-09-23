# Toolchain policy

## Assemblers

C64 Codecraft deliberately supports multiple real assemblers.

### Canonical beginner path

**64tass** is the initial canonical syntax used to introduce 6510 assembly.

### Scene paths

**ACME** and **KickAssembler** are first-class targets so students encounter tooling and source styles found in real C64 development and demoscene work.

### Additional path

**ca65** is supported for the cc65 ecosystem and broader 6502-family development.

Lessons distinguish CPU/hardware concepts from assembler-specific syntax. Codecraft will not define its own assembly language or macro framework.

## Emulator and debugger

VICE/x64sc is the reference emulator for course qualification. The VICE monitor itself is a tool students should learn, not merely a backend hidden by scripts.

Advanced visual debugging tools may supplement VICE where useful.

## Editors

The course is editor-independent.

- VSCodium: recommended
- VS Code: supported
- Vim/Neovim/Emacs/other editors: supported through ordinary files and CLI tools

No lesson may require an editor extension.

## Scene tools

Established music, graphics, packing, disk-image and conversion tools should be used where appropriate. The course should teach transferable workflows rather than replacing mature scene tools with Codecraft equivalents.

## Project automation

Small repository scripts are allowed for CI, publishing and deterministic tests. They are not part of a Codecraft programming platform and should not replace direct assembler/emulator commands in the curriculum.
