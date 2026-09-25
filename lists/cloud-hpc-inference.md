# Cloud Infrastructure, HPC and AI Inference

**Core question:** What is the reliable cost of serving accepted work at real active load?

**Claim boundary:** Tokens per second alone do not capture task quality, GPU idle cost or human review.

## Evaluation axes

- Throughput
- Time to first token
- P99 latency
- Energy per accepted task
- Recovery time

## Candidate references

These are starting references, pending human editorial review. Inclusion is not an endorsement or benchmark result.

| Reference | Kind | Why it belongs in this scope |
| --- | --- | --- |
| [Kubernetes](https://kubernetes.io/docs/home/) | tool | Defines common container orchestration primitives. |
| [Ray](https://docs.ray.io/en/latest/) | tool | Supports distributed execution across ML and agent workloads. |
| [vLLM](https://docs.vllm.ai/) | tool | Offers a reference high-throughput model-serving engine. |
| [MLPerf Inference](https://mlcommons.org/benchmarks/inference-datacenter/) | benchmark | Provides a governed datacenter inference measurement suite. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
