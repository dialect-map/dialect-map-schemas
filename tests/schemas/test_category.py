# -*- coding: utf-8 -*-

import pytest

from copy import deepcopy
from datetime import datetime

from src.dialect_map_schemas import CategorySchema


class TestCategorySchema:
    """Class to group all the Category schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test Category values
        :return: dictionary with test Category values
        """

        return {
            "category_id": "category-id",
            "description": "example text",
            "archived": True,
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_alternative_keys(self, test_data: dict):
        """
        Tests the correct extraction of alternative key values
        :param test_data: test Category values
        """

        schema = CategorySchema()

        cat_data = deepcopy(test_data)
        cat_data.pop("category_id")
        cat_data.pop("description")
        cat_data["id"] = "alt-id"
        cat_data["name"] = "alt-desc"

        record = schema.load(cat_data)

        assert isinstance(record, dict)
        assert record.get("category_id") == "alt-id"
        assert record.get("description") == "alt-desc"
