# Lab 00.06 — (zp),Y pointer walking

## Goal
Use `(zp),Y` to access data through a pointer.

## Expected result
Sixteen bytes from `message` are copied to the first 16 screen cells.

The table deliberately contains screen codes, not unexplained host text conversion.

## Observe
Inspect source pointer $fb/$fc, Y and the effective source address.

## Modify
Move `message` elsewhere in memory without changing the copy loop.

## Think like a demo coder
Pointer-driven code can operate on relocated data and streams—the same basic mechanism appears in scrollers, loaders and asset processing.
