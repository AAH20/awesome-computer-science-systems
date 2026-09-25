# Internet Routing and Network Protocols

**Core question:** How do independent networks preserve reachability without trusting every announcement?

**Claim boundary:** References are for read-only analysis and offline simulation, not live route control.

## Evaluation axes

- Origin-validation coverage
- False route rejection
- Convergence time
- Incident detection delay
- Affected prefixes

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [BGP-4 RFC 4271](https://www.rfc-editor.org/info/rfc4271/) | standard | candidate | Defines inter-autonomous-system reachability exchange. |
| [RPKI Origin Validation RFC 6811](https://www.rfc-editor.org/info/rfc6811/) | standard | candidate | Defines origin-validation behavior for BGP routes. |
| [FRRouting](https://github.com/FRRouting/frr) | tool | candidate | Offers an inspectable routing implementation for controlled labs. |
| [RIPE Atlas](https://atlas.ripe.net/) | measurement | candidate | Provides a public platform for Internet reachability measurement. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
