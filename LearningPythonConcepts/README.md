# Learning Python Concepts

A beginner-friendly Python project designed to demonstrate the typical structure and components of a real-world Python project.

## What This Project Teaches

This is a simple **Calculator + Greeting App** built with proper project structure. The goal is not the app itself but to learn:

- How Python projects are organized into folders and modules
- What each special file does (`requirements.txt`, `.gitignore`, `setup.py`, etc.)
- How to separate configuration, source code, tests, and utilities
- How to use logging, environment variables, and configuration files
- How to write and run unit tests

## Project Structure

```
LearningPythonConcepts/
│
├── README.md                  # This file - project overview
├── PROJECT_STRUCTURE.md       # Detailed explanation of every file
├── requirements.txt           # List of external Python packages needed
├── setup.py                   # Makes project installable as a package
├── .gitignore                 # Tells Git which files to ignore
├── .env.example               # Template for environment variables
│
├── config/                    # All configuration lives here
│   ├── __init__.py
│   └── config.py              # App settings (constants, paths, etc.)
│
├── src/                       # All source code (the actual program)
│   ├── __init__.py
│   ├── main.py                # The entry point - run this file
│   ├── calculator.py          # Example business-logic module
│   └── utils/                 # Reusable helper modules
│       ├── __init__.py
│       ├── logger.py          # Sets up logging
│       └── helpers.py         # Misc helper functions
│
└── tests/                     # Unit tests live here
    ├── __init__.py
    └── test_calculator.py     # Tests for calculator.py
```

## How to Run

1. **Install dependencies** (only needed once):
   ```
   pip install -r requirements.txt
   ```

2. **Copy the env template** and fill in your values:
   ```
   copy .env.example .env
   ```

3. **Run the app**:
   ```
   python -m src.main
   ```

4. **Run the tests**:
   ```
   python -m unittest discover tests
   ```

## Next Steps

Open `PROJECT_STRUCTURE.md` to read a detailed line-by-line explanation of what every file in this project does and why it exists.
