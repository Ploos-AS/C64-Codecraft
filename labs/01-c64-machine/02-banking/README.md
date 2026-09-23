# Lab 01.02 — Banking experiment

## Goal
Observe the 6510 processor port used in C64 memory configuration without blindly changing machine state.

The starter program records $00/$01 into RAM and returns. Use the monitor to inspect the values and relate them to the banking lesson.

## Challenge
Only after reading the lesson, design a controlled experiment that changes mapping, accesses the intended RAM/ROM/I/O view, and restores the original port state.

**Why does a demo coder care?** Demo memory often uses RAM that can be hidden by ROM/I/O. Banking changes must be intentional and reversible.
