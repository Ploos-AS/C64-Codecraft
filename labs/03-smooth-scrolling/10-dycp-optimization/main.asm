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
looped:
 lda source,x
 sta $c000,x
 inx
 cpx #8
 bne looped

 lda source+0
 sta $c010
 lda source+1
 sta $c011
 lda source+2
 sta $c012
 lda source+3
 sta $c013
 lda source+4
 sta $c014
 lda source+5
 sta $c015
 lda source+6
 sta $c016
 lda source+7
 sta $c017
 rts
source:
 .byte $18,$3c,$7e,$ff,$ff,$7e,$3c,$18
