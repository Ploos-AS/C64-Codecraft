P=8
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
 ldy #0
loop: lda chars,y
 sta $0400,x
 lda cols,y
 sta $d800,x
 inx
 iny
 cpy #P
 bne nowrap
 ldy #0
nowrap: cpx #W
 bne loop
 rts
chars:.byte 1,2,3,4,4,3,2,1
cols:.byte 1,7,15,10,8,10,15,7
