# -*- coding: utf-8 -*-

import pytest

from datetime import datetime

from src.dialect_map_schemas import BaseStaticSchema
from src.dialect_map_schemas import BaseArchivalSchema
from src.dialect_map_schemas import BaseEvolvingSchema
from src.dialect_map_schemas import SchemaError


class TestBaseStaticSchema:
    """
    Class to group all the BaseStatic schema tests

    Given that the base schemas define no fields, the @validates_schema
    decorated method needs to be called directly, instead of relying on the standard validate()
    """

    pass


class TestBaseArchivalSchema:
    """
    Class to group all the BaseArchival schema tests

    Given that the base schemas define no fields, the @validates_schema
    decorated method needs to be called directly, instead of relying on the standard validate()
    """

    def test_valid_archived_at(self):
        """Tests the correct validation of the valid datetime fields"""

        schema = BaseArchivalSchema()
        dt_now = datetime.utcnow()

        record = {
            "created_at": dt_now,
            "archived_at": dt_now,
        }

        assert schema.validate_archival_date(record) is None

    def test_invalid_archived_at(self):
        """Tests the correct validation of the invalid datetime fields"""

        schema = BaseArchivalSchema()
        tm_now = datetime.utcnow().timestamp()

        record = {
            "created_at": datetime.fromtimestamp(tm_now + 1),
            "archived_at": datetime.fromtimestamp(tm_now + 0),
        }

        assert pytest.raises(SchemaError, schema.validate_archival_date, record)


class TestBaseEvolvingSchema:
    """
    Class to group all the BaseEvolving schema tests

    Given that the base schemas define no fields, the @validates_schema
    decorated method needs to be called directly, instead of relying on the standard validate()
    """

    def test_valid_updated_at(self):
        """Tests the correct validation of the valid datetime fields"""

        schema = BaseEvolvingSchema()
        dt_now = datetime.utcnow()

        record = {
            "created_at": dt_now,
            "updated_at": dt_now,
        }

        assert schema.validate_update_date(record) is None

    def test_invalid_updated_at(self):
        """Tests the correct validation of the invalid datetime fields"""

        schema = BaseEvolvingSchema()
        tm_now = datetime.utcnow().timestamp()

        record = {
            "created_at": datetime.fromtimestamp(tm_now + 1),
            "updated_at": datetime.fromtimestamp(tm_now + 0),
        }

        assert pytest.raises(SchemaError, schema.validate_update_date, record)
