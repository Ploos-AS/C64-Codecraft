# Appendix B — ACME

ACME is a first-class scene-relevant assembler in Codecraft.

The course does not require students to rewrite every lesson in ACME. The goal is dialect literacy: recognize the same 6510 program beneath different directives, expression syntax, labels and data/import mechanisms.

## Workflow
Use ACME directly or through the production's transparent build recipe. Record the exact target/output options used by a lab rather than relying on editor magic.

## Comparison exercise
Take a small 64tass program and identify:
- origin/output setup;
- constants;
- local/global labels;
- byte/word data;
- binary inclusion;
- macros, if used.

Then express the same machine-level intent using ACME conventions.

## Rule
A production that uses ACME should look like an ACME project—not like ACME forced through a Codecraft abstraction layer.
