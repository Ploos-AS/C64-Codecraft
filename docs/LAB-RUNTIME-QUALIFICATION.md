# Deterministic lab runtime qualification

## Purpose

C64 Codecraft separates three different verification layers instead of treating
"it assembled" as proof that a lab behaves correctly.

1. **Assembly** — the reference source builds with 64tass.
2. **Deterministic CPU/RAM state** — suitable labs execute in a controlled 6510
   harness with explicit initial state and machine-readable assertions.
3. **C64 hardware qualification** — VIC-II, SID, CIA, raster timing, DMA and
   video-standard-sensitive labs run in a qualified C64 emulator or real
   hardware harness.

The existing `verification.emulator_state` field remains `false` until a lab
has a real runtime assertion path. It must never be enabled merely because the
lab assembles.

## M0.1 CPU/RAM harness contract

The first runtime harness targets labs whose observable result depends only on
6510 execution and RAM. It deliberately excludes VIC-II, SID, CIA, ROM calls,
raster timing and undocumented-opcode compatibility.

Each qualified lab will declare:

- a deterministic entry address;
- explicit initial CPU/RAM state where needed;
- a deterministic stop condition;
- a maximum instruction/cycle budget;
- expected RAM/register/flag state.

The harness must fail on timeout, unsupported I/O access, unexpected control
flow, or assertion mismatch.

## CPU/RAM qualification status

M0.1 is operational. Qualified labs opt in with `verification.cpu_state: true`
and provide `runtime_test.py`; `tools/run_cpu_labs.py` discovers and executes
them in CI. The current audited set is tracked in `docs/CPU-RUNTIME-MATRIX.md`.

The harness is intentionally CPU/RAM-only. CPU-visible accesses to the C64 I/O
window `$D000-$DFFF` fail closed, including effective addresses reached through
indexed or indirect addressing. VIC-II, SID, CIA, raster timing and other
hardware semantics therefore cannot accidentally pass as ordinary RAM behavior.

## C64 hardware path

VICE remains the reference C64 emulator, but Debian 13's packaged VICE 3.9 has
not yet provided a deterministic state-control interface acceptable for CI.
The old monitor-command experiment is not a qualified assertion mechanism.

Hardware-sensitive labs therefore remain `emulator_state: false` until that
interface is solved and independently qualified.

## M0.2 C64 hardware/emulator qualification contract

M0.2 adds a separate machine-level path; it does not extend the CPU/RAM harness
with partial VIC-II/SID/CIA behavior.

A hardware-qualified lab must declare its machine assumptions and observable
contract. The runner must provide:

- a pinned emulator/version and ROM provenance;
- an explicit PAL/NTSC machine profile where timing matters;
- deterministic program loading and entry;
- a bounded run/stop condition;
- machine-readable assertions for the hardware state actually under test;
- fail-closed handling when required emulator state cannot be observed;
- no proprietary Commodore ROMs committed to the repository.

Qualification classes are tracked separately: VIC-II register/state, raster and
timing, SID, CIA, banking/6510 port, color RAM, and disk/loader behavior. A lab
must not receive `emulator_state: true` merely because it boots or produces a
screenshot.

The first M0.2 target should be a small non-cycle-exact VIC-II register lab
before raster/badline/DMA-sensitive work. This gives the machine runner a
deterministic state assertion without conflating it with video-output
qualification.

## Gate

M0.1 is complete. The gate requires representative CPU/RAM labs to:

1. assembles in CI;
2. executes from a declared deterministic initial state;
3. terminates through the declared stop condition;
4. has machine-readable post-state assertions;
5. fail CI when an expected result is intentionally changed.

The harness self-test exercises both the positive assertion path and an
intentional mismatch through the same assertion helper, as well as unsupported
opcodes and fail-closed C64 I/O access.
