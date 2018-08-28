"""Clean Code in Python - Chapter 9: Common Design Patterns

> Tests Composite
"""

import unittest

from composite_1 import Product, ProductBundle


class TestProducts(unittest.TestCase):
    def test_product_bundle(self):

        tablet = Product("tablet", 200)
        bundle = ProductBundle(
            "electronics",
            0.1,
            tablet,
            Product("smartphone", 100),
            Product("laptop", 700),
        )
        self.assertEqual(tablet.price, 200)
        self.assertEqual(bundle.price, 900)

    def test_nested_bundle(self):
        electronics = ProductBundle(
            "electronics",
            0,
            ProductBundle(
                "smartphones",
                0.15,
                Product("smartphone1", 200),
                Product("smartphone2", 700),
            ),
            ProductBundle(
                "laptops",
                0.05,
                Product("laptop1", 700),
                Product("laptop2", 950),
            ),
        )
        tablets = ProductBundle(
            "tablets", 0.05, Product("tablet1", 200), Product("tablet2", 300)
        )
        total = ProductBundle("total", 0, electronics, tablets)
        expected_total_price = (0.85 * 900) + (0.95 * 1650) + (0.95 * 500)

        self.assertEqual(total.price, expected_total_price)


if __name__ == "__main__":
    unittest.main()
