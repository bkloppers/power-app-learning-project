from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
COMMAND_BRANCH = "agent-command-gateway"
COMMAND_PATH_RE = re.compile(r"^agent-commands/inbox/[A-Za-z0-9._-]+\.json$")
COMMAND_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{7,127}$")
TICKET_ID_RE = re.compile(r"^PH\d{2}-G\d{2}-T\d{2}$")
GATE_ID_RE = re.compile(r"^PH\d{2}-G\d{2}$")
PHASE_ID_RE = re.compile(r"^PH\d{2}$")
STATUS_TO_LABEL = {
    "NOT STARTED": "status:not-started",
    "READY": "status:ready",
    "IN PROGRESS": "status:in-progress",
    "BLOCKED": "status:blocked",
    "VALIDATION": "status:validation",
    "COMPLETE": "status:complete",
}
TYPE_LABELS = {
    "design", "doc", "build", "data", "security", "automation", "ai",
    "test", "alm", "validate", "gate", "bug", "decision",
}
PRIORITY_LABELS = {"high", "normal", "low"}
LABEL_COLORS = {
    "phase": "c4fac6",
    "gate": "748056",
    "type": "0a4dcd",
    "status:not-started": "321219",
    "status:ready": "fce56a",
    "status:in-progress": "25e77c",
    "status:blocked": "d93f0b",
    "status:validation": "fbca04",
    "status:complete": "aee79f",
    "priority:high": "d93f0b",
    "priority:normal": "0e8a16",
    "priority:low": "c5def5",
}
ALLOWED_OPERATIONS = {
    "create_gate",
    "create_ticket",
    "start_ticket",
    "complete_ticket",
    "add_issue_comment",
}


class GatewayError(RuntimeError):
    pass


