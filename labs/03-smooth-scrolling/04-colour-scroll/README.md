# Lab 03.04 — Colour scrolling

## Goal
Move colour RAM together with screen RAM.

The top row shifts both character codes and colours left, then inserts one new character/colour pair.

Inspect $0400-$0427 beside $d800-$d827.

**Why does a demo coder care?** Visual state often lives in parallel memory streams. Updating only one creates artifacts.
