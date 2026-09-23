---
title: Read real assembler dialects
course: 10-production-craft
lesson: 02
level: advanced
prerequisites: [01-project-layout]
labs: [assembler-dialects]
---
# Read real assembler dialects
The 6510 instruction set is the machine; assembler syntax is a tool interface.

Codecraft's initial examples use 64tass, but scene source may use ACME, KickAssembler or other assemblers. Differences can include directives, expressions, local labels, macros, namespaces, imports, binary inclusion and output configuration.

Learn to translate concepts, not punctuation.

## No artificial Codecraft dialect
We do not normalize all assemblers behind a Codecraft language. When reading another project, use that project's native build and conventions.

## Lab
Express one small routine/data block in 64tass and ACME syntax, then inspect a documented KickAssembler equivalent without changing the underlying 6510 logic.

## Next
We use symbols and the emulator debugger as normal development tools.
