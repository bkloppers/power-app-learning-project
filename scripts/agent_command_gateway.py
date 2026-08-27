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
from datetime import datetime, timezone
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

    def paginate(self, path: str, params: dict[str, Any] | None = None) -> list[Any]:
        """Return every item from a GitHub REST collection using page/per_page pagination."""
        base_params = dict(params or {})
        base_params.pop("page", None)
        base_params["per_page"] = 100
        items: list[Any] = []
        page = 1
        while True:
            page_params = {**base_params, "page": page}
            separator = "&" if "?" in path else "?"
            result = self.request("GET", f"{path}{separator}{urllib.parse.urlencode(page_params)}")
            if not isinstance(result, list):
                raise GatewayError(f"Expected GitHub collection response for {path}")
            items.extend(result)
            if len(result) < 100:
                break
            page += 1
        return items

    def get_content_text(self, path: str, ref: str) -> str:
        encoded_path = urllib.parse.quote(path, safe="/")
        result = self.request("GET", f"/contents/{encoded_path}?ref={urllib.parse.quote(ref, safe='')}")
        if not isinstance(result, dict) or result.get("encoding") != "base64":
            raise GatewayError(f"Expected base64 file content for {path}@{ref}")
        return base64.b64decode(result["content"]).decode("utf-8")

    def content_exists(self, path: str, ref: str = "main") -> bool:
        try:
            self.get_content_text(path, ref)
            return True
        except GatewayError as exc:
            if " 404 " in str(exc):
                return False
            raise


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
    return [require_string(item, f"{field}[{index}]", max_len=1000) for index, item in enumerate(value)]


def command_marker(command_id: str) -> str:
    return f"<!-- Gateway-Command-ID: {command_id} -->"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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
    if command["operation"] in {"start_ticket", "complete_ticket"}:
        ticket_id = require_string(command.get("ticketId"), "ticketId", max_len=20)
        require(bool(TICKET_ID_RE.fullmatch(ticket_id)), "ticketId must match PHxx-Gxx-Txx")
    if command["operation"] == "complete_ticket":
        paths = require_string_list(command.get("evidencePaths"), "evidencePaths", allow_empty=False)
        phase = command["ticketId"].split("-")[0]
        prefix = f"project-management/phases/{phase}/evidence/"
        for path in paths:
            require(path.startswith(prefix), f"Evidence for {command['ticketId']} must be under {prefix}")
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
    client.request("POST", "/labels", {"name": label, "color": canonical_label_color(label), "description": "Managed by Agent Command Gateway"})


def list_issues(client: GitHubClient, *, state: str = "all", labels: str | None = None) -> list[dict[str, Any]]:
    params: dict[str, Any] = {"state": state}
    if labels:
        params["labels"] = labels
    result = client.paginate("/issues", params)
    return [item for item in result if isinstance(item, dict) and "pull_request" not in item]


def list_issue_comments(client: GitHubClient, issue_number: int) -> list[dict[str, Any]]:
    result = client.paginate(f"/issues/{issue_number}/comments")
    return [item for item in result if isinstance(item, dict)]


def find_issue_by_exact_id(client: GitHubClient, item_id: str) -> list[dict[str, Any]]:
    pattern = re.compile(rf"(?m)^###\s+(?:Ticket ID|Gate ID)\s*\n`{re.escape(item_id)}`\s*$")
    return [issue for issue in list_issues(client) if pattern.search(issue.get("body") or "")]


def find_issue_by_marker(client: GitHubClient, command_id: str) -> dict[str, Any] | None:
    marker = command_marker(command_id)
    matches = [issue for issue in list_issues(client) if marker in (issue.get("body") or "")]
    require(len(matches) <= 1, f"Multiple Issues contain gateway marker {command_id}")
    return matches[0] if matches else None


def issue_status(issue: dict[str, Any]) -> str:
    match = re.search(r"(?m)^Status:\s*`([^`]+)`\s*$", issue.get("body") or "")
    require(match is not None, "Target Issue has no canonical Status line")
    return match.group(1).strip().upper()


def ticket_id_from_issue(issue: dict[str, Any]) -> str:
    match = re.search(r"(?m)^###\s+Ticket ID\s*\n`([^`]+)`\s*$", issue.get("body") or "")
    require(match is not None, "Target Issue has no canonical Ticket ID field")
    ticket_id = match.group(1).strip()
    require(bool(TICKET_ID_RE.fullmatch(ticket_id)), "Target Issue Ticket ID is malformed")
    return ticket_id


