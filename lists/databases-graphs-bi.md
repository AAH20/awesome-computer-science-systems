# Databases, Knowledge Graphs and Business Intelligence

**Core question:** Can decisions be reproduced from fresh, permissioned and traceable data?

**Claim boundary:** Fast retrieval is not evidence that a source is correct or licensed.

## Evaluation axes

- Snapshot reproducibility
- Query p95
- Schema compatibility
- Lineage coverage
- Cost per accepted analysis

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [Apache Iceberg](https://iceberg.apache.org/spec/) | standard | candidate | Defines versioned analytical table snapshots and evolution. |
| [Apache Arrow Flight](https://arrow.apache.org/docs/format/Flight.html) | standard | candidate | Defines high-throughput transport for Arrow data services. |
| [DuckDB](https://duckdb.org/docs/) | tool | candidate | Makes local analytical reproduction accessible. |
| [Apache Superset](https://superset.apache.org/) | tool | candidate | Offers inspectable data exploration and BI interfaces. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
