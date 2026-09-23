# Appendix J — C64 memory-map quick reference

The 6510 sees a 64 KiB address space, but not every address always exposes RAM. ROM and I/O visibility depend on banking state.

## Important regions
- $0000-$00ff — zero page, including 6510 port-related locations at the start.
- $0100-$01ff — hardware stack page.
- $0400 — conventional default text screen base after normal startup; software can configure other screen locations.
- $d000-$dfff — I/O region when mapped in; VIC-II, SID, colour RAM, CIA and related devices occupy subranges.
- $e000-$ffff and other ROM-visible regions — mapping depends on banking configuration.

## Banking
The 6510 processor port at $0000/$0001 participates in selecting RAM/ROM/I/O visibility. Always reason about both CPU-visible memory and what VIC-II can fetch.

## Rule
A production memory map should record:
- address range;
- owner;
- CPU visibility/banking;
- VIC-II visibility where relevant;
- lifetime;
- alignment;
- overwrite/transition rules.

Do not treat the startup map as a fixed hardware law.
