*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr event0
 jsr event1
 jsr event2
 rts
event0:
 lda #2
 sta $d020
 rts
event1:
 lda #5
 sta $d020
 rts
event2:
 lda #0
 sta $d020
 rts
schedule:
 .byte $40
 .word event0
 .byte $80
 .word event1
 .byte $c0
 .word event2
