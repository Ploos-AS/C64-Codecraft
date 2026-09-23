*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx #$10
 lda aligned,x
 sta $c000
 lda crossing,x
 sta $c001
 rts
*=$3000
aligned:
 .fill 64,$11
*=$30f8
crossing:
 .fill 32,$22
