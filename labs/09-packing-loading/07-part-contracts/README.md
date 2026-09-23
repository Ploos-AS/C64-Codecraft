# Lab 09.07 — Multipart part contracts

## Goal
Make every demo part declare what it requires and what it leaves behind.

The starter stores a compact teaching descriptor for two parts. In a real production, keep the human-readable contract in source/docs and derive machine metadata only when useful.

## Contract fields
Document for each part:
- load and execution address,
- entry point,
- owned RAM and zero page,
- VIC/SID/CIA/IRQ state expected on entry,
- music ownership,
- loader/resident-core requirements,
- exit condition,
- state guaranteed on exit.

**Why does a demo coder care?** Multipart demos become manageable when transitions are interfaces rather than undocumented accidents.
