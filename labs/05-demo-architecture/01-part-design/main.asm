state=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr part_init
 jsr part_update
 jsr part_render
 jsr part_shutdown
 rts
part_init:
 lda #0
 sta state
 rts
part_update:
 inc state
 rts
part_render:
 lda state
 and #15
 sta $d020
 rts
part_shutdown:
 lda #0
 sta $d020
 rts
