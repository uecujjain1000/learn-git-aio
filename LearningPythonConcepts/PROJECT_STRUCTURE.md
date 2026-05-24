# Project Structure Explained

This document explains **every file and folder** in this project, what role it plays, and why projects usually include it. Read this top to bottom.

---

## 1. `README.md`
The "front page" of the project. The first thing anyone (including future-you) reads. Written in Markdown. Should answer: what is this, how do I install it, how do I run it.

---

## 2. `requirements.txt`
A plain-text list of **external Python packages** the project depends on, with optional pinned versions.

Example line: `requests==2.31.0`

Install all of them at once with:
```
pip install -r requirements.txt
```

Why it exists: so anyone can recreate your exact environment with one command.

---

## 3. `setup.py`
A script that tells Python how to **package and install** this project. It defines the project name, version, author, and dependencies. With it, you can run `pip install .` to install your own project like any other library.

Modern alternative: `pyproject.toml`. We use `setup.py` here because it's the classic form most tutorials show.

---

## 4. `.gitignore`
A list of file/folder **patterns Git should ignore** when committing. We don't want to commit:
- `__pycache__/` (Python's compiled bytecode cache)
- `.env` (contains secrets like API keys)
- `venv/` (virtual environment - too large, machine-specific)
- `*.pyc` (compiled Python files)

---

## 5. `.env.example`
A **template** showing which environment variables the app needs. Users copy this to `.env` and fill in their actual values. The real `.env` is `.gitignore`d so secrets never leak into the repo.

Example:
```
API_KEY=your_api_key_here
DEBUG=True
```

---

## 6. `config/` folder

### `config/__init__.py`
An **empty file** that tells Python: "treat this folder as a package, so you can `import config`." Every folder you want to import from needs this file.

### `config/config.py`
Holds **all configuration** in one place: constants, file paths, default settings. Loads values from environment variables (`.env`). Keeping config separate from code means you can change behavior without editing logic.

---

## 7. `src/` folder
Short for "source". Contains the actual program code. Separating source from tests, config, and docs is standard practice.

### `src/__init__.py`
Marks `src` as a package so you can do `from src import calculator`.

### `src/main.py`
The **entry point**. Run this file to start the app. Convention: every project has a single, obvious "where do I start reading?" file. Often contains an `if __name__ == "__main__":` block.

### `src/calculator.py`
Example **business logic module**. Contains the `Calculator` class with `add`, `subtract`, `multiply`, `divide` functions. In a real project, each major feature gets its own module file.

### `src/utils/` folder
**Reusable helpers** that don't belong to any specific feature - logging setup, string helpers, date utilities, etc.

#### `src/utils/logger.py`
Sets up Python's `logging` module so the rest of the code can do `logger.info("something happened")` instead of `print(...)`. `print` is for quick scripts; `logging` is for real apps because it has levels (DEBUG/INFO/WARNING/ERROR), timestamps, and can write to files.

#### `src/utils/helpers.py`
Catch-all for small utility functions used in multiple places.

---

## 8. `tests/` folder
Holds **unit tests** - small bits of code that verify your real code works correctly.

### `tests/__init__.py`
Marks `tests` as a package.

### `tests/test_calculator.py`
Tests for `src/calculator.py`. Convention: test files are named `test_<thing_being_tested>.py`. Run them with:
```
python -m unittest discover tests
```

---

## Summary: Categories of Files in Any Python Project

| Category | Examples in this project |
|----------|--------------------------|
| **Documentation** | `README.md`, `PROJECT_STRUCTURE.md` |
| **Dependencies** | `requirements.txt`, `setup.py` |
| **Configuration** | `config/config.py`, `.env`, `.env.example` |
| **Source code** | `src/main.py`, `src/calculator.py` |
| **Utilities** | `src/utils/logger.py`, `src/utils/helpers.py` |
| **Tests** | `tests/test_calculator.py` |
| **Version control** | `.gitignore` |
| **Package markers** | every `__init__.py` |

When you start any new Python project, ask yourself: "where does each new file belong in these categories?"
