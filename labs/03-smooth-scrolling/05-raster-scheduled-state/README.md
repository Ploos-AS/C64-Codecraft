# Lab 03.05 — Raster-scheduled scroller state

## Goal
Place scroller updates at a chosen raster position without hiding the mechanism in a framework.

This teaching version polls a fresh transition onto TARGET, updates fine-scroll state once, and returns. It is the bridge from manual calls to a later IRQ scheduler.

Do not treat polling as the final demo architecture.

**Why does a demo coder care?** Effect state must advance at a deliberate point in the frame if graphics, music and other effects are to compose cleanly.
