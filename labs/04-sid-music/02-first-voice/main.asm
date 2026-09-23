*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #$0f
 sta $d418
 lda #$00
 sta $d400
 lda #$20
 sta $d401
 lda #$09
 sta $d405
 lda #$f0
 sta $d406
 lda #$11
 sta $d404
 rts
