; C64 Codecraft Lab 00.06
src = $fb

*=$0801
.word basic_end
.word 10
.byte $9e
.text "2064"
.byte 0
basic_end: .word 0

*=$0810
start:
    lda #<message
    sta src
    lda #>message
    sta src+1
    ldy #0
loop:
    lda (src),y
    sta $0400,y
    iny
    cpy #16
    bne loop
    rts

; Screen codes: A..P
message:
    .byte 1,2,3,4,5,6,7,8
    .byte 9,10,11,12,13,14,15,16
