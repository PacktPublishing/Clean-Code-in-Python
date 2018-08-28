"""Clean Code in Python - Chapter 3: General Traits of Good Code
"""


import unittest

from exceptions_3 import InternalDataError, process


class TestExceptions(unittest.TestCase):
    def test_original_exception(self):
        try:
            process({}, "anything")
        except InternalDataError as e:
            self.assertIsInstance(e.__cause__, KeyError)
