---
title: Opening the borders
course: 06-advanced-vicii
lesson: 05
level: advanced
prerequisites: [04-line-crunching]
labs: [border-opening]
---
# Opening the borders
The normal C64 display has border regions controlled by VIC-II display sequencing. Carefully timed changes to display-control state can interfere with when border state is established or released, allowing graphics activity in areas normally covered by the border.

There are distinct vertical and side-border techniques. They are not one generic "open border" switch, and their timing requirements differ.

This lesson first separates the mechanisms and target assumptions. Executable code belongs in target-specific labs with cycle annotations.

## Scene connection
**Why does a demo coder care about this?**
Opening borders changes the apparent physical limits of the stock display and became an important visual signature of advanced C64 productions.

## Lab
Reproduce one documented border-opening mechanism on the stated VIC-II target and verify it over many frames before adding content.

## Next
Side-border work demands especially precise horizontal timing.
