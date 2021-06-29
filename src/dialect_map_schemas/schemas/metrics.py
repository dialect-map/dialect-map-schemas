# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema


class JargonCategoryMetrics(BaseStaticSchema):
    """ArXiv category jargon NLP metrics"""

    metric_id = fields.String(required=False)
    jargon_id = fields.String(required=True)
    category_id = fields.String(required=True)
    abs_freq = fields.Integer(required=True)
    rel_freq = fields.Float(required=True)
    created_at = fields.DateTime(required=True)


class JargonPaperMetrics(BaseStaticSchema):
    """ArXiv paper jargon NLP metrics"""

    metric_id = fields.String(required=False)
    jargon_id = fields.String(required=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True)
    abs_freq = fields.Integer(required=True)
    rel_freq = fields.Float(required=True)
    created_at = fields.DateTime(required=True)
