TARGET=$f0
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
leave:
 lda $d012
 cmp #TARGET
 beq leave
wait:
 lda $d012
 cmp #TARGET
 bne wait
 lda $d011
 sta $c000
 lda $d016
 sta $c001
 lda #5
 sta $d020
 nop
 nop
 nop
 lda #0
 sta $d020
 rts
