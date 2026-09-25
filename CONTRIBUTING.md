# Contributing

Open a focused PR against one domain. Explain the reference's primary purpose, why it fits that domain rather than another, what you personally inspected, and one falsifiable evaluation question. Link to the original project or standard; write your own short description. Include license and maintenance status in the PR body. For a benchmark, provide a pinned workload and reproducible result instead of a marketing number.

Edit `catalog/domains.json`, then run:

```bash
python3 scripts/build_lists.py
python3 scripts/build_lists.py --check
python3 -m unittest discover -s tests -v
```

The initial catalog is a set of candidates. A merged PR confirms that the entry meets this repository's formatting and scope rules; the `reviewed` or `measured` status needs a separate documented human review. Each record has a `status` field. To promote a reference to `reviewed`, record a named `reviewer`, ISO `reviewed_on` date, `suitable_workload`, `limitations`, `maintenance_evidence`, `license_or_terms`, and a `starting_point` a reader can actually use. `measured` additionally requires a `benchmark_record` pointing to a reproducible result; `production_reference` also needs `deployment_permission`. A machine-valid record does not substitute for editorial approval.

Maintainer-owned projects must be disclosed and use the same standard. No paid placement, referral codes, copied descriptions or unverifiable superlatives. Security issues should be reported privately rather than placed in an ordinary PR.
