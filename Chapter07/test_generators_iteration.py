"""Tests for generators_iteration_*.py"""
from unittest import TestCase, main

from generators_iteration_2 import MappedRange, SequenceWrapper


class TestSequenceWrapper(TestCase):
    def test_sequence(self):
        sequence = SequenceWrapper(list(range(10)))
        for i in sequence:
            self.assertEqual(i, sequence[i])


class TestMappedRange(TestCase):
    def test_limits(self):
        self.assertEqual(len(MappedRange(None, 1, 10)), 9)

        seq = MappedRange(abs, -5, 5)
        self.assertEqual(seq[-5], 0)
        self.assertEqual(seq[-1], 4)
        self.assertEqual(seq[4], abs(-1))
        self.assertRaises(IndexError, seq.__getitem__, -16)
        self.assertRaises(IndexError, seq.__getitem__, 10)

    def test_getitem(self):
        seq = MappedRange(lambda x: x ** 2, 1, 10)
        self.assertEqual(seq[5], 36)

    def test_iterate(self):
        test_data = (  # start, end, expected
            (0, 5, [1, 2, 3, 4, 5]),
            (100, 106, [101, 102, 103, 104, 105, 106]),
        )
        for start, end, expected in test_data:
            with self.subTest(start=start, end=end, expected=expected):
                seq = MappedRange(lambda x: x + 1, start, end)
                self.assertEqual(list(seq), expected)


if __name__ == "__main__":
    main()
