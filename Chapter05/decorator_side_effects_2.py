"""Clean Code in Python - Chapter 5: Decorators

> Example of desired side effects on decorators

"""


EVENTS_REGISTRY = {}


def register_event(event_cls):
    """Place the class for the event into the registry to make it accessible in
    the module.
    """
    EVENTS_REGISTRY[event_cls.__name__] = event_cls
    return event_cls


class Event:
    """A base event object"""


class UserEvent:
    TYPE = "user"


@register_event
class UserLoginEvent(UserEvent):
    """Represents the event of a user when it has just accessed the system."""


@register_event
class UserLogoutEvent(UserEvent):
    """Event triggered right after a user abandoned the system."""


def test():
    """
    >>> sorted(EVENTS_REGISTRY.keys()) == sorted(('UserLoginEvent', 'UserLogoutEvent'))
    True
    """
