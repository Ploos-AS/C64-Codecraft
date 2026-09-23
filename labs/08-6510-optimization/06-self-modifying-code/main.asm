*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #$0e
 sta patched_value+1
 jsr patched_value
 rts
patched_value:
 lda #$00
 sta $d020
 rts
