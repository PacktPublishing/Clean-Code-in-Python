"""Clean Code in Python - Chapter 5: Decorators

> Undesired side effects on decorators
"""

import time
from functools import wraps

from log import logger


def traced_function_wrong(function):
    """An example of a badly defined decorator."""
    logger.debug("started execution of %s", function)
    start_time = time.time()

    @wraps(function)
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)
        logger.info(
            "function %s took %.2fs", function, time.time() - start_time
        )
        return result

    return wrapped


@traced_function_wrong
def process_with_delay(callback, delay=0):
    logger.info("sleep(%d)", delay)
    return callback


def traced_function(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("started execution of %s", function)
        start_time = time.time()
        result = function(*args, **kwargs)
        logger.info(
            "function %s took %.2fs", function, time.time() - start_time
        )
        return result

    return wrapped


@traced_function
def call_with_delay(callback, delay=0):
    logger.info("sleep(%d)", delay)
    return callback
