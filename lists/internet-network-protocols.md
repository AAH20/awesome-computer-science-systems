# Internet Routing and Network Protocols

**Core question:** How do independent networks preserve reachability without trusting every announcement?

**Claim boundary:** References are for read-only analysis and offline simulation, not live route control.

## Evaluation axes

- Origin-validation coverage
- False route rejection
- Convergence time
- Incident detection delay
- Affected prefixes

## Candidate references

These are starting references, pending human editorial review. Inclusion is not an endorsement or benchmark result.

| Reference | Kind | Why it belongs in this scope |
| --- | --- | --- |
| [BGP-4 RFC 4271](https://www.rfc-editor.org/info/rfc4271/) | standard | Defines inter-autonomous-system reachability exchange. |
| [RPKI Origin Validation RFC 6811](https://www.rfc-editor.org/info/rfc6811/) | standard | Defines origin-validation behavior for BGP routes. |
| [FRRouting](https://github.com/FRRouting/frr) | tool | Offers an inspectable routing implementation for controlled labs. |
| [RIPE Atlas](https://atlas.ripe.net/) | measurement | Provides a public platform for Internet reachability measurement. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
