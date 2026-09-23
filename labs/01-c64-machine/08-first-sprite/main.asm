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
 sta $d001
 lda #1
 sta $d027
 sta $d015
 rts
*=$2000
sprite:
 .fill 21,$18
 .fill 21,$3c
 .fill 21,$7e
 .byte 0
