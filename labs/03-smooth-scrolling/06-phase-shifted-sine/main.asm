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
 lda #0
 sta phase
 ldx #0
loop:
 txa
 asl
 clc
 adc phase
 and #15
 tay
 lda sintab,y
 sta $c000,x
 inx
 cpx #8
 bne loop
 inc phase
 lda phase
 and #15
 sta phase
 rts
sintab:
 .byte 8,11,13,15,15,15,13,11
 .byte 8,5,3,1,1,1,3,5
