---
title: Undocumented opcodes
course: 08-6510-optimization
lesson: 07
level: advanced
prerequisites: [06-self-modifying-code]
labs: [undocumented-opcodes]
---
# Undocumented opcodes
NMOS 6510 har instruction encodings utover dokumentert instruction set. Noen er historisk brukt i C64-software og demos fordi en nyttig kombinert operation kan spare bytes eller cycles.

De er ikke et gratis optimization-tier. Behaviour og egnethet varierer mellom opcodes, CPU implementations og emulators, og enkelte encodings er uegnede for dependable code.

For hver kandidat:
1. dokumenter operation og flags;
2. identifiser target CPU assumption;
3. verifiser assembler syntax/support;
4. sammenlign documented-instruction alternative;
5. test på qualified emulation og real hardware når mulig;
6. bruk den bare når gevinsten betyr noe.

## Scene-kobling
**Hvorfor bryr en demo-koder seg om dette?**
Kunnskap om undocumented instructions er del av historisk 6510-praksis. Scene credibility betyr også å vite når man *ikke* skal bruke en.

## Lab
Evaluer én godt dokumentert kandidat mot vanlig instruction sequence. Noter cycles, bytes, assumptions og test evidence før du avgjør om produksjonen kan bruke den.

## Neste
Vi skiller speed optimization fra sizecoding.
