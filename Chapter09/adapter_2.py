"""Clean Code in Python - Chapter 9: Common Design Patterns

> Adapter (Composition)
"""

from _adapter_base import UsernameLookup


class UserSource:
    def __init__(self, username_lookup: UsernameLookup) -> None:
        self.username_lookup = username_lookup

    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.username_lookup.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f"{user_id}:{username}"
