"""Clean Code in Python - Chapter 9: Common Design Patterns

> Test monostate_4.py
"""
import unittest

from monostate_4 import BranchFetcher, TagFetcher


class BaseTest:
    def test_pull(self):
        tf = self.test_cls(0.1)
        for i in range(3):
            self.test_cls(i)

        self.assertEqual(tf.source, 2)
        self.assertEqual(tf.pull(), f"{self.exp} = 2")

    def test_change_any(self):
        tf1, tf2, tf3 = (self.test_cls(i) for i in range(3))

        self.assertEqual(tf1.source, tf2.source)

        tf3.new_attribute = "any data"

        self.assertEqual(tf1.new_attribute, "any data")
        self.assertEqual(tf2.new_attribute, "any data")

    def test_not_any(self):
        tf1, tf2 = self.test_cls(1), self.test_cls(2)

        self.assertRaises(AttributeError, getattr, tf1, "non_existing")

        tf1.new = "new"
        self.assertEqual(tf2.new, "new")


class TestTag(BaseTest, unittest.TestCase):
    def setUp(self):
        self.test_cls = TagFetcher
        self.exp = "Tag"


class TestBranch(BaseTest, unittest.TestCase):
    def setUp(self):
        self.test_cls = BranchFetcher
        self.exp = "Branch"


class TestTagAndBranch(unittest.TestCase):
    """Test attributes aren't mixed between different hierarchies"""

    def test_tag_and_branch(self):
        tf1 = TagFetcher(1)
        tf2 = TagFetcher(2)
        bf1 = BranchFetcher("branch-1")
        bf2 = BranchFetcher("branch-2")

        self.assertEqual(tf1.source, 2)
        self.assertEqual(bf1.source, "branch-2")

        bf2.source = "develop"
        tf1.source = 2.1

        self.assertEqual(bf1.source, "develop")
        self.assertEqual(tf2.source, 2.1)


if __name__ == "__main__":
    unittest.main()
