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
 lda tile,x
 sta $2000,x
 inx
 cpx #8
 bne copy
 lda #$16
 sta $0400
 rts
tile:
 .byte %00111100,%01100110,%11000011,%11000011
 .byte %11000011,%11000011,%01100110,%00111100
