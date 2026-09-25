# Editorial and benchmark methodology

## Evidence states

`candidate` means a useful primary reference proposed for review. `reviewed` means a named maintainer has checked URL, scope, capability, maintenance, license and a runnable starting point. `measured` requires a pinned workload, baseline, hardware, raw results, failure cases, uncertainty and an independent replay. `production_reference` additionally requires a consenting operator and permission to cite its deployment. The initial catalog contains only candidates; none has earned the latter states.

The catalog stores this state per reference. Promotion requires the metadata listed in [CONTRIBUTING.md](../CONTRIBUTING.md); a public benchmark record is required for `measured`, and explicit citation permission for `production_reference`. A machine check establishes field completeness, while human review establishes credibility.

## Benchmark contract

Each future benchmark record must include `protocol`, `upstream_version`, `dataset_hash`, `split`, `baseline`, `candidate`, `hardware`, `metric_formula`, `denominator`, `confidence_interval`, `excluded_cases`, `total_cost`, `failure_modes`, `source_rights`, and `reviewer`. Hard failures (unauthorized access, scope leaks, unsafe physical action, unsupported claim) are reported separately and cannot be averaged away. Compare identical tasks and budgets; never compare percentages across incompatible leaderboards.

The ten list-specific benchmark dimensions are **questions to test**, not current measurements. A cross-domain evaluation should name a real composition boundary—for example A2A task → identity decision → Iceberg snapshot → OTLP receipt—and measure the whole outcome as well as each component. See [Swarm-Context-Commander's protocol lab](https://github.com/AAH20/Swarm-Context-Commander/blob/main/docs/protocol-interoperability-lab.md) for one explicitly synthetic starting fixture.

## Editorial independence

The portfolio owner may nominate their own projects. The same rubric applies, ownership is disclosed, and neutral list ordering is alphabetical within kind rather than sponsorship or popularity. Paid placement is not accepted. External contributors must not be required to join a commercial service. Do not scrape proprietary data, copy another list's descriptions, or present a vendor's benchmark claim as an independently reproduced result.

## Evolution parameters

Track per domain: reviewed references; median link age and maintenance age; proposals received; accepted/declined PRs and reasons; distinct external contributors; references with reproducible commands; references with independent benchmark artifacts; broken-link rate; and qualified referrals to original sources. A growing item count alone is a poor measure. Reassess a domain when its scope becomes too broad, its links decay, or contributors cannot explain why a new item belongs.

For the system of systems, track cross-domain case studies completed, interface failures discovered, external reproductions, and how often readers successfully locate a relevant standard or benchmark. Use an opt-in, privacy-conscious analytics method if a website is added; GitHub alone does not expose every conversion metric.
