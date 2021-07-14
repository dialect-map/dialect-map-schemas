# -*- coding: utf-8 -*-

import pytest

from copy import deepcopy
from datetime import datetime

from src.dialect_map_schemas import JargonCategoryMetricsSchema
from src.dialect_map_schemas import JargonPaperMetricsSchema
from src.dialect_map_schemas import SchemaError


class TestJargonCategoryMetricsSchema:
    """Class to group all the JargonCategoryMetrics schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test JargonCategoryMetrics values
        :return: dictionary with test JargonCategoryMetrics values
        """

        return {
            "metric_id": "metric-id",
            "jargon_id": "jargon-id",
            "category_id": "category-id",
            "abs_freq": 5,
            "rel_freq": 0.10,
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid JargonCategoryMetrics schema values
        :param test_data: test JargonCategoryMetrics values
        """

        schema = JargonCategoryMetricsSchema()

        metrics_data = deepcopy(test_data)
        metrics_data["metric_id"] = "metric-id-test"
        metrics_data["jargon_id"] = "jargon-id-test"

        record = schema.load(metrics_data)

        assert isinstance(record, dict)
        assert record.get("metric_id") == "metric-id-test"
        assert record.get("jargon_id") == "jargon-id-test"

    def test_load_invalid_abs_freq(self, test_data: dict):
        """
        Tests the correct validation of invalid absolute freq. values
        :param test_data: test JargonCategoryMetrics values
        """

        schema = JargonCategoryMetricsSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": +float(1.5)})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": +float("inf")})

    def test_load_invalid_rel_freq(self, test_data: dict):
        """
        Tests the correct validation of invalid relative freq. values
        :param test_data: test JargonCategoryMetrics values
        """

        schema = JargonCategoryMetricsSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "rel_freq": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "rel_freq": +1.5})


class TestJargonPaperMetricsSchema:
    """Class to group all the JargonPaperMetrics schema tests"""

    @pytest.fixture(scope="class")
    def test_data(self) -> dict:
        """
        Builds a dictionary with test JargonPaperMetrics values
        :return: dictionary with test JargonPaperMetrics values
        """

        return {
            "metric_id": "metric-id",
            "jargon_id": "jargon-id",
            "arxiv_id": "paper-id",
            "arxiv_rev": 1,
            "abs_freq": 5,
            "rel_freq": 0.10,
            "created_at": datetime.utcnow().isoformat(),
        }

    def test_load_valid_values(self, test_data: dict):
        """
        Tests the correct loading of valid JargonPaperMetrics schema values
        :param test_data: test JargonPaperMetrics values
        """

        schema = JargonPaperMetricsSchema()

        metrics_data = deepcopy(test_data)
        metrics_data["metric_id"] = "metric-id-test"
        metrics_data["jargon_id"] = "jargon-id-test"

        record = schema.load(metrics_data)

        assert isinstance(record, dict)
        assert record.get("metric_id") == "metric-id-test"
        assert record.get("jargon_id") == "jargon-id-test"

    def test_load_invalid_abs_freq(self, test_data: dict):
        """
        Tests the correct validation of invalid absolute freq. values
        :param test_data: test JargonPaperMetrics values
        """

        schema = JargonPaperMetricsSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": +float(1.5)})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "abs_freq": +float("inf")})

    def test_load_invalid_rel_freq(self, test_data: dict):
        """
        Tests the correct validation of invalid relative freq. values
        :param test_data: test JargonPaperMetrics values
        """

        schema = JargonPaperMetricsSchema()

        assert pytest.raises(SchemaError, schema.load, {**test_data, "rel_freq": -1})
        assert pytest.raises(SchemaError, schema.load, {**test_data, "rel_freq": +1.5})
