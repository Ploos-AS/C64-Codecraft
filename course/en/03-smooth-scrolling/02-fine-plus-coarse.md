---
title: Fine plus coarse scrolling
course: 03-smooth-scrolling
lesson: 02
level: intermediate
prerequisites: [01-d016-fine-x-scroll]
labs: [fine-coarse-scroll]
---
# Fine plus coarse scrolling
A continuous character scroller has two rhythms.

Every frame, adjust the $D016 fine-scroll phase. When that phase crosses the character boundary, shift the screen row by one character and insert new data at the edge.

Conceptually:

```text
frame: change fine phase
frame: change fine phase
...
boundary:
    shift screen codes by one cell
    insert next character
    wrap/reset fine phase
```

The exact direction and phase sequence must match how VIC-II interprets the scroll field.

## Budget the coarse step
Most frames are cheap. The coarse-update frame is more expensive because it copies many screen bytes. This creates a periodic timing spike that must fit the frame plan.

## Scene connection
**Why does a demo coder care about this?**
Smoothness often comes from combining a cheap hardware operation with less frequent memory work. This pattern appears throughout C64 effects.

## Lab
Combine a one-row coarse shift with $D016 fine scrolling and mark the coarse-update frame with a border timing probe.

## Next
We replace fixed incoming characters with a proper text stream.
