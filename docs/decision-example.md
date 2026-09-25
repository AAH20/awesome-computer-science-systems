# Decision example: a control-plane state store

**Question:** For a regional service scheduler, which state store better satisfies the team's *specified* correctness, recovery and operating-cost requirements: etcd or FoundationDB? This is a comparison protocol, not a published benchmark or recommendation. No runs have been performed for this atlas.

## Define the workload before choosing

The fictional scheduler has 10,000 workers. It stores worker leases, desired assignments and observed acknowledgements. Proposed test levels are 100, 1,000 and 10,000 active workers with read:write ratios of 10:1 and 1:1. The tester must record payload sizes, client count, topology, versions, hardware, storage, network, transaction boundaries and retry policy. These numbers are **test inputs**, not production observations.

The invariants are: no assignment is acknowledged by two owners at the same revision; a revoked worker cannot acquire new work after the defined revocation deadline; and an acknowledged assignment survives a permitted single-node failure. A crash, partition and client reconnect are injected separately. An operator must define acceptable recovery time and p99 latency *before* inspecting results.

| Candidate | Documented interface relevant to this question | What the experiment must establish |
| --- | --- | --- |
| [etcd](https://etcd.io/docs/v3.6/learning/api/) | Revisioned key-value API with linearizable reads by default, compare-and-swap transactions, leases and watch. | Whether leases, watch recovery and transaction limits match the scheduler's state model under the selected failure schedule. |
| [FoundationDB](https://apple.github.io/foundationdb/) | Ordered key-value store with ACID transactions; its [developer guide](https://apple.github.io/foundationdb/developer-guide.html) explains transaction and retry behavior. | Whether the required multi-key invariants, application-level lease mechanism and operational topology meet the same schedule and cost budget. |

These are different architectures. Feature names alone do not establish equivalence. The test harness must implement the **same application-level invariant and accepted outcome** for both candidates; adapter-specific behavior must be documented.

## Evidence to capture

1. Pin source version, configuration, adapter commit and workload generator commit. Archive the exact fixture, fault schedule and random seed.
2. Record accepted and rejected operations, invariant violations, retry counts, stale reads, p50/p95/p99 latency, recovery time, storage footprint and total infrastructure cost. Publish denominators and error bars; a throughput number alone is insufficient.
3. Replay the failure schedule and inspect raw logs for cases the aggregate metrics hide. Report all exclusions and operator interventions.
4. Have a second reviewer rerun the artifacts. Until that happens, label the result *vendor claim* or *local experiment*, not *independently reproduced*.

## Decision rule

Reject a candidate that violates a hard invariant or misses a precommitted recovery deadline. If both pass, compare cost per **accepted, correct assignment** at the required load, then account for operational complexity and migration risk. If neither passes, revise the application design or broaden the candidate set. Do not declare a winner based on stars, an unrelated benchmark, or one successful demo.

The protocol reflects the distinctions documented in the [etcd API](https://etcd.io/docs/v3.6/learning/api/) and [FoundationDB's simulation and testing guide](https://apple.github.io/foundationdb/testing.html). It does not claim either project passed this scenario.
