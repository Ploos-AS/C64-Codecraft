# Lab 01.11 — Multicolor sprite setup

## Goal
Configure sprite 0 multicolor state explicitly.

The lab enables sprite 0 multicolor through $D01C, sets shared colours at $D025/$D026 and its individual colour at $D027.

Relate the two-bit pixel groups from Course 01 to their colour sources. Change only the shared colours and observe which pixels change.

**Why does a demo coder care?** Sprite pixel data and shared/per-sprite colour state must be designed together.
