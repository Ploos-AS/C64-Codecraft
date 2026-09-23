qual=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #0
 sta qual
 ; Set bits only after the corresponding external qualification evidence exists.
 lda qual
 sta $c000
 rts
