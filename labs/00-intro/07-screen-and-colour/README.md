# Lab 00.07 — Screen RAM and colour RAM

## Goal
See that character selection and character colour are separate data paths.

## Expected result
The first 16 screen cells display screen codes 1..16 while their colours follow a second table.

## Observe
Compare $0400-$040f with $d800-$d80f.

## Modify
Change only the colour table, then only the screen-code table.

## Think like a demo coder
Separating representation from presentation is fundamental to scrollers, char effects and generated screens.
