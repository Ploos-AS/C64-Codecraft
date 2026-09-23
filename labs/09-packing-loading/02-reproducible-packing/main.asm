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
 lda payload,x
 sta $c000,x
 inx
 cpx #16
 bne copy
 rts
payload:
 .byte 0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3
