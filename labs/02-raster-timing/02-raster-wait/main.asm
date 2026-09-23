TARGET=$80
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
wait:
 lda $d012
 cmp #TARGET
 bne wait
 lda #2
 sta $d020
 rts
