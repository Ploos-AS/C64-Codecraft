---
title: Feed the scroller a text stream
course: 03-smooth-scrolling
lesson: 03
level: intermediate
prerequisites: [02-fine-plus-coarse]
labs: [scroll-text-stream]
---
# Feed the scroller a text stream
A scroller needs state beyond the visible row: a pointer or index into message data.

```asm
message:
    .text "C64 CODECRAFT   "
    .byte 0
```

On each coarse update, fetch the next message value, translate it if your source encoding requires it, write the resulting screen code at the incoming edge, and advance the stream position.

A terminator can restart the message, switch messages or trigger another action.

## Keep representations explicit
Source text, PETSCII and screen codes are related but not identical representations. Do not hide conversions behind unexplained constants.

## Scene connection
**Why does a demo coder care about this?**
A scroller is both an effect and a data pipeline. Scene productions often embed greetings, credits and synchronization commands in that stream.

## Lab
Scroll a terminated message continuously. Add one documented control value that changes a harmless effect parameter instead of displaying a character.

## Next
We keep colour moving with the characters.
