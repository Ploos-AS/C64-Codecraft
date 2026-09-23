*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #3
 sta $d020
 lda #0
 sta $d021
 rts
