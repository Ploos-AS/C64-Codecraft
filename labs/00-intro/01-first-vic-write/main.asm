; C64 Codecraft — Lab 00.01
; First direct VIC-II write
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
    lda #$06        ; blue
    sta $d020       ; border

    lda #$0e        ; light blue
    sta $d021       ; background

    rts
