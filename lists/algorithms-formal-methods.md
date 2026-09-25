# Algorithms and Formal Methods

**Core question:** Can a system prove or falsify its safety, consistency and complexity claims?

**Claim boundary:** A solver result is limited to its model, assumptions and bounded state space.

## Evaluation axes

- Invariant coverage
- Counterexample discovery
- Solver runtime
- Specification-to-implementation fidelity

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [TLA+](https://foundation.tlapl.us/) | method | candidate | Specify state machines and inspect concurrency invariants. |
| [Alloy](https://alloytools.org/) | method | candidate | Explore relational models and bounded counterexamples. |
| [Z3](https://github.com/Z3Prover/z3) | tool | candidate | Test satisfiability and constraints with a maintained SMT solver. |
| [Lean](https://lean-lang.org/) | tool | candidate | Build machine-checked proofs with explicit assumptions. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
