# C64 Codecraft labs

Labs turn lesson concepts into real 6510 programs. They use ordinary scene/development tools directly; there is no Codecraft runtime or assembly dialect.

## Standard lab shape

```text
labs/<course>/<lab>/
  README.md
  main.asm
  Makefile
  lab.yml
```

A lab should document:
- lesson and learning goal;
- assembler/tool requirement;
- target machine/video assumptions;
- build/run commands;
- expected visible/observable result;
- debugger task;
- modification/challenge;
- what CI can verify versus what still needs manual/emulator/hardware inspection.

Generated `.prg`, symbols, disk images and build directories are not source.

## Reference assembler

Early labs use 64tass so beginners see one consistent syntax. Later lessons deliberately introduce ACME/KickAssembler/ca65 literacy without creating a Codecraft abstraction layer.
