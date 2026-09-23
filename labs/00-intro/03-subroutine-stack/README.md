# Lab 00.03 — Subroutines and stack

## Goal
Use `JSR`/`RTS` deliberately and observe the hardware stack.

Build with `make`, run with `make run`.

## Expected result
The subroutine changes border/background colours and returns through two nested subroutine calls to BASIC.

## Observe
Break at `start`, `set_colours` and `set_background`. Watch SP and inspect $0100-$01ff around each JSR/RTS.

## Modify
Add another subroutine call. Predict stack activity before stepping it.

## Think like a demo coder
Subroutines improve structure, but calls cost bytes/cycles and use stack space. Later raster-critical code may inline selected hot paths.
