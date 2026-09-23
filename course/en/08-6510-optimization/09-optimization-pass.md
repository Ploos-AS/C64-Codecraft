---
title: A complete optimization pass
course: 08-6510-optimization
lesson: 09
level: advanced
prerequisites: [08-size-vs-speed]
labs: [08.09-optimization-pass]
---
# A complete optimization pass
Return to a real effect from the mini-demo or advanced VIC-II work.

Run the full process:
1. define the production constraint;
2. capture baseline cycles/bytes and worst path;
3. identify the bottleneck;
4. propose one change;
5. measure again;
6. keep or revert;
7. repeat until the constraint is satisfied or another resource becomes limiting.

Keep a small optimization log. Failed ideas are useful evidence too.

## Qualification
After optimization, rerun functional and timing tests. Faster code that changes flags, memory ownership, IRQ latency or visible output can introduce subtle regressions.

## Checkpoint
You can optimize 6510 code from evidence, explain the cost of each technique and distinguish scene knowledge from cargo-cult tricks.

## Next
The next block covers packing, loading and multipart demo construction: compression, depacking, disk layout, loaders and transitions between independently built parts.
