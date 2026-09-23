---
title: $D016 fine X scrolling
course: 03-smooth-scrolling
lesson: 01
level: intermediate
prerequisites: [02-raster-timing/10-raster-splits]
labs: [fine-x-scroll]
---
# $D016 fine X scrolling
The low three X-scroll bits in $D016 let VIC-II shift character display horizontally by sub-character steps. Other bits in $D016 control unrelated display features, so preserve them.

Fine scrolling alone only moves the displayed interpretation within its limited range. It does not create an endless stream of new characters.

## Scene connection
**Why does a demo coder care about this?**
Fine scroll is the hardware half of a classic smooth scroller. The other half is carefully timed screen-memory maintenance.

## Lab
Change only the X-scroll field of $D016 across its range while preserving the other bits. Observe movement without changing screen RAM.

## Next
We combine fine movement with the coarse row shift learned earlier.
