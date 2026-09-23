# OCI qualification

## Alpine qualification result

Alpine 3.22 was tested first, in accordance with the Ploos Alpine-first policy.

**Result: FAIL as the practical C64 Codecraft base.**

The GitHub Actions qualification run showed that the Alpine 3.22 repositories used by the image do not provide the core course packages:

- 64tass
- ACME
- cc65
- VICE

The full image additionally lacked Exomizer.

These are not peripheral dependencies: they are the real assemblers/emulator/scene tools the course intends to teach directly. Building and maintaining a parallel source-packaging layer merely to preserve an Alpine base would add project-specific infrastructure around tools that should remain the focus.

Therefore C64 Codecraft uses the documented fallback: **Debian slim**.

This is a maintainability decision, not a change to the ASM-first/toolbox architecture.

## Debian qualification result

**Result: PASS for the M0 OCI/toolchain gates.**

GitHub Actions confirmed that both the minimal and full Debian 13 slim toolboxes build, internal diagnostics run, and the canonical 64tass example assembles to a non-empty PRG inside the minimal toolbox.

The Debian 13 slim toolbox includes:

- 64tass
- ACME
- cc65/ca65
- VICE
- Java runtime for later KickAssembler integration
- Python and Make

The full toolbox adds broader build utilities. Exomizer remains outside the M0 base until a clean reproducible packaging path is qualified.

## Gates

1. Both Debian OCI definitions build.
2. Internal tool diagnostics confirm the expected native tools.
3. The canonical 64tass smoke program assembles inside the minimal image.
4. VICE is present before emulator automation is enabled.
5. KickAssembler is added only with a reproducible, license-compatible acquisition mechanism.
6. A deterministic VICE runtime smoke test passes.

Passing image build alone does not complete M0.
