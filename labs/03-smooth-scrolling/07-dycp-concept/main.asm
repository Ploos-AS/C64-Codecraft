phase=$fb
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
column:
 txa
 asl
 clc
 adc phase
 and #15
 tay
 lda ytable,y
 sta $c000,x
 inx
 cpx #8
 bne column
 inc phase
 rts
ytable:
 .byte 4,6,8,10,11,10,8,6
 .byte 4,2,0,0,0,0,0,2
