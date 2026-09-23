ptr=$f8
phase=$fa
temp=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #<source
 sta ptr
 lda #>source
 sta ptr+1
 lda #0
 sta phase
 sta temp
 ldy #0
copy:
 lda (ptr),y
 sta $c000,y
 iny
 cpy #8
 bne copy
 inc phase
 lda phase
 sta temp
 rts
source:
 .byte 8,7,6,5,4,3,2,1
