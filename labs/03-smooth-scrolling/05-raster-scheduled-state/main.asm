phase=$fb
TARGET=$e0
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
 lda phase
 sec
 sbc #1
 and #7
 sta phase
 tax
 lda $d016
 and #$f8
 sta $d016
 txa
 ora $d016
 sta $d016
 rts
