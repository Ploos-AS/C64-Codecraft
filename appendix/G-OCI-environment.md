# Appendix G — OCI reference environment

The Codecraft OCI environment is a reproducible toolbox, not a programming framework.

## Image roles
- `c64-codecraft`: minimal reference build/test environment.
- `c64-codecraft-full`: broader tool environment when dependencies are qualified.

Alpine is the preferred Ploos OCI base where practical. Codecraft qualification found the required packaged C64 toolchain insufficient there, so Debian slim is the practical fallback for this project.

## Current principle
Only document tools as bundled when the image actually installs and CI qualifies them. Host-native GUI applications can remain outside the container.

## Use
The same source should remain understandable without OCI: the container packages ordinary tools and versions so builds are easier to reproduce.

## Troubleshooting
When a container build differs from a native build, compare assembler/tool versions, file paths, generated assets and emulator/ROM assumptions before adding project-specific workarounds.
