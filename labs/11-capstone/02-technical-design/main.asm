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
 lda design_state,x
 sta $c000,x
 inx
 cpx #8
 bne copy
 rts
design_state:
 .byte $00,$04,$00,$20,$00,$40,$fb,$ff
