*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda $d012
 sta $c000
 lda $d011
 and #$80
 sta $c001
 rts
