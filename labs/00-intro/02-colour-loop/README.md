# Lab 00.02 — Colour loop

Related lesson: Course 00 lesson 09.

## Goal
Turn a loop into a visible hardware effect while practicing X, indexed addressing and branching.

## Build/run

```sh
make
make run
```

## Expected result
The routine copies a 16-entry colour table into the first 16 cells of colour RAM ($d800...), making the first part of the top text row use the table's colours.

The existing screen characters remain; this lab changes their colour information.

## Observe
Single-step the loop and watch X. Inspect $d800-$d80f before and after execution.

## Modify
Reorder the table. Then extend the exercise to repeat a shorter palette pattern.

## Think like a demo coder
Count how often the loop body executes and identify which work is loop overhead rather than the visible operation.

## CI boundary
Assembly and output bytes can be checked deterministically. The human-facing visual result remains an emulator/hardware observation until runtime-state qualification is added.
