frame=$fb
music_tick=$fc
gfx_state=$fd
effect_state=$fe
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
 sta music_tick
 sta gfx_state
 sta effect_state
 jsr music_job
 jsr graphics_job
 jsr effect_job
 inc frame
 rts
music_job:
 inc music_tick
 lda music_tick
 sta $c000
 rts
graphics_job:
 lda frame
 and #7
 sta gfx_state
 sta $c010
 rts
effect_job:
 lda frame
 lsr
 lsr
 and #15
 sta effect_state
 sta $c020
 rts
