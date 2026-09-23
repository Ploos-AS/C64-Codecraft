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
hot_path:
 lda source,x
 asl
 clc
 adc #3
 eor #$55
 sta $c000,x
 inx
 cpx #16
 bne hot_path
 rts
source:
 .byte 0,1,2,3,4,5,6,7
 .byte 8,9,10,11,12,13,14,15
