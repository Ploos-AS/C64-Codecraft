value=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #3
 sta value
 lda value
 asl
 asl
 sta $c000
 ldx value
 lda times4,x
 sta $c001
 rts
times4:
 .byte 0,4,8,12,16,20,24,28
 .byte 32,36,40,44,48,52,56,60
