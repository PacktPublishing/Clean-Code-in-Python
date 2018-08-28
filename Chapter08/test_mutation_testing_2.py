import unittest
from collections import namedtuple
from itertools import starmap

from mrstatus import MergeRequestStatus as Status
from mutation_testing_1 import evaluate_merge_request

TestCase = namedtuple(
    "TestCase", "number_approved,number_rejected,expected_status"
)

TEST_DATA = tuple(
    starmap(
        TestCase,
        (
            (2, 1, Status.REJECTED),
            (0, 1, Status.REJECTED),
            (2, 0, Status.APPROVED),
            (3, 0, Status.APPROVED),
            (1, 0, Status.PENDING),
            (0, 0, Status.PENDING),
        ),
    )
)

status_str = {
    Status.REJECTED: "rejected",
    Status.APPROVED: "approved",
    Status.PENDING: "pending",
}


class TestMergeRequestEvaluation(unittest.TestCase):
    def test_status_resolution(self):
        for number_approved, number_rejected, expected_status in TEST_DATA:
            obtained = evaluate_merge_request(number_approved, number_rejected)

            self.assertEqual(obtained, expected_status)

    def test_string_values(self):
        for number_approved, number_rejected, expected_status in TEST_DATA:
            obtained = evaluate_merge_request(number_approved, number_rejected)

            self.assertEqual(obtained.value, status_str[obtained])


if __name__ == "__main__":
    unittest.main()
