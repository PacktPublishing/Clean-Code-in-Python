"""Clean Code in Python - Chapter 8: Unit Testing & Refactoring

> Frameworks and Libraries for Unit Testing
"""

from mrstatus import MergeRequestStatus


class MergeRequest:
    """An entity abstracting a merge request."""

    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}

    @property
    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING

    def upvote(self, by_user):
        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)
