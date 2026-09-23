*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 ldx #0
copy:
 lda regions,x
 sta $c000,x
 inx
 cpx #16
 bne copy
 rts
; start-lo,start-hi,end-lo,end-hi for four teaching regions
regions:
 .word $3000,$37ff
 .word $4000,$47ff
 .word $0800,$0fff
 .word $c000,$cfff
