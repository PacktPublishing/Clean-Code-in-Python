"""Clean Code in Python - Chapter 6: Descriptors

> Methods of the descriptor interface: __get__
"""


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return f"{self.__class__.__name__}.{owner.__name__}"
        return f"value for {instance}"


class ClientClass:
    """
    >>> ClientClass.descriptor
    'DescriptorClass.ClientClass'

    >>> ClientClass().descriptor  # doctest: +ELLIPSIS
    'value for <descriptors_methods_1.ClientClass object at 0x...>'
    """

    descriptor = DescriptorClass()
