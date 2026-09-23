---
title: Assemble a multipart demo
course: 09-packing-loading
lesson: 08
level: advanced
prerequisites: [07-part-contracts]
labs: [09.08-multipart-demo]
---
# Assemble a multipart demo
A multipart demo is now a sequence of explicit states:

```text
boot -> load/depack part A -> run A
     -> transition/load B -> run B
     -> transition/load C -> run C
     -> ending
```

The interesting work is at the boundaries: what remains resident, when loading happens, where packed data lives, when depacking is safe and which machine state is handed onward.

Build each part independently, then integrate through documented contracts.

## Failure paths
Development builds should make loader/depacker failures visible rather than jumping into invalid memory. Release behaviour can be compact, but debugging needs evidence.

## Lab
Connect at least three small teaching parts into a repeatable sequence from one disk image.

## Next
We qualify the disk as a reproducible scene release artifact.
