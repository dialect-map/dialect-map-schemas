# -*- coding: utf-8 -*-

from abc import abstractmethod
from datetime import datetime

from marshmallow import EXCLUDE
from marshmallow import pre_load
from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import validates_schema
from marshmallow.fields import Field

from .__utils import get_from_keys


class BaseSchema(Schema):
    """Base schema to set up additional-field handling"""

    class Meta:
        """
        Metaclass to define serialization properties

        :attr ordered: how to serialize upon dump.
        :attr unknown: how to handle unknown fields.
        Ref: https://marshmallow.readthedocs.io/en/stable/quickstart.html
        """

        ordered = True
        unknown = EXCLUDE

    def on_bind_field(self, field_name: str, field_obj: Field) -> None:
        """
        Overrides default no-op binding to make field object attrs available
        :param field_name: schema field attribute name
        :param field_obj: schema field instantiated object
        """

        setattr(self, field_name, field_obj)

    @pre_load
    def map_alternative_keys(self, data: dict, **_):
        """
        Maps alternative key values to schema fields.
        :param data: dictionary with schema fields
        :param _: rest of object creation arguments
        """

        ### NOTE:
        ###
        ### This function takes advantage of the multi-purpose 'metadata'
        ### field argument in order to define deserializing alternative keys
        ###
        ### This is a cleaner approach than defining one 'pre_load' function
        ### for each field that defines any deserializing alternative keys
        ###
        for name, field in self.fields.items():
            if field.metadata:
                keys = [name] + field.metadata["alt"]
                data[name] = get_from_keys(data, keys)

        return data


class BaseStaticSchema(BaseSchema):
    """Base class defining validations for the static models"""

    @property
    @abstractmethod
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        raise NotImplementedError()


class BaseArchivalSchema(BaseSchema):
    """Base class defining validations for the archival models"""

    @property
    @abstractmethod
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        raise NotImplementedError()

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

    @property
    @abstractmethod
    def schema_id(self) -> str:
        """
        Gets the ID field name of the schema
        :return: ID field name
        """

        raise NotImplementedError()

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
