# Lab 03.03 — Text stream

## Goal
Feed new screen codes from a persistent message stream when coarse scrolling needs a new rightmost character.

The lab isolates stream state from scroll state. Repeated calls insert successive screen codes at $0427 and wrap at the explicit terminator.

## Observe
Watch `text_index` and the rightmost screen cell.

**Why does a demo coder care?** A scroller is not just movement; it is a consumer of a data stream with explicit lifetime and wrap rules.
