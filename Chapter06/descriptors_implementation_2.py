"""Clean Code in Python - Chapter 6: Descriptors

> Different forms of implementing descriptors (``__dict__`` vs. ``weakref``)

  - Implementation with weakref
"""

from weakref import WeakKeyDictionary


class DescriptorClass:
    def __init__(self, initial_value):
        self.value = initial_value
        self.mapping = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.mapping.get(instance, self.value)

    def __set__(self, instance, value):
        self.mapping[instance] = value


class ClientClass:
    """
    >>> client1 = ClientClass()
    >>> client2 = ClientClass()

    >>> client1.descriptor = "new value"

    client1 must have the new value, whilst client2 has to still be with the
    default one:

    >>> client1.descriptor
    'new value'
    >>> client2.descriptor
    'default value'

    Changing the value for client2 doesn't affect client1

    >>> client2.descriptor = "value for client2"
    >>> client2.descriptor
    'value for client2'
    >>> client2.descriptor != client1.descriptor
    True
    """

    descriptor = DescriptorClass("default value")
