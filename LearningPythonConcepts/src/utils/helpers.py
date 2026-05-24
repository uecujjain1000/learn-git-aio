"""
src/utils/helpers.py
-------------------------------------------------------------------------------
A catch-all module for small REUSABLE helper functions.

If you find yourself writing the same little snippet in two different files,
move it here.
-------------------------------------------------------------------------------
"""

from datetime import datetime


def greet(name: str) -> str:
    """
    Return a greeting string that changes based on the time of day.

    Example:
        >>> greet("Deepak")
        'Good morning, Deepak!'
    """
    hour = datetime.now().hour

    if hour < 12:
        part_of_day = "morning"
    elif hour < 18:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"

    return f"Good {part_of_day}, {name}!"


def is_even(number: int) -> bool:
    """Return True if `number` is even, False otherwise."""
    return number % 2 == 0
