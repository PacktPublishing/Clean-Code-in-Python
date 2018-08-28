"""Clean Code in Python - Chapter 5: Decorators

Parametrized decorators using callable objects.
"""
from functools import wraps

from decorator_function_1 import ControlledException
from log import logger

RETRIES_LIMIT = 3


class WithRetry:
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    logger.info(
                        "retrying %s due to %s", operation.__qualname__, e
                    )
                    last_raised = e
            raise last_raised

        return wrapped


@WithRetry()
def run_operation(task):
    return task.run()


@WithRetry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.run()


@WithRetry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    return task.run()


@WithRetry(
    retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError)
)
def run_with_custom_parameters(task):
    return task.run()
