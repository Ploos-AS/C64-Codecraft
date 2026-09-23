# Appendix F — Packing, disk images and release tools

Packing and disk tooling belongs to the delivery pipeline, not the programming model.

## Packers
For every packer workflow record:
- tool/version;
- exact command/options;
- source/destination assumptions;
- depacker requirements;
- packed and unpacked size.

Exomizer is a relevant scene tool to evaluate, but Codecraft must not claim it is bundled in the reference OCI image until that installation/redistribution path is actually qualified.

## Disk images
Generate .d64 images from source/build recipes. Record file names/order where relevant and verify expected contents with suitable tooling.

## Release
Release artifacts should be generated from an identified source revision. Record hashes where practical. Keep proprietary ROMs and unlicensed third-party assets out of the repository.
