"""Clean Code in Python - Chapter 5

Separation of Concerns (SoC).
Break a coupled decorator into smaller ones.
"""
import time
from functools import wraps

from log import logger


def log_execution(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("started execution of %s", function.__qualname__)
        return function(*kwargs, **kwargs)

    return wrapped


def measure_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)

        logger.info(
            "function %s took %.2f",
            function.__qualname__,
            time.time() - start_time,
        )
        return result

    return wrapped


@measure_time
@log_execution
def operation():
    time.sleep(3)
    logger.info("running operation...")
    return 33
