"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally.

"""

import io
import re
from contextlib import redirect_stdout
from unittest import TestCase, main

from descriptors_cpython_1 import Method, MyClass1, MyClass2, NewMethod


class TestDescriptorsCPython1(TestCase):
    def setUp(self):
        self.pattern = re.compile(
            r"(External|Internal) call: .* called with \S+ and \S+",
            re.DOTALL | re.MULTILINE,
        )

    def test_method_unbound_fails(self):
        instance = MyClass1()

        capture = io.StringIO()
        with redirect_stdout(capture):
            Method("External call")(instance, "first", "second")

        result = capture.getvalue()

        self.assertIsNotNone(self.pattern.match(result), repr(result))

        with self.assertRaises(TypeError):
            instance.method("first", "second")

    def test_working_example(self):
        instance = MyClass2()
        capture = io.StringIO()

        with redirect_stdout(capture):
            NewMethod("External call")(instance, "first", "second")

        external = capture.getvalue()
        self.assertIsNotNone(self.pattern.match(external), repr(external))

        capture = io.StringIO()
        with redirect_stdout(capture):
            instance.method("first", "second")

        internal = capture.getvalue()
        self.assertIsNotNone(self.pattern.match(internal), repr(internal))


if __name__ == "__main__":
    main()
