from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

from scripts.validate_instructor_pack import ROOT, validate


class InstructorPackContractTests(unittest.TestCase):
    def make_fixture(self) -> Path:
        temp = Path(tempfile.mkdtemp())
        for relative in (
            "docs/instructor/index.md",
            "docs/instructor/lessons.md",
            "docs/instructor/submission-template.md",
            "docs/instructor/rubric.md",
            "docs/instructor/demo.md",
            "docs/instructor/cohort-manifest.yaml",
            "metrics/instructor-cohort-kpi.json",
        ):
            src = ROOT / relative
            dst = temp / relative
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        self.addCleanup(shutil.rmtree, temp)
        return temp

    def test_repository_contract_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_nonzero_commercial_claim_without_evidence_fails(self) -> None:
        root = self.make_fixture()
        path = root / "docs/instructor/cohort-manifest.yaml"
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifest["commercial_evidence"]["paid_cohorts"] = 1
        path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
        self.assertTrue(any("require evidence" in error for error in validate(root)))

    def test_wrong_unity_version_fails(self) -> None:
        root = self.make_fixture()
        path = root / "docs/instructor/cohort-manifest.yaml"
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifest["software"]["unity"]["baseline"] = "latest"
        path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
        self.assertTrue(any("Unity baseline" in error for error in validate(root)))

    def test_not_started_kpi_cannot_claim_results(self) -> None:
        root = self.make_fixture()
        path = root / "metrics/instructor-cohort-kpi.json"
        kpi = json.loads(path.read_text(encoding="utf-8"))
        kpi["metrics"]["instructor_demos"] = 1
        path.write_text(json.dumps(kpi), encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("require evidence" in error for error in errors))
        self.assertTrue(any("NOT_STARTED" in error for error in errors))

    def test_instructor_inquiry_collects_minimum_public_context(self) -> None:
        index = (ROOT / "docs/instructor/index.md").read_text(encoding="utf-8")
        marker = "[Instructor Cohort Packについて相談する]("
        start = index.index(marker) + len(marker)
        end = index.index(")", start)
        url = index[start:end]
        parsed = urlparse(url)
        self.assertEqual(parsed.scheme, "https")
        self.assertEqual(parsed.netloc, "github.com")
        self.assertEqual(parsed.path, "/KAFKA2306/marvelousdesigner/issues/new")
        query = parse_qs(parsed.query)
        self.assertIn("Instructor Cohort Pack PoC相談", query["title"][0])
        body = query["body"][0]
        for field in (
            "対象受講者",
            "予定人数",
            "開催時期",
            "授業回数",
            "利用予定software/version",
            "相談内容",
        ):
            self.assertIn(field, body)
        for warning in ("個人情報", "認証情報", "ライセンスID", "非公開の契約条件"):
            self.assertIn(warning, body)
        self.assertIn("アカデミックライセンス購入ガイドライン", index)
        self.assertIn("support.marvelousdesigner.com", index)


if __name__ == "__main__":
    unittest.main()
