; C64 Codecraft Lab 00.03
*=$0801
.word basic_end
.word 10
.byte $9e
.text "2064"
.byte 0
basic_end: .word 0

*=$0810
start:
    jsr set_colours
    rts

set_colours:
    lda #$05
    sta $d020
    jsr set_background
    rts

set_background:
    lda #$00
    sta $d021
    rts
