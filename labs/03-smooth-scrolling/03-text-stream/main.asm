text_index=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx text_index
 lda text,x
 bne put
 ldx #0
 stx text_index
 lda text,x
put:
 sta $0427
 inx
 stx text_index
 rts
text:
 .byte 3,15,4,5,3,18,1,6,20,0
