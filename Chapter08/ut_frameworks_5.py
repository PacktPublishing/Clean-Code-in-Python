"""Clean Code in Python - Chapter 8: Unit Testing & Refactoring

> Frameworks and Libraries for Unit Testing

"""

import pytest

from mrstatus import MergeRequestException
from mrstatus import MergeRequestExtendedStatus as MergeRequestStatus


class AcceptanceThreshold:
    def __init__(self, merge_request_context: dict) -> None:
        self._context = merge_request_context

    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING


class MergeRequest:
    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        return AcceptanceThreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("can't vote on a closed merge request")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)


@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()

    merge_request.downvote("dev1")
    merge_request.upvote("dev2")
    merge_request.upvote("dev3")
    merge_request.downvote("dev4")

    return merge_request


def test_simple_rejected(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_with_approvals(rejected_mr):
    rejected_mr.upvote("dev2")
    rejected_mr.upvote("dev3")
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_to_pending(rejected_mr):
    rejected_mr.upvote("dev1")
    assert rejected_mr.status == MergeRequestStatus.PENDING


def test_rejected_to_approved(rejected_mr):
    rejected_mr.upvote("dev1")
    rejected_mr.upvote("dev2")
    assert rejected_mr.status == MergeRequestStatus.APPROVED


def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_approved():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")

    assert merge_request.status == MergeRequestStatus.APPROVED


def test_no_double_approve():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev1")

    assert merge_request.status == MergeRequestStatus.PENDING


def test_upvote_changes_to_downvote():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")
    merge_request.downvote("dev1")

    assert merge_request.status == MergeRequestStatus.REJECTED


def test_downvote_to_upvote():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.downvote("dev2")
    merge_request.upvote("dev2")

    assert merge_request.status == MergeRequestStatus.APPROVED


def test_invalid_types():
    merge_request = MergeRequest()
    pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})


def test_cannot_vote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
    with pytest.raises(
        MergeRequestException, match="can't vote on a closed merge request"
    ):
        merge_request.downvote("dev1")


@pytest.mark.parametrize(
    "context,expected_status",
    (
        ({"downvotes": set(), "upvotes": set()}, MergeRequestStatus.PENDING),
        (
            {"downvotes": set(), "upvotes": {"dev1"}},
            MergeRequestStatus.PENDING,
        ),
        ({"downvotes": "dev1", "upvotes": set()}, MergeRequestStatus.REJECTED),
        (
            {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
            MergeRequestStatus.APPROVED,
        ),
    ),
)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status
