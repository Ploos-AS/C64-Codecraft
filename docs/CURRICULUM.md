# Curriculum

C64 Codecraft targets a progression from **absolute beginner** to competent C64 demo coder. It assumes no previous machine-code or assembly experience.

The fundamentals come first, but the whole course has a C64 demoscene flavour. Scene relevance is not postponed until the advanced chapters: each foundational concept should show why it matters on a real C64 and where it leads in demo coding.

A recurring lesson question is: **Why does a demo coder care about this?**

Examples of that progression:

- loads/stores -> directly changing VIC-II state
- loops -> movement, animation and repeated screen work
- tables -> colour tables, lookup tables and eventually sine tables
- branches -> control flow, cycles and timing consequences
- zero page -> faster/smaller addressing and scarce-resource decisions
- subroutines -> structuring effects and demo parts
- interrupts -> raster effects and music playback
- cycle counting -> stable and increasingly cycle-exact effects

The course teaches the prerequisite concept before using the advanced technique. Scene flavour must motivate the fundamentals, not replace them.

## Course 0 — Meet the C64

No prerequisites. What machine code and assembly are; how a CPU executes instructions; binary and hexadecimal; bits, bytes and words; addresses and memory; the basic C64 memory map; the build/run/debug workflow. Get visible C64 feedback as early as practical.

## Course 1 — 6510 Assembly

Registers, flags, addressing modes, data movement, arithmetic, logic, branches, loops, subroutines, stack, tables, pointers and zero page. Pair the fundamentals with small C64/scene-oriented exercises and begin reasoning about instruction size and cycle cost.

## Course 2 — VIC-II

Text, color RAM, VIC banks, character sets, sprites, bitmap modes, scrolling and graphics memory organization.

## Course 3 — Interrupts and Timing

IRQ/NMI, raster beam, cycle counting, badlines, bus contention, sprite DMA, PAL/NTSC and stable raster.

## Course 4 — SID and Demo Architecture

SID basics, existing music playback, synchronization, memory planning, loaders and demo-part architecture.

## Course 5 — Demo Effects

Raster bars, scrollers, sine effects, sprite multiplexing, FLD and progressively advanced VIC-II techniques.

## Course 6 — Advanced 6510 / Scene Coding

Cycle budgets, zero-page engineering, page crossings, unrolling, lookup tables, self-modifying code, undocumented opcodes, compression and optimization.

## Final Project — Your First C64 Demo

A release-quality multi-part demo with music, graphics, transitions and at least one timing-critical effect.

## Lab method

Each major concept should follow:

**Learn -> Observe -> Modify -> Break -> Debug -> Optimize -> Challenge**

The goal is not merely to reproduce an effect, but to understand why it works.

## Lesson design rule

A beginner lesson should normally contain: the new concept in plain language, the smallest useful 6510 example, what changes in CPU/memory/C64 hardware, a visible or inspectable result, cycle/byte notes appropriate to the learner's level, a short **Scene connection**, and a lab following the course method. Advanced terminology may be previewed, but must not be required before it has been taught.
