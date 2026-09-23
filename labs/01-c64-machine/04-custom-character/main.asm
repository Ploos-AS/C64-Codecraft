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
 lda glyph,x
 sta $c800,x
 inx
 cpx #8
 bne copy
 rts
glyph:
 .byte %00011000
 .byte %00111100
 .byte %01111110
 .byte %11011011
 .byte %11111111
 .byte %00100100
 .byte %01011010
 .byte %10100101
