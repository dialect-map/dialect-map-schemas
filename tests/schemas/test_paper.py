# -*- coding: utf-8 -*-

import pytest

from copy import deepcopy
from datetime import date
from datetime import datetime

from src.dialect_map_schemas import PaperSchema
from src.dialect_map_schemas import PaperReferenceCountersSchema
from src.dialect_map_schemas import SchemaError


class TestPaperSchema:
    """Class to group all the Paper schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test Paper values
        :return: dictionary with test Paper values
        """

        return {
            "arxiv_id": "paper-id",
            "arxiv_rev": 1,
            "title": "example",
            "submission_date": date.today().isoformat(),
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid Paper schema values
        :param test_data: test Paper values
        """

        schema = PaperSchema()

        paper_data = deepcopy(test_data)
        paper_data["arxiv_id"] = "paper-id-test"
        paper_data["arxiv_rev"] = 10

        record = schema.load(paper_data)

        assert isinstance(record, dict)
        assert record.get("arxiv_id") == "paper-id-test"
        assert record.get("arxiv_rev") == 10


class TestCPaperAuthorSchema:
    """Class to group all the PaperAuthor schema tests"""

    pass


class TestPaperReferenceCountersSchema:
    """Class to group all the PaperReferenceCounters schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test PaperReferenceCounters values
        :return: dictionary with test PaperReferenceCounters values
        """

        return {
            "arxiv_id": "arxiv-id",
            "arxiv_rev": 1,
            "arxiv_ref_count": 10,
            "total_ref_count": 20,
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid PaperReferenceCounters schema values
        :param test_data: test PaperReferenceCounters values
        """

        schema = PaperReferenceCountersSchema()

        data = deepcopy(test_data)
        record = schema.load(data)

        assert isinstance(record, dict)

    def test_load_invalid_arxiv_refs(self, test_data: dict):
        """
        Tests the correct validation of invalid ArXiv references value
        :param test_data: test PaperReferenceCounters values
        """

        schema = PaperReferenceCountersSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "arxiv_ref_count": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "arxiv_ref_count": +1.5})

    def test_load_invalid_total_refs(self, test_data: dict):
        """
        Tests the correct validation of invalid total references value
        :param test_data: test PaperReferenceCounters values
        """

        schema = PaperReferenceCountersSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "total_ref_count": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "total_ref_count": +1.5})
