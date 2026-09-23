; C64 Codecraft — Lab 00.02
; Table-driven colour loop
;
; BASIC: 10 SYS 2064

* = $0801
.word basic_end
.word 10
.byte $9e
.text "2064"
.byte 0
basic_end:
.word 0

* = $0810
start:
    ldx #$00
loop:
    lda colours,x
    sta $d800,x
    inx
    cpx #$10
    bne loop
    rts

colours:
    .byte $00,$01,$02,$03,$04,$05,$06,$07
    .byte $08,$09,$0a,$0b,$0c,$0d,$0e,$0f
