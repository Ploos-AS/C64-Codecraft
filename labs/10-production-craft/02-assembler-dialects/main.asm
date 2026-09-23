*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx #0
loop:
 lda colours,x
 sta $d020
 inx
 cpx #4
 bne loop
 rts
colours:
 .byte 0,6,14,1
