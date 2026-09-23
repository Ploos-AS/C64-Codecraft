phase=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda $d016
 and #$f8
 ora phase
 sta $d016
 inc phase
 lda phase
 and #7
 sta phase
 rts
