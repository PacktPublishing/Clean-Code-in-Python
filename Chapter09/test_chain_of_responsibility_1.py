"""Clean Code in Python - Chapter 9: Common Design Patterns

> Chain of Responsibility

"""
import unittest

from chain_of_responsibility_1 import LoginEvent, LogoutEvent, SessionEvent


class TestMatching(unittest.TestCase):
    def test_match_login_event(self):
        logline = "1234: login John"
        expected = {"id": "1234", "value": "John"}

        self.assertTrue(LoginEvent.can_process(logline))
        self.assertDictEqual(LoginEvent._parse_data(logline), expected)

    def test_match_logout(self):
        logline = "5678: logout Jade"
        expected = {"id": "5678", "value": "Jade"}

        self.assertTrue(LogoutEvent.can_process(logline))
        self.assertDictEqual(LogoutEvent._parse_data(logline), expected)

    def test_session_event(self):
        cases = ("1234: login John", "789: logout Jade")
        for logline in cases:
            with self.subTest(logline=logline):
                self.assertTrue(SessionEvent.can_process(logline))


class TestChain(unittest.TestCase):
    def test_no_reception(self):
        logline = "no event can match this log"
        chain = LoginEvent(LogoutEvent(SessionEvent()))
        self.assertIsNone(chain.process(logline))

    def test_login(self):
        logline = "567: login User"
        chain = LogoutEvent(LoginEvent())
        expected = {"id": "567", "type": LoginEvent.__name__, "value": "User"}

        self.assertEqual(chain.process(logline), expected)

    def test_login_first(self):
        logline = "567: login User"
        chain = LogoutEvent(LoginEvent(SessionEvent()))
        result = chain.process(logline)
        expected = {"id": "567", "type": LoginEvent.__name__, "value": "User"}

        self.assertEqual(result, expected)

    def test_logout_first(self):
        logline = "987: logout other_user"
        chain = LoginEvent(LogoutEvent(SessionEvent()))
        expected = {
            "id": "987",
            "type": LogoutEvent.__name__,
            "value": "other_user",
        }
        self.assertDictEqual(chain.process(logline), expected)

    def test_generic_first(self):
        cases = ("123: login user", "123: logout user")
        expected = {
            "id": "123",
            "type": SessionEvent.__name__,
            "value": "user",
        }
        chain = SessionEvent(LoginEvent(LogoutEvent()))
        for logline in cases:
            with self.subTest(logline=logline):
                self.assertDictEqual(chain.process(logline), expected)


if __name__ == "__main__":
    unittest.main()
