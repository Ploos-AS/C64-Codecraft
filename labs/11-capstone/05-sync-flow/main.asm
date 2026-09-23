tick=$fb
cue=$fc
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
 sta tick
 sta cue
 inc tick
 lda tick
 lsr
 lsr
 lsr
 lsr
 and #3
 sta cue
 tax
 lda cue_colours,x
 sta $d020
 rts
cue_colours:
 .byte 0,6,14,1
