# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseSchema
from .base import ArchivalSchema
from .validators import group_id_regex
from .validators import jargon_id_regex
from .validators import jargon_term_regex


class JargonSchema(BaseSchema, ArchivalSchema):
    """Jargon de/serializing schema"""

    group_id = fields.String(required=False, validate=group_id_regex)
    jargon_id = fields.String(required=True, validate=jargon_id_regex)
    jargon_term = fields.String(required=True, validate=jargon_term_regex)
    jargon_regex = fields.String(required=True)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True, metadata={"CTX_GET": "group_dt"})
    archived_at = fields.DateTime(required=False)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.jargon_id.name)


class JargonGroupSchema(BaseSchema, ArchivalSchema):
    """Jargon group de/serializing schema"""

    group_id = fields.String(required=True, validate=group_id_regex, metadata={"ALT": "id"})
    description = fields.String(required=True)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True, metadata={"CTX_SET": "group_dt"})
    archived_at = fields.DateTime(required=False)

    # List of nested schemas
    jargons = fields.Nested(
        required=True,
        nested=JargonSchema,
        many=True,
    )

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.group_id.name)
