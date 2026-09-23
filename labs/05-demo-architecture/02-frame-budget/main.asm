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
 jsr music_work
 lda #5
 sta $d020
 jsr update_work
 lda #7
 sta $d020
 jsr render_work
 lda #0
 sta $d020
 rts
music_work:
 ldx #4
m: dex
 bne m
 rts
update_work:
 ldx #8
u: dex
 bne u
 rts
render_work:
 ldx #12
r: dex
 bne r
 rts
