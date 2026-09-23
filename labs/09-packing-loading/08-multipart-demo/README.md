# Lab 09.08 — Multipart demo state machine

## Goal
Model a complete multipart production as explicit resident state.

The teaching core moves through LOAD → INIT → RUN → EXIT for two parts. Loading is simulated so the architecture stays inspectable and independent of one loader implementation.

## Challenge
Replace only the simulated load step with your qualified loader while keeping the part interface unchanged.

**Why does a demo coder care?** A resident core should coordinate parts without forcing every effect to know loader internals.
