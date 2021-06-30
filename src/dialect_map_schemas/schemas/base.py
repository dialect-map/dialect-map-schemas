# -*- coding: utf-8 -*-

from datetime import datetime

from marshmallow import EXCLUDE
from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import validates_schema


class BaseSchema(Schema):
    """Base schema to set up additional-field handling"""

    class Meta:
        """
        Metaclass to define serialization properties

        :attr unknown: how to handle unknown fields.
        Ref: https://marshmallow.readthedocs.io/en/stable/quickstart.html#handling-unknown-fields
        """

        unknown = EXCLUDE


class BaseStaticSchema(BaseSchema):
    """Base class defining validations for the static models"""


class BaseArchivalSchema(BaseSchema):
    """Base class defining validations for the archival models"""

    @validates_schema
    def validate_archival_date(self, data: dict, **_):
        """
        Validates the relationship between the archival date and the creation date
        :param data: dictionary with schema fields
        :param _: rest of object creation arguments
        """

        created_date = data.get("created_at")
        archived_date = data.get("archived_at")

        if (
            True
            and isinstance(created_date, datetime)
            and isinstance(archived_date, datetime)
            and created_date > archived_date
        ):
            raise ValidationError(f"The archival date cannot be prior the creation date")


class BaseEvolvingSchema(BaseSchema):
    """Base class defining validations for the evolving models"""

    @validates_schema
    def validate_update_date(self, data: dict, **_):
        """
        Validates the relationship between the updated date and the creation date
        :param data: dictionary with schema fields
        :param _: rest of object creation arguments
        """

        created_date = data.get("created_at")
        updated_date = data.get("updated_at")

        if (
            True
            and isinstance(created_date, datetime)
            and isinstance(updated_date, datetime)
            and created_date > updated_date
        ):
            raise ValidationError("The update date cannot be prior to the creation date")
