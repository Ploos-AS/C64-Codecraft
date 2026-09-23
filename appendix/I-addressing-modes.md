# Appendix I — Addressing modes

Addressing mode answers: **where does this instruction get its operand?**

Common 6510 forms include:
- implied/accumulator;
- immediate;
- zero page;
- zero page indexed;
- absolute;
- absolute indexed;
- relative branches;
- indexed indirect `(zp,X)`;
- indirect indexed `(zp),Y`;
- indirect `JMP`.

## Scene relevance
Addressing mode changes code size, cycle cost, available operations and sometimes timing variation. Zero-page and indirect modes are especially important for pointers and hot paths.

## Page crossings
Selected indexed reads can gain a cycle when their effective address crosses a page. Taken branches also have path-dependent timing, including an additional page-cross case.

Do not turn that into folklore: inspect the exact instruction/path being optimized.

## Rule
Choose the mode that expresses the data flow first. Optimize placement/mode only after the path is understood and measured.
