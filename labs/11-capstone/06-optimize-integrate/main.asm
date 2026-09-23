music=$fb
effect=$fc
transition=$fd
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr music_job
 jsr effect_job
 jsr transition_job
 rts
music_job:
 inc music
 rts
effect_job:
 inc effect
 lda effect
 and #15
 sta $d020
 rts
transition_job:
 lda effect
 cmp #$40
 bne done
 lda #1
 sta transition
done:
 rts
