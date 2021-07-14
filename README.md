# Dialect map schemas

### About
This repository contains the data schemas shared across the different components.

Data schemas are logical abstractions wrapping database data model definitions that
are use by different software components to either serialize or deserialize certain
attributes of those models (or the models in their entirety).


### Documentation
For more information about data schemas and their relationship to [the core package][dialect-map-core]
defined data models:

- [Data schemas][docs-schemas].


### Dependencies
Python dependencies are specified within the `setup.py` file.

In order to install the development packages, as long as the defined commit hooks:
```sh
pip install ".[dev]"
pre-commit install
```


### Formatting
All Python files are formatted using [Black][web-black], and the custom properties defined
in the `pyproject.toml` file.
```sh
make check
```


### Testing
Project testing is performed using [Pytest][web-pytest]. In order to run the tests:
```sh
make test
```


### Tagging
Commits can be tagged to create _informal_ releases of the package. In order to do so:

1. Bump up the package version (`VERSION`) following [Semantic Versioning][web-semver].
2. Create and push a tag: `make tag`.


[dialect-map-core]: https://github.com/dialect-map/dialect-map-core
[docs-schemas]: docs/schemas.md
[web-black]: https://black.readthedocs.io/en/stable/
[web-pytest]: https://docs.pytest.org/en/latest/#
[web-semver]: https://semver.org/
