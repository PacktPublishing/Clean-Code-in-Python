import unittest

from mrstatus import MergeRequestStatus as Status
from mutation_testing_1 import evaluate_merge_request


class TestMergeRequestEvaluation(unittest.TestCase):
    def test_approved(self):
        result = evaluate_merge_request(3, 0)
        self.assertEqual(result, Status.APPROVED)


if __name__ == "__main__":
    unittest.main()
