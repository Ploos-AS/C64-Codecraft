# Lab 04.05 — PAL/NTSC playback-rate model

## Goal
Separate “call once per frame” from “play at the tune's intended update rate”.

The starter is a software model: each call advances a frame counter and conditionally advances a music tick according to a small policy byte. It deliberately avoids hard-coding one universal PAL/NTSC conversion recipe.

## Challenge
Using the lesson, document the intended tune rate and target machine before choosing a scheduler policy.

**Why does a demo coder care?** Playback speed is part of the production contract; video standard and tune expectations must be explicit.
