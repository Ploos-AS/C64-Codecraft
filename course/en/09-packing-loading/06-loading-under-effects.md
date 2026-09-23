---
title: Loading while the demo continues
course: 09-packing-loading
lesson: 06
level: advanced
prerequisites: [05-loader-basics]
labs: [09.06-loading-under-effects]
---
# Loading while the demo continues
A seamless transition may require music or a visual effect to remain alive while data for the next part is loaded.

That creates competing requirements for CPU time, interrupts, I/O, memory buffers and sometimes drive communication timing.

Do not begin by writing a fastloader. First define what must remain alive and how much interruption is acceptable. Then measure the ordinary loader path and identify the actual bottleneck.

## Resident core
A multipart production often benefits from a deliberately small resident region containing only the state/code that truly must survive between parts. Its ownership must be documented.

## Scene connection
**Why does a demo coder care about this?**
Perceived continuity is part of presentation. Loader engineering can be as important to flow as the effects themselves.

## Lab
Keep one simple frame-driven visual or music test alive around a controlled loading experiment. Document what the chosen loading method can and cannot preserve.

## Next
We define contracts between independently built demo parts.
