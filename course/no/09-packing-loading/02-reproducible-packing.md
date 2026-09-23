---
title: Reproducible packing
course: 09-packing-loading
lesson: 02
level: advanced
prerequisites: [01-hvorfor-pakke]
labs: [09.02-reproducible-packing]
---
# Reproducible packing
Et build skal dokumentere nøyaktig hvordan packed data ble produsert:
- source file og forventet load/destination range;
- packer og version;
- command/options;
- output format;
- depacker assumptions;
- målt packed size.

Et vanlig scene-tool kan læres som én workflow, men Codecraft source/architecture skal ikke avhenge av en proprietær wrapper rundt det. Alternative packers kan sammenlignes når de oppfyller samme contract.

## Tool qualification
Et tool hører hjemme i reference OCI-image først etter at redistribution/build-story er kvalifisert. Frem til da dokumenteres native install eller external build step i stedet for å påstå at det er bundled.

## Lab
Legg til én deterministic packing recipe og verifiser at clean environment reproduserer samme unpacked payload.

## Neste
Vi designer depacking rundt memory safety.
