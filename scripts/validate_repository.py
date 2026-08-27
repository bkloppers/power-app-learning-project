from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def validate_required_structure() -> None:
    required_files = [
        ROOT / "project-management" / "control" / "PROJECT-CONTROL.md",
        ROOT / "project-management" / "control" / "AI-PROJECT-CONTINUITY-FLOW.md",
        ROOT / "project-management" / "governance" / "GITHUB-OPERATIONAL-CONTROL-STANDARD.md",
        ROOT / "project-management" / "governance" / "PROCESS-AND-PROGRESS-FRAMEWORK.md",
        ROOT / "project-management" / "governance" / "GATE-TRACKING-MODEL.md",
        ROOT / "project-management" / "governance" / "CHAT-SESSION-TICKET-CAPACITY-MODEL.md",
        ROOT / "project-management" / "governance" / "PHASE-FOLDER-STANDARD.md",
        ROOT / "project-management" / "planning" / "PROJECT-OPERATIONAL-DELIVERY-PLAN.md",
        ROOT / "project-management" / "registers" / "DECISIONS.md",
        ROOT / "project-management" / "registers" / "ISSUES.md",
        ROOT / "project-management" / "registers" / "APPROVALS.md",
        ROOT / "docs" / "standards" / "POWER-APPS-FUTURE-FIRST-STANDARD.md",
    ]
    for path in required_files:
        if not path.exists():
            error(f"Missing canonical repository file: {path.relative_to(ROOT)}")

    deprecated_files = [
        "project-management/PROJECT-CONTROL.md",
        "project-management/AI-PROJECT-CONTINUITY-FLOW.md",
        "project-management/GITHUB-OPERATIONAL-CONTROL-STANDARD.md",
        "project-management/PROCESS-AND-PROGRESS-FRAMEWORK.md",
        "project-management/GATE-TRACKING-MODEL.md",
        "project-management/CHAT-SESSION-TICKET-CAPACITY-MODEL.md",
        "project-management/PHASE-FOLDER-STANDARD.md",
        "project-management/PROJECT-OPERATIONAL-DELIVERY-PLAN.md",
        "project-management/DECISIONS.md",
        "project-management/ISSUES.md",
        "project-management/APPROVALS.md",
        "project-management/POWER-APPS-FUTURE-FIRST-STANDARD.md",
    ]
    for relative in deprecated_files:
        path = ROOT / relative
        if path.exists():
            error(f"Deprecated pre-reorganization path still exists: {relative}")


def validate_phase_structure() -> None:
    phases = ROOT / "project-management" / "phases"
    if not phases.exists():
        error("Missing project-management/phases directory")
        return

    for phase_dir in sorted(p for p in phases.iterdir() if p.is_dir()):
        if not re.fullmatch(r"PH\d{2}", phase_dir.name):
            error(f"Invalid phase folder name: {phase_dir.relative_to(ROOT)}")
            continue
        number = phase_dir.name[2:]
        expected = phase_dir / f"PHASE-{number}.md"
        if not expected.exists():
            error(f"Missing phase definition: {expected.relative_to(ROOT)}")

    deprecated = ROOT / "project-management" / "evidence"
    if deprecated.exists():
        error("Deprecated shared project-management/evidence directory exists; phase evidence must live under project-management/phases/PHxx/evidence")


def validate_id_headings(path: Path, prefix: str) -> None:
    if not path.exists():
        error(f"Missing {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    ids = re.findall(rf"^##\s+({prefix}-\d{{3}})\s*$", text, flags=re.MULTILINE)
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in ids:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    if duplicates:
        error(f"Duplicate {prefix} headings in {path.relative_to(ROOT)}: {', '.join(sorted(duplicates))}")


def validate_pr_body() -> None:
    body = os.environ.get("PR_BODY", "").strip()
    if not body:
        return
    required = [
        "## Scope",
        "## Selected Solution",
        "## Dependencies",
        "## Validation",
        "## Evidence",
        "## Unresolved Items",
        "## Project Control Impact",
    ]
    missing = [heading for heading in required if heading not in body]
    if missing:
        error("PR body is missing required sections: " + ", ".join(missing))

    placeholders = [
        "**Ticket ID / Governance scope:**\n\n",
        "**Phase / Gate:**\n\n",
        "Describe exactly one selected solution implemented by this PR.",
        "Describe the validation performed against the ticket/gate acceptance criteria and applicable standards.",
        "List canonical repository evidence paths produced or updated by this PR.",
        "State the required `PROJECT-CONTROL.md` change, or explain why no snapshot change is required.",
    ]
    remaining = [p for p in placeholders if p in body]
    if remaining:
        error("PR template still contains uncompleted required placeholders")


def main() -> int:
    validate_required_structure()
    validate_phase_structure()
    validate_id_headings(ROOT / "project-management" / "registers" / "DECISIONS.md", "DEC")
    validate_id_headings(ROOT / "project-management" / "registers" / "ISSUES.md", "ISS")
    validate_pr_body()

    if ERRORS:
        print("Repository integrity validation failed:")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print("Repository integrity validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
