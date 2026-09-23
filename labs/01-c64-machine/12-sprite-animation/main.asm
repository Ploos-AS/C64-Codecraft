frame=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda frame
 clc
 adc #$80
 sta $07f8
 inc frame
 lda frame
 cmp #3
 bne done
 lda #0
 sta frame
done:
 lda #1
 sta $d015
 rts
*=$2000
f0:.fill 63,$18
 .byte 0
f1:.fill 63,$3c
 .byte 0
f2:.fill 63,$7e
 .byte 0
