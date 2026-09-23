state=$fb
part=$fc
age=$fd
LOAD=0
INIT=1
RUN=2
EXIT=3
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #LOAD
 sta state
 lda #0
 sta part
 sta age
step=$0826
step:
 lda state
 cmp #LOAD
 beq do_load
 cmp #INIT
 beq do_init
 cmp #RUN
 beq do_run
 jmp do_exit
do_load:
 lda #INIT
 sta state
 rts
do_init:
 lda #0
 sta age
 lda #RUN
 sta state
 rts
do_run:
 inc age
 lda age
 cmp #16
 bne done
 lda #EXIT
 sta state
done:
 rts
do_exit:
 inc part
 lda part
 cmp #2
 bcs finished
 lda #LOAD
 sta state
finished:
 rts
