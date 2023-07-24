# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseSchema
from .base import StaticSchema


class CategoryMembershipSchema(BaseSchema, StaticSchema):
    """Category membership de/serializing schema"""

    membership_id = fields.String(required=False, dump_only=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, strict=True)
    category_id = fields.String(required=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.membership_id.name)
