.PHONY: help doctor example docs-check publication-manifest site

help:
	@echo "C64 Codecraft M0"
	@echo "  make doctor                inspect toolchain"
	@echo "  make example               assemble M0 smoke example"
	@echo "  make docs-check            validate canonical NO/EN course sources"
	@echo "  make publication-manifest  emit deterministic source manifest"\n\t@echo "  make site                  build GitHub Pages output"

doctor:
	sh tools/c64cc doctor

example:
	mkdir -p build
	64tass --cbm-prg -o build/hello.prg examples/hello-64tass/main.asm

docs-check:
	python3 tools/publish.py check

publication-manifest:
	python3 tools/publish.py manifest

site:
	python3 tools/publish.py site
