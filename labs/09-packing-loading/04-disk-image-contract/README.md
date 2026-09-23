# Lab 09.04 — Disk-image contract

## Goal
Define what belongs on a release disk before depending on a particular disk-image utility.

The program itself is a tiny release candidate. The lab README is the contract: disk title/id, boot filename, part filenames/order and reproducible image-build command belong in version control.

## Challenge
Qualify one disk-image tool from the packing/release appendix and add a deterministic image target without making the assembler lab depend on an unavailable host tool.

**Why does a demo coder care?** The disk directory and file layout are part of the production, loader design and release experience.
