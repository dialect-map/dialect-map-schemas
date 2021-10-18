# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


# Package meta-data
NAME = "dialect-map-schemas"
INFO = "Python package containing the data schemas for the Dialect Map"
URL = "https://github.com/dialect-map/dialect-map-schemas"
REQUIRES_PYTHON = ">=3.7, <4"
AUTHORS = "NYU DS3 Team"
VERSION = open("VERSION", "r").read().strip()


# Package requirements
INSTALLATION_REQS = [
    "marshmallow==3.14.0",
]

LINTING_REQS = [
    "black>=21.6b0",
    "mypy>=0.910",
]

TESTING_REQS = [
    "pytest>=6.2.2",
    "pytest-cov>=2.10.0",
]


setup(
    name=NAME,
    version=VERSION,
    description=INFO,
    author=AUTHORS,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=INSTALLATION_REQS,
    extras_require={
        "lint": LINTING_REQS,
        "test": TESTING_REQS,
        "all": [
            *LINTING_REQS,
            *TESTING_REQS,
        ],
    },
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={},
)
