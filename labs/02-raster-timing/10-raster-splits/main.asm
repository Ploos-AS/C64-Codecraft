SPLIT1=$60
SPLIT2=$c0
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #6
 sta $d020
 lda #0
 sta $d021
wait1:
 lda $d012
 cmp #SPLIT1
 bne wait1
 lda #14
 sta $d020
 lda #6
 sta $d021
wait2:
 lda $d012
 cmp #SPLIT2
 bne wait2
 lda #0
 sta $d020
 sta $d021
 rts
