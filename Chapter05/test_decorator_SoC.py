"""Clean Code in Python - Chapter 5: Decorators

Test for separation of concerns with decorators.

"""
import unittest
from unittest import mock

from decorator_SoC_1 import operation1
from decorator_SoC_2 import operation


def mocked_time():
    _delta_time = 0

    def time():
        nonlocal _delta_time
        _delta_time += 1
        return _delta_time

    return time


@mock.patch("time.sleep")
@mock.patch("time.time", side_effect=mocked_time())
@mock.patch("decorator_SoC_1.logger")
class TestSoC1(unittest.TestCase):
    def test_operation(self, logger, time, sleep):
        operation1()
        expected_calls = [
            mock.call("started execution of %s", "operation1"),
            mock.call("running operation 1"),
            mock.call("function %s took %.2fs", "operation1", 1),
        ]
        logger.info.assert_has_calls(expected_calls)


@mock.patch("time.sleep")
@mock.patch("time.time", side_effect=mocked_time())
@mock.patch("decorator_SoC_2.logger")
class TestSoC2(unittest.TestCase):
    def test_operation(self, logger, time, sleep):
        operation()
        expected_calls = [
            mock.call("started execution of %s", "operation"),
            mock.call("running operation..."),
            mock.call("function %s took %.2f", "operation", 1),
        ]
        logger.info.assert_has_calls(expected_calls)


if __name__ == "__main__":
    unittest.main()
