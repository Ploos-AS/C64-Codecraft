# Lab 05.04 — IRQ chain model

## Goal
Understand an IRQ chain as an ordered schedule before implementing a hardware takeover.

A software dispatcher walks three event records containing raster-line metadata and handler addresses. The starter invokes the handlers directly so ordering/state can be inspected safely.

## Challenge
Using Course 02, design how each event would program the next raster compare and acknowledge the VIC-II source.

**Why does a demo coder care?** Complex parts are often a sequence of timed jobs, not one giant interrupt handler.
