"""Clean Code in Python - Chapter 7: Using Generators

> Idiomatic Iteration

"""


class NumberSequence:
    """
    >>> seq = NumberSequence()
    >>> seq.next()
    0
    >>> seq.next()
    1

    >>> seq2 = NumberSequence(10)
    >>> seq2.next()
    10
    >>> seq2.next()
    11

    """

    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current


class SequenceOfNumbers:
    """
    >>> list(zip(SequenceOfNumbers(), "abcdef"))
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]

    >>> seq = SequenceOfNumbers(100)
    >>> next(seq)
    100
    >>> next(seq)
    101

    """

    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


def sequence(start=0):
    """
    >>> seq = sequence(10)
    >>> next(seq)
    10
    >>> next(seq)
    11

    >>> list(zip(sequence(), "abcdef"))
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]
    """
    while True:
        yield start
        start += 1
