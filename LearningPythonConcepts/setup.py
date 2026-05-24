"""
setup.py
-------------------------------------------------------------------------------
This file makes the project INSTALLABLE as a Python package.

After writing this file, you can run:
    pip install .

...and your project becomes importable from anywhere on your machine, just
like 'requests' or 'numpy'.

Modern projects increasingly use 'pyproject.toml' instead, but setup.py is
still the most common form you'll see in tutorials.
-------------------------------------------------------------------------------
"""

from setuptools import setup, find_packages

setup(
    # Name of the package as it would appear on PyPI (the Python package index)
    name="learning_python_concepts",

    # Version number. Convention: MAJOR.MINOR.PATCH (Semantic Versioning).
    version="0.1.0",

    # Short, one-line description
    description="A beginner project that demonstrates Python project structure.",

    # Who wrote it
    author="Deepak Singh Tomar",
    author_email="deepaksinghtomar88@gmail.com",

    # Automatically discover all subpackages (folders with __init__.py)
    packages=find_packages(),

    # External dependencies. Mirrors what's in requirements.txt.
    install_requires=[
        "python-dotenv>=1.0.0",
    ],

    # Minimum Python version required
    python_requires=">=3.8",
)
