# Lab 00.04 — Indexed tables

## Goal
Use X as an index into data rather than embedding every value in code.

## Expected result
The first eight colour-RAM cells receive a palette table.

## Observe
Inspect `palette`, X and $d800-$d807 while stepping.

## Modify
Change table length and make the loop derive its stopping point from a named constant.

## Think like a demo coder
Tables turn expensive/repeated decisions into cheap indexed data access. Later the same idea drives sine motion, colour gradients and precalculation.
