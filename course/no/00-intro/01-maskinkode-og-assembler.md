---
title: Hva er maskinkode og assembler?
course: 00-intro
lesson: 01
level: absolute-beginner
prerequisites: []
labs: []
---

# Hva er maskinkode og assembler?

Du trenger ingen tidligere erfaring med programmering, maskinkode eller assembler.

## Hva du skal lære

Du skal forstå forskjellen mellom maskinkode og assembly/assemblerkode, hva en assembler gjør, og hvorfor C64 Codecraft arbeider tett på maskinvaren.

## Hvorfor dette betyr noe på C64

6510-prosessoren i C64 kjører maskinkode. Demoer får mye av særpreget sitt fra direkte kontroll over minne, VIC-II, SID og etter hvert svært presis timing.

Assembly gir oss en lesbar måte å beskrive CPU-instruksjonene på uten å skjule maskinen.

## Ideen

CPU-en kjører ikke ordene `LDA` og `STA`. Den kjører bytes i minnet som representerer instruksjoner og operander.

Senere møter du for eksempel:

```asm
lda #$06
sta $d020
```

Dette er assembly. En assembler som 64tass oversetter det til bytes som 6510 kan kjøre.

Du trenger ikke forstå `#$06` eller `$d020` ennå. Hex, registre, adresser og instruksjonene blir forklart før vi forventer at du bruker dem.

## Hva maskinen gjør

Arbeidsflyten er i grove trekk:

1. Vi skriver assembly-kildekode.
2. 64tass oversetter den til maskinkode.
3. Maskinkoden lastes i C64 eller emulator.
4. 6510 henter og utfører instruksjonene.
5. Instruksjonene kan endre minne og maskinvare.

VICE lar oss observere dette uten å erstatte den virkelige C64-programmeringsmodellen.

## Bytes og cycles

Maskinkode består av bytes. CPU-instruksjoner bruker også tid, målt i clock cycles.

Begge deler blir svært viktig i demo-koding. Foreløpig holder det å vite at en instruksjon har både størrelse og tidskostnad.

## Scene-kobling

**Hvorfor bryr en demo-koder seg om dette?**

Klassiske C64-effekter kommer ofte fra nøye valgte instruksjoner som arbeider direkte mot maskinvaren. Senere kan enkelt-cycles bli viktige. Reisen starter med å forstå hva 6510 faktisk kjører.

## Kontrollpunkt

Du skal nå kunne forklare at maskinkode er bytes CPU-en kjører, assembly er en lesbar representasjon, og assembleren oversetter mellom dem.

## Neste

Neste leksjon lærer akkurat nok binær og hexadecimal til at C64-verdier og adresser blir forståelige.
