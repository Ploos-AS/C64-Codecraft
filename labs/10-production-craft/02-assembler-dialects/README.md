# Lab 10.02 — Assembler dialect literacy

## Goal
Separate 6510 knowledge from assembler-specific syntax.

This reference implementation is 64tass. Port the same tiny program to ACME and, where available, KickAssembler or ca65 without changing its observable C64 behaviour.

Record differences in:
- origin/directives,
- byte/word data,
- local labels,
- expressions,
- binary inclusion,
- symbol/debug output.

Do not invent a Codecraft assembly dialect or compatibility layer.

**Why does a demo coder care?** Scene sources use several real assemblers; reading and porting them is more valuable than dependence on one course abstraction.
