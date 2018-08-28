"""Clean Code in Python - Chapter 2: Pythonic Code

> Callable objects

"""

from collections import defaultdict


class CallCount:
    """
    >>> cc = CallCount()
    >>> cc(1)
    1
    >>> cc(2)
    1
    >>> cc(1)
    2
    >>> cc(1)
    3
    >>> cc("something")
    1

    >>> callable(cc)
    True
    """

    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]
