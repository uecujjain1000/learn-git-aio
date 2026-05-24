"""
tests/test_calculator.py
-------------------------------------------------------------------------------
UNIT TESTS for src/calculator.py.

What is a unit test?
    A small piece of code that checks that ONE function or method behaves
    correctly. Tests let you change code later with confidence: if you break
    something, a test will fail.

Run all tests from the project root with:
    python -m unittest discover tests
-------------------------------------------------------------------------------
"""

import unittest

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """A group of related tests, all about the Calculator class."""

    def setUp(self):
        """
        Runs before EACH test method. Used to create a fresh Calculator so
        tests don't accidentally share state.
        """
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_by_zero_raises(self):
        # assertRaises checks that an exception of the given type is raised.
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_history_is_tracked(self):
        self.calc.add(1, 1)
        self.calc.multiply(2, 2)
        history = self.calc.show_history()
        self.assertEqual(len(history), 2)


# This block lets you run the file directly with `python tests/test_calculator.py`
if __name__ == "__main__":
    unittest.main()
