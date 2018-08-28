"""Clean Code in Python - Chapter 3: General Traits of Good Code

"""

import unittest
from unittest.mock import Mock, patch

from exceptions_1 import DataTransport, Event


class FailsAfterNTimes:
    def __init__(self, n_times: int, with_exception) -> None:
        self._remaining_failures = n_times
        self._exception = with_exception

    def connect(self):
        self._remaining_failures -= 1
        if self._remaining_failures >= 0:
            raise self._exception
        return self

    def send(self, data):
        return data


@patch("time.sleep", return_value=0)
class TestTransport(unittest.TestCase):
    def test_connects_after_retries(self, sleep):
        data_transport = DataTransport(
            FailsAfterNTimes(2, with_exception=ConnectionError)
        )
        data_transport.send = Mock()
        data_transport.deliver_event(Event("test"))

        data_transport.send.assert_called_once_with("decoded test")

        assert (
            sleep.call_count == DataTransport.retry_n_times - 1
        ), sleep.call_count

    def test_connects_directly(self, sleep):
        connector = Mock()
        data_transport = DataTransport(connector)
        data_transport.send = Mock()
        data_transport.deliver_event(Event("test"))

        connector.connect.assert_called_once()
        assert sleep.call_count == 0

    def test_connection_error(self, sleep):
        data_transport = DataTransport(
            Mock(connect=Mock(side_effect=ConnectionError))
        )

        self.assertRaisesRegex(
            ConnectionError,
            "Couldn't connect after \d+ times",
            data_transport.deliver_event,
            Event("connection error"),
        )
        assert sleep.call_count == DataTransport.retry_n_times

    def test_error_in_event(self, sleep):
        data_transport = DataTransport(Mock())
        event = Mock(decode=Mock(side_effect=ValueError))
        with patch("exceptions_1.logger.error"):
            self.assertRaises(ValueError, data_transport.deliver_event, event)

        assert not sleep.called


if __name__ == "__main__":
    unittest.main()
