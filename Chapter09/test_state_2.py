"""Clean Code in Python - Chapter 9: Common Design Patterns

> Test State 2
"""


import unittest

from state_2 import Closed, InvalidTransitionError, Merged, MergeRequest, Open


class TestMergeRequestTransitions(unittest.TestCase):
    def setUp(self):
        self.mr = MergeRequest("develop", "master")

    def test_reopen(self):
        self.mr.approvals = 3
        self.mr.open()

        self.assertEqual(self.mr.approvals, 0)

    def test_open_to_closed(self):
        self.mr.approvals = 2
        self.assertEqual(self.mr.status, Open.__name__)
        self.mr.close()
        self.assertEqual(self.mr.approvals, 0)
        self.assertEqual(self.mr.status, Closed.__name__)

    def test_closed_to_open(self):
        self.mr.close()
        self.assertEqual(self.mr.status, Closed.__name__)
        self.mr.open()
        self.assertEqual(self.mr.status, Open.__name__)

    def test_double_close(self):
        self.mr.close()
        self.mr.close()

    def test_open_to_merge(self):
        self.mr.merge()
        self.assertEqual(self.mr.status, Merged.__name__)

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
