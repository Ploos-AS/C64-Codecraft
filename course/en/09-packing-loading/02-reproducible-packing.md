---
title: Reproducible packing
course: 09-packing-loading
lesson: 02
level: advanced
prerequisites: [01-why-pack]
labs: [reproducible-packing]
---
# Reproducible packing
A build should record exactly how packed data was produced:
- source file and expected load/destination range;
- packer and version;
- command/options;
- output format;
- depacker assumptions;
- measured packed size.

A commonly used scene tool may be taught as one workflow, but Codecraft source and architecture must not depend on a proprietary wrapper around it. Alternative packers can be compared when they satisfy the same contract.

## Tool qualification
A tool belongs in the reference OCI image only after its redistribution/build story is qualified. Until then, document native installation or an external build step rather than claiming it is bundled.

## Lab
Add one deterministic packing recipe and verify that a clean environment reproduces the same unpacked payload.

## Next
We design depacking around memory safety.
