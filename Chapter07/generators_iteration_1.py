"""Clean Code in Python - Chapter 7: Using Generators

> The Interface for Iteration

    * Distinguish between iterable objects and iterators
    * Create iterators
"""


class SequenceIterator:
    """
    >>> si = SequenceIterator(1, 2)
    >>> next(si)
    1
    >>> next(si)
    3
    >>> next(si)
    5
    """
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __next__(self):
        value = self.current
        self.current += self.step
        return value
