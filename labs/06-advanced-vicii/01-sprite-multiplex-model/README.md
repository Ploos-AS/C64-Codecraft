# Lab 06.01 — Sprite multiplex model

## Goal
Model sprite multiplexing as reuse of a limited hardware object at later raster positions.

Two logical objects share sprite 0. The teaching code applies the first object's state, waits for a later raster line, then applies the second object's state.

This is a scheduling model, not yet a production multiplexer.

**Why does a demo coder care?** Multiplexing is resource reuse under timing constraints: logical sprites outnumber physical VIC-II sprites.
