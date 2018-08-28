"""Clean Code in Python - Chapter 8: Unit Testing

> Refactoring Code

    - File under test: refactoring_1.py

"""
from unittest.mock import Mock

import pytest

from refactoring_1 import BuildStatus


@pytest.fixture
def build_status():
    bstatus = BuildStatus(Mock())
    bstatus.build_date = Mock(return_value="2018-01-01T00:00:01")
    return bstatus


def test_build_notification_sent(build_status):

    build_status.notify(1234, "OK")

    expected_payload = {
        "id": 1234,
        "status": "OK",
        "built_at": build_status.build_date(),
    }

    build_status.transport.post.assert_called_with(
        build_status.endpoint, json=expected_payload
    )
