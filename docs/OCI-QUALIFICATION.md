# OCI qualification

## M0 candidate: Alpine Linux

C64 Codecraft follows an Alpine-first policy, but the base image is accepted only after CI proves that the required course toolchain is practical and maintainable.

The first qualification candidate includes:

- 64tass
- ACME
- cc65/ca65
- VICE
- Java runtime for the later KickAssembler integration
- Python and Make

The full candidate additionally carries broader build/scene utilities.

## Gates

1. Both OCI definitions build.
2. `c64cc doctor` can inspect the installed toolchain.
3. The canonical 64tass smoke program assembles inside the minimal image.
4. VICE is present before emulator automation is enabled.
5. KickAssembler is added only with a reproducible, license-compatible acquisition mechanism.
6. If Alpine fails due to package availability or upstream compatibility, document the failure and qualify Debian slim rather than patching around it indefinitely.

Passing image build alone does not complete M0. A deterministic VICE smoke test remains a separate gate.
