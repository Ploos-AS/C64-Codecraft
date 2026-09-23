# Appendix R — Troubleshooting checklist

Debug from the lowest-cost evidence upward.

## Program does not start
Check build success, load/start address, BASIC/SYS stub if used, entry address and emulator invocation.

## Wrong colours/characters
Check screen codes versus PETSCII, colour RAM writes, charset selection, $d018 and active VIC bank.

## Sprite missing or corrupt
Check $d015, X/Y registers, $d010 high X bit, sprite pointer, 64-byte alignment/block, active VIC bank and sprite data.

## Raster effect jitters
Check IRQ source/acknowledge, entry jitter, instruction path variation, page crossings, badlines, sprite DMA and target model.

## Works alone, fails after integration
Check memory/zero-page ownership, IRQ/CIA state, register clobbers, banking, stack depth and timing budget.

## Music changes behaviour
Check documented init/play cadence, clobbers, memory/ZP use and whether the raster schedule leaves enough time.

## Emulator differs from hardware
Record emulator machine model, VIC-II/SID assumptions, ROM environment and exact binary. Reduce to the smallest failing test before changing production code.

## Principle
Do not fix an unexplained symptom with an unexplained delay. First identify which machine assumption was wrong.
