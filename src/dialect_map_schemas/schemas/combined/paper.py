# -*- coding: utf-8 -*-

from marshmallow import fields
from marshmallow import validates_schema

from .base import BaseCombinedSchema
from .validators import validate_arxiv_id
from .validators import validate_arxiv_rev
from .validators import validate_created_at

from ..standard import CategoryMembershipSchema
from ..standard import PaperSchema
from ..standard import PaperAuthorSchema


class PaperMetadataSchema(BaseCombinedSchema):
    """ArXiv paper metadata combined de/serializing schema"""

    paper = fields.Nested(
        PaperSchema,
        required=True,
    )

    authors = fields.List(
        fields.Nested(PaperAuthorSchema),
        required=True,
    )

    memberships = fields.List(
        fields.Nested(CategoryMembershipSchema),
        required=True,
    )

    @validates_schema
    def validate_shared_fields(self, data: dict, **_):
        """
        Validates the consistency among the nested record shared fields
        :param data: dictionary with schema fields
        :param _: rest of object creation arguments
        """

        for field_name in {"authors", "memberships"}:
            self._validate_identifiers(data, target_field=field_name)
            self._validate_creation_date(data, target_field=field_name)

    def _validate_creation_date(self, data: dict, target_field: str):
        """
        Validates the consistency among the nested record creation dates
        :param data: dictionary with schema fields
        :param target_field: field name to validate
        """

        origin_record = data["paper"]
        target_records = data[target_field]

        for record in target_records:
            validate_created_at(origin_record=origin_record, target_record=record)

    def _validate_identifiers(self, data: dict, target_field: str):
        """
        Validates the consistency among the nested record identifiers
        :param data: dictionary with schema fields
        :param target_field: field name to validate
        """

        origin_record = data["paper"]
        target_records = data[target_field]

        for record in target_records:
            validate_arxiv_id(origin_record=origin_record, target_record=record)
            validate_arxiv_rev(origin_record=origin_record, target_record=record)
