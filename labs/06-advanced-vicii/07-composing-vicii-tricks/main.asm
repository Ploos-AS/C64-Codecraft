event_index=$fb
*=$0801
.word e
.word 10
.byte $9e
.text "2064"
.byte 0
e:.word 0
*=$0810
start:
 lda #0
 sta event_index
next:
 ldx event_index
 lda event_lines,x
 sta $c000,x
 lda event_jobs,x
 sta $c010,x
 lda event_budget,x
 sta $c020,x
 inc event_index
 lda event_index
 cmp #4
 bne next
 rts
event_lines:
 .byte $40,$70,$a0,$d0
event_jobs:
 .byte 1,2,3,4
event_budget:
 .byte 1,3,2,4
