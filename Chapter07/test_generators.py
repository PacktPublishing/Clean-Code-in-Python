"""Clean code in Python - Chapter 07: Using generators

> Tests for:  generators_1.py
"""
from unittest import TestCase, main

from generators_1 import PurchasesStats


class TestPurchaseStats(TestCase):
    def test_calculations(self):
        stats = PurchasesStats(range(1, 11 + 1)).process()

        self.assertEqual(stats.min_price, 1)
        self.assertEqual(stats.max_price, 11)
        self.assertEqual(stats.avg_price, 6)

    def test_empty(self):
        self.assertRaises(ValueError, PurchasesStats, [])


if __name__ == "__main__":
    main()
