"""Indexes and slices
Getting elements by an index or range
"""
import doctest


def index_last():
    """
    >>> my_numbers = (4, 5, 3, 9)
    >>> my_numbers[-1]
    9
    >>> my_numbers[-3]
    5
    """


def get_slices():
    """
    >>> my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
    >>> my_numbers[2:5]
    (2, 3, 5)
    >>> my_numbers[:3]
    (1, 1, 2)
    >>> my_numbers[3:]
    (3, 5, 8, 13, 21)
    >>> my_numbers[::]
    (1, 1, 2, 3, 5, 8, 13, 21)
    >>> my_numbers[1:7:2]
    (1, 3, 8)

    >>> interval = slice(1, 7, 2)
    >>> my_numbers[interval]
    (1, 3, 8)

    >>> interval = slice(None, 3)
    >>> my_numbers[interval] == my_numbers[:3]
    True
    """


def main():
    index_last()
    get_slices()
    fail_count, _ = doctest.testmod(verbose=True)
    raise SystemExit(fail_count)


if __name__ == "__main__":
    main()