def assert_ticket_identity(issue: dict[str, Any], ticket_id: str) -> None:
    require(ticket_id_from_issue(issue) == ticket_id, "ticketId does not match target Issue")


def apply_status(client: GitHubClient, issue: dict[str, Any], new_status: str, command_id: str) -> None:
    body = issue.get("body") or ""
    updated_body, count = re.subn(
        r"(?m)^Status:\s*`(?:NOT STARTED|READY|IN PROGRESS|BLOCKED|VALIDATION|COMPLETE)`\s*$",
        f"Status: `{new_status}`",
        body,
        count=1,
    )
    require(count == 1, "Issue body does not contain exactly one canonical Status line")
    marker = command_marker(command_id)
    if marker not in updated_body:
        updated_body = updated_body.rstrip() + f"\n\n{marker}\n"
    existing = [label["name"] for label in issue.get("labels", []) if isinstance(label, dict) and "name" in label]
    status_labels = set(STATUS_TO_LABEL.values())
    labels = [label for label in existing if label not in status_labels]
    status_label = STATUS_TO_LABEL[new_status]
    ensure_label(client, status_label)
    labels.append(status_label)
    client.request("PATCH", f"/issues/{issue['number']}", {"body": updated_body, "labels": labels})


def build_gate_body(gate: dict[str, Any], command_id: str) -> str:
    checklist = lambda items: "\n".join(f"- [ ] {item}" for item in items)
    bullets = lambda items: "\n".join(f"- {item}" for item in items)
    return (
        f"### Gate ID\n`{gate['id']}`\n\n### Phase\n{gate['phase']}\n\n"
        f"### Objective\n{gate['objective'].strip()}\n\n### Entry Criteria\n{checklist(gate['entryCriteria'])}\n\n"
        f"### Required Tickets\n{bullets(gate['requiredTickets'])}\n\n### Required Evidence\n{bullets(gate['requiredEvidence'])}\n\n"
        f"### Acceptance Criteria\n{checklist(gate['acceptanceCriteria'])}\n\n### Gate Decision\n`NOT DECIDED`\n\n"
        f"{command_marker(command_id)}\n"
    )


def build_ticket_body(ticket: dict[str, Any], command_id: str) -> str:
    dependencies = "\n".join(f"- {item}" for item in ticket["dependencies"])
    criteria = "\n".join(f"- [ ] {item}" for item in ticket["acceptanceCriteria"])
    evidence = "\n".join(f"- `{item}`" for item in ticket["evidence"])
    return (
        f"### Ticket ID\n`{ticket['id']}`\n\nStatus: `{ticket['status'].upper()}`\n"
        f"Points: {ticket['points']}\nWorkstream: `{ticket['workstream']}`\n\n"
        f"### Dependencies\n{dependencies}\n\n### Selected Solution\n{ticket['selectedSolution'].strip()}\n\n"
        f"### Acceptance Criteria\n{criteria}\n\n### Evidence\n{evidence}\n\n{command_marker(command_id)}\n"
    )


def dependency_satisfied(client: GitHubClient, dependency: str) -> bool:
    for ticket_id in re.findall(r"PH\d{2}-G\d{2}-T\d{2}", dependency):
        matches = find_issue_by_exact_id(client, ticket_id)
        if len(matches) != 1 or matches[0].get("state") != "closed" or issue_status(matches[0]) != "COMPLETE":
            return False
    for gate_id in re.findall(r"PH\d{2}-G\d{2}(?!-T)", dependency):
        matches = find_issue_by_exact_id(client, gate_id)
        if len(matches) != 1:
            return False
        body = matches[0].get("body") or ""
        if matches[0].get("state") != "closed" or not re.search(r"(?m)^`PASSED`\s*$", body):
            return False
    return True


