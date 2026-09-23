*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #44
 sta $d000
 lda $d010
 ora #1
 sta $d010
 lda #120
 sta $d001
 rts
