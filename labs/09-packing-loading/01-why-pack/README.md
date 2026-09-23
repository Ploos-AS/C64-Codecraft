# Lab 09.01 — Packing tradeoff baseline

## Goal
Measure what you would actually gain before adding a packer.

The lab builds a deliberately repetitive payload and records its unpacked address/size contract. Compare the PRG/payload size with a qualified external packer later.

Packing is not automatically useful: account for depacker bytes, depack time, temporary memory and loader constraints.

**Why does a demo coder care?** Disk/memory savings only matter when the total production cost is understood.
