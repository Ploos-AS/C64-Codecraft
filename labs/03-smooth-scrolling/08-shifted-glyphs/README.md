# Lab 03.08 — Shifted glyph variants

## Goal
See how pre-shifted glyph data trades memory for cheaper runtime rendering.

A simple 8-row glyph is accompanied by one pre-shifted variant. The program copies both into RAM for direct byte/bit comparison.

## Challenge
Create the remaining horizontal shift variants offline or in source data and calculate the memory cost.

**Why does a demo coder care?** Precomputation is a central scene tradeoff: spend bytes before runtime to save cycles during the effect.
