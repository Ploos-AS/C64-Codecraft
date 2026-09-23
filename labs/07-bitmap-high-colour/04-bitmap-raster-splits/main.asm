TOP=$60
BOTTOM=$c0
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
wait_top:
 lda $d012
 cmp #TOP
 bne wait_top
 lda #6
 sta $d020
wait_bottom:
 lda $d012
 cmp #BOTTOM
 bne wait_bottom
 lda #14
 sta $d020
 rts
