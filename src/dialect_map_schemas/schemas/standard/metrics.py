# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema
from .validators import arxiv_rev_range
from .validators import jargon_abs_freq
from .validators import jargon_rel_freq


class JargonCategoryMetricsSchema(BaseStaticSchema):
    """Jargon - category NLP metrics de/serializing schema"""

    metric_id = fields.String(required=False, dump_only=True)
    jargon_id = fields.String(required=True)
    category_id = fields.String(required=True)
    abs_freq = fields.Integer(required=True, validate=jargon_abs_freq, strict=True)
    rel_freq = fields.Float(required=True, validate=jargon_rel_freq)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.metric_id.name)


class JargonPaperMetricsSchema(BaseStaticSchema):
    """Jargon - paper NLP metrics de/serializing schema"""

    metric_id = fields.String(required=False, dump_only=True)
    jargon_id = fields.String(required=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, validate=arxiv_rev_range, strict=True)
    abs_freq = fields.Integer(required=True, validate=jargon_abs_freq, strict=True)
    rel_freq = fields.Float(required=True, validate=jargon_rel_freq)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.metric_id.name)
