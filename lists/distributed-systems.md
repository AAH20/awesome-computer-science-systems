# Distributed Systems and Consensus

**Core question:** What remains correct when nodes fail, partitions occur and clocks disagree?

**Claim boundary:** A single-node throughput result says nothing about distributed correctness.

## Evaluation axes

- Linearizability
- Recovery time
- Availability under partitions
- P99 latency
- State divergence

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [etcd](https://github.com/etcd-io/etcd) | tool | candidate | Study a production-oriented distributed key-value control plane. |
| [FoundationDB](https://github.com/apple/foundationdb) | tool | candidate | Examine transactional storage and fault-injection testing. |
| [Jepsen](https://jepsen.io/) | benchmark | candidate | Investigate observable consistency under failures. |
| [NATS](https://github.com/nats-io/nats-server) | tool | candidate | Compare messaging semantics and operational recovery. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
