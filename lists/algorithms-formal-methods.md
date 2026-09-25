# Algorithms and Formal Methods

**Core question:** Can a system prove or falsify its safety, consistency and complexity claims?

**Claim boundary:** A solver result is limited to its model, assumptions and bounded state space.

## Evaluation axes

- Invariant coverage
- Counterexample discovery
- Solver runtime
- Specification-to-implementation fidelity

## Candidate references

These are starting references, pending human editorial review. Inclusion is not an endorsement or benchmark result.

| Reference | Kind | Why it belongs in this scope |
| --- | --- | --- |
| [TLA+](https://foundation.tlapl.us/) | method | Specify state machines and inspect concurrency invariants. |
| [Alloy](https://alloytools.org/) | method | Explore relational models and bounded counterexamples. |
| [Z3](https://github.com/Z3Prover/z3) | tool | Test satisfiability and constraints with a maintained SMT solver. |
| [Lean](https://lean-lang.org/) | tool | Build machine-checked proofs with explicit assumptions. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
