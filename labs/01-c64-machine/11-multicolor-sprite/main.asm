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
 lda #2
 sta $d025
 lda #7
 sta $d026
 lda #1
 sta $d027
 lda #1
 sta $d01c
 sta $d015
 rts
*=$2000
sprite:
 .fill 21,$1b
 .fill 21,$6c
 .fill 21,$b1
 .byte 0
