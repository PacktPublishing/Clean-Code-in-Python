"""Clean Code in Python - Chapter6: Getting more out of our objects with
descriptors

> Different forms of implementing descriptors (``__dict__`` vs. ``weakref``)

  - The global state problem
"""


class SharedDataDescriptor:
    def __init__(self, initial_value):
        self.value = initial_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value


class ClientClass:
    """
    >>> client1 = ClientClass()
    >>> client1.descriptor
    'first value'

    >>> client2 = ClientClass()
    >>> client2.descriptor
    'first value'

    >>> client2.descriptor = "value for client 2"
    >>> client2.descriptor
    'value for client 2'

    >>> client1.descriptor
    'value for client 2'
    """

    descriptor = SharedDataDescriptor("first value")
