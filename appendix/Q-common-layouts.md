# Appendix Q — Common production layouts

There is no universal Codecraft memory layout. These patterns are starting points for reasoning.

## Single-part effect
Often consists of:
- entry/init code;
- IRQ/timing code;
- effect state;
- graphics/data;
- music/player;
- stack/zero-page reservations.

## Multipart production
Add:
- small resident loader/core where needed;
- load/depack buffer;
- explicit per-part ranges;
- transition overlap rules;
- packed-source lifetime;
- next-part destination.

## VIC-II-oriented layout
When choosing screen, charset, bitmap and sprite data, reason within the selected VIC bank and the addressing/alignment constraints of each resource.

## Rule
Draw the map. Mark every byte range with owner and lifetime. "There should be room" is not a memory-management strategy.
