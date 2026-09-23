frame=$fb
sync=$fc
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 inc frame
 lda frame
 and #15
 sta $d020
 lda frame
 lsr
 lsr
 lsr
 sta sync
 sta $c000
 rts
