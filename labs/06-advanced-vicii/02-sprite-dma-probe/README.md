# Lab 06.02 — Sprite DMA observation

## Goal
Observe sprite activity as a VIC-II bus-time consumer rather than memorizing a magic timing penalty.

The program enables sprite 0 with known data and brackets a small CPU work block with border colours. Compare traces with the sprite enabled and disabled in VICE.

Record video standard/chip model and raster position when making timing observations.

**Why does a demo coder care?** Sprite reuse and cycle-critical effects must budget for VIC-II memory fetches.
