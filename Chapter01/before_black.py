"""Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

> Black:
    A code that is compliant with PEP-8, but that still can be modified by back


Run::
    black -l 79 before_black.py

To see the difference
"""


def my_function(name):
    """
    >>> my_function('black')
    'received Black'
    """
    return 'received {0}'.format(name.title())
