request=$fb
destlo=$fc
desthi=$fd
status=$fe
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #1
 sta request
 lda #<$4000
 sta destlo
 lda #>$4000
 sta desthi
 lda #0
 sta status
 jsr loader_model
 rts
loader_model:
 lda request
 beq done
 lda #1
 sta status
 lda #0
 sta request
done:
 rts
