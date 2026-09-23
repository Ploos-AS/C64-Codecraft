*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #$80
 sta $07f8
 lda #100
 sta $d000
 lda #100
 sta $d001
 lda #1
 sta $d015
 lda #2
 sta $d020
 ldx #16
work:
 dex
 bne work
 lda #0
 sta $d020
 rts
*=$2000
sprite:
 .fill 63,$3c
 .byte 0
