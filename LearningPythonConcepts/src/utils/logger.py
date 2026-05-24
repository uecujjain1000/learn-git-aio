"""
src/utils/logger.py
-------------------------------------------------------------------------------
Centralized LOGGING setup.

Why a logger instead of print()?
    - Logs include timestamps and severity levels automatically.
    - You can turn levels up or down without editing every print().
    - You can write to a file as well as the screen.
    - In production, print() output is often lost; logs are not.

How to use in any other file:
    from src.utils.logger import get_logger
    logger = get_logger(__name__)
    logger.info("hello")
    logger.warning("careful")
    logger.error("something broke")
-------------------------------------------------------------------------------
"""

import logging
from config import config


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    `name` is usually __name__ (the module's own name), which makes
    log messages show which file they came from.
    """
    logger = logging.getLogger(name)

    # Avoid adding handlers twice if get_logger is called many times.
    if logger.handlers:
        return logger

    # If DEBUG is on in config, show everything; otherwise only INFO and above.
    level = logging.DEBUG if config.DEBUG else logging.INFO
    logger.setLevel(level)

    # A "handler" decides WHERE log messages go. StreamHandler = the screen.
    handler = logging.StreamHandler()

    # A "formatter" decides what each log line looks like.
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
