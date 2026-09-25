"""Validate and render the ten independent reference lists from one catalog."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "catalog/domains.json"
OUTPUT = ROOT / "lists"
KINDS = {"standard", "method", "tool", "benchmark", "measurement"}
STATES = {"candidate", "reviewed", "measured", "production_reference"}
EXPECTED_IDS = (
    "algorithms-formal-methods",
    "distributed-systems",
    "internet-network-protocols",
    "identity-cryptography-pqc",
    "databases-graphs-bi",
    "statistics-ml-causality",
    "agents-memory-graphrag",
    "cloud-hpc-inference",
    "robotics-control-twins",
    "hci-human-command",
)


def validate(data: dict) -> None:
    if data.get("schema_version") != "cs-systems-atlas/v2":
        raise ValueError("unexpected catalog schema")
    domains = data.get("domains")
    if not isinstance(domains, list) or tuple(item.get("id") for item in domains) != EXPECTED_IDS:
        raise ValueError("exactly ten ordered domains are required")
    seen = set()
    for domain in domains:
        for field in ("title", "question", "boundary"):
            if not isinstance(domain.get(field), str) or len(domain[field]) < 12:
                raise ValueError(f"{domain['id']}: missing {field}")
        metrics = domain.get("benchmark_dimensions")
        if not isinstance(metrics, list) or len(metrics) < 4 or len(metrics) != len(set(metrics)):
            raise ValueError(f"{domain['id']}: needs distinct benchmark dimensions")
        refs = domain.get("references")
        if not isinstance(refs, list) or len(refs) < 4:
            raise ValueError(f"{domain['id']}: needs at least four references")
        for ref in refs:
            state = ref.get("status")
            if state not in STATES:
                raise ValueError(f"{domain['id']}: invalid reference status")
            if ref.get("kind") not in KINDS or not isinstance(ref.get("why"), str) or len(ref["why"]) < 25:
                raise ValueError(f"{domain['id']}: incomplete reference annotation")
            if state != "candidate":
                required = ("reviewer", "reviewed_on", "suitable_workload", "limitations",
                            "maintenance_evidence", "license_or_terms", "starting_point")
                if any(not isinstance(ref.get(field), str) or not ref[field].strip() for field in required):
                    raise ValueError(f"{domain['id']}: reviewed reference lacks evidence fields")
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ref["reviewed_on"]):
                    raise ValueError(f"{domain['id']}: invalid review date")
            if state in {"measured", "production_reference"} and not ref.get("benchmark_record"):
                raise ValueError(f"{domain['id']}: measured reference lacks benchmark record")
            if state == "production_reference" and not ref.get("deployment_permission"):
                raise ValueError(f"{domain['id']}: production reference lacks citation permission")
            name, url = ref.get("name"), ref.get("url")
            if not isinstance(name, str) or not 2 <= len(name) <= 80 or not isinstance(url, str):
                raise ValueError(f"{domain['id']}: invalid reference name or URL")
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                raise ValueError(f"{domain['id']}: reference must have a public HTTPS URL")
            key = url.rstrip("/").lower()
            if key in seen:
                raise ValueError(f"duplicate reference URL: {url}")
            seen.add(key)
            if re.search(r"github\.com/AAH20/", url, re.I):
                raise ValueError("maintainer projects belong in the separate portfolio map")


def render(domain: dict) -> str:
    lines = [f"# {domain['title']}", "", f"**Core question:** {domain['question']}", "",
             f"**Claim boundary:** {domain['boundary']}", "", "## Evaluation axes", ""]
    lines.extend(f"- {metric.capitalize()}" for metric in domain["benchmark_dimensions"])
    lines += ["", "## References", "",
              "The initial entries are candidates pending human editorial review. Status distinguishes scope review from reproduced measurement; inclusion alone is not an endorsement.", "",
              "| Reference | Kind | Status | Why it belongs in this scope |", "| --- | --- | --- | --- |"]
    for ref in domain["references"]:
        lines.append(f"| [{ref['name']}]({ref['url']}) | {ref['kind']} | {ref['status']} | {ref['why']} |")
    reviewed = [ref for ref in domain["references"] if ref["status"] != "candidate"]
    if reviewed:
        lines += ["", "## Reviewed reference notes", ""]
        for ref in reviewed:
            lines += [f"### {ref['name']}", "", f"- Suitable workload: {ref['suitable_workload']}",
                      f"- Limitations: {ref['limitations']}",
                      f"- License or terms: {ref['license_or_terms']}",
                      f"- Maintenance evidence: {ref['maintenance_evidence']}",
                      f"- Starting point: {ref['starting_point']}",
                      f"- Reviewed by {ref['reviewer']} on {ref['reviewed_on']}."]
            if ref.get("benchmark_record"):
                lines.append(f"- Benchmark record: {ref['benchmark_record']}")
            lines.append("")
    lines += ["", "## Contribute", "",
              "Submit a reproducible benchmark, a primary standard, or a distinct implementation through the [contribution guide](../CONTRIBUTING.md). Explain the evaluation gap it fills. Maintainer-owned projects are disclosed separately in the [portfolio map](../docs/portfolio-map.md).", ""]
    return "\n".join(lines)


def build(*, check: bool = False) -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    validate(data)
    OUTPUT.mkdir(exist_ok=True)
    expected = {}
    for domain in data["domains"]:
        path = OUTPUT / f"{domain['id']}.md"
        expected[path] = render(domain)
    stale = [path for path, content in expected.items()
             if not path.exists() or path.read_text(encoding="utf-8") != content]
    extra = sorted(set(OUTPUT.glob("*.md")) - set(expected))
    if check:
        if stale or extra:
            raise ValueError(f"generated lists out of date: {[str(p.name) for p in stale + extra]}")
        return
    for path in extra:
        path.unlink()
    for path, content in expected.items():
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build(check=args.check)
