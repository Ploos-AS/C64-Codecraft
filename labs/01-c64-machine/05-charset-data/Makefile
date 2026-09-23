ASM ?= 64tass
VICE ?= x64sc
BUILD := build
PRG := $(BUILD)/charset-data.prg
.PHONY: all run clean
all: $(PRG)
$(PRG): main.asm
	mkdir -p $(BUILD)
	$(ASM) --cbm-prg -o $@ $<
run: $(PRG)
	$(VICE) -autostart $(PRG)
clean:
	rm -rf $(BUILD)
