; C64 Codecraft Lab 00.05
ptr = $fb

*=$0801
.word basic_end
.word 10
.byte $9e
.text "2064"
.byte 0
basic_end: .word 0

*=$0810
start:
    lda #<$0400
    sta ptr
    lda #>$0400
    sta ptr+1
    ldy #0
loop:
    lda fill_value
    sta (ptr),y
    iny
    cpy #16
    bne loop
    rts

fill_value:
    .byte 1
