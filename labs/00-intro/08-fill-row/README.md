# Lab 00.08 — Fill a screen row

Combine a loop with the C64's 40-column text layout. Inspect $0400-$0427 and $d800-$d827, then move the destination to row two without changing loop logic.

**Why does a demo coder care?** Screen geometry becomes address arithmetic; effects need exact ownership of visible bytes.
