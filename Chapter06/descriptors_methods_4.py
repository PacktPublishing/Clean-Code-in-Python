"""Clean Code in Python - Chapter 6: Descriptors

> Methods of the descriptor interface: __set_name__

"""
from log import logger


class DescriptorWithName:
    """This descriptor requires the name to be explicitly set."""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return self
        logger.debug("getting %r attribute from %r", self.name, instance)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ClientClass:
    """
    >>> client = ClientClass()
    >>> client.descriptor = "value"
    >>> client.descriptor
    'value'

    >>> ClientClass.descriptor_2.name
    "a name that doesn't match the attribute"
    """

    descriptor = DescriptorWithName("descriptor")
    descriptor_2 = DescriptorWithName("a name that doesn't match the attribute")


class DescriptorWithAutomaticName(DescriptorWithName):
    """This descriptor can infer the name of the attribute, if not provided.
    It also supports setting a different name explicitly.
    """

    def __init__(self, name: str = None) -> None:
        self.name = name

    def __set_name__(self, owner, name):
        self.name = self.name or name


class NewClientClass:
    """
    >>> NewClientClass.descriptor_with_default_name.name
    'descriptor_with_default_name'

    >>> NewClientClass.named_descriptor.name
    'named_descriptor'

    >>> NewClientClass.descriptor_named_differently.name
    'a_different_name'

    >>> client = NewClientClass()
    >>> client.descriptor_named_differently = "foo"
    >>> client.__dict__["a_different_name"]
    'foo'

    >>> client.descriptor_named_differently
    'foo'

    >>> client.a_different_name
    'foo'
    """

    descriptor_with_default_name = DescriptorWithAutomaticName()
    named_descriptor = DescriptorWithAutomaticName("named_descriptor")
    descriptor_named_differently = DescriptorWithAutomaticName(
        "a_different_name"
    )
