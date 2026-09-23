*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr compact
 jsr expanded
 rts
compact:
 ldx #7
c:
 lda data,x
 sta $c000,x
 dex
 bpl c
 rts
expanded:
 lda data+0
 sta $c010
 lda data+1
 sta $c011
 lda data+2
 sta $c012
 lda data+3
 sta $c013
 lda data+4
 sta $c014
 lda data+5
 sta $c015
 lda data+6
 sta $c016
 lda data+7
 sta $c017
 rts
data:
 .byte 1,2,3,4,5,6,7,8
