"""Clean Code in Python - Chapter 8: Unit Testing & Refactoring

> Mutation Testing 2
"""

from mrstatus import MergeRequestStatus


def evaluate_merge_request(upvote_counts, downvotes_count):
    if downvotes_count > 0:
        return MergeRequestStatus.REJECTED
    if upvote_counts >= 2:
        return MergeRequestStatus.APPROVED
    return MergeRequestStatus.PENDING
