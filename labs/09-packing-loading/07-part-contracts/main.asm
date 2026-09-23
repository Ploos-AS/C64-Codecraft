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
 lda part_contracts,x
 sta $c000,x
 inx
 cpx #16
 bne copy
 rts
; load, entry, workspace start, workspace end
part_contracts:
 .word $4000,$4000,$4000,$5fff
 .word $6000,$6000,$6000,$7fff
