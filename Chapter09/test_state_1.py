"""Clean Code in Python - Chapter 9: Common Design Patterns

> Test State
"""


import unittest

from state_1 import Closed, InvalidTransitionError, Merged, MergeRequest, Open


class TestMergeRequestTransitions(unittest.TestCase):
    def setUp(self):
        self.mr = MergeRequest("develop", "master")

    def test_reopen(self):
        self.mr.approvals = 3
        self.mr.open()

        self.assertEqual(self.mr.approvals, 0)

    def test_open_to_closed(self):
        self.mr.approvals = 2
        self.assertIsInstance(self.mr.state, Open)
        self.mr.close()
        self.assertEqual(self.mr.approvals, 0)
        self.assertIsInstance(self.mr.state, Closed)

    def test_closed_to_open(self):
        self.mr.close()
        self.assertIsInstance(self.mr.state, Closed)
        self.mr.open()
        self.assertIsInstance(self.mr.state, Open)

    def test_double_close(self):
        self.mr.close()
        self.mr.close()

    def test_open_to_merge(self):
        self.mr.merge()
        self.assertIsInstance(self.mr.state, Merged)

    def test_merge_is_final(self):
        self.mr.merge()
        regex = "already merged request"
        self.assertRaisesRegex(InvalidTransitionError, regex, self.mr.open)
        self.assertRaisesRegex(InvalidTransitionError, regex, self.mr.close)

    def test_cannot_merge_closed(self):
        self.mr.close()
        self.assertRaises(InvalidTransitionError, self.mr.merge)


if __name__ == "__main__":
    unittest.main()
