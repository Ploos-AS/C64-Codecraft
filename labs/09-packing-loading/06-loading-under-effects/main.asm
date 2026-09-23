frame=$fb
load_progress=$fc
effect_phase=$fd
music_tick=$fe
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
 sta frame
 sta load_progress
 sta effect_phase
 sta music_tick
 jsr music_job
 jsr effect_job
 jsr loader_job
 inc frame
 rts
music_job:
 inc music_tick
 lda music_tick
 sta $c000
 rts
effect_job:
 inc effect_phase
 lda effect_phase
 sta $c010
 rts
loader_job:
 lda load_progress
 cmp #16
 beq loaded
 inc load_progress
loaded:
 lda load_progress
 sta $c020
 rts
