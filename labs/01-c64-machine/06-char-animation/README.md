# Lab 01.06 — Character animation data

## Goal
Treat animation as selecting frames from prepared character data.

Each invocation copies one of four 8-byte frames to $c800 and advances the frame index. Use repeated SYS calls or the monitor to inspect the changing bytes.

This is deliberately **not** a busy-loop animation. Frame/raster scheduling comes later.

**Why does a demo coder care?** Animation is data plus controlled scheduling; separating those concerns makes later effects predictable.
