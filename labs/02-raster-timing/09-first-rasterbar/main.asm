START=$70
COUNT=8
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
line:
 txa
 clc
 adc #START
wait:
 cmp $d012
 bne wait
 lda colours,x
 sta $d020
 inx
 cpx #COUNT
 bne line
 lda #0
 sta $d020
 rts
colours:
 .byte 6,14,3,1,3,14,6,0
