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
 lda asset_bitmap,x
 sta $2000,x
 lda asset_screen,x
 sta $0400,x
 inx
 cpx #8
 bne copy
 rts
asset_bitmap:
 .byte $18,$3c,$7e,$ff,$ff,$7e,$3c,$18
asset_screen:
 .byte $16,$26,$36,$46,$56,$66,$76,$86
