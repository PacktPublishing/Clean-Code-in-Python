"""Clean Code in Python - Chapter 3: Traits of good code

> Inheritance & Composition - Inheritance anti-pattern
"""
import collections
from datetime import datetime
from unittest import TestCase, main


class TransactionalPolicy(collections.UserDict):
    """Example of an incorrect use of inheritance."""

    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)


class TestPolicy(TestCase):
    def test_get_policy(self):
        policy = TransactionalPolicy(
            {
                "client001": {
                    "fee": 1000.0,
                    "expiration_date": datetime(2020, 1, 3),
                }
            }
        )
        self.assertDictEqual(
            policy["client001"],
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 3)},
        )

        policy.change_in_policy(
            "client001", expiration_date=datetime(2020, 1, 4)
        )
        self.assertDictEqual(
            policy["client001"],
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 4)},
        )


if __name__ == "__main__":
    main()
