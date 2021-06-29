PKG_VERSION   = $(shell cat VERSION)
SOURCE_FOLDER = "src"
TESTS_FOLDER  = "tests"


.PHONY: check
check:
	@echo "Checking code format"
	@black --check $(SOURCE_FOLDER)
	@black --check $(TESTS_FOLDER)
	@echo "Checking type annotations"
	@mypy $(SOURCE_FOLDER)
	@mypy $(TESTS_FOLDER)


.PHONY: tag
tag:
	@echo "Tagging current commit"
	@git tag --annotate "v$(PKG_VERSION)" --message "Tag v$(PKG_VERSION)"
	@git push --follow-tags
