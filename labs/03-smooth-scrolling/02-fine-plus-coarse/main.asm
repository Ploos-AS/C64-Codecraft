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
 lda phase
 sec
 sbc #1
 and #7
 sta phase
 pha
 lda $d016
 and #$f8
 sta $d016
 pla
 ora $d016
 sta $d016
 lda phase
 cmp #7
 bne done
 ldx #0
shift:
 lda $0401,x
 sta $0400,x
 inx
 cpx #39
 bne shift
 lda #1
 sta $0427
done:
 rts
