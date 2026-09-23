# Lab 09.03 — Memory-safe depacking plan

## Goal
Reason about source, destination, depacker and live-demo memory before running a real depacker.

The starter stores a compact region descriptor table. Treat it as a planning artifact: packed input, destination, resident core and scratch space must not collide incorrectly.

## Exercise
Draw the memory map and mark which regions are live during depacking. Then qualify your chosen packer's direction/overlap requirements from its documentation.

**Why does a demo coder care?** A good compression ratio is useless if depacking overwrites the loader, music or the part that is still on screen.
