*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #80
 sta $d000
 lda #70
 sta $d001
 lda #2
 sta $d027
 lda #1
 sta $d015
wait:
 lda $d012
 cmp #$90
 bne wait
 lda #160
 sta $d000
 lda #170
 sta $d001
 lda #7
 sta $d027
 rts
