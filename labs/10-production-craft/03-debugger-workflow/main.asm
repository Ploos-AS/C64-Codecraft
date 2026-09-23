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
 lda data,x
 sta $c000,x
 inx
 cpx #7
 bne copy
 rts
data:
 .byte 1,2,3,4,5,6,7,8
