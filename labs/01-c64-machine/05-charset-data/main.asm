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
 lda charset,x
 sta $c800,x
 inx
 cpx #32
 bne copy
 rts
charset:
 .byte $00,$18,$3c,$7e,$ff,$7e,$3c,$18
 .byte $18,$18,$18,$18,$18,$18,$18,$18
 .byte $ff,$81,$81,$81,$81,$81,$81,$ff
 .byte $aa,$55,$aa,$55,$aa,$55,$aa,$55
