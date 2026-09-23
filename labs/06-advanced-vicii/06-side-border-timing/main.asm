TARGET=$80
DELAY_COUNT=8
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
 ldx #DELAY_COUNT
delay_loop:
 dex
 bne delay_loop
 lda #7
 sta $d020
 nop
 nop
 lda #0
 sta $d020
 rts
