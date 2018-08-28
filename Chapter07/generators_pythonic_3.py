"""Clean Code in Python - Chapter 7: Using Generators

> Idiomatic Iteration

"""
import logging
from itertools import tee
from statistics import median

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def produce_values(how_many):
    for i in range(1, how_many + 1):
        logger.debug("producing purchase %i", i)
        yield i


def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


def main():
    data = produce_values(7)
    obtained = process_purchases(data)
    logger.info("Obtained: %s", obtained)
    assert obtained == (1, 7, 4)


if __name__ == "__main__":
    main()
