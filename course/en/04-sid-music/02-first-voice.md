---
title: One SID voice
course: 04-sid-music
lesson: 02
level: intermediate
prerequisites: [01-meet-the-sid]
labs: [04.02-first-voice]
---
# One SID voice
To understand a player later, first control one voice directly.

A useful experiment sets frequency, waveform/control and ADSR, then uses the gate bit to start and release a note. The exact frequency register value depends on SID clock/model assumptions, so the lab states its target explicitly.

Do not confuse oscillator waveform with envelope: waveform determines the repeating shape; ADSR shapes amplitude over time.

## Scene connection
**Why does a demo coder care about this?**
You do not need to become a SID composer to write demos, but knowing what a player changes helps when debugging silence, conflicts or timing-sensitive integration.

## Lab
Produce one tone, change its frequency, then alter attack/release and describe the audible difference.

## Next
Rather than composing a soundtrack in assembly, we integrate an existing SID player interface.
