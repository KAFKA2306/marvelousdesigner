#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/instructor/cohort-manifest.yaml"
KPI = ROOT / "metrics/instructor-cohort-kpi.json"
REQUIRED_FILES = [
    ROOT / "docs/instructor/index.md",
    ROOT / "docs/instructor/lessons.md",
    ROOT / "docs/instructor/submission-template.md",
    ROOT / "docs/instructor/rubric.md",
    ROOT / "docs/instructor/demo.md",
]
REQUIRED_LESSON_KEYS = {"id", "file", "submission"}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    manifest_path = root / MANIFEST.relative_to(ROOT)
    kpi_path = root / KPI.relative_to(ROOT)

    for path in [root / p.relative_to(ROOT) for p in REQUIRED_FILES] + [manifest_path, kpi_path]:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(root)}")

    if errors:
        return errors

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "instructor-cohort.v1":
        errors.append("unexpected manifest schema_version")
    if manifest.get("status") not in {"PREVIEW", "PILOT", "RELEASED"}:
        errors.append("invalid manifest status")

    lessons = manifest.get("lessons")
    if not isinstance(lessons, list) or len(lessons) != 4:
        errors.append("manifest must contain exactly four lessons")
    else:
        ids: set[str] = set()
        for lesson in lessons:
            if not isinstance(lesson, dict) or not REQUIRED_LESSON_KEYS.issubset(lesson):
                errors.append("each lesson requires id, file, and submission")
                continue
            if lesson["id"] in ids:
                errors.append(f"duplicate lesson id: {lesson['id']}")
            ids.add(lesson["id"])
            if not (root / "docs/instructor" / lesson["file"]).is_file():
                errors.append(f"lesson file does not exist: {lesson['file']}")

    software = manifest.get("software", {})
    unity = software.get("unity", {})
    if unity.get("baseline") != "2022.3.22f1":
        errors.append("Unity baseline must be the verified VRChat-supported 2022.3.22f1")
    if unity.get("exact_version_policy") != "MUST_MATCH_BASELINE":
        errors.append("Unity exact-version policy must fail closed")
    if unity.get("source") != "https://creators.vrchat.com/sdk/upgrade/current-unity-version/":
        errors.append("Unity baseline must retain the VRChat primary-source URL")

    rights = manifest.get("rights", {})
    if rights.get("redistributed_commercial_assets") is not False:
        errors.append("commercial asset redistribution must remain false")
    if rights.get("redistributed_avatars") is not False:
        errors.append("avatar redistribution must remain false")
    if rights.get("learner_must_hold_asset_rights") is not True:
        errors.append("learner asset-rights responsibility must be explicit")

    commercial = manifest.get("commercial_evidence", {})
    for field in ("paid_cohorts", "learners", "completed_cohorts"):
        value = commercial.get(field)
        if not isinstance(value, int) or value < 0:
            errors.append(f"commercial_evidence.{field} must be a non-negative integer")
    if commercial.get("evidence") != [] and not isinstance(commercial.get("evidence"), list):
        errors.append("commercial evidence must be a list")
    if any(commercial.get(field, 0) > 0 for field in ("paid_cohorts", "learners", "completed_cohorts")) and not commercial.get("evidence"):
        errors.append("non-zero commercial claims require evidence")

    kpi = json.loads(kpi_path.read_text(encoding="utf-8"))
    if kpi.get("schema_version") != "instructor-cohort-kpi.v1":
        errors.append("unexpected KPI schema_version")
    metrics = kpi.get("metrics", {})
    observed = [v for v in metrics.values() if isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0]
    if observed and not kpi.get("evidence"):
        errors.append("non-zero KPI values require evidence")
    if kpi.get("status") == "NOT_STARTED" and (observed or kpi.get("evidence")):
        errors.append("NOT_STARTED KPI ledger cannot contain observed results")

    rubric = (root / "docs/instructor/rubric.md").read_text(encoding="utf-8")
    for assertion_type in (
        "VendorDocumentedFact",
        "ExperimentalObservation",
        "Instruction",
        "CalculatedValue",
        "AestheticJudgment",
        "CompatibilityClaim",
    ):
        if assertion_type not in rubric:
            errors.append(f"rubric missing evidence type: {assertion_type}")
    if "PASS / REVISE / NOT_TESTED" not in rubric:
        errors.append("rubric must retain the three-state grading boundary")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Instructor pack contract: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
