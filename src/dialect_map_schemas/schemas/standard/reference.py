# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema
from .validators import arxiv_rev_range


class PaperReferenceSchema(BaseStaticSchema):
    """ArXiv paper reference de/serializing schema"""

    reference_id = fields.String(required=False, dump_only=True)
    source_arxiv_id = fields.String(required=True)
    source_arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    target_arxiv_id = fields.String(required=True)
    target_arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.reference_id.name)
