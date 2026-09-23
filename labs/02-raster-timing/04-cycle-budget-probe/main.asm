*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #2
 sta $d020
 ldx #16
work:
 dex
 bne work
 lda #0
 sta $d020
 rts
