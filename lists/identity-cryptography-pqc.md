# Identity, Privileged Access and Post-Quantum Cryptography

**Core question:** Who may act, how quickly can that authority be revoked, and can cryptography evolve safely?

**Claim boundary:** A policy engine does not replace authenticated identity or certified cryptographic modules.

## Evaluation axes

- False grants
- Revocation lag
- Policy-decision p99
- Blast radius
- Crypto migration interoperability

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | standard | candidate | Frames resource-centered access decisions without implicit location trust. |
| [SPIFFE](https://spiffe.io/docs/latest/spiffe-specs/) | standard | candidate | Defines workload identity across heterogeneous systems. |
| [OpenBao](https://github.com/openbao/openbao) | tool | candidate | Provides an inspectable secrets-management implementation. |
| [NIST Post-Quantum Cryptography](https://www.nist.gov/pqc) | standard | candidate | Tracks finalized PQC algorithms and migration guidance. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
