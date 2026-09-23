*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #2
 sta $d020
 jsr baseline
 lda #5
 sta $d020
 jsr candidate
 lda #0
 sta $d020
 rts
baseline:
 ldx #0
b:
 lda source,x
 sta $c000,x
 inx
 cpx #8
 bne b
 rts
candidate:
 ldx #7
c:
 lda source,x
 sta $c010,x
 dex
 bpl c
 rts
source:
 .byte 0,1,2,3,4,5,6,7
