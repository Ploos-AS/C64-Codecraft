phase=$fb
TARGET=$e0
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
leave:
 lda $d012
 cmp #TARGET
 beq leave
wait:
 lda $d012
 cmp #TARGET
 bne wait
 jsr music_play
 rts
music_play:
 inc phase
 lda phase
 sta $d400
 lda #$20
 sta $d401
 lda #$11
 sta $d404
 lda #$0f
 sta $d418
 rts
