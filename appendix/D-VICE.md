# Appendix D — VICE and monitor/debugging

VICE/x64sc is the reference C64 emulator for Codecraft labs where practical.

## Basic development loop

```sh
64tass --cbm-prg -o build/example.prg main.asm
x64sc -autostart build/example.prg
```

Exact startup requirements depend on the installed VICE build and ROM setup.

## Monitor/debugging skills
Students should become comfortable with:
- pausing execution;
- inspecting CPU registers;
- examining/changing memory;
- disassembly;
- breakpoints/watchpoints where supported;
- stepping;
- labels/symbols;
- relating raster observations to source and cycle counts.

## Timing
VICE is valuable for controlled experiments, but always state the emulated machine/video model for model-sensitive code.

## Qualification boundary
The current Codecraft reference-container work has qualified VICE more narrowly than a full deterministic remote-monitor test harness. Interactive monitor use and automated state assertion are separate capabilities. Documentation must not claim the latter until it is actually qualified.

## Real hardware
Emulation is essential for reproducible teaching and debugging; timing-sensitive releases should also be tested on real C64 hardware when available.
