phase=$fb
age=$fc
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 jsr update
 jsr render
 rts
update:
 inc age
 lda age
 cmp #8
 bne done
 lda #0
 sta age
 inc phase
 lda phase
 cmp #3
 bcc done
 lda #2
 sta phase
done:
 rts
render:
 lda phase
 beq part_a
 cmp #1
 beq transition
 lda #6
 sta $d020
 rts
part_a:
 lda #2
 sta $d020
 rts
transition:
 lda age
 and #15
 sta $d020
 rts
