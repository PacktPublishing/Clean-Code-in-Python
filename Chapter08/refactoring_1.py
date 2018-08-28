"""Clean Code in Python - Chapter 8: Unit Testing

> Refactoring Code
"""

from datetime import datetime

from constants import STATUS_ENDPOINT


class BuildStatus:

    endpoint = STATUS_ENDPOINT

    def __init__(self, transport):
        self.transport = transport

    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    def compose_payload(self, merge_request_id, status) -> dict:
        return {
            "id": merge_request_id,
            "status": status,
            "built_at": self.build_date(),
        }

    def deliver(self, payload):
        response = self.transport.post(self.endpoint, json=payload)
        response.raise_for_status()
        return response

    def notify(self, merge_request_id, status):
        return self.deliver(self.compose_payload(merge_request_id, status))
