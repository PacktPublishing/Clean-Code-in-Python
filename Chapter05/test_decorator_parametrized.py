"""Unit tests for files `decorator_parametrized_*.py`"""
import unittest
from unittest import mock

from decorator_function_1 import (
    ControlledException,
    OperationObject,
    RunWithFailure,
)
from decorator_parametrized_1 import run_operation as run_operation_1
from decorator_parametrized_1 import (
    run_with_custom_exceptions as run_with_custom_exceptions_1
)
from decorator_parametrized_1 import (
    run_with_custom_parameters as run_with_custom_parameters_1
)
from decorator_parametrized_1 import (
    run_with_custom_retries_limit as run_with_custom_retries_limit_1
)
from decorator_parametrized_2 import run_operation as run_operation_2
from decorator_parametrized_2 import (
    run_with_custom_exceptions as run_with_custom_exceptions_2
)
from decorator_parametrized_2 import (
    run_with_custom_parameters as run_with_custom_parameters_2
)
from decorator_parametrized_2 import (
    run_with_custom_retries_limit as run_with_custom_retries_limit_2
)

RUN_OPERATION = enumerate((run_operation_1, run_operation_2), start=1)
CUSTOM_EXCEPTION = enumerate(
    (run_with_custom_exceptions_1, run_with_custom_exceptions_2), start=1
)
RETRIES_LIMIT = enumerate(
    (run_with_custom_retries_limit_1, run_with_custom_retries_limit_2), start=1
)
CUSTOM_PARAMETERS = enumerate(
    (run_with_custom_parameters_1, run_with_custom_parameters_2), start=1
)


def test_cases(test_functions):
    for i, function in test_functions:
        yield f"{function.__qualname__}_{i}", function


class WithRetryDecoratorTest(unittest.TestCase):

    def setUp(self):
        self.info = mock.patch("log.logger.info").start()
        self.warning = mock.patch("log.logger.warning").start()

    def tearDown(self):
        self.info.stop()
        self.warning.stop()

    def test_fail_less_than_retry_limit(self):
        """Retry = 3, fail = 2, should work"""
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=2)
        for fname, run_operation in test_cases(RUN_OPERATION):
            with self.subTest(fx=fname):
                times_run = run_operation(failing_task)

                self.assertEqual(times_run, 3)
                self.assertEqual(task._times_called, 3)

    def test_fail_equal_retry_limit(self):
        """Retry = fail = 3, will fail"""
        for fname, run_operation in test_cases(RUN_OPERATION):
            task = OperationObject()
            failing_task = RunWithFailure(task, fail_n_times=3)
            with self.subTest(fx=fname), self.assertRaises(
                ControlledException
            ):
                run_operation(failing_task)

    def test_no_failures(self):
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=0)
        for fname, run_operation in test_cases(RUN_OPERATION):
            with self.subTest(tx=fname):
                times_run = run_operation(failing_task)

                self.assertEqual(times_run, 1)
                self.assertEqual(task._times_called, 1)

    def test_retry_custom_limit_ok(self):
        """Retry = 5, fail = 2, OK"""
        task = RunWithFailure(OperationObject(), fail_n_times=2)
        for fname, run_with_custom_retries_limit in test_cases(RETRIES_LIMIT):
            with self.subTest(tx=fname):

                result = run_with_custom_retries_limit(task)
                self.assertEqual(result, 3)

    def test_retry_custom_limit_fail(self):
        """Retry = 5, fail = 5, Fail"""
        for fname, run_with_custom_retries_limit in test_cases(RETRIES_LIMIT):
            t = OperationObject()
            task = RunWithFailure(t, fail_n_times=5)
            with self.subTest(fx=fname), self.assertRaises(
                ControlledException
            ):
                run_with_custom_retries_limit(task)
                self.assertEqual(t._times_called, 5)

    def test_custom_exception_fails(self):
        task = RunWithFailure(OperationObject(), fail_n_times=2)
        for fname, run_with_custom_exceptions in test_cases(CUSTOM_EXCEPTION):
            with self.subTest(fx=fname), self.assertRaises(
                ControlledException
            ):
                run_with_custom_exceptions(task)

    def test_custom_parameters_and_exception_fails(self):
        """doesn't catch the right exception"""
        t = OperationObject()
        task = RunWithFailure(t, fail_n_times=4)
        for fname, run_with_custom_parameters in test_cases(CUSTOM_PARAMETERS):
            with self.subTest(fx=fname), self.assertRaises(
                ControlledException
            ):

                run_with_custom_parameters(task)
                self.assertEqual(t._times_called, 1)

    def test_run_with_custom_parameters_controlled(self):
        task = RunWithFailure(
            OperationObject(), fail_n_times=3, exception_cls=AttributeError
        )
        for fname, run_with_custom_parameters in test_cases(CUSTOM_PARAMETERS):
            with self.subTest(tx=fname):
                times_run = run_with_custom_parameters(task)

                self.assertEqual(times_run, 4)


if __name__ == "__main__":
    unittest.main()
