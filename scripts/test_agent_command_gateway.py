from __future__ import annotations

import urllib.parse
import unittest

from scripts.agent_command_gateway import (
    GatewayError,
    add_issue_comment,
    build_ticket_body,
    complete_ticket,
    create_ticket,
    execute_operation,
    start_ticket,
    validate_command,
    verify_command_commit,
)

REPO = "bkloppers/power-app-learning-project"


def gate_issue(number: int = 12, gate_id: str = "PH03-G01", phase: str = "PH03") -> dict:
    return {
        "number": number,
        "state": "open",
        "title": f"[GATE][{gate_id}] Gate",
        "body": f"### Gate ID\n`{gate_id}`\n\n### Gate Decision\n`NOT DECIDED`\n",
        "labels": [{"name": "type:gate"}, {"name": f"phase:{phase}"}, {"name": f"gate:{gate_id}"}],
    }


def ticket_issue(number: int = 20, ticket_id: str = "PH03-G01-T01", status: str = "READY", checked: bool = True) -> dict:
    mark = "x" if checked else " "
    return {
        "number": number,
        "state": "open",
        "title": f"[{ticket_id}][BUILD] Test",
        "body": (
            f"### Ticket ID\n`{ticket_id}`\n\nStatus: `{status}`\n\n"
            f"### Acceptance Criteria\n- [{mark}] Criterion\n\n"
            "### Evidence\n- `project-management/phases/PH03/evidence/test.md`\n"
        ),
        "labels": [
            {"name": "phase:PH03"}, {"name": "gate:PH03-G01"},
            {"name": "type:build"}, {"name": "status:" + status.lower().replace(" ", "-")},
        ],
    }


class FakeClient:
    def __init__(self, issues=None, contents=None):
        self.issues = {item["number"]: item for item in (issues or [])}
        self.contents = set(contents or [])
        self.comments = {}
        self.labels = set()
        self.next_issue = max(self.issues.keys(), default=30) + 1
        self.next_comment = 1000
        self.commit_fixture = {"parents": [{"sha": "parent"}], "files": [{"filename": "agent-commands/inbox/test-command.json", "status": "added"}]}

    def content_exists(self, path, ref="main"):
        return path in self.contents

    def request(self, method, path, payload=None):
        if method == "GET" and path.startswith("/labels/"):
            name = urllib.parse.unquote(path.split("/labels/", 1)[1])
            if name not in self.labels:
                raise GatewayError("GitHub API GET failed: 404 missing")
            return {"name": name}
        if method == "POST" and path == "/labels":
            self.labels.add(payload["name"])
            return payload
        if method == "GET" and path.startswith("/commits/"):
            return self.commit_fixture
        if method == "GET" and path.startswith("/issues?"):
            query = urllib.parse.parse_qs(path.split("?", 1)[1])
            state = query.get("state", ["open"])[0]
            labels = set(query.get("labels", [""])[0].split(",")) - {""}
            result = []
            for item in self.issues.values():
                if state != "all" and item["state"] != state:
                    continue
                names = {x["name"] for x in item.get("labels", [])}
                if labels and not labels.issubset(names):
                    continue
                result.append(item)
            return result
        if method == "POST" and path == "/issues":
            issue = {"number": self.next_issue, "state": "open", "html_url": f"https://example/{self.next_issue}", **payload}
            issue["labels"] = [{"name": x} for x in payload.get("labels", [])]
            self.issues[self.next_issue] = issue
            self.next_issue += 1
            return issue
        match = __import__("re").match(r"/issues/(\d+)(?:/comments)?(?:\?.*)?$", path)
        if match:
            number = int(match.group(1))
            if "/comments" in path:
                if method == "GET":
                    return self.comments.get(number, [])
                if method == "POST":
                    item = {"id": self.next_comment, "body": payload["body"]}
                    self.next_comment += 1
                    self.comments.setdefault(number, []).append(item)
                    return item
            if method == "GET":
                return self.issues[number]
            if method == "PATCH":
                issue = self.issues[number]
                issue.update(payload)
                if "labels" in payload:
                    issue["labels"] = [{"name": x} for x in payload["labels"]]
                return issue
        raise AssertionError(f"Unexpected fake request: {method} {path}")


def create_ticket_command(status="NOT STARTED"):
    return {
        "schemaVersion": 1,
        "commandId": "20260827-PH03-G01-T01",
        "operation": "create_ticket",
        "repository": REPO,
        "ticket": {
            "id": "PH03-G01-T01", "phase": "PH03", "gate": "PH03-G01",
            "type": "build", "status": status, "priority": "normal",
            "title": "Create governed application object", "points": 2,
            "workstream": "02 - Application Foundation", "dependencies": ["No ticket dependency"],
            "selectedSolution": "Create only the approved app object.",
            "acceptanceCriteria": ["App object exists."],
            "evidence": ["project-management/phases/PH03/evidence/test.md"],
        },
    }


