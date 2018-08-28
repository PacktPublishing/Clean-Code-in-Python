"""Clean Code in Python - Chapter 5

Class decorators.

Reimplement the serialization of the events by applying a class decorator.
Use the @dataclass decorator.

This code only works in Python 3.7+
"""
import sys
import unittest
from datetime import datetime

from decorator_class_2 import (
    Serialization,
    format_time,
    hide_field,
    show_original,
)

try:
    from dataclasses import dataclass
except ImportError:

    def dataclass(cls):
        return cls


@Serialization(
    username=show_original,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime


class TestLoginEventSerialized(unittest.TestCase):
    @unittest.skipIf(
        sys.version_info[:3] < (3, 7, 0), reason="Requires Python 3.7+ to run"
    )
    def test_serializetion(self):
        event = LoginEvent(
            "username", "password", "127.0.0.1", datetime(2016, 7, 20, 15, 45)
        )
        expected = {
            "username": "username",
            "password": "**redacted**",
            "ip": "127.0.0.1",
            "timestamp": "2016-07-20 15:45",
        }
        self.assertEqual(event.serialize(), expected)


if __name__ == "__main__":
    unittest.main()
