# Databases, Knowledge Graphs and Business Intelligence

**Core question:** Can decisions be reproduced from fresh, permissioned and traceable data?

**Claim boundary:** Fast retrieval is not evidence that a source is correct or licensed.

## Evaluation axes

- Snapshot reproducibility
- Query p95
- Schema compatibility
- Lineage coverage
- Cost per accepted analysis

## Candidate references

These are starting references, pending human editorial review. Inclusion is not an endorsement or benchmark result.

| Reference | Kind | Why it belongs in this scope |
| --- | --- | --- |
| [Apache Iceberg](https://iceberg.apache.org/spec/) | standard | Defines versioned analytical table snapshots and evolution. |
| [Apache Arrow Flight](https://arrow.apache.org/docs/format/Flight.html) | standard | Defines high-throughput transport for Arrow data services. |
| [DuckDB](https://duckdb.org/docs/) | tool | Makes local analytical reproduction accessible. |
| [Apache Superset](https://superset.apache.org/) | tool | Offers inspectable data exploration and BI interfaces. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
