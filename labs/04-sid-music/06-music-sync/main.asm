tick=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr music_play
 jsr sync_update
 rts
music_play:
 inc tick
 rts
sync_update:
 lda tick
 lsr
 lsr
 lsr
 sta $c000
 rts
