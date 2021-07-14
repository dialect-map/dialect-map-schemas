# -*- coding: utf-8 -*-

from marshmallow import fields
from marshmallow import validates

from .base import BaseStaticSchema


class JargonCategoryMetrics(BaseStaticSchema):
    """Jargon - category NLP metrics de/serializing schema"""

    metric_id = fields.String(required=False)
    jargon_id = fields.String(required=True)
    category_id = fields.String(required=True)
    abs_freq = fields.Integer(required=True, strict=True)
    rel_freq = fields.Float(required=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.metric_id.name)

    @validates("abs_freq")
    def validate_abs_freq(self, freq: int):
        """
        Validates jargon absolute frequency within a category
        :param freq: jargon term occurrences within a category
        """

        assert freq >= 0, f"Invalid absolute frequency: {freq}"

    @validates("rel_freq")
    def validate_rel_freq(self, freq: float):
        """
        Validates jargon relative frequency within a category
        :param freq: jargon term relative frequency within a category
        """

        assert freq >= 0, f"Invalid relative frequency: {freq}"
        assert freq <= 1, f"Invalid relative frequency: {freq}"


class JargonPaperMetrics(BaseStaticSchema):
    """Jargon - paper NLP metrics de/serializing schema"""

    metric_id = fields.String(required=False)
    jargon_id = fields.String(required=True)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True, strict=True)
    abs_freq = fields.Integer(required=True, strict=True)
    rel_freq = fields.Float(required=True)
    created_at = fields.DateTime(required=True)

    @property
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        return str(self.metric_id.name)

    @validates("abs_freq")
    def validate_abs_freq(self, freq: int):
        """
        Validates jargon absolute frequency within a paper
        :param freq: jargon term occurrences within a paper
        """

        assert freq >= 0, f"Invalid absolute frequency: {freq}"

    @validates("rel_freq")
    def validate_rel_freq(self, freq: float):
        """
        Validates jargon relative frequency within a paper
        :param freq: jargon term relative frequency within a paper
        """

        assert freq >= 0, f"Invalid relative frequency: {freq}"
        assert freq <= 1, f"Invalid relative frequency: {freq}"
