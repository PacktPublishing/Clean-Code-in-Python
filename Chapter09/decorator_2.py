"""Clean Code in Python - Chapter 9: Common Design Patterns

> Decorator: A function-based version
"""
from typing import Callable, Dict, Iterable


class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(
        self,
        query: DictQuery,
        *decorators: Iterable[Callable[[Dict[str, str]], Dict[str, str]]]
    ) -> None:
        self._decorated = query
        self._decorators = decorators

    def render(self):
        current_result = self._decorated.render()
        for deco in self._decorators:
            current_result = deco(current_result)
        return current_result


def remove_empty(original: dict) -> dict:
    return {k: v for k, v in original.items() if v}


def case_insensitive(original: dict) -> dict:
    return {k: v.lower() for k, v in original.items()}
