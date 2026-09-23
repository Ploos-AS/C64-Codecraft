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
 lda pixels,x
 sta $2000,x
 inx
 cpx #8
 bne copy
 lda #$26
 sta $0400
 lda #$0e
 sta $d800
 lda #$00
 sta $d021
 rts
pixels:
 .byte %00011011,%01101100,%10110001,%11000110
 .byte %11000110,%10110001,%01101100,%00011011
