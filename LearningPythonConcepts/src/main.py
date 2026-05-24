"""
src/main.py
-------------------------------------------------------------------------------
This is the ENTRY POINT of the application - the file you actually run.

How to run from the project root:
    python -m src.main

Why `python -m src.main` and not `python src/main.py`?
    Because we use package-style imports like `from src.calculator import ...`,
    we need Python to recognize 'src' as a package. The `-m` flag does that.
-------------------------------------------------------------------------------
"""

# Standard-library imports come first
import sys

# Local (our own project) imports
from config import config
from src.calculator import Calculator
from src.utils.logger import get_logger
from src.utils.helpers import greet


# Get a logger configured for THIS module. The name shows up in log lines,
# making it easy to know where a message came from.
logger = get_logger(__name__)


def run():
    """
    The main function. Putting logic inside a function (instead of at the top
    of the file) is a good practice - it keeps the file clean and lets the
    code be imported without side effects.
    """
    logger.info("Starting %s v%s", config.APP_NAME, config.APP_VERSION)

    # Greet the user. The name comes from the .env config file.
    print(greet(config.APP_USER_NAME))

    # Create an instance of the Calculator class and try a few operations.
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")

    # Show how to handle errors safely.
    try:
        calc.divide(5, 0)
    except ZeroDivisionError as e:
        # Log the error instead of crashing the program.
        logger.warning("Caught expected error: %s", e)

    logger.info("Finished successfully.")


# -----------------------------------------------------------------------------
# The `if __name__ == "__main__":` guard.
# -----------------------------------------------------------------------------
# This block ONLY runs when this file is executed directly (not imported).
# It is the standard Python convention for "this is the start of the program".
if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        # Top-level safety net so any uncaught error gets logged nicely.
        logger.exception("Unhandled error: %s", e)
        sys.exit(1)  # exit code 1 = error
