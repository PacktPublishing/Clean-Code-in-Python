"""Clean Code in Python - Chapter 6: Descriptors

> Types of Descriptors:

    1. Non-Data Descriptors (non-overriding)
    2. Data Descriptors (overriding)

Code examples to illustrate [2].
"""
from log import logger


class DataDescriptor:
    """A descriptor that implements __get__ & __set__."""

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

    def __set__(self, instance, value):
        logger.debug("setting %s.descriptor to %s", instance, value)
        instance.__dict__["descriptor"] = value


class ClientClass:
    """Test DataDescriptor

    Let's see what the value of the descriptor returns::

    >>> client = ClientClass()
    >>> client.descriptor
    42

    >>> client.descriptor = 99
    >>> client.descriptor
    42

    >>> vars(client)
    {'descriptor': 99}

    >>> client.__dict__["descriptor"]
    99

    >>> del client.descriptor
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AttributeError: __delete__

    """
    descriptor = DataDescriptor()
