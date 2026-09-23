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
 lda glyph0,x
 sta $c800,x
 lda glyph1,x
 sta $c808,x
 inx
 cpx #8
 bne copy
 rts
glyph0:
 .byte %00111100,%01100110,%01100110,%01111110
 .byte %01100110,%01100110,%01100110,%00000000
glyph1:
 .byte %00011110,%00110011,%00110011,%00111111
 .byte %00110011,%00110011,%00110011,%00000000
