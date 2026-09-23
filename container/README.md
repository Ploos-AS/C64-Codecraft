# OCI environment

C64 Codecraft uses OCI images as reproducible reference environments.

## Planned images

- `c64-codecraft`: minimal build/test/CI image
- `c64-codecraft-full`: extended scene toolbox

## Base image policy

Alpine is qualified first. Debian slim is the fallback if compatibility or maintenance costs make Alpine unsuitable.

## Initial tool candidates

- 64tass
- ACME
- KickAssembler + Java runtime
- ca65
- VICE/x64sc
- Exomizer
- disk/image utilities
- Python and build tooling
- documentation validation tooling

GUI-first scene applications are not required to live inside the OCI image.
