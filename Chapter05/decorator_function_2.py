"""Clean Code in Python - Chapter 5: Decorators

> Function decorators
    - Creating a decorator to be applied over a function.
    - Implement the decorator as an object.
"""
from functools import wraps
from unittest import TestCase, main, mock

from decorator_function_1 import (ControlledException, OperationObject,
                                  RunWithFailure)
from log import logger


class Retry:
    def __init__(self, operation):
        self.operation = operation
        wraps(operation)(self)

    def __call__(self, *args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return self.operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", self.operation.__qualname__)
                last_raised = e
        raise last_raised


@Retry
def run_operation(task):
    """Run the operation in the task"""
    return task.run()


class RetryDecoratorTest(TestCase):
    def setUp(self):
        self.info = mock.patch("log.logger.info").start()

    def tearDown(self):
        self.info.stop()

    def test_fail_less_than_retry_limit(self):
        """Retry = 3, fail = 2 --> OK"""
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=2)
        times_run = run_operation(failing_task)

        self.assertEqual(times_run, 3)
        self.assertEqual(task._times_called, 3)

    def test_fail_equal_retry_limit(self):
        """Retry = fail = 3, will fail"""
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=3)
        with self.assertRaises(ControlledException):
            run_operation(failing_task)

    def test_no_failures(self):
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=0)
        times_run = run_operation(failing_task)

        self.assertEqual(times_run, 1)
        self.assertEqual(task._times_called, 1)

    def test_doc(self):
        self.assertEqual(
            run_operation.__doc__, "Run the operation in the task"
        )


if __name__ == "__main__":
    main()
