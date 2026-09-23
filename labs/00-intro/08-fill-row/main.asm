W=40
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start: ldx #0
loop: lda #1
 sta $0400,x
 lda #14
 sta $d800,x
 inx
 cpx #W
 bne loop
 rts
