"""Clean Code in Python - Chapter 5: Decorators

Creating a decorator to be applied over a function.
"""

from functools import wraps
from unittest import TestCase, main, mock

from log import logger


class ControlledException(Exception):
    """A generic exception on the program's domain."""


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised

    return wrapped


class OperationObject:
    """A helper object to test the decorator."""

    def __init__(self):
        self._times_called: int = 0

    def run(self) -> int:
        """Base operation for a particular action"""
        self._times_called += 1
        return self._times_called

    def __str__(self):
        return f"{self.__class__.__name__}()"

    __repr__ = __str__


class RunWithFailure:
    def __init__(
        self,
        task: "OperationObject",
        fail_n_times: int = 0,
        exception_cls=ControlledException,
    ):
        self._task = task
        self._fail_n_times = fail_n_times
        self._times_failed = 0
        self._exception_cls = exception_cls

    def run(self):
        called = self._task.run()
        if self._times_failed < self._fail_n_times:
            self._times_failed += 1
            raise self._exception_cls(f"{self._task!s} failed!")
        return called


@retry
def run_operation(task):
    """Run a particular task, simulating some failures on its execution."""
    return task.run()


class RetryDecoratorTest(TestCase):
    def setUp(self):
        self.info = mock.patch("log.logger.info").start()

    def tearDown(self):
        self.info.stop()

    def test_fail_less_than_retry_limit(self):
        """Retry = 3, fail = 2, should work"""
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


if __name__ == "__main__":
    main()
