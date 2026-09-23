---
title: Lesson title
course: course-id
lesson: lesson-id
level: beginner
prerequisites: []
labs: []
---

# Lesson title

## What you will learn

State the small set of concepts the learner should understand by the end. Do not assume terminology that has not already been taught.

## Why this matters on the C64

Connect the concept to the real machine: CPU, memory, VIC-II, SID, CIA, timing or development workflow.

## The idea

Explain the concept in plain language before introducing syntax.

## Smallest useful 6510 example

Use ordinary assembler syntax and real tools. Keep the first example small enough that every instruction can be explained.

## What the machine does

Walk through registers, memory and relevant hardware state step by step.

## Bytes and cycles

Show instruction size and cycle cost at a level appropriate for this point in the course. Explain why a demo coder will eventually care; do not require advanced raster knowledge prematurely.

## Scene connection

Answer: **Why does a demo coder care about this?**

Show where this foundational idea grows into real scene work without turning the lesson into an advanced-effects tutorial.

## Lab

Follow the Codecraft loop:

**Learn -> Observe -> Modify -> Break -> Debug -> Optimize -> Challenge**

### Observe
Inspect the expected result in VICE and, where useful, its monitor.

### Modify
Make one controlled change and predict the result before running it.

### Break
Introduce a deliberate, understandable mistake.

### Debug
Use the real assembler/VICE workflow to identify the mistake.

### Optimize
Compare a small size/cycle/memory trade-off appropriate to the lesson.

### Challenge
Apply the concept in a small C64/scene-flavoured task without a Codecraft-specific runtime or API.

## Checkpoint

List what the learner should now be able to explain and do unaided.

## Next

Connect this lesson to the next concept and, where useful, preview the later demo technique it enables.
