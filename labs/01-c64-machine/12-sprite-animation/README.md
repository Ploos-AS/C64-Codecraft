# Lab 01.12 — Sprite animation frames

## Goal
Animate by changing the sprite pointer rather than copying an entire sprite every frame.

Three 64-byte blocks at $2000/$2040/$2080 correspond to pointers $80/$81/$82. Each invocation advances $07f8.

Inspect the pointer while invoking the routine repeatedly.

**Why does a demo coder care?** Pointer animation is cheap and deterministic, and later composes naturally with raster scheduling and multiplexing.
