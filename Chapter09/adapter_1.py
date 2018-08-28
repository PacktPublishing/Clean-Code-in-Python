"""Clean Code in Python - Chapter 9: Common Design Patterns

> Adapter (Inheritance)
"""

from _adapter_base import UsernameLookup


class UserSource(UsernameLookup):
    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f"{user_id}:{username}"
