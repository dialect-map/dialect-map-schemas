# -*- coding: utf-8 -*-

from copy import deepcopy
from datetime import datetime

import pytest

from src.dialect_map_schemas import JargonSchema
from src.dialect_map_schemas import JargonGroupSchema
from src.dialect_map_schemas import SchemaError


class TestJargonSchema:
    """Class to group all the Jargon schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test Jargon values
        :return: dictionary with test Jargon values
        """

        return {
            "group_id": "group-0",
            "jargon_id": "group-0-jargon-0",
            "jargon_term": "jargon-term",
            "jargon_regex": "jargon[ -]term",
            "archived": True,
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid Jargon schema values
        :param test_data: test Jargon values
        """

        schema = JargonSchema()

        jargon_data = deepcopy(test_data)
        jargon_data["group_id"] = "group-1"
        jargon_data["jargon_id"] = "group-1-jargon-0"
        jargon_data["jargon_term"] = "term"

        record = schema.load(jargon_data)

        assert isinstance(record, dict)
        assert record.get("group_id") == "group-1"
        assert record.get("jargon_id") == "group-1-jargon-0"
        assert record.get("jargon_term") == "term"

    def test_load_invalid_group_id(self, test_data: dict):
        """
        Tests the correct validation of invalid group ID values
        :param test_data: test Jargon values
        """

        schema = JargonSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "001"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "group"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "group-no"})

    def test_load_invalid_jargon_id(self, test_data: dict):
        """
        Tests the correct validation of invalid jargon ID values
        :param test_data: test Jargon values
        """

        schema = JargonSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_id": "001"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_id": "group"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_id": "group-no"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_id": "group-0"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_id": "group-0-jargon"})

    def test_load_invalid_jargon_term(self, test_data: dict):
        """
        Tests the correct validation of invalid jargon term values
        :param test_data: test Jargon values
        """

        schema = JargonSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_term": "001"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_term": "term "})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_term": "term-"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_term": " term"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "jargon_term": "-term"})


class TestJargonGroupSchema:
    """Class to group all the JargonGroup schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test JargonGroup values
        :return: dictionary with test JargonGroup values
        """

        return {
            "group_id": "group-0",
            "description": "example text",
            "archived": True,
            "jargons": [],
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_nested_schemas(self, test_data: dict):
        """
        Tests the correct loading of nested schemas
        :param test_data: test JargonGroup values
        """

        schema = JargonGroupSchema()
        dt_now = datetime.utcnow()

        group_data = deepcopy(test_data)
        group_data["created_at"] = dt_now.isoformat()
        group_data["jargons"] = [
            {
                "group_id": "group-1",
                "jargon_id": "group-1-jargon-1",
                "jargon_term": "jargon-term",
                "jargon_regex": "jargon[ -]term",
                "archived": False,
            },
            {
                "group_id": "group-1",
                "jargon_id": "group-2-jargon-2",
                "jargon_term": "jargon-term",
                "jargon_regex": "jargon[ -]term",
                "archived": False,
            },
        ]

        record = schema.load(group_data)
        jargons = record["jargons"]

        assert jargons[0].get("created_at") == dt_now
        assert jargons[1].get("created_at") == dt_now

    def test_load_invalid_group_id(self, test_data: dict):
        """
        Tests the correct validation of invalid group ID values
        :param test_data: test JargonGroup values
        """

        schema = JargonGroupSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "001"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "group"})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "group_id": "group-no"})
