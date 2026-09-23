---
title: Les ekte assembler dialects
course: 10-production-craft
lesson: 02
level: advanced
prerequisites: [01-project-layout]
labs: [10.02-assembler-dialects]
---
# Les ekte assembler dialects
6510 instruction set er maskinen; assembler syntax er tool-interface.

Codecrafts første eksempler bruker 64tass, men scene-source kan bruke ACME, KickAssembler eller andre assemblers. Forskjeller kan ligge i directives, expressions, local labels, macros, namespaces, imports, binary inclusion og output configuration.

Lær å oversette concepts, ikke punctuation.

## Ingen kunstig Codecraft-dialect
Vi normaliserer ikke assemblers bak et Codecraft-language. Når du leser et annet prosjekt brukes prosjektets native build og conventions.

## Lab
Uttrykk én liten routine/data-block i 64tass- og ACME-syntax og inspiser deretter en dokumentert KickAssembler-equivalent uten å endre underliggende 6510-logic.

## Neste
Vi bruker symbols og emulator-debugger som normale development tools.
