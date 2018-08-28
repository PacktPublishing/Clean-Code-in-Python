"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally.

"""
from types import MethodType


class Method:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, arg1, arg2):
        print(f"{self.name}: {instance} called with {arg1} and {arg2}")


class MyClass1:
    method = Method("Internal call")


class NewMethod:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, arg1, arg2):
        print(f"{self.name}: {instance} called with {arg1} and {arg2}")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return MethodType(self, instance)


class MyClass2:
    method = NewMethod("Internal call")
