"""Clean Code in Python - Chapter 9: Common Design Patterns

> State
"""
import abc

from log import logger
from state_1 import InvalidTransitionError


class MergeRequestState(abc.ABC):
    def __init__(self, merge_request):
        self._merge_request = merge_request

    @abc.abstractmethod
    def open(self):
        ...

    @abc.abstractmethod
    def close(self):
        ...

    @abc.abstractmethod
    def merge(self):
        ...

    def __str__(self):
        return self.__class__.__name__


class Open(MergeRequestState):
    def open(self):
        self._merge_request.approvals = 0

    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Closed

    def merge(self):
        logger.info("merging %s", self._merge_request)
        logger.info("deleting branch %s", self._merge_request.source_branch)
        self._merge_request.state = Merged


class Closed(MergeRequestState):
    def open(self):
        logger.info("reopening closed merge request %s", self._merge_request)
        self._merge_request.state = Open

    def close(self):
        """Current state."""

    def merge(self):
        raise InvalidTransitionError("can't merge a closed request")


class Merged(MergeRequestState):
    def open(self):
        raise InvalidTransitionError("already merged request")

    def close(self):
        raise InvalidTransitionError("already merged request")

    def merge(self):
        """Current state."""


class MergeRequest:
    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state: MergeRequestState
        self.approvals = 0
        self.state = Open

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        self._state = new_state_cls(self)

    @property
    def status(self):
        return str(self.state)

    def __getattr__(self, method):
        return getattr(self.state, method)

    def __str__(self):
        return f"{self.target_branch}:{self.source_branch}"
