import unittest
from datetime import datetime, timedelta

from caveats import BadList, GoodList
from dynamic import DynamicAttributes
from iterables import (
    DateRangeContainerIterable,
    DateRangeIterable,
    DateRangeSequence,
)
from properties import User, is_valid_email
from sequences import Items


class TestCaveats(unittest.TestCase):
    def test_bad_list(self):
        bl = BadList((0, 1, 2, 3, 4, 5))
        self.assertEqual(bl[0], "[even] 0")
        self.assertEqual(bl[3], "[odd] 3")
        self.assertRaises(TypeError, str.join, bl)

    def test_good_list(self):
        gl = GoodList((0, 1, 2))
        self.assertEqual(gl[0], "[even] 0")
        self.assertEqual(gl[1], "[odd] 1")

        expected = "[even] 0; [odd] 1; [even] 2"
        self.assertEqual("; ".join(gl), expected)


class TestSequences(unittest.TestCase):
    def test_items(self):
        items = Items(1, 2, 3, 4, 5)

        self.assertEqual(items[-1], 5)
        self.assertEqual(items[0], 1)
        self.assertEqual(len(items), 5)


class TestProperties(unittest.TestCase):
    def test_is_valid_email(self):
        data = ("user@domain.com", "user.surname@something.org")
        for email in data:
            self.assertTrue(is_valid_email(email))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("invalid"))

    def test_user_valid_email(self):
        user = User("username")
        user.email = "something@domain.com"
        self.assertEqual(user.email, "something@domain.com")

    def test_user_invalid_domain(self):
        user = User("username")
        with self.assertRaisesRegex(
            ValueError, "Can't set .* not a valid email"
        ):
            user.email = "something"


class TestIterables(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime(2016, 7, 17)
        self.end_date = datetime(2016, 7, 24)
        self.expected = [datetime(2016, 7, i) for i in range(17, 24)]

    def _base_test_date_range(self, range_cls):
        date_range = range_cls(self.start_date, self.end_date)
        self.assertListEqual(list(date_range), self.expected)
        self.assertEqual(date_range.start_date, self.start_date)
        self.assertEqual(date_range.end_date, self.end_date)

    def test_date_range(self):
        for range_cls in (
            DateRangeIterable,
            DateRangeContainerIterable,
            DateRangeSequence,
        ):
            with self.subTest(type_=range_cls.__name__):
                self._base_test_date_range(range_cls)

    def test_date_range_sequence(self):
        date_range = DateRangeSequence(self.start_date, self.end_date)

        self.assertEqual(date_range[0], self.start_date)
        self.assertEqual(date_range[-1], self.end_date - timedelta(days=1))
        self.assertEqual(len(date_range), len(self.expected))


class TestDynamic(unittest.TestCase):
    def test_dynamic_attributes(self):
        dyn = DynamicAttributes("value")

        self.assertEqual(dyn.attribute, "value")
        self.assertEqual(dyn.fallback_test, "[fallback resolved] test")
        self.assertEqual(getattr(dyn, "something", "default"), "default")
        with self.assertRaisesRegex(AttributeError, ".* has no attribute \S+"):
            dyn.something_not_found


if __name__ == "__main__":
    unittest.main()
