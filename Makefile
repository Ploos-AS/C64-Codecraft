.PHONY: help doctor example

help:
	@echo "C64 Codecraft M0"
	@echo "  make doctor   inspect toolchain"
	@echo "  make example  assemble M0 smoke example"

doctor:
	sh tools/c64cc doctor

example:
	mkdir -p build
	64tass --cbm-prg -o build/hello.prg examples/hello-64tass/main.asm
