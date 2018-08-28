"""Clean Code in Python - Chapter 7: Using Generators

> Idiomatic Iteration: simplifying loops

"""
import unittest

from log import logger


def search_nested_bad(array, desired_value):
    """Example of an iteration in a nested loop."""
    coords = None
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == desired_value:
                coords = (i, j)
                break

        if coords is not None:
            break

    if coords is None:
        raise ValueError(f"{desired_value} not found")

    logger.info("value %r found at [%i, %i]", desired_value, *coords)
    return coords


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell


def search_nested(array, desired_value):
    """"Searching in multiple dimensions with a single loop."""
    try:
        coord = next(
            coord
            for (coord, cell) in _iterate_array2d(array)
            if cell == desired_value
        )
    except StopIteration:
        raise ValueError("{desired_value} not found")

    logger.debug("value %r found at [%i, %i]", desired_value, *coord)
    return coord


if __name__ == "__main__":
    unittest.main()
