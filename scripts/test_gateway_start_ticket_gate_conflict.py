from __future__ import annotations

import unittest

from scripts.agent_command_gateway import start_ticket
from scripts.test_agent_command_gateway import FakeClient, gate_issue, ticket_issue


class GatewayStartTicketGateConflictRegressionTests(unittest.TestCase):
    def test_parent_gate_in_progress_does_not_block_ready_ticket(self):
        gate = gate_issue(number=12, gate_id="PH02-G01", phase="PH02")
        gate["body"] += "\nStatus: `IN PROGRESS`\n"
        gate["labels"].append({"name": "status:in-progress"})

        ticket = ticket_issue(
            number=18,
            ticket_id="PH02-G01-T06",
            status="READY",
        )
        ticket["labels"] = [
            {"name": "phase:PH02"},
            {"name": "gate:PH02-G01"},
            {"name": "type:validate"},
            {"name": "status:ready"},
        ]

        client = FakeClient([gate, ticket])
        result = start_ticket(
            client,
            {
                "issueNumber": 18,
                "ticketId": "PH02-G01-T06",
                "commandId": "20260827-start-regression-001",
            },
        )

        self.assertEqual(result["targetBeforeStatus"], "READY")
        self.assertEqual(result["targetAfterStatus"], "IN PROGRESS")
        self.assertIn("status:in-progress", {item["name"] for item in client.issues[18]["labels"]})


if __name__ == "__main__":
    unittest.main()
