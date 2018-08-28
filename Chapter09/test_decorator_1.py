"""Clean Code in Python - Chapter 9: Common Design Patterns

> Test Decorator
"""
import unittest

from decorator_1 import CaseInsensitive, DictQuery, RemoveEmpty


class TestDecoration(unittest.TestCase):
    def setUp(self):
        self.query = DictQuery(
            foo="bar", empty="", none=None, upper="UPPERCASE", title="Title"
        )

    def test_no_decorate(self):
        expected = {
            "foo": "bar",
            "empty": "",
            "none": None,
            "upper": "UPPERCASE",
            "title": "Title",
        }
        self.assertDictEqual(self.query.render(), expected)

    def test_decorate(self):
        expected = {"foo": "bar", "upper": "uppercase", "title": "title"}
        result = CaseInsensitive(RemoveEmpty(self.query)).render()
        self.assertDictEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
