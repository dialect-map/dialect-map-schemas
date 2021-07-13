# Dialect map schemas

### About
This repository contains the data schemas shared across the different components.

Data schemas are logical abstractions wrapping database data model definitions that
are use by different software components to either serialize or deserialize certain
attributes of those models (or the models in their entirety).


### Dependencies
Python dependencies are specified within the `setup.py` file.

In order to install the development packages, as long as the defined commit hooks:
```sh
pip install ".[dev]"
pre-commit install
```


### Formatting
All Python files are formatted using [Black][black-web], and the custom properties defined
in the `pyproject.toml` file.
```sh
make check
```


### Testing
Project testing is performed using [Pytest][pytest-web]. In order to run the tests:
```sh
make test
```


### Tagging
Commits can be tagged to create _informal_ releases of the package. In order to do so:

1. Bump up the package version (`VERSION`) following [Semantic Versioning][semantic-web].
2. Create and push a tag: `make tag`.


[black-web]: https://black.readthedocs.io/en/stable/
[pytest-web]: https://docs.pytest.org/en/latest/#
[semantic-web]: https://semver.org/
