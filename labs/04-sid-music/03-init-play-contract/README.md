# Lab 04.03 — Init/play contract

## Goal
Learn the interface shape used by many C64 music players without bundling copyrighted tune data.

A tiny local teaching player exposes `music_init` and `music_play`. Init resets phase; each play call advances a simple SID frequency byte.

Replace this teaching stub later with a properly licensed/exported player while preserving the call contract.

**Why does a demo coder care?** Demo code normally integrates music through a small, explicit init/play interface and known memory placement.
