"""
src/calculator.py
-------------------------------------------------------------------------------
An example BUSINESS-LOGIC module.

In a real project each major feature gets its own module file.
Here the "feature" is a simple calculator.

This file also demonstrates:
    - Defining a class with methods
    - Type hints (the ': int' and '-> int' parts)
    - Docstrings (the triple-quoted strings inside functions)
    - Raising exceptions for error cases
-------------------------------------------------------------------------------
"""


class Calculator:
    """A very simple calculator class to demonstrate Python OOP basics."""

    def __init__(self):
        """
        The constructor. Runs automatically when you create a new
        Calculator object: `calc = Calculator()`.

        We keep a small history list so each instance remembers what it did.
        """
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        """Return a + b."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return a - b."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return a * b."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Return a / b.

        Raises:
            ZeroDivisionError: If b is 0.
        """
        if b == 0:
            # Better to raise an explicit error than to silently return
            # something wrong. Callers can `try/except` this.
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self) -> list[str]:
        """Return the list of operations performed so far."""
        return self.history
