*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx #0
shift:
 lda $0401,x
 sta $0400,x
 lda $d801,x
 sta $d800,x
 inx
 cpx #39
 bne shift
 lda #1
 sta $0427
 lda #14
 sta $d827
 rts
