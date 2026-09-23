# Lab 04.04 — Frame-scheduled playback

## Goal
Call a play routine once at a deliberate raster position.

This lab uses the familiar polling bridge so scheduling remains visible. It is not presented as the final IRQ architecture.

Invoke repeatedly and inspect that one `music_play` call corresponds to one scheduled update.

**Why does a demo coder care?** A music player consumes recurring CPU time and must coexist with raster effects inside the frame plan.
