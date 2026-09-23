# Lab 09.02 — Reproducible packing contract

## Goal
Make packing a reproducible build step rather than a manual release ritual.

The starter remains buildable with the reference 64tass environment. Add a packer only after it is qualified and record:
- tool and exact version,
- command line,
- input artifact,
- output artifact,
- load/start assumptions,
- expected deterministic/non-deterministic properties.

Exomizer is scene-relevant but is **not currently bundled in the Codecraft OCI image**; do not silently make it a mandatory dependency.

**Why does a demo coder care?** A release should be rebuildable months later by someone other than its original author.
