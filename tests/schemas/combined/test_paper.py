# -*- coding: utf-8 -*-

from copy import deepcopy
from datetime import date
from datetime import datetime
from datetime import timezone

import pytest

from src.dialect_map_schemas import PaperMetadataSchema
from src.dialect_map_schemas import SchemaError


class TestPaperMetadataSchema:
    """Class to group all the PaperMetadata schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test PaperMetadata values
        :return: dictionary with test PaperMetadata values
        """

        paper_id = "paper-id"
        paper_rev = 1
        time_now = datetime.now(timezone.utc).isoformat()

        return {
            "paper": {
                "arxiv_id": paper_id,
                "arxiv_rev": paper_rev,
                "title": "example",
                "submission_date": date.today().isoformat(),
                "created_at": time_now,
                "updated_at": time_now,
            },
            "authors": [
                {
                    "arxiv_id": paper_id,
                    "arxiv_rev": paper_rev,
                    "author_name": "John Doe",
                    "created_at": time_now,
                },
            ],
            "memberships": [],
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid PaperMetadata schema values
        :param test_data: test PaperMetadata values
        """

        schema = PaperMetadataSchema()

        record = schema.load(test_data)

        assert isinstance(record, dict)
        assert isinstance(record["paper"], dict)
        assert isinstance(record["authors"], list)
        assert isinstance(record["memberships"], list)

        assert record["paper"]["arxiv_id"] == "paper-id"
        assert record["paper"]["arxiv_rev"] == 1

    def test_load_invalid_identifier(self, test_data: dict):
        """
        Tests the correct validation of inconsistent identifier values
        :param test_data: test PaperMetadata values
        """

        schema = PaperMetadataSchema()

        paper_metadata = deepcopy(test_data)
        paper_metadata["paper"]["arxiv_id"] = "other"
        paper_metadata["paper"]["arxiv_rev"] = 10

        assert pytest.raises(SchemaError, schema.load, paper_metadata)

    def test_load_invalid_creation_date(self, test_data: dict):
        """
        Tests the correct validation of inconsistent creation date values
        :param test_data: test PaperMetadata values
        """

        schema = PaperMetadataSchema()

        paper_metadata = deepcopy(test_data)
        paper_metadata["paper"]["created_at"] = datetime.now(timezone.utc).isoformat()

        assert pytest.raises(SchemaError, schema.load, paper_metadata)
