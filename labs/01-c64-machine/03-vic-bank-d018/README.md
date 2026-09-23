# Lab 01.03 — VIC bank and $D018 observation

## Goal
Read the machine's current VIC-II memory-selection state before changing it.

The lab stores $D018 and CIA2 port A ($DD00) snapshots at $c000/$c001.

## Observe
Use the Course 01 lessons to explain what information these registers contribute to VIC-II memory selection. Do not treat either byte alone as a complete address.

## Challenge
Draw the currently selected VIC bank and screen/character regions for your emulator startup configuration.

**Why does a demo coder care?** CPU placement and VIC-II fetch placement are related but different address problems.
