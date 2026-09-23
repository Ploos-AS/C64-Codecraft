; C64 Codecraft Lab 00.07
COUNT = 16

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
    lda chars,x
    sta $0400,x
    lda colours,x
    sta $d800,x
    inx
    cpx #COUNT
    bne loop
    rts

chars:
    .byte 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
colours:
    .byte 1,7,15,10,8,2,9,0,1,7,15,10,8,2,9,0
