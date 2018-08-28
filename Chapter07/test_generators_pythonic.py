from itertools import chain
from random import choice, randint
from unittest import TestCase, main

from generators_pythonic_3 import process_purchases, produce_values
from generators_pythonic_4 import search_nested, search_nested_bad


class TestPurchaseStats(TestCase):
    """Tests for generators_pythonic_3.py"""

    def test_calculations(self):
        min_price, max_price, avg_price = process_purchases(produce_values(11))

        self.assertEqual(min_price, 1)
        self.assertEqual(max_price, 11)
        self.assertEqual(avg_price, 6)

    def test_empty(self):
        self.assertRaises(ValueError, process_purchases, [])


class TestSimplifiedIteration(TestCase):
    """Tests for generators_pythonic_4.py"""

    def test_found(self):
        test_matrix = [[randint(1, 100) for _ in range(10)] for _ in range(10)]
        to_search_for = choice(list(chain.from_iterable(test_matrix)))
        for finding_function in (search_nested_bad, search_nested):
            row, column = finding_function(test_matrix, to_search_for)
            self.assertEqual(test_matrix[row][column], to_search_for)

    def test_not_found(self):
        matrix = [[i for i in range(10)] for _ in range(2)]
        for ffunc in search_nested_bad, search_nested:
            self.assertRaises(ValueError, ffunc, matrix, -1)


if __name__ == "__main__":
    main()
