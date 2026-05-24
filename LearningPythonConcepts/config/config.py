"""
config/config.py
-------------------------------------------------------------------------------
This is the CONFIGURATION file of the project.

Why a separate config file?
    - Keeps "settings" out of your business logic.
    - Lets you change behavior (debug on/off, paths, etc.) without touching
      the actual code.
    - Loads SECRETS (like API keys) from environment variables instead of
      hard-coding them.
-------------------------------------------------------------------------------
"""

import os
from pathlib import Path
from dotenv import load_dotenv  # 3rd-party package from requirements.txt

# -----------------------------------------------------------------------------
# 1. Load environment variables from a .env file (if one exists).
# After this call, you can read values with os.getenv("VAR_NAME").
# -----------------------------------------------------------------------------
load_dotenv()

# -----------------------------------------------------------------------------
# 2. PATH CONSTANTS
# Path(__file__) is THIS file's path. .parent goes up one folder.
# We use this so paths work no matter where the project is on disk.
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent.parent  # project root folder
LOG_DIR = BASE_DIR / "logs"              # where log files go

# -----------------------------------------------------------------------------
# 3. SETTINGS read from environment variables (with sensible defaults).
# os.getenv("NAME", "default_value") returns the env var or the default.
# -----------------------------------------------------------------------------

# DEBUG mode: turns on verbose logging.
# Note: env vars are always strings, so we compare to "True".
DEBUG = os.getenv("DEBUG", "False") == "True"

# A user-facing name the app uses when greeting.
APP_USER_NAME = os.getenv("APP_USER_NAME", "Friend")

# An example secret (we never put real secrets directly in code).
API_KEY = os.getenv("API_KEY", "")

# -----------------------------------------------------------------------------
# 4. STATIC SETTINGS that don't change between environments.
# -----------------------------------------------------------------------------
APP_NAME = "Learning Python Concepts"
APP_VERSION = "0.1.0"
