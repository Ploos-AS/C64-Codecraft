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
 ldx phase
 lda motion,x
 sta $d020
 inc phase
 lda phase
 and #7
 sta phase
 ldx #0
copy:
 lda asset,x
 sta $c000,x
 inx
 cpx #8
 bne copy
 rts
motion:
 .byte 0,6,14,3,1,3,14,6
asset:
 .byte $18,$3c,$7e,$ff,$ff,$7e,$3c,$18
