---
title: The C64 as a Machine
course: 01-c64-machine
lesson: overview
level: beginner
prerequisites: [00-intro]
labs: []
---

# The C64 as a Machine

You can now write small 6510 routines. This block builds the mental model needed to understand where code, RAM, ROM and hardware live.

We will cover the 64 KiB CPU address space, RAM/ROM/I/O visibility, the 6510 port at $00/$01, the VIC-II register area and the CIA chips.

The scene goal is practical: stop treating addresses as magic constants and start reasoning about the machine's configuration.
