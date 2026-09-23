---
title: Synchronize visuals to music
course: 04-sid-music
lesson: 06
level: intermediate
prerequisites: [05-pal-ntsc-playback]
labs: [music-sync]
---
# Synchronize visuals to music
Visual synchronization needs a reliable source of musical state.

Depending on the music system, useful state might be an exported song position, pattern/row value, explicit cue byte, or a counter maintained by integration code at known musical boundaries. Do not scrape undocumented internal player memory and call it an API.

A simple cue interface can let visual code react to events:

```text
cue 0: normal
cue 1: start rasterbar
cue 2: change scroller palette
cue 3: launch sprite formation
```

The exact mechanism belongs to the chosen player/composer workflow.

## Scene connection
**Why does a demo coder care about this?**
Music sync turns simultaneous audio and graphics into choreography. It also decouples visual event logic from fragile wall-clock delays.

## Lab
Use a documented cue/state source to trigger at least three visible changes while the music continues uninterrupted.

## Checkpoint
You can integrate a player, schedule it, state its timing target and expose documented synchronization state to visual code.

## Next
We combine music, rasterbars, scroller and sprites into a small timed demo part.
