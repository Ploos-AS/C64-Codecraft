# Appendix O — PAL, NTSC and VIC-II variants

"C64 timing" is not one universal set of numbers.

Different VIC-II/video variants use different raster geometry and timing. A common PAL-B 6569 target is often described as 312 raster lines with 63 CPU cycles per line, but Codecraft does not treat those values as universal C64 constants.

## For timing-sensitive work, record
- video standard;
- VIC-II model/assumption;
- lines per frame;
- cycles per line;
- frame/playback cadence;
- which raster constants are target-specific.

## Course policy
A lab may use an explicitly stated PAL target first. NTSC support must be implemented/tested rather than inferred.

## Music
"Call play once per frame" is not automatically portable across songs, players or video standards. Follow the player's documented cadence and the production's timing policy.

## Release
State supported/primary targets honestly. "Works in my emulator configuration" is evidence for that configuration, not proof for every C64.
