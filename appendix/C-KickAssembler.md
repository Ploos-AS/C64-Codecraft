# Appendix C — KickAssembler

KickAssembler is important for reading and working with modern C64 scene source.

It is Java-based and has a rich assembler-time language. That power is useful, but students must keep assembler-time computation distinct from code executed by the 6510.

## Topics
Learn enough to recognize:
- program counter/segment placement;
- labels and constants;
- imports/binary data;
- macros;
- namespaces/scopes;
- assembler-time loops/functions/data generation;
- symbol/debug output used by a project.

## Reproducibility
Pin/document the version required by a production. Do not assume Codecraft may redistribute a tool until its license/redistribution terms have been qualified for the reference environment.

## Rule
Use KickAssembler's native strengths when a project chooses it. Do not invent a compatibility dialect merely to make it resemble 64tass.
