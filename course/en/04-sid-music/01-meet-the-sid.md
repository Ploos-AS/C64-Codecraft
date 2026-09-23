---
title: Meet the SID
course: 04-sid-music
lesson: 01
level: intermediate
prerequisites: [03-smooth-scrolling/10-dycp-optimization]
labs: [sid-register-map]
---
# Meet the SID
The C64 SID is a programmable sound chip with three voices plus shared filter and volume/control facilities. Its main register area begins at $D400.

Each voice has registers for frequency, pulse width, waveform/control and ADSR envelope. The voices share filter-related registers.

We begin with the register model, not a music abstraction.

## Scene connection
**Why does a demo coder care about this?**
A demo part must coexist with the music player. Understanding SID state makes player calls, timing, memory placement and visual synchronization much less mysterious.

## Lab
Map the three voice register groups and shared registers. Identify which bytes belong to frequency, pulse width, control and envelope.

## Next
We make one voice produce a controlled tone.
