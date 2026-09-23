frame=$fb
music_tick=$fc
phase=$fd
part=$fe
TARGET=$e0
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
leave:
 lda $d012
 cmp #TARGET
 beq leave
wait:
 lda $d012
 cmp #TARGET
 bne wait
 jsr music_play
 jsr update
 jsr render
 rts
music_play:
 inc music_tick
 rts
update:
 inc frame
 inc phase
 lda phase
 and #15
 sta phase
 lda frame
 cmp #32
 bne keep
 lda #0
 sta frame
 lda part
 eor #1
 sta part
keep:
 rts
render:
 ldx phase
 lda sintab,x
 clc
 adc music_tick
 and #15
 tay
 lda colours,y
 sta $d020
 lda part
 beq done
 lda colours+1,y
 sta $d021
done:
 rts
sintab:
 .byte 0,1,2,3,4,5,6,7,7,7,6,5,4,3,2,1
colours:
 .byte 0,6,14,3,1,3,14,6,0,11,12,15,1,15,12,11,0
