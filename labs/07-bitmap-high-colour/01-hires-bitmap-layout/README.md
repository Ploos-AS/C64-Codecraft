# Lab 07.01 — Hires bitmap layout

## Goal
Understand bitmap memory as bytes before enabling a graphics mode.

The starter writes a small 8×8 teaching tile into the beginning of an 8 KB bitmap region at $2000 and places colour-selection bytes in a separate screen-memory teaching region.

Inspect the bytes first; then use the lesson to map them to pixels and colour sources.

**Why does a demo coder care?** Bitmap effects start with exact memory layout, not an image API.
