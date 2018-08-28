"""Clean Code in Python - Chapter 5: Decorators

> Class decorators.
"""
import unittest
from datetime import datetime


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "**redacted**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M"),
        }


class LoginEvent:
    SERIALIZER = LoginEventSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()


class TestLoginEventSerialized(unittest.TestCase):
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
