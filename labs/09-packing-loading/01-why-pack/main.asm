*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda payload
 sta $c000
 rts
payload:
 .fill 256,$55
 .fill 256,$aa
payload_end:
