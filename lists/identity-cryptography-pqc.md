# Identity, Privileged Access and Post-Quantum Cryptography

**Core question:** Who may act, how quickly can that authority be revoked, and can cryptography evolve safely?

**Claim boundary:** A policy engine does not replace authenticated identity or certified cryptographic modules.

## Evaluation axes

- False grants
- Revocation lag
- Policy-decision p99
- Blast radius
- Crypto migration interoperability

## Candidate references

These are starting references, pending human editorial review. Inclusion is not an endorsement or benchmark result.

| Reference | Kind | Why it belongs in this scope |
| --- | --- | --- |
| [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | standard | Frames resource-centered access decisions without implicit location trust. |
| [SPIFFE](https://spiffe.io/docs/latest/spiffe-specs/) | standard | Defines workload identity across heterogeneous systems. |
| [OpenBao](https://github.com/openbao/openbao) | tool | Provides an inspectable secrets-management implementation. |
| [NIST Post-Quantum Cryptography](https://www.nist.gov/pqc) | standard | Tracks finalized PQC algorithms and migration guidance. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
