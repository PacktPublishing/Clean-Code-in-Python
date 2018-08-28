import doctest
import unittest
import doctest_module


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(doctest_module))
    return tests


if __name__ == "__main__":
    unittest.main()
