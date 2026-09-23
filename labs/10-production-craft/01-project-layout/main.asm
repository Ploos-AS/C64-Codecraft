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
 jsr part_run
 rts
part_init:
 lda #0
 sta $d020
 rts
part_run:
 lda #6
 sta $d021
 rts
