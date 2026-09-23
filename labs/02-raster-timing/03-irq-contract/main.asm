TARGET=$80
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda $d011
 sta $c000
 lda $0314
 sta $c001
 lda $0315
 sta $c002
 lda #TARGET
 sta $d012
 lda $d011
 and #$7f
 sta $d011
 lda #1
 sta $d01a
 rts
