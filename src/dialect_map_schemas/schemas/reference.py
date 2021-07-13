# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema


class PaperReference(BaseStaticSchema):
    """ArXiv paper - paper reference record"""

    reference_id = fields.String(required=False)
    source_arxiv_id = fields.String(required=True)
    source_arxiv_rev = fields.Integer(required=True, strict=True)
    target_arxiv_id = fields.String(required=True)
    target_arxiv_rev = fields.Integer(required=True, strict=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.reference_id.name)
