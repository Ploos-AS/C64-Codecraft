---
title: The DYCP idea
course: 03-smooth-scrolling
lesson: 07
level: intermediate
prerequisites: [06-phase-shifted-sine]
labs: [dycp-paper-design]
---
# The DYCP idea
**DYCP** means *Different Y Character Positions*. Instead of every character in a scroller sharing one vertical baseline, individual characters appear at different Y positions, often following a wave.

A normal character screen is cell-based, so arbitrary per-character vertical pixel placement is not a free operation. A DYCP therefore needs a representation and update strategy that creates the illusion or reconstructed character image at the desired offsets.

There are several historical implementation families. Codecraft will build one understandable version first, then compare alternatives rather than claiming a single canonical algorithm.

## Design before code
For each visible character ask:

- which source glyph is needed?
- what vertical offset does its phase request?
- which destination character data must be generated or selected?
- how much work happens per frame?
- what can be precalculated?

## Scene connection
**Why does a demo coder care about this?**
DYCP is a classic step from "scroll some text" to manipulating character graphics as effect data under a strict frame budget.

## Lab
Design an eight-character wave on paper. For each character, record glyph, phase, desired vertical offset and required output rows.

## Next
We construct shifted character data from source glyphs.
