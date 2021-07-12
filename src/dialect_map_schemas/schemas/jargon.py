# -*- coding: utf-8 -*-

import re

from marshmallow import fields
from marshmallow import validates

from .base import BaseArchivalSchema


JARGON_TERM_REGEX = re.compile("^[a-z \\-]+$")
JARGON_ID_REGEX = re.compile("^group-\\d+-jargon-\\d+$")
GROUP_ID_REGEX = re.compile("^group-\\d+$")


class Jargon(BaseArchivalSchema):
    """Jargon term related information record"""

    group_id = fields.String(required=False)
    jargon_id = fields.String(required=True)
    jargon_term = fields.String(required=True)
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

    @validates("group_id")
    def validate_group_id(self, id: str):
        """
        Validates the jargon group ID format
        :param id: jargon group ID
        """

        assert re.match(GROUP_ID_REGEX, id), f"Invalid ID: {id}"

    @validates("jargon_id")
    def validate_jargon_id(self, id: str):
        """
        Validates the jargon ID format
        :param id: jargon ID
        """

        assert re.match(JARGON_ID_REGEX, id), f"Invalid ID: {id}"

    @validates("jargon_term")
    def validate_jargon_term(self, term: str):
        """
        Validates the jargon term format
        :param term: jargon term
        """

        assert re.match(JARGON_TERM_REGEX, term), f"Invalid term: {term}"


class JargonGroup(BaseArchivalSchema):
    """Jargon group to relate jargons with similar meaning"""

    group_id = fields.String(required=True, metadata={"ALT": "id"})
    description = fields.String(required=True)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True, metadata={"CTX_SET": "group_dt"})
    archived_at = fields.DateTime(required=False)

    # List of nested schemas
    jargons = fields.Nested(
        required=True,
        nested=Jargon,
        many=True,
    )

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.group_id.name)

    @validates("group_id")
    def validate_group_id(self, id: str):
        """
        Validates the jargon group ID format
        :param id: jargon group ID
        """

        assert re.match(GROUP_ID_REGEX, id), f"Invalid ID: {id}"
