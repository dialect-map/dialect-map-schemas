# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseArchivalSchema


class CategorySchema(BaseArchivalSchema):
    """Category de/serializing schema"""

    category_id = fields.String(required=True, metadata={"ALT": "id"})
    description = fields.String(required=True, metadata={"ALT": "name"})
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    archived_at = fields.DateTime(required=False)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.category_id.name)
