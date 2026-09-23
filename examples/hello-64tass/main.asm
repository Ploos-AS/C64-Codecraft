; C64 Codecraft M0 smoke example
; 64tass syntax
;
; BASIC stub: 10 SYS 2064

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
    lda #$06
    sta $d020
    lda #$0e
    sta $d021
    rts
