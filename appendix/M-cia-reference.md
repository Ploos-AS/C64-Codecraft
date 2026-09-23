# Appendix M — CIA quick reference

The C64 contains two 6526 CIA devices. They provide timers and I/O functions used by the machine and by low-level software.

## Why demo coders care
CIA state can affect interrupt behaviour and system assumptions. A raster routine that takes over interrupt handling must understand what remains enabled rather than treating VIC-II IRQs as the only possible interrupt source.

CIA functionality includes:
- two programmable timers per CIA;
- interrupt control;
- parallel I/O ports;
- time-of-day functionality;
- serial-related functionality.

CIA2 port state also participates in VIC-II bank selection.

## Rule
When taking over machine state, record which CIA interrupts/timers are enabled, disabled or preserved. Restore state when the surrounding environment requires it.

Exact register/interrupt sequences used by executable labs should be source-verified and tested rather than copied from folklore.
