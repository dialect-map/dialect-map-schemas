# -*- coding: utf-8 -*-

import pytest

from copy import deepcopy
from datetime import datetime
from marshmallow import fields

from src.dialect_map_schemas import BaseSchema
from src.dialect_map_schemas import BaseStaticSchema
from src.dialect_map_schemas import BaseArchivalSchema
from src.dialect_map_schemas import BaseEvolvingSchema
from src.dialect_map_schemas import SchemaError


class Child(BaseSchema):
    """Child schema to use during the tests"""

    child_id = fields.String(required=True)
    inherited = fields.String(required=True, metadata={"CTX_GET": "ctx_key"})


class Parent(BaseSchema):
    """Parent schema to use during the tests"""

    parent_id = fields.String(required=True, metadata={"ALT": "other_id"})
    field_ctx = fields.String(required=True, metadata={"CTX_SET": "ctx_key"})
    children = fields.Nested(required=True, nested=Child, many=True)


class TestBaseSchema:
    """Class to group all the BaseSchema tests"""

    def test_load_alternative_keys(self):
        """Tests the correct extraction of alternative key values"""

        parent_data = {
            "other_id": "parent-id",
            "field_ctx": "value-ctx",
            "children": [],
        }

        parent_copy = deepcopy(parent_data)

        schema = Parent()
        record = schema.load(parent_data)

        # Assert that the original dictionary is preserved
        assert parent_data == parent_copy
        assert record.get("other_id") is None
        assert record.get("parent_id") == "parent-id"

    def test_load_from_context(self):
        """Tests the correct extraction of values from the context"""

        children_data = [
            {"child_id": "child-1"},
            {"child_id": "child-2"},
        ]

        children_copy = deepcopy(children_data)

        schemas = Child(many=True)
        schemas.context = {"ctx_key": "ctx-val"}
        records = schemas.load(children_data)

        # Assert that the original list is preserved
        assert children_data == children_copy
        assert all(record.get("inherited") == "ctx-val" for record in records)

    def test_load_into_context(self):
        """Tests the correct storage of values into the context"""

        parent_data = {
            "parent_id": "parent-id",
            "field_ctx": "value-ctx",
            "children": [],
        }
        parent_copy = deepcopy(parent_data)

        schema = Parent()
        record = schema.load(parent_data)

        # Assert that the original dictionary is preserved
        assert parent_data == parent_copy
        assert parent_data == record
        assert schema.context.get("ctx_key") == "value-ctx"


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
