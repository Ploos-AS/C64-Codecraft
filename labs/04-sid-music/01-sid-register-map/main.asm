*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #0
 ldx #$18
clear:
 sta $d400,x
 dex
 bpl clear
 lda #$0f
 sta $d418
 rts
