from __future__ import annotations

import unittest

from scripts.agent_command_gateway import GatewayError, validate_command

REPO = "bkloppers/power-app-learning-project"


class GatewayValidationTests(unittest.TestCase):
    def test_valid_create_ticket(self) -> None:
        command = {
            "schemaVersion": 1,
            "commandId": "20260827-PH03-G01-T01",
            "operation": "create_ticket",
            "repository": REPO,
            "ticket": {
                "id": "PH03-G01-T01",
                "phase": "PH03",
                "gate": "PH03-G01",
                "type": "build",
                "status": "READY",
                "priority": "normal",
                "title": "Create governed application object",
                "points": 2,
                "workstream": "02 - Application Foundation",
                "dependencies": ["PH02-G01 PASSED"],
                "selectedSolution": "Create only the approved app object inside the governed solution.",
                "acceptanceCriteria": ["App object exists in the governed solution."],
                "evidence": ["project-management/phases/PH03/evidence/example.md"],
            },
        }
        validate_command(command, REPO)

    def test_rejects_wrong_repository(self) -> None:
        command = {
            "schemaVersion": 1,
            "commandId": "20260827-comment-001",
            "operation": "add_issue_comment",
            "repository": "other/repo",
            "issueNumber": 1,
            "comment": "test",
        }
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)

    def test_rejects_arbitrary_operation(self) -> None:
        command = {
            "schemaVersion": 1,
            "commandId": "20260827-run-shell",
            "operation": "run",
            "repository": REPO,
            "issueNumber": 1,
        }
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)

    def test_complete_requires_phase_evidence(self) -> None:
        command = {
            "schemaVersion": 1,
            "commandId": "20260827-complete-001",
            "operation": "complete_ticket",
            "repository": REPO,
            "issueNumber": 99,
            "ticketId": "PH03-G01-T01",
            "evidencePaths": ["README.md"],
        }
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)


if __name__ == "__main__":
    unittest.main()