@dataclass(frozen=True)
class GitHubClient:
    repository: str
    token: str

    @property
    def api_root(self) -> str:
        return f"https://api.github.com/repos/{self.repository}"

    def request(self, method: str, path: str, payload: Any | None = None) -> Any:
        url = path if path.startswith("https://") else f"{self.api_root}{path}"
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=data, method=method)
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self.token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "power-app-learning-agent-command-gateway")
        if data is not None:
            request.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read()
                return None if not body else json.loads(body.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise GatewayError(f"GitHub API {method} {url} failed: {exc.code} {detail}") from exc

    def get_content_text(self, path: str, ref: str) -> str:
        encoded_path = urllib.parse.quote(path, safe="/")
        result = self.request("GET", f"/contents/{encoded_path}?ref={urllib.parse.quote(ref, safe='')}")
        if not isinstance(result, dict) or result.get("encoding") != "base64":
            raise GatewayError(f"Expected base64 file content for {path}@{ref}")
        return base64.b64decode(result["content"]).decode("utf-8")

    def content_exists(self, path: str, ref: str = "main") -> bool:
        encoded_path = urllib.parse.quote(path, safe="/")
        url = f"{self.api_root}/contents/{encoded_path}?ref={urllib.parse.quote(ref, safe='')}"
        request = urllib.request.Request(url, method="GET")
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("Authorization", f"Bearer {self.token}")
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        request.add_header("User-Agent", "power-app-learning-agent-command-gateway")
        try:
            with urllib.request.urlopen(request, timeout=30):
                return True
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return False
            detail = exc.read().decode("utf-8", errors="replace")
            raise GatewayError(f"GitHub API content check failed: {exc.code} {detail}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GatewayError(message)


def require_string(value: Any, field: str, *, max_len: int = 5000) -> str:
    require(isinstance(value, str), f"{field} must be a string")
    result = value.strip()
    require(bool(result), f"{field} must not be blank")
    require(len(result) <= max_len, f"{field} exceeds {max_len} characters")
    return result


def require_string_list(value: Any, field: str, *, allow_empty: bool = True) -> list[str]:
    require(isinstance(value, list), f"{field} must be an array")
    if not allow_empty:
        require(bool(value), f"{field} must contain at least one item")
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(require_string(item, f"{field}[{index}]", max_len=1000))
    return result


def validate_envelope(command: dict[str, Any], expected_repository: str) -> None:
    require(command.get("schemaVersion") == SCHEMA_VERSION, "Unsupported schemaVersion")
    command_id = require_string(command.get("commandId"), "commandId", max_len=128)
    require(bool(COMMAND_ID_RE.fullmatch(command_id)), "Invalid commandId format")
    operation = require_string(command.get("operation"), "operation", max_len=64)
    require(operation in ALLOWED_OPERATIONS, f"Operation is not allow-listed: {operation}")
    repository = require_string(command.get("repository"), "repository", max_len=200)
    require(repository == expected_repository, "Command repository does not match workflow repository")


def validate_gate_payload(command: dict[str, Any]) -> None:
    gate = command.get("gate")
    require(isinstance(gate, dict), "gate must be an object")
    gate_id = require_string(gate.get("id"), "gate.id", max_len=16)
    phase = require_string(gate.get("phase"), "gate.phase", max_len=8)
    require(bool(GATE_ID_RE.fullmatch(gate_id)), "gate.id must match PHxx-Gxx")
    require(bool(PHASE_ID_RE.fullmatch(phase)), "gate.phase must match PHxx")
    require(gate_id.startswith(phase + "-"), "gate.id must belong to gate.phase")
    require_string(gate.get("title"), "gate.title", max_len=180)
    require_string(gate.get("objective"), "gate.objective")
    require_string_list(gate.get("entryCriteria"), "gate.entryCriteria", allow_empty=False)
    require_string_list(gate.get("requiredTickets"), "gate.requiredTickets", allow_empty=False)
    require_string_list(gate.get("requiredEvidence"), "gate.requiredEvidence", allow_empty=False)
    require_string_list(gate.get("acceptanceCriteria"), "gate.acceptanceCriteria", allow_empty=False)


def validate_ticket_payload(command: dict[str, Any]) -> None:
    ticket = command.get("ticket")
    require(isinstance(ticket, dict), "ticket must be an object")
    ticket_id = require_string(ticket.get("id"), "ticket.id", max_len=20)
    phase = require_string(ticket.get("phase"), "ticket.phase", max_len=8)
    gate = require_string(ticket.get("gate"), "ticket.gate", max_len=16)
    ticket_type = require_string(ticket.get("type"), "ticket.type", max_len=32).lower()
    status = require_string(ticket.get("status"), "ticket.status", max_len=32).upper()
    priority = require_string(ticket.get("priority", "normal"), "ticket.priority", max_len=16).lower()
    require(bool(TICKET_ID_RE.fullmatch(ticket_id)), "ticket.id must match PHxx-Gxx-Txx")
    require(bool(PHASE_ID_RE.fullmatch(phase)), "ticket.phase must match PHxx")
    require(bool(GATE_ID_RE.fullmatch(gate)), "ticket.gate must match PHxx-Gxx")
    require(ticket_id.startswith(gate + "-"), "ticket.id must belong to ticket.gate")
    require(gate.startswith(phase + "-"), "ticket.gate must belong to ticket.phase")
    require(ticket_type in TYPE_LABELS - {"gate"}, "ticket.type is not a canonical type")
    require(status in {"NOT STARTED", "READY"}, "New tickets may only start as NOT STARTED or READY")
    require(priority in PRIORITY_LABELS, "ticket.priority must be high, normal, or low")
    points = ticket.get("points")
    require(isinstance(points, int) and 1 <= points <= 5, "ticket.points must be an integer from 1 to 5")
    require_string(ticket.get("title"), "ticket.title", max_len=180)
    require_string(ticket.get("workstream"), "ticket.workstream", max_len=200)
    require_string_list(ticket.get("dependencies"), "ticket.dependencies", allow_empty=False)
    require_string(ticket.get("selectedSolution"), "ticket.selectedSolution")
    require_string_list(ticket.get("acceptanceCriteria"), "ticket.acceptanceCriteria", allow_empty=False)
    require_string_list(ticket.get("evidence"), "ticket.evidence", allow_empty=False)


def validate_issue_operation(command: dict[str, Any]) -> None:
    issue_number = command.get("issueNumber")
    require(isinstance(issue_number, int) and issue_number > 0, "issueNumber must be a positive integer")
    ticket_id = command.get("ticketId")
    if ticket_id is not None:
        ticket_id = require_string(ticket_id, "ticketId", max_len=20)
        require(bool(TICKET_ID_RE.fullmatch(ticket_id)), "ticketId must match PHxx-Gxx-Txx")
    if command["operation"] == "complete_ticket":
        paths = require_string_list(command.get("evidencePaths"), "evidencePaths", allow_empty=False)
        for path in paths:
            require(path.startswith("project-management/phases/"), "Evidence must be phase-owned")
            require("/evidence/" in path, "evidencePaths must point inside a phase evidence folder")
    if command["operation"] == "add_issue_comment":
        require_string(command.get("comment"), "comment", max_len=20000)


def validate_command(command: dict[str, Any], expected_repository: str) -> None:
    validate_envelope(command, expected_repository)
    operation = command["operation"]
    if operation == "create_gate":
        validate_gate_payload(command)
    elif operation == "create_ticket":
        validate_ticket_payload(command)
    else:
        validate_issue_operation(command)


def canonical_label_color(label: str) -> str:
    if label.startswith("phase:"):
        return LABEL_COLORS["phase"]
    if label.startswith("gate:"):
        return LABEL_COLORS["gate"]
    if label.startswith("type:"):
        return LABEL_COLORS["type"]
    return LABEL_COLORS.get(label, "ededed")


def ensure_label(client: GitHubClient, label: str) -> None:
    encoded = urllib.parse.quote(label, safe="")
    try:
        client.request("GET", f"/labels/{encoded}")
        return
    except GatewayError as exc:
        if " 404 " not in str(exc):
            raise
    client.request(
        "POST",
        "/labels",
        {
            "name": label,
            "color": canonical_label_color(label),
            "description": "Managed by Agent Command Gateway",
        },
    )


def apply_status(client: GitHubClient, issue: dict[str, Any], new_status: str) -> None:
    body = issue.get("body") or ""
    updated_body, count = re.subn(
        r"(?m)^Status:\s*`(?:NOT STARTED|READY|IN PROGRESS|BLOCKED|VALIDATION|COMPLETE)`\s*$",
        f"Status: `{new_status}`",
        body,
        count=1,
    )
    require(count == 1, "Issue body does not contain exactly one canonical Status line")
    existing = [label["name"] for label in issue.get("labels", []) if isinstance(label, dict) and "name" in label]
    status_labels = set(STATUS_TO_LABEL.values())
    labels = [label for label in existing if label not in status_labels]
    status_label = STATUS_TO_LABEL[new_status]
    ensure_label(client, status_label)
    labels.append(status_label)
    client.request("PATCH", f"/issues/{issue['number']}", {"body": updated_body, "labels": labels})


def build_gate_body(gate: dict[str, Any]) -> str:
    def checklist(items: list[str]) -> str:
        return "\n".join(f"- [ ] {item}" for item in items)

    def bullets(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items)

    return (
        f"### Gate ID\n`{gate['id']}`\n\n"
        f"### Phase\n{gate['phase']}\n\n"
        f"### Objective\n{gate['objective'].strip()}\n\n"
        f"### Entry Criteria\n{checklist(gate['entryCriteria'])}\n\n"
        f"### Required Tickets\n{bullets(gate['requiredTickets'])}\n\n"
        f"### Required Evidence\n{bullets(gate['requiredEvidence'])}\n\n"
        f"### Acceptance Criteria\n{checklist(gate['acceptanceCriteria'])}\n\n"
        "### Gate Decision\n`NOT DECIDED`\n"
    )


def build_ticket_body(ticket: dict[str, Any]) -> str:
    dependencies = "\n".join(f"- {item}" for item in ticket["dependencies"])
    criteria = "\n".join(f"- [ ] {item}" for item in ticket["acceptanceCriteria"])
    evidence = "\n".join(f"- `{item}`" for item in ticket["evidence"])
    return (
        f"Status: `{ticket['status'].upper()}`\n"
        f"Points: {ticket['points']}\n"
        f"Workstream: `{ticket['workstream']}`\n\n"
        f"### Dependencies\n{dependencies}\n\n"
        f"### Selected Solution\n{ticket['selectedSolution'].strip()}\n\n"
        f"### Acceptance Criteria\n{criteria}\n\n"
        f"### Evidence\n{evidence}\n"
    )


def create_gate(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    gate = command["gate"]
    labels = [f"phase:{gate['phase']}", f"gate:{gate['id']}", "type:gate", "status:not-started"]
    for label in labels:
        ensure_label(client, label)
    return client.request(
        "POST",
        "/issues",
        {
            "title": f"[GATE][{gate['id']}] {gate['title'].strip()}",
            "body": build_gate_body(gate),
            "labels": labels,
        },
    )


def create_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    ticket = command["ticket"]
    status = ticket["status"].upper()
    ticket_type = ticket["type"].lower()
    priority = ticket.get("priority", "normal").lower()
    labels = [
        f"phase:{ticket['phase']}",
        f"gate:{ticket['gate']}",
        f"type:{ticket_type}",
        STATUS_TO_LABEL[status],
        f"priority:{priority}",
    ]
    for label in labels:
        ensure_label(client, label)
    gate_short = ticket["gate"].split("-")[-1]
    return client.request(
        "POST",
        "/issues",
        {
            "title": f"[{ticket['phase']}][{gate_short}][{ticket_type.upper()}] {ticket['title'].strip()}",
            "body": build_ticket_body(ticket),
            "labels": labels,
        },
    )


def fetch_issue(client: GitHubClient, issue_number: int) -> dict[str, Any]:
    issue = client.request("GET", f"/issues/{issue_number}")
    require(isinstance(issue, dict) and "pull_request" not in issue, "Target must be a GitHub Issue, not a Pull Request")
    return issue


def assert_ticket_identity(issue: dict[str, Any], ticket_id: str | None) -> None:
    if ticket_id:
        require(ticket_id in issue.get("title", "") or ticket_id in (issue.get("body") or ""), "ticketId does not match target Issue")


def issue_status(issue: dict[str, Any]) -> str:
    match = re.search(r"(?m)^Status:\s*`([^`]+)`\s*$", issue.get("body") or "")
    require(match is not None, "Target Issue has no canonical Status line")
    return match.group(1).strip().upper()


def start_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    assert_ticket_identity(issue, command.get("ticketId"))
    require(issue.get("state") == "open", "Ticket must be open")
    require(issue_status(issue) == "READY", "Only a READY ticket may move to IN PROGRESS")
    gate_labels = [label["name"] for label in issue.get("labels", []) if label.get("name", "").startswith("gate:")]
    require(len(gate_labels) == 1, "Ticket must have exactly one gate label")
    query = urllib.parse.urlencode({"state": "open", "labels": f"{gate_labels[0]},status:in-progress", "per_page": 100})
    active = client.request("GET", f"/issues?{query}")
    conflicting = [item for item in active if item.get("number") != issue["number"] and "pull_request" not in item]
    require(not conflicting, f"Another ticket is already IN PROGRESS for {gate_labels[0]}")
    apply_status(client, issue, "IN PROGRESS")
    return {"issueNumber": issue["number"], "status": "IN PROGRESS"}


def complete_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    assert_ticket_identity(issue, command.get("ticketId"))
    require(issue.get("state") == "open", "Ticket must be open")
    require(issue_status(issue) in {"IN PROGRESS", "VALIDATION"}, "Ticket must be IN PROGRESS or VALIDATION before completion")
    body = issue.get("body") or ""
    acceptance_section = body.split("### Acceptance Criteria", 1)
    require(len(acceptance_section) == 2, "Issue has no Acceptance Criteria section")
    acceptance_text = acceptance_section[1].split("### ", 1)[0]
    unchecked = re.findall(r"(?m)^\s*-\s*\[ \]\s+.+$", acceptance_text)
    checked = re.findall(r"(?m)^\s*-\s*\[[xX]\]\s+.+$", acceptance_text)
    require(bool(checked), "Acceptance Criteria section contains no checked criteria")
    require(not unchecked, "Acceptance Criteria still contain unchecked items")
    for path in command["evidencePaths"]:
        require(client.content_exists(path, "main"), f"Required evidence is missing from main: {path}")
    apply_status(client, issue, "COMPLETE")
    client.request("PATCH", f"/issues/{issue['number']}", {"state": "closed", "state_reason": "completed"})
    return {"issueNumber": issue["number"], "status": "COMPLETE", "closed": True}


def add_issue_comment(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    result = client.request("POST", f"/issues/{issue['number']}/comments", {"body": command["comment"].strip()})
    return {"issueNumber": issue["number"], "commentId": result.get("id")}


def execute_operation(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    operation = command["operation"]
    if operation == "create_gate":
        issue = create_gate(client, command)
        return {"issueNumber": issue.get("number"), "url": issue.get("html_url")}
    if operation == "create_ticket":
        issue = create_ticket(client, command)
        return {"issueNumber": issue.get("number"), "url": issue.get("html_url")}
    if operation == "start_ticket":
        return start_ticket(client, command)
    if operation == "complete_ticket":
        return complete_ticket(client, command)
    if operation == "add_issue_comment":
        return add_issue_comment(client, command)
    raise GatewayError(f"Unsupported operation: {operation}")


def verify_command_commit(client: GitHubClient, head_sha: str, expected_branch: str) -> str:
    require(expected_branch == COMMAND_BRANCH, f"Unexpected command branch: {expected_branch}")
    commit = client.request("GET", f"/commits/{head_sha}")
    require(len(commit.get("parents", [])) == 1, "Command push must resolve to a single-parent commit")
    files = commit.get("files", [])
    require(len(files) == 1, "A command commit must change exactly one file")
    item = files[0]
    path = item.get("filename", "")
    require(bool(COMMAND_PATH_RE.fullmatch(path)), "Command commit may only add one agent-commands/inbox/*.json file")
    require(item.get("status") == "added", "Command file must be newly added")
    return path


def result_path(command_id: str) -> str:
    return f"agent-commands/results/{command_id}.json"


def write_result(client: GitHubClient, command: dict[str, Any], status: str, detail: dict[str, Any]) -> None:
    path = result_path(command["commandId"])
    payload = {
        "schemaVersion": SCHEMA_VERSION,
        "commandId": command["commandId"],
        "operation": command["operation"],
        "status": status,
        "detail": detail,
    }
    body = {
        "message": f"GATEWAY: record {command['commandId']} {status.lower()}",
        "content": base64.b64encode((json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")).decode("ascii"),
        "branch": COMMAND_BRANCH,
    }
    client.request("PUT", f"/contents/{urllib.parse.quote(path, safe='/')}", body)


def run_execute(args: argparse.Namespace) -> int:
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    head_sha = os.environ.get("GATEWAY_HEAD_SHA", "").strip()
    head_branch = os.environ.get("GATEWAY_HEAD_BRANCH", "").strip()
    require(repository and token and head_sha and head_branch, "Required gateway workflow environment is missing")
    client = GitHubClient(repository=repository, token=token)
    path = verify_command_commit(client, head_sha, head_branch)
    command = json.loads(client.get_content_text(path, head_sha))
    require(isinstance(command, dict), "Command document must be a JSON object")
    validate_command(command, repository)
    if client.content_exists(result_path(command["commandId"]), COMMAND_BRANCH):
        print(f"Command {command['commandId']} already has a result; treating rerun as idempotent success.")
        return 0
    try:
        detail = execute_operation(client, command)
        write_result(client, command, "SUCCEEDED", detail)
        print(json.dumps({"status": "SUCCEEDED", "detail": detail}, indent=2))
        return 0
    except Exception as exc:
        try:
            write_result(client, command, "FAILED", {"error": str(exc)})
        except Exception as result_exc:
            print(f"Failed to write gateway failure result: {result_exc}", file=sys.stderr)
        raise


def run_validate_file(args: argparse.Namespace) -> int:
    path = Path(args.path)
    command = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(command, dict), "Command document must be a JSON object")
    validate_command(command, args.repository)
    print(f"Valid Agent Command Gateway v{SCHEMA_VERSION} command: {command['commandId']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agent Command Gateway validator and executor")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    execute = subparsers.add_parser("execute", help="Execute the command from a validated gateway workflow run")
    execute.set_defaults(func=run_execute)
    validate = subparsers.add_parser("validate-file", help="Validate one local command JSON file")
    validate.add_argument("path")
    validate.add_argument("--repository", required=True)
    validate.set_defaults(func=run_validate_file)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except (GatewayError, json.JSONDecodeError) as exc:
        print(f"Agent Command Gateway rejected request: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
