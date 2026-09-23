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
copy:
 lda signature,x
 sta $c000,x
 inx
 cpx #8
 bne copy
 rts
signature:
 .text "CCRC0001"
