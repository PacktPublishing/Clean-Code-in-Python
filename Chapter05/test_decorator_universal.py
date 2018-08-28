"""Clean Code in Python - Chapter 5: Decorators

Tests for decorator_universal_1

"""

from unittest import TestCase, main, mock

from decorator_universal_1 import DataHandler, run_query
from decorator_universal_2 import DataHandler as DataHandler_2
from decorator_universal_2 import run_query as run_query_2


class TestDecorator(TestCase):
    def setUp(self):
        self.logger = mock.patch("log.logger.info").start()

    def tearDown(self):
        self.logger.stop()

    def test_decorator_function_ok(self):
        self.assertEqual(
            run_query("function_ok"), "query test_function at function_ok"
        )

    def test_decorator_method_fails(self):
        data_handler = DataHandler()
        self.assertRaisesRegex(
            TypeError,
            "\S+ takes \d+ positional argument but \d+ were given",
            data_handler.run_query,
            "method_fails",
        )

    def test_decorator_function_2(self):
        self.assertEqual(
            run_query_2("second_works"),
            "query test_function_2 at second_works",
        )

    def test_decorator_method_2(self):
        data_handler = DataHandler_2()
        self.assertEqual(
            data_handler.run_query("method_2"),
            "query test_method_2 at method_2",
        )


if __name__ == "__main__":
    main()
