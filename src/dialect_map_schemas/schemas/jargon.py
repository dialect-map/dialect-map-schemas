# -*- coding: utf-8 -*-

import re

from marshmallow import fields
from marshmallow import validates

from .base import BaseArchivalSchema


JARGON_ID_REGEX = re.compile("^group-\\d+-jargon-\\d+$")
GROUP_ID_REGEX = re.compile("^group-\\d+$")


class Jargon(BaseArchivalSchema):
    """Jargon term related information record"""

    jargon_id = fields.String(required=True, metadata={"alt": ["id"]})
    jargon_term = fields.String(required=True, metadata={"alt": ["name"]})
    jargon_regex = fields.String(required=True, metadata={"alt": ["regex"]})
    group_id = fields.String(required=False)
    num_words = fields.Integer(required=False)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    archived_at = fields.DateTime(required=False)

    @validates("jargon_id")
    def validate_jargon_id(self, id: str):
        """
        Validates the jargon ID format
        :param id: jargon ID
        """

        assert re.match(JARGON_ID_REGEX, id), f"Invalid ID: {id}"

    @validates("group_id")
    def validate_group_id(self, id: str):
        """
        Validates the jargon group ID format
        :param id: jargon group ID
        """

        assert re.match(GROUP_ID_REGEX, id), f"Invalid ID: {id}"


class JargonGroup(BaseArchivalSchema):
    """Jargon group to relate jargons with similar meaning"""

    group_id = fields.String(required=True)
    description = fields.String(required=True)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    archived_at = fields.DateTime(required=False)

    @validates("group_id")
    def validate_group_id(self, id: str):
        """
        Validates the jargon group ID format
        :param id: jargon group ID
        """

        assert re.match(GROUP_ID_REGEX, id), f"Invalid ID: {id}"
