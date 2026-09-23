# Lab 03.07 — DYCP column concept

## Goal
Model DYCP as independent vertical positions for successive character columns.

Eight phase-shifted lookup results are stored as column Y offsets. No renderer is hidden behind the exercise: first understand the data model.

Inspect $c000-$c007 and sketch where eight columns would appear vertically.

**Why does a demo coder care?** DYCP becomes manageable when motion generation and glyph rendering are separate problems.
