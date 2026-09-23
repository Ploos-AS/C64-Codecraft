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
 lda modes,x
 sta $c000,x
 inx
 cpx #12
 bne copy
 rts
; four descriptors: memory-class, timing-class, flexibility-class
modes:
 .byte 1,1,1
 .byte 2,3,3
 .byte 3,4,4
 .byte 4,4,3
