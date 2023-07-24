# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseSchema
from .base import StaticSchema
from .base import EvolvingSchema
from .validators import arxiv_rev_range
from .validators import paper_ref_count


class PaperSchema(BaseSchema, EvolvingSchema):
    """ArXiv paper de/serializing schema"""

    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    title = fields.String(required=True)
    doi_id = fields.String(required=False)
    url_pdf = fields.URL(required=False)
    url_dvi = fields.URL(required=False)
    url_html = fields.URL(required=False)
    url_latex = fields.URL(required=False)
    url_posts = fields.URL(required=False)
    revision_date = fields.Date(required=False)
    submission_date = fields.Date(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.arxiv_id.name)


class PaperAuthorSchema(BaseSchema, StaticSchema):
    """ArXiv paper author de/serializing schema"""

    author_id = fields.String(required=False, dump_only=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    author_name = fields.String(required=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.author_id.name)


class PaperReferenceCountersSchema(BaseSchema, StaticSchema):
    """ArXiv paper reference counters de/serializing schema"""

    count_id = fields.String(required=False, dump_only=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    arxiv_ref_count = fields.Integer(required=True, validate=paper_ref_count, strict=True)
    total_ref_count = fields.Integer(required=True, validate=paper_ref_count, strict=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.count_id.name)
