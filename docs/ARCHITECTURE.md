# Architecture

## Principle

C64 Codecraft is a course, executable lab collection and reproducible toolbox. It is deliberately **not** a C64 programming framework.

```text
Markdown + ordinary ASM source
       |
       +--> real assemblers
       +--> VICE qualification
       +--> GitHub Pages
       +--> PDF / EPUB
```

## Student workflow

Lessons show native tool invocation. For example:

```sh
64tass --cbm-prg -o build/example.prg example.asm
x64sc -autostart build/example.prg
```

Equivalent ACME/KickAssembler workflows are introduced as appropriate.

There is no required Codecraft runtime, API, assembler dialect or build wrapper between the student and the machine.

## Host

Any reasonable editor may be used. VSCodium is recommended.

VICE, Retro Debugger, music editors, graphics editors and other scene tools may run natively.

## OCI toolbox

The OCI environment provides reproducible versions of command-line tools used by lessons and CI.

Two images are planned:

- c64-codecraft — minimal course/build/test toolbox
- c64-codecraft-full — broader scene-development toolbox

The images package existing tools; they do not define a new development platform.

Alpine is qualified first. Debian slim is the documented fallback when musl/upstream/tool compatibility would make Alpine fragile or disproportionately difficult to maintain.

## Internal automation

Repository scripts may perform documentation builds, CI qualification, emulator automation and repetitive checks. Such scripts are infrastructure. Course material should expose the native assembler and emulator operations being tested.

## Qualification

A lesson is not qualified merely because its Markdown renders. Where practical, CI assembles the same ordinary ASM source shown to students and executes deterministic tests through VICE.