def create_gate(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    gate = command["gate"]
    require(not find_issue_by_exact_id(client, gate["id"]), f"Gate already exists: {gate['id']}")
    active_gates = list_issues(client, state="open", labels="type:gate")
    require(not active_gates, "A gate is already open; close the current gate before creating another")
    labels = [f"phase:{gate['phase']}", f"gate:{gate['id']}", "type:gate", "status:not-started"]
    for label in labels:
        ensure_label(client, label)
    return client.request("POST", "/issues", {
        "title": f"[GATE][{gate['id']}] {gate['title'].strip()}",
        "body": build_gate_body(gate, command["commandId"]),
        "labels": labels,
    })


def create_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    ticket = command["ticket"]
    require(not find_issue_by_exact_id(client, ticket["id"]), f"Ticket already exists: {ticket['id']}")
    parent = find_issue_by_exact_id(client, ticket["gate"])
    require(len(parent) == 1, "Exactly one matching parent gate must exist")
    gate_issue = parent[0]
    require(gate_issue.get("state") == "open", "Parent gate must be open")
    label_names = {item.get("name") for item in gate_issue.get("labels", [])}
    require(f"phase:{ticket['phase']}" in label_names and f"gate:{ticket['gate']}" in label_names, "Parent gate labels do not match ticket phase/gate")
    if ticket["status"].upper() == "READY":
        unsatisfied = [item for item in ticket["dependencies"] if not dependency_satisfied(client, item)]
        require(not unsatisfied, "READY ticket has unsatisfied dependencies: " + "; ".join(unsatisfied))
    status = ticket["status"].upper()
    ticket_type = ticket["type"].lower()
    priority = ticket.get("priority", "normal").lower()
    labels = [f"phase:{ticket['phase']}", f"gate:{ticket['gate']}", f"type:{ticket_type}", STATUS_TO_LABEL[status], f"priority:{priority}"]
    for label in labels:
        ensure_label(client, label)
    return client.request("POST", "/issues", {
        "title": f"[{ticket['id']}][{ticket_type.upper()}] {ticket['title'].strip()}",
        "body": build_ticket_body(ticket, command["commandId"]),
        "labels": labels,
    })


def fetch_issue(client: GitHubClient, issue_number: int) -> dict[str, Any]:
    issue = client.request("GET", f"/issues/{issue_number}")
    require(isinstance(issue, dict) and "pull_request" not in issue, "Target must be a GitHub Issue, not a Pull Request")
    return issue


def start_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    assert_ticket_identity(issue, command["ticketId"])
    before = issue_status(issue)
    require(issue.get("state") == "open", "Ticket must be open")
    require(before == "READY", "Only a READY ticket may move to IN PROGRESS")
    gate_labels = [label["name"] for label in issue.get("labels", []) if label.get("name", "").startswith("gate:")]
    require(len(gate_labels) == 1, "Ticket must have exactly one gate label")
    active = list_issues(client, state="open", labels=f"{gate_labels[0]},status:in-progress")
    conflicting = [item for item in active if item.get("number") != issue["number"]]
    require(not conflicting, f"Another ticket is already IN PROGRESS for {gate_labels[0]}")
    apply_status(client, issue, "IN PROGRESS", command["commandId"])
    return {"issueNumber": issue["number"], "targetBeforeStatus": before, "targetAfterStatus": "IN PROGRESS"}


def declared_evidence_paths(issue: dict[str, Any]) -> set[str]:
    body = issue.get("body") or ""
    parts = body.split("### Evidence", 1)
    require(len(parts) == 2, "Issue has no Evidence section")
    section = parts[1].split("### ", 1)[0]
    return set(re.findall(r"(?m)^\s*-\s*`([^`]+)`\s*$", section))


def complete_ticket(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    assert_ticket_identity(issue, command["ticketId"])
    before = issue_status(issue)
    require(issue.get("state") == "open", "Ticket must be open")
    require(before in {"IN PROGRESS", "VALIDATION"}, "Ticket must be IN PROGRESS or VALIDATION before completion")
    body = issue.get("body") or ""
    acceptance_section = body.split("### Acceptance Criteria", 1)
    require(len(acceptance_section) == 2, "Issue has no Acceptance Criteria section")
    acceptance_text = acceptance_section[1].split("### ", 1)[0]
    require(bool(re.findall(r"(?m)^\s*-\s*\[[xX]\]\s+.+$", acceptance_text)), "Acceptance Criteria section contains no checked criteria")
    require(not re.findall(r"(?m)^\s*-\s*\[ \]\s+.+$", acceptance_text), "Acceptance Criteria still contain unchecked items")
    declared = declared_evidence_paths(issue)
    for path in command["evidencePaths"]:
        require(path in declared, f"Evidence path is not declared by the ticket: {path}")
        require(client.content_exists(path, "main"), f"Required evidence is missing from main: {path}")
    apply_status(client, issue, "COMPLETE", command["commandId"])
    client.request("PATCH", f"/issues/{issue['number']}", {"state": "closed", "state_reason": "completed"})
    return {"issueNumber": issue["number"], "targetBeforeStatus": before, "targetAfterStatus": "COMPLETE", "closed": True}


def add_issue_comment(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    issue = fetch_issue(client, command["issueNumber"])
    body = command["comment"].strip() + "\n\n" + command_marker(command["commandId"])
    result = client.request("POST", f"/issues/{issue['number']}/comments", {"body": body})
    return {"issueNumber": issue["number"], "commentId": result.get("id")}


def recover_operation(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any] | None:
    operation = command["operation"]
    marker = command_marker(command["commandId"])
    if operation in {"create_gate", "create_ticket"}:
        issue = find_issue_by_marker(client, command["commandId"])
        if issue:
            return {"issueNumber": issue.get("number"), "url": issue.get("html_url"), "recovered": True}
    if operation == "add_issue_comment":
        comments = list_issue_comments(client, command["issueNumber"])
        matches = [item for item in comments if marker in (item.get("body") or "")]
        require(len(matches) <= 1, "Multiple comments contain the same gateway command marker")
        if matches:
            return {"issueNumber": command["issueNumber"], "commentId": matches[0].get("id"), "recovered": True}
    if operation in {"start_ticket", "complete_ticket"}:
        issue = fetch_issue(client, command["issueNumber"])
        if marker in (issue.get("body") or ""):
            status = issue_status(issue)
            if operation == "complete_ticket" and issue.get("state") != "closed":
                client.request("PATCH", f"/issues/{issue['number']}", {"state": "closed", "state_reason": "completed"})
            return {"issueNumber": issue["number"], "targetAfterStatus": status, "recovered": True}
    return None


def execute_operation(client: GitHubClient, command: dict[str, Any]) -> dict[str, Any]:
    recovered = recover_operation(client, command)
    if recovered is not None:
        return recovered
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


def build_provenance() -> dict[str, Any]:
    return {
        "submittedCommandSha": os.environ.get("GATEWAY_HEAD_SHA", ""),
        "intakeWorkflowRunId": os.environ.get("GATEWAY_INTAKE_RUN_ID", ""),
        "executorWorkflowRunId": os.environ.get("GATEWAY_EXECUTOR_RUN_ID", ""),
        "workflowActor": os.environ.get("GATEWAY_ACTOR", ""),
        "executorMainSha": os.environ.get("GATEWAY_EXECUTOR_MAIN_SHA", ""),
        "executedAt": utc_now(),
    }


def write_result(client: GitHubClient, command: dict[str, Any], status: str, detail: dict[str, Any]) -> None:
    path = result_path(command["commandId"])
    payload = {
        "schemaVersion": SCHEMA_VERSION,
        "commandId": command["commandId"],
        "operation": command["operation"],
        "status": status,
        "provenance": build_provenance(),
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
    actor = os.environ.get("GATEWAY_ACTOR", "").strip()
    expected_actor = os.environ.get("GATEWAY_EXPECTED_ACTOR", "").strip()
    require(repository and token and head_sha and head_branch and actor and expected_actor, "Required gateway workflow environment is missing")
    require(actor == expected_actor, f"Unauthorized gateway workflow actor: {actor}")
    client = GitHubClient(repository=repository, token=token)
    path = verify_command_commit(client, head_sha, head_branch)
    command = json.loads(client.get_content_text(path, head_sha))
    require(isinstance(command, dict), "Command document must be a JSON object")
    validate_command(command, repository)
    existing_path = result_path(command["commandId"])
    if client.content_exists(existing_path, COMMAND_BRANCH):
        existing = json.loads(client.get_content_text(existing_path, COMMAND_BRANCH))
        require(existing.get("status") == "SUCCEEDED", f"Command already has terminal result: {existing.get('status')}")
        print(f"Command {command['commandId']} already has a SUCCEEDED result.")
        return 0
    try:
        detail = execute_operation(client, command)
        write_result(client, command, "SUCCEEDED", detail)
        print(json.dumps({"status": "SUCCEEDED", "detail": detail}, indent=2))
        return 0
    except Exception as exc:
        try:
            if not client.content_exists(existing_path, COMMAND_BRANCH):
                write_result(client, command, "FAILED", {"error": str(exc)})
        except Exception as result_exc:
            print(f"Failed to write gateway failure result: {result_exc}", file=sys.stderr)
        raise


def run_validate_file(args: argparse.Namespace) -> int:
    command = json.loads(Path(args.path).read_text(encoding="utf-8"))
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
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except (GatewayError, json.JSONDecodeError) as exc:
        print(f"Agent Command Gateway rejected request: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
