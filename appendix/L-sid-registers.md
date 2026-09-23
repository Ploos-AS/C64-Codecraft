# Appendix L — SID quick reference

SID begins at $d400 in the normal C64 I/O map.

## Voice structure
Each of the three voices has controls for frequency, pulse width, waveform/control and ADSR envelope. SID also provides shared filter and volume/output controls.

## Production practice
Most demos integrate a music player rather than manually composing every SID write in the effect code.

For an imported player document:
- init entry and required inputs;
- play entry;
- intended call cadence;
- memory ranges;
- zero-page use;
- register/flag clobbers;
- cue/song-position interface if provided;
- SID model assumptions when relevant.

## 6581 and 8580
Do not imply identical analogue sound across SID revisions. Filter behaviour and perceived output can differ. A production should state important SID assumptions when sound depends on them.

## Rule
Never scrape undocumented internal player variables and silently promote them to a stable API. Make the integration contract explicit.
