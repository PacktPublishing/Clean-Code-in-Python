"""Clean Code in Python - Chapter 5: Decorators

> functools.wraps
"""

from functools import wraps

from log import logger


def trace_decorator(function):
    """Log when a function is being called."""

    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("running %s", function.__qualname__)
        return function(*args, **kwargs)

    return wrapped


@trace_decorator
def process_account(account_id):
    """Process an account by Id."""
    logger.info("processing account %s", account_id)
    ...


def decorator(original_function):
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        # modifications done by the decorator ...
        return original_function(*args, **kwargs)

    return decorated_function
