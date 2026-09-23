---
title: Organize a real production
course: 10-production-craft
lesson: 01
level: advanced
prerequisites: [09-packing-loading/09-release-d64]
labs: [production-layout]
---
# Organize a real production
A larger demo needs a source tree that makes ownership visible.

Separate authored source, generated data, third-party inputs, build scripts, tools/configuration, documentation and release output. Keep generated artifacts reproducible rather than hand-edited.

Part boundaries should remain understandable from the tree instead of being hidden behind a custom framework.

## Scene connection
**Why does a demo coder care about this?**
A production may be tuned for months. Clear structure makes aggressive low-level code easier to change without losing track of assets, generated tables or part contracts.

## Lab
Refactor the teaching multipart demo into an explicit production tree and rebuild it from clean checkout.

## Next
We learn to read more than one real assembler dialect.
