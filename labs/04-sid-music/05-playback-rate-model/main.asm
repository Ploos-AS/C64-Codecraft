frame=$fb
tick=$fc
policy=$fd
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 inc frame
 lda policy
 beq every_frame
 lda frame
 and #1
 bne done
every_frame:
 inc tick
done:
 rts
