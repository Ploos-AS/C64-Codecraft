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
 lda generated_asset,x
 sta $c000,x
 inx
 cpx #8
 bne copy
 rts
generated_asset:
 .byte $18,$3c,$7e,$ff,$ff,$7e,$3c,$18
