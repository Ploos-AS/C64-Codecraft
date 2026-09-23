phase=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx phase
 lda sintab,x
 sta $d000
 inc phase
 lda phase
 and #15
 sta phase
 rts
sintab:
 .byte 80,91,101,109,112,109,101,91
 .byte 80,69,59,51,48,51,59,69
