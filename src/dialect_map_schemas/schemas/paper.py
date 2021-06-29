# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema
from .base import BaseEvolvingSchema


class Paper(BaseEvolvingSchema):
    """ArXiv paper - category membership record"""

    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True)
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


class PaperAuthor(BaseStaticSchema):
    """ArXiv paper author record"""

    author_id = fields.String(required=False)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True)
    author_name = fields.String(required=True)
    created_at = fields.DateTime(required=True)


class PaperReferenceCounters(BaseStaticSchema):
    """ArXiv paper reference counters record"""

    count_id = fields.String(required=False)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True)
    arxiv_ref_count = fields.Integer(required=True)
    total_ref_count = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
