"""Clean Code in Python - Chapter 7: Using Generators

> Idiomatic Iteration with itertools

"""
import logging
from itertools import filterfalse, tee

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IteratorWrapper:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __next__(self):
        value = next(self.iterable)
        logger.debug(
            "%s Producing next value: %r", self.__class__.__name__, value
        )
        return value

    def __iter__(self):
        return self


def partition(condition, iterable):
    """Return 2 new iterables

    true_cond, false_cond = partition(condition, iterable)

    * in true_cond, condition is true over all elements of iterable
    * in false_cond, condition is false over all elements of iterable
    """
    for_true, for_false = tee(iterable)
    return filter(condition, for_true), filterfalse(condition, for_false)


iterable = IteratorWrapper(
    {"name": f"element_{i}", "index": i} for i in range(20)
)


def is_even(record):
    return record["index"] % 2 == 0


def show(records):
    return ", ".join(e["name"] for e in records)


if __name__ == "__main__":
    even, odd = partition(is_even, iterable)

    logger.info(
        "\n\tEven records: %s\n\t Odd records: %s", show(even), show(odd)
    )
