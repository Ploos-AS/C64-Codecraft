# KickAssembler qualification policy

KickAssembler is a first-class supported assembler in C64 Codecraft, but its binary is not committed to this repository.

## Rules

1. The upstream `kickass.jar` remains external to the repository.
2. CI must never download an unversioned or unverified "latest" binary.
3. A qualified KickAssembler release is recorded with an explicit version, upstream source URL and SHA-256 digest.
4. The full OCI image may consume the JAR only through an explicit build input or a separately maintained acquisition step whose redistribution terms have been reviewed.
5. Until those three provenance fields are recorded and verified, KickAssembler examples are source-qualified but the binary toolchain gate remains pending.
6. Codecraft's canonical beginner baseline remains 64tass. KickAssembler-specific features are taught as assembler-specific features, not as C64 fundamentals.

## Invocation contract

The upstream manual documents the normal command-line form:

```text
java -jar kickass.jar source.asm
```

For qualification, Codecraft additionally requires an explicit output path and compares the resulting PRG against the canonical M0 smoke program.

## Why this is deliberately strict

Reproducibility means more than "Java is installed". A build that silently fetches a mutable external JAR cannot prove which assembler produced the result. Codecraft therefore keeps the example and the binary qualification as separate gates.
