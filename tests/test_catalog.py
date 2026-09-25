import copy
import json
import unittest

from scripts.build_lists import EXPECTED_IDS, SOURCE, build, validate


class CatalogTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_ten_distinct_domains_and_forty_initial_references(self):
        validate(self.data)
        self.assertEqual(tuple(domain["id"] for domain in self.data["domains"]), EXPECTED_IDS)
        self.assertEqual(sum(len(domain["references"]) for domain in self.data["domains"]), 40)
        self.assertEqual(self.data["editorial_status"], "candidate_references_pending_human_review")

    def test_generated_pages_are_current(self):
        build(check=True)

    def test_rejects_maintainer_self_placement(self):
        altered = copy.deepcopy(self.data)
        altered["domains"][0]["references"][0]["url"] = "https://github.com/AAH20/Swarm-Context-Commander"
        with self.assertRaisesRegex(ValueError, "maintainer projects"):
            validate(altered)

    def test_rejects_duplicate_and_insecure_urls(self):
        duplicate = copy.deepcopy(self.data)
        duplicate["domains"][1]["references"][0]["url"] = duplicate["domains"][0]["references"][0]["url"]
        with self.assertRaisesRegex(ValueError, "duplicate reference"):
            validate(duplicate)
        insecure = copy.deepcopy(self.data)
        insecure["domains"][0]["references"][0]["url"] = "http://example.com"
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            validate(insecure)

    def test_review_status_requires_human_evidence(self):
        altered = copy.deepcopy(self.data)
        altered["domains"][0]["references"][0]["status"] = "reviewed"
        with self.assertRaisesRegex(ValueError, "lacks evidence fields"):
            validate(altered)

    def test_measured_status_requires_benchmark_record(self):
        altered = copy.deepcopy(self.data)
        ref = altered["domains"][0]["references"][0]
        ref.update(status="measured", reviewer="Test reviewer", reviewed_on="2026-09-25",
                   suitable_workload="Synthetic invariant checking", limitations="Bounded model only",
                   maintenance_evidence="Current project release", license_or_terms="See source",
                   starting_point="Pinned example")
        with self.assertRaisesRegex(ValueError, "lacks benchmark record"):
            validate(altered)


if __name__ == "__main__":
    unittest.main()
