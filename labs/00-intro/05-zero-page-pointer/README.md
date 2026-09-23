# Lab 00.05 — Zero-page pointer

## Goal
Reserve and use a zero-page pointer explicitly.

## Expected result
The first 16 screen cells are filled with the screen code stored in `fill_value`.

## Observe
Inspect $fb/$fc and explain why the pointer contains $0400 in little-endian order.

## Modify
Point the same routine at another 256-byte-aligned RAM area and inspect the result in the monitor.

## Think like a demo coder
Zero page is fast and useful, but finite. Treat addresses as owned production resources, not anonymous scratch bytes.
