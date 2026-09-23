# Appendix N — PETSCII, screen codes and text data

C64 text has several representations that beginners often accidentally mix.

## Keep these distinct
- **source text** — characters in the host-side assembly/source file;
- **PETSCII** — Commodore character encoding used by KERNAL/text-oriented interfaces and data;
- **screen codes** — values placed in screen RAM to select displayed character cells;
- **charset bitmap data** — the pixel rows defining the glyph itself.

A byte that means a printable character in one context is not automatically the byte you should store directly into screen RAM.

## Scene relevance
Scrollers frequently preprocess message text into the representation the runtime routine wants. That conversion can happen at assembly/build time instead of wasting frame time.

## Rule
Every text pipeline should state its input encoding and runtime representation. Avoid unexplained assembler string conversions.
