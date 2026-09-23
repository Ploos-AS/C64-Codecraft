*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda effect_table
 sta $d020
 rts
*=$c000
effect_table:
 .byte 0,6,14,3,1,3,14,6
*=$2000
sprite_data:
 .fill 63,$18
 .byte 0
