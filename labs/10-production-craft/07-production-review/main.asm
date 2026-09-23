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
 lda gates,x
 sta $c000,x
 inx
 cpx #7
 bne copy
 rts
; 0 = not reviewed, 1 = evidence recorded
gates:
 .byte 0,0,0,0,0,0,0
