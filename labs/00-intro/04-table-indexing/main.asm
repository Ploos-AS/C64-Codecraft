; C64 Codecraft Lab 00.04
COUNT = 8

*=$0801
.word basic_end
.word 10
.byte $9e
.text "2064"
.byte 0
basic_end: .word 0

*=$0810
start:
    ldx #0
loop:
    lda palette,x
    sta $d800,x
    inx
    cpx #COUNT
    bne loop
    rts

palette:
    .byte $01,$07,$0f,$0a,$08,$02,$09,$00
