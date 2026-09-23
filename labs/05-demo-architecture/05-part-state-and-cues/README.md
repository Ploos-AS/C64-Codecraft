# Lab 05.05 — Part state and cues

## Goal
Drive a part from explicit state and cue data instead of scattering timing decisions through effect code.

A frame counter produces coarse cues. The part consumes the cue and changes its own state; rendering only reads that state.

## Observe
Separate three jobs: time/cue production, state transition, presentation.

## Challenge
Replace the synthetic cue with the music-sync event from Course 04.

**Why does a demo coder care?** Explicit cues let music, effects and transitions coordinate without becoming tightly coupled.