class GatewayHardeningTests(unittest.TestCase):
    def test_valid_create_ticket(self):
        validate_command(create_ticket_command(), REPO)

    def test_ticket_body_contains_canonical_ticket_id(self):
        body = build_ticket_body(create_ticket_command()["ticket"], "20260827-PH03-G01-T01")
        self.assertIn("### Ticket ID\n`PH03-G01-T01`", body)

    def test_lifecycle_ticket_id_is_mandatory(self):
        command = {"schemaVersion": 1, "commandId": "20260827-start-001", "operation": "start_ticket", "repository": REPO, "issueNumber": 20}
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)

    def test_complete_rejects_wrong_phase_evidence(self):
        command = {"schemaVersion": 1, "commandId": "20260827-complete-001", "operation": "complete_ticket", "repository": REPO, "issueNumber": 20, "ticketId": "PH03-G01-T01", "evidencePaths": ["project-management/phases/PH01/evidence/old.md"]}
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)

    def test_create_ticket_rejects_duplicate(self):
        client = FakeClient([gate_issue(), ticket_issue()])
        with self.assertRaises(GatewayError):
            create_ticket(client, create_ticket_command())

    def test_create_ticket_rejects_missing_parent_gate(self):
        client = FakeClient([])
        with self.assertRaises(GatewayError):
            create_ticket(client, create_ticket_command())

    def test_start_ready_ticket(self):
        issue = ticket_issue()
        client = FakeClient([gate_issue(), issue])
        result = start_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-start-001"})
        self.assertEqual(result["targetAfterStatus"], "IN PROGRESS")
        self.assertIn("Gateway-Command-ID: 20260827-start-001", client.issues[20]["body"])

    def test_start_rejects_not_started(self):
        client = FakeClient([gate_issue(), ticket_issue(status="NOT STARTED")])
        with self.assertRaises(GatewayError):
            start_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-start-002"})

    def test_start_rejects_wrong_ticket_id(self):
        client = FakeClient([gate_issue(), ticket_issue()])
        with self.assertRaises(GatewayError):
            start_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T99", "commandId": "20260827-start-003"})

    def test_start_rejects_second_in_progress_ticket(self):
        other = ticket_issue(number=21, ticket_id="PH03-G01-T02", status="IN PROGRESS")
        client = FakeClient([gate_issue(), ticket_issue(), other])
        with self.assertRaises(GatewayError):
            start_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-start-004"})

    def test_complete_ticket_closes_with_declared_evidence(self):
        client = FakeClient([gate_issue(), ticket_issue(status="IN PROGRESS")], {"project-management/phases/PH03/evidence/test.md"})
        result = complete_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-complete-002", "evidencePaths": ["project-management/phases/PH03/evidence/test.md"]})
        self.assertTrue(result["closed"])
        self.assertEqual(client.issues[20]["state"], "closed")

    def test_complete_rejects_undeclared_evidence(self):
        client = FakeClient([gate_issue(), ticket_issue(status="IN PROGRESS")], {"project-management/phases/PH03/evidence/other.md"})
        with self.assertRaises(GatewayError):
            complete_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-complete-003", "evidencePaths": ["project-management/phases/PH03/evidence/other.md"]})

    def test_complete_rejects_unchecked_criteria(self):
        client = FakeClient([gate_issue(), ticket_issue(status="IN PROGRESS", checked=False)], {"project-management/phases/PH03/evidence/test.md"})
        with self.assertRaises(GatewayError):
            complete_ticket(client, {"issueNumber": 20, "ticketId": "PH03-G01-T01", "commandId": "20260827-complete-004", "evidencePaths": ["project-management/phases/PH03/evidence/test.md"]})

    def test_command_commit_rejects_multiple_files(self):
        client = FakeClient()
        client.commit_fixture["files"].append({"filename": "README.md", "status": "modified"})
        with self.assertRaises(GatewayError):
            verify_command_commit(client, "sha", "agent-command-gateway")

    def test_command_commit_rejects_modified_inbox_file(self):
        client = FakeClient()
        client.commit_fixture["files"][0]["status"] = "modified"
        with self.assertRaises(GatewayError):
            verify_command_commit(client, "sha", "agent-command-gateway")

    def test_command_commit_rejects_merge_commit(self):
        client = FakeClient()
        client.commit_fixture["parents"].append({"sha": "second"})
        with self.assertRaises(GatewayError):
            verify_command_commit(client, "sha", "agent-command-gateway")

    def test_command_commit_rejects_wrong_branch(self):
        with self.assertRaises(GatewayError):
            verify_command_commit(FakeClient(), "sha", "main")

    def test_comment_recovery_prevents_duplicate_mutation(self):
        client = FakeClient([gate_issue()])
        command = {"schemaVersion": 1, "commandId": "20260827-comment-001", "operation": "add_issue_comment", "repository": REPO, "issueNumber": 12, "comment": "smoke"}
        first = add_issue_comment(client, command)
        second = execute_operation(client, command)
        self.assertEqual(first["commentId"], second["commentId"])
        self.assertTrue(second["recovered"])
        self.assertEqual(len(client.comments[12]), 1)

    def test_rejects_wrong_repository(self):
        command = {"schemaVersion": 1, "commandId": "20260827-comment-002", "operation": "add_issue_comment", "repository": "other/repo", "issueNumber": 1, "comment": "test"}
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)

    def test_rejects_arbitrary_operation(self):
        command = {"schemaVersion": 1, "commandId": "20260827-run-shell", "operation": "run", "repository": REPO, "issueNumber": 1}
        with self.assertRaises(GatewayError):
            validate_command(command, REPO)


if __name__ == "__main__":
    unittest.main()
