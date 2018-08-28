"""Tests for ut_frameworks_{1..3}.py"""

from unittest import TestCase, main

from mrstatus import MergeRequestException, MergeRequestStatus
from ut_frameworks_1 import MergeRequest as MergeRequest1
from ut_frameworks_2 import MergeRequest as MergeRequest2
from ut_frameworks_3 import MergeRequest as MergeRequest3, AcceptanceThreshold


class BaseCase:
    """Base test suite."""

    def setUp(self):
        self.merge_request = self.mr_cls()

    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.REJECTED.value
        )

    def test_just_created_is_pending(self):
        self.assertEqual(
            self.mr_cls().status.value, MergeRequestStatus.PENDING.value
        )

    def test_pending_awaiting_review(self):
        self.merge_request.upvote("core-dev")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.PENDING.value
        )

    def test_approved(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")

        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.APPROVED.value
        )

    def test_no_double_approve(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev1")

        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.PENDING.value
        )

    def test_upvote_changes_to_downvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")

        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.REJECTED.value
        )

    def test_downvote_to_upvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")

        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.APPROVED.value
        )

    def test_invalid_types(self):
        self.assertRaises(
            TypeError, self.merge_request.upvote, {"invalid-object"}
        )


class ExtendedCases:
    """For the MRs that use the extended status."""

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(
            MergeRequestException, self.merge_request.upvote, "dev1"
        )

    def test_cannot_downvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            self.merge_request.downvote,
            "dev1",
        )


class TestsUTFrameworks1(BaseCase, TestCase):
    """tests for ut_frameworks_1"""

    mr_cls = MergeRequest1


class TestsUTFrameworks2(BaseCase, ExtendedCases, TestCase):
    """tests for ut_frameworks_2"""

    mr_cls = MergeRequest2


class TestsUTFrameworks3(BaseCase, ExtendedCases, TestCase):
    """Tests for ut_frameworks_3"""

    mr_cls = MergeRequest3

    def setUp(self):
        super().setUp()
        self.fixture_data = (
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": "dev1", "upvotes": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status.value, expected.value)


if __name__ == "__main__":
    main()
