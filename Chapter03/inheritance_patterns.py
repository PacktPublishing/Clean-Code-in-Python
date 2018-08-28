"""Clean Code in Python - Chapter 3: Traits of good code

> Inheritance & Composition: use of composition
"""

from datetime import datetime
from unittest import TestCase, main


class TransactionalPolicy:
    """Example refactored to use composition."""

    def __init__(self, policy_data, **extra_data):
        self._data = {**policy_data, **extra_data}

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)


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
