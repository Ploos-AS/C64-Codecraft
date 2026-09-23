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
 lda screen_state,x
 sta $c000,x
 lda colour_state,x
 sta $c010,x
 inx
 cpx #8
 bne copy
 rts
screen_state:
 .byte 0,1,2,3,4,5,6,7
colour_state:
 .byte 0,6,14,3,1,3,14,6
