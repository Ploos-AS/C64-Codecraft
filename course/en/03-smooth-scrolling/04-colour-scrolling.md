---
title: Colour in the scroller
course: 03-smooth-scrolling
lesson: 04
level: intermediate
prerequisites: [03-text-stream]
labs: [03.04-colour-scroll]
---
# Colour in the scroller
Screen RAM and colour RAM are separate. If the visual design expects colour to move with character cells, the effect must update both representations deliberately.

Possible designs include:

- shift colour RAM alongside screen codes;
- assign a fixed colour to each incoming character;
- use a repeating colour table;
- derive colour from scroller phase;
- change global/background colours instead of per-cell colour.

Each has a different CPU and memory cost.

## Scene connection
**Why does a demo coder care about this?**
The cheapest representation that produces the intended look is often the best one. Moving 40 colour values every coarse step may be unnecessary if a table or global register can create the same impression.

## Lab
Implement two colour strategies and compare their cycle cost with the border timing probe.

## Next
We schedule the scroller inside a raster region rather than letting it run whenever the main loop reaches it.
