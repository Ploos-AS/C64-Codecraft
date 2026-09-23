---
title: Loader basics and contracts
course: 09-packing-loading
lesson: 05
level: advanced
prerequisites: [04-disk-image]
labs: [09.05-loader-basics]
---
# Loader basics and contracts
A loader moves data from storage into the memory layout required by the production.

Start with correctness before speed. Define a loader contract:
- requested file/part identity;
- destination or file-defined load address;
- memory that must remain resident;
- machine/IRQ state required during loading;
- success/failure behaviour;
- state handed back to the caller.

KERNAL-assisted loading is useful for understanding the flow and for non-time-critical transitions. More specialized loaders can be introduced later when the production constraint justifies them.

## Scene connection
**Why does a demo coder care about this?**
A loader is infrastructure shared by parts. A clear contract prevents each effect from inventing incompatible assumptions.

## Lab
Load the next part/data file under a documented simple loader contract and verify destination bytes before execution.

## Next
We examine what changes when music or visuals must continue during loading.
