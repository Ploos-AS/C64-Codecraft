# Appendix H — 6510 quick reference

This appendix is a lookup companion, not a substitute for the beginner lessons.

## Registers
- **A** — accumulator; arithmetic, logic and many loads/stores.
- **X, Y** — index registers; counters, indexing and selected transfers.
- **SP** — 8-bit stack pointer; stack lives in page $01.
- **P** — processor status flags.
- **PC** — program counter.

## Status flags
`N V - B D I Z C`

Understand which instructions read/change each flag before relying on a compact sequence.

## Stack
The hardware stack occupies $0100-$01ff and grows downward through the 8-bit stack pointer. JSR/RTS, interrupts and explicit push/pull instructions all affect stack planning.

## Decimal mode
The NMOS 6510 supports decimal-mode arithmetic. C64 code that assumes binary arithmetic should keep the relevant processor-state assumptions explicit.

## Optimization rule
Instruction choice is not only about source length. Compare bytes, cycles, addressing mode, flags and path determinism.

For exact opcode/cycle tables, keep a source-verified machine-readable/reference table in the project rather than duplicating unchecked numbers across lessons.
