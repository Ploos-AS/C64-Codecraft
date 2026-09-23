# Lab 03.09 — First DYCP data path

## Goal
Combine text-column identity, phase-shifted Y motion and glyph-row selection into one inspectable data path.

For eight columns, the starter stores a generated Y position and one glyph byte into two result buffers. This is intentionally a small renderer precursor rather than a hidden full DYCP engine.

Inspect $c000-$c007 and $c010-$c017 together.

**Why does a demo coder care?** A real DYCP is built from explicit per-column state; understanding that state is more valuable than pasting a finished effect.
