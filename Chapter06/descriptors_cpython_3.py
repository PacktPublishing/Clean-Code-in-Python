"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally: @clasmethod

"""
from types import MethodType


class ClassMethod:
    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        return self.method(*args, **kwargs)

    def __get__(self, instance, owner):
        return MethodType(self.method, owner)


class MyClass:
    """
    >>> MyClass().class_method("first", "second")
    'MyClass called with arguments: first, and second'

    >>> MyClass.class_method("one", "two")
    'MyClass called with arguments: one, and two'

    >>> MyClass().method()  # doctest: +ELLIPSIS
    'MyClass called with arguments: self, and from method'
    """

    @ClassMethod
    def class_method(cls, arg1, arg2) -> str:
        return f"{cls.__name__} called with arguments: {arg1}, and {arg2}"

    def method(self):
        return self.class_method("self", "from method")


class classproperty:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget(owner)


def read_prefix_from_config():
    return ""


class TableEvent:
    """
    >>> TableEvent.topic
    'public.user'

    >>> TableEvent().topic
    'public.user'
    """

    schema = "public"
    table = "user"

    @classproperty
    def topic(cls):
        prefix = read_prefix_from_config()
        return f"{prefix}{cls.schema}.{cls.table}"
