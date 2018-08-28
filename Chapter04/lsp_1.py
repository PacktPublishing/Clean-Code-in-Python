"""Clean Code in Python - Chapter 4, The SOLID Principles

> Liskov's Substitution Principle (LSP)

Detecting violations of LSP through tools (mypy, pylint, etc.)
"""


class Event:
    ...

    def meets_condition(self, event_data: dict) -> bool:
        return False


class LoginEvent(Event):
    def meets_condition(self, event_data: list) -> bool:
        return bool(event_data)


class LogoutEvent(Event):
    def meets_condition(self, event_data: dict, override: bool) -> bool:
        if override:
            return True
        ...
