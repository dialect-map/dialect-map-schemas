# -*- coding: utf-8 -*-

import re

from marshmallow import fields
from marshmallow import validates

from .base import BaseArchivalSchema


CATEGORY_ID_REGEX = re.compile("^\\w+(-\\w+)?(\\.\\w+)?(-\\w+)?$")


class Category(BaseArchivalSchema):
    """ArXiv category information record"""

    category_id = fields.String(required=True)
    description = fields.String(required=True)
    archived = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    archived_at = fields.DateTime(required=False)

    @validates("category_id")
    def validate_category_id(self, id: str):
        """
        Validates the category ID format
        :param id: category ID
        """

        assert re.match(CATEGORY_ID_REGEX, id), f"Invalid ID: {id}"
