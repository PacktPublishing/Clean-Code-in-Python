"""Clean Code in Python - Chapter 8: Unit Testing

> Mock Objects

    - File under test: mock_1.py

"""

from unittest import mock

from constants import STATUS_ENDPOINT
from mock_2 import BuildStatus


@mock.patch("mock_2.requests")
def test_build_notification_sent(mock_requests):
    build_date = "2018-01-01T00:00:01"
    with mock.patch("mock_2.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK")

    expected_payload = {"id": 123, "status": "OK", "built_at": build_date}
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )
