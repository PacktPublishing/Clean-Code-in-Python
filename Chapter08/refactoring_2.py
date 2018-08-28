"""Clean Code in Python - Chapter 8: Unit Testing and refactoring

> Refactoring Code

"""
from mrstatus import MergeRequestExtendedStatus, MergeRequestException


class AcceptanceThreshold:
    def __init__(self, merge_request_context: dict) -> None:
        self._context = merge_request_context

    def status(self):
        if self._context["downvotes"]:
            return MergeRequestExtendedStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestExtendedStatus.APPROVED
        return MergeRequestExtendedStatus.PENDING


class MergeRequest:
    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = MergeRequestExtendedStatus.OPEN

    def close(self):
        self._status = MergeRequestExtendedStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestExtendedStatus.CLOSED:
            return self._status

        return AcceptanceThreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestExtendedStatus.CLOSED:
            raise MergeRequestException("can't vote on a closed merge request")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)
