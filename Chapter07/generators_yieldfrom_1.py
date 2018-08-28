"""Clean Code in Python - Chapter 7: Using Generators

> The ``yield from`` syntax: chain generators.

"""


def chain(*iterables):
    """
    >>> list(chain("hello", ["world"], ("tuple", " of ", "values.")))
    ['h', 'e', 'l', 'l', 'o', 'world', 'tuple', ' of ', 'values.']
    """
    for it in iterables:
        yield from it


def _chain(*iterables):
    for it in iterables:
        for value in it:
            yield value


def all_powers(n, power):
    yield from (n ** i for i in range(power + 1))
