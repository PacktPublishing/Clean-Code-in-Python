"""Clean Code in Python - Chapter 8: Unit Testing and refactoring

> Tests for refactoring_2.py
"""
from unittest import TestCase, main

from refactoring_2 import (AcceptanceThreshold, MergeRequest,
                           MergeRequestException, MergeRequestExtendedStatus)


class TestMergeRequestStatus(TestCase):
    def setUp(self):
        self.merge_request = MergeRequest()

    def assert_rejected(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.REJECTED
        )

    def assert_pending(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.PENDING
        )

    def assert_approved(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.APPROVED
        )

    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assert_rejected()

    def test_just_created_is_pending(self):
        self.assert_pending()

    def test_pending_awaiting_review(self):
        self.merge_request.upvote("core-dev")
        self.assert_pending()

    def test_approved(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assert_approved()

    def test_no_double_approve(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev1")
        self.assert_pending()

    def test_upvote_changes_to_downvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")

        self.assert_rejected()

    def test_downvote_to_upvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")

        self.assert_approved()

    def test_invalid_types(self):
        merge_request = MergeRequest()
        self.assertRaises(TypeError, merge_request.upvote, {"invalid-object"})

    def test_cannot_vote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaises(MergeRequestException, merge_request.upvote, "dev1")
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            merge_request.downvote,
            "dev1",
        )


class TestAcceptanceThreshold(TestCase):
    def setUp(self):
        self.fixture_data = (
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestExtendedStatus.PENDING,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestExtendedStatus.PENDING,
            ),
            (
                {"downvotes": "dev1", "upvotes": set()},
                MergeRequestExtendedStatus.REJECTED,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestExtendedStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)


if __name__ == "__main__":
    main()
