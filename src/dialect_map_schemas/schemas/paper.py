# -*- coding: utf-8 -*-

from marshmallow import fields
from marshmallow import validates

from .base import BaseStaticSchema
from .base import BaseEvolvingSchema


class Paper(BaseEvolvingSchema):
    """ArXiv paper de/serializing schema"""

    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, strict=True)
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


class PaperAuthor(BaseStaticSchema):
    """ArXiv paper author de/serializing schema"""

    author_id = fields.String(required=False)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, strict=True)
    author_name = fields.String(required=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.author_id.name)


class PaperReferenceCounters(BaseStaticSchema):
    """ArXiv paper reference counters de/serializing schema"""

    count_id = fields.String(required=False)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, strict=True)
    arxiv_ref_count = fields.Integer(required=True, strict=True)
    total_ref_count = fields.Integer(required=True, strict=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.count_id.name)

    @validates("arxiv_ref_count")
    def validate_arxiv_ref_count(self, count: int):
        """
        Validates paper ArXiv internal references
        :param count: paper ArXiv internal references
        """

        assert count >= 0, f"Invalid references count: {count}"

    @validates("total_ref_count")
    def validate_total_ref_count(self, count: int):
        """
        Validates paper total references
        :param count: paper total references
        """

        assert count >= 0, f"Invalid references count: {count}"
