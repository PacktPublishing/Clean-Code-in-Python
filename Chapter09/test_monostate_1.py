"""Clean Code in Python - Chapter 9: Common Design Patterns

> Test Monostate Pattern
"""
import unittest

from monostate_1 import GitFetcher


class TestFetcher(unittest.TestCase):
    def test_fetch_single(self):
        fetcher = GitFetcher(0.1)
        self.assertEqual(fetcher.pull(), 0.1)

    def test_fetch_multiple(self):
        f1 = GitFetcher(0.1)
        f2 = GitFetcher(0.2)

        self.assertEqual(f1.pull(), 0.2)
        # There is a new version in f1's request
        f1.current_tag = 0.3

        self.assertEqual(f2.pull(), 0.3)
        self.assertEqual(f1.pull(), 0.3)

    def test_multiple_consecutive_versions(self):
        fetchers = {GitFetcher(i) for i in range(5)}

        self.assertTrue(all(f.current_tag == 4 for f in fetchers))

    def test_never_set(self):
        fetcher = GitFetcher(None)
        self.assertRaisesRegex(
            AttributeError, "\S+ was never set", fetcher.pull
        )


if __name__ == "__main__":
    unittest.main()
