---
title: Phase-shifted sine motion
course: 03-smooth-scrolling
lesson: 06
level: intermediate
prerequisites: [05-raster-scheduled-scroller]
labs: [phase-shifted-sine]
---
# Phase-shifted sine motion
One sine lookup moves one object periodically. Several lookups with different phase offsets create a wave.

```text
y0 = sine[phase + 0]
y1 = sine[phase + step]
y2 = sine[phase + 2*step]
...
```

On the 6510 we normally arrange tables and indices so runtime work is cheap. A duplicated or suitably sized table can sometimes remove wrap checks from a critical path; that spends memory to save cycles.

## Scene connection
**Why does a demo coder care about this?**
Phase offsets turn one small table into coordinated motion across many elements. This idea appears in sprite formations, logos, plasma-like indexing and scrollers.

## Lab
Use one sine table to drive several sprite Y positions with different phases. Compare a runtime wrap check with a table layout that avoids it.

## Next
We apply the same phase idea to characters rather than sprites.
