frame=$fb
cue=$fc
part_state=$fd
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
 sta cue
 sta part_state
 jsr cue_update
 jsr part_update
 jsr part_render
 rts
cue_update:
 inc frame
 lda frame
 and #$0f
 bne no_cue
 inc cue
no_cue:
 rts
part_update:
 lda cue
 cmp part_state
 beq unchanged
 sta part_state
unchanged:
 rts
part_render:
 lda part_state
 and #15
 sta $d020
 rts
