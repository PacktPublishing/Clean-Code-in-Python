"""Clean Code in Python - Chapter 8: Unit Testing

> Mock Objects

"""
from datetime import datetime

import requests
from constants import STATUS_ENDPOINT


class BuildStatus:
    """The CI status of a pull request."""

    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    @classmethod
    def notify(cls, merge_request_id, status):
        build_status = {
            "id": merge_request_id,
            "status": status,
            "built_at": cls.build_date(),
        }
        response = requests.post(STATUS_ENDPOINT, json=build_status)
        response.raise_for_status()
        return response
