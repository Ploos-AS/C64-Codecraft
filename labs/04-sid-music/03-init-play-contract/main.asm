phase=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr music_init
 jsr music_play
 rts
music_init:
 lda #0
 sta phase
 lda #$0f
 sta $d418
 lda #$11
 sta $d404
 rts
music_play:
 inc phase
 lda phase
 sta $d400
 lda #$20
 sta $d401
 rts
