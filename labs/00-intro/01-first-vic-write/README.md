# Lab 00.01 — First VIC-II write

Related lesson: Course 00, first direct hardware-control lessons.

## Goal
Assemble a real C64 PRG that writes directly to VIC-II colour registers.

## Build

```sh
make
```

Equivalent underlying command:

```sh
64tass --cbm-prg -o build/first-vic-write.prg main.asm
```

## Run

```sh
make run
```

This launches `x64sc` with the generated PRG when VICE is installed/configured on the host.

## Expected result
After `RUN`, the BASIC stub executes `SYS 2064`. The machine-code routine changes the border to blue and background to light blue, then returns to BASIC.

## Observe in the monitor
Find the routine at $0810 and relate each `lda`/`sta` to A and the VIC-II registers $d020/$d021.

## Modify
Change only the immediate colour values. Rebuild and predict the result before running it.

## Break it
Change the SYS address or one destination register and explain the symptom.

## CI boundary
CI can assemble the PRG and verify its deterministic bytes. Visible colour/emulator state is a separate runtime check.
