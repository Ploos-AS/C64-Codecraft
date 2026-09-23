frame=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda frame
 and #3
 asl
 asl
 asl
 tax
 ldy #0
copy:
 lda frames,x
 sta $c800,y
 inx
 iny
 cpy #8
 bne copy
 inc frame
 rts
frames:
 .byte $18,$18,$18,$18,$18,$18,$18,$18
 .byte $00,$18,$18,$7e,$18,$18,$00,$00
 .byte $00,$00,$3c,$7e,$3c,$00,$00,$00
 .byte $00,$00,$00,$ff,$00,$00,$00,$00
