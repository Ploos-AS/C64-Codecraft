# Architecture

## Principle

C64 Codecraft is a versioned teaching work consisting of course text, executable examples, labs and reproducible tooling.

```text
Markdown + source
       |
       +--> validation / executable labs
       +--> GitHub Pages
       +--> PDF
       +--> EPUB
```

## Development layers

### Host

Any reasonable editor may be used. VSCodium is recommended.

GUI tools such as VICE, Retro Debugger, music editors and graphics editors may run natively.

### OCI

The OCI environment provides the reproducible CLI toolchain used by lessons and CI.

Two images are planned:

- c64-codecraft — minimal course/build/test environment
- c64-codecraft-full — broader scene-development toolbox

Alpine is qualified first. Debian slim is the documented fallback when musl/upstream/tool compatibility would make Alpine fragile or disproportionately difficult to maintain.

### c64cc

c64cc is orchestration, not a proprietary development environment.

Planned interface:

```sh
c64cc doctor
c64cc build <project>
c64cc build <project> --assembler 64tass
c64cc build <project> --assembler acme
c64cc build <project> --assembler kick
c64cc run <project>
c64cc debug <project>
c64cc test <project>
```

The student is progressively shown the native commands behind these operations.

## Qualification

A lesson is not considered qualified merely because its Markdown renders. Where applicable, CI should assemble the code and execute deterministic tests through VICE.
