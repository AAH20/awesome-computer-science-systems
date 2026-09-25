# Agent Protocols, Memory and GraphRAG

**Core question:** Can independent agents exchange tasks and use bounded, source-linked memory correctly?

**Claim boundary:** Logical agent registration is not active execution or upstream conformance.

## Evaluation axes

- Protocol conformance
- Grounded task success
- Retrieval recall
- Cancellation correctness
- Active-agent capacity

## References

The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.

| Reference | Kind | Status | Why it belongs in this scope |
| --- | --- | --- | --- |
| [A2A Protocol](https://a2a-protocol.org/latest/specification/) | standard | candidate | Defines interoperable agent discovery and task exchange. |
| [Model Context Protocol](https://modelcontextprotocol.io/specification) | standard | candidate | Defines interoperable tool and context interfaces. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | tool | candidate | Offers explicit graph-based workflow and state patterns. |
| [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2) | benchmark | candidate | Provides a long-history memory evaluation reference. |

## Contribute

Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).
