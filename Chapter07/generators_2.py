"""Clean Code in Python - Chapter 7: Using Generators

> Introduction to generators
"""


def sequence(start=0):
    """
    >>> import inspect
    >>> seq = sequence()
    >>> inspect.getgeneratorstate(seq)
    'GEN_CREATED'

    >>> seq = sequence()
    >>> next(seq)
    0
    >>> inspect.getgeneratorstate(seq)
    'GEN_SUSPENDED'

    >>> seq = sequence()
    >>> next(seq)
    0
    >>> seq.close()
    >>> inspect.getgeneratorstate(seq)
    'GEN_CLOSED'
    >>> next(seq)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    StopIteration

    """
    while True:
        yield start
        start += 1
