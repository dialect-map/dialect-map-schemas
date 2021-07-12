# -*- coding: utf-8 -*-

from abc import abstractmethod
from datetime import datetime

from marshmallow import EXCLUDE
from marshmallow import pre_load
from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import validates_schema
from marshmallow.fields import Field


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
    def pre_populate(self, data: dict, **_) -> dict:
        """
        Perform preliminary population of fields before the standard loading
        :param data: dictionary with schema fields
        :param _: rest of object creation arguments
        """

        ### NOTE:
        ###
        ### These functions take advantage of the multi-purpose 'metadata'
        ### field argument in order to define:
        ###
        ### - Deserializing alternative keys.
        ### - Deserializing context gettable keys.
        ### - Deserializing context settable keys.
        ###
        ### This is a cleaner approach than defining one 'pre_load' function
        ### for each field that defines any deserializing custom behaviour
        ###
        data = self._get_alt_values(data)
        data = self._get_ctx_values(data)

        self._set_ctx_values(data)
        return data

    def _get_alt_values(self, data: dict) -> dict:
        """
        Retrieves alternative key values from the provided data
        :param data: dictionary with the schema keys
        :return: new dictionary
        """

        for name, field in self.fields.items():
            if name in data:
                continue

            key = field.metadata.get("ALT")
            val = data.get(key)

            if val is not None:
                data[name] = val

        return data

    def _get_ctx_values(self, data: dict) -> dict:
        """
        Retrieves alternative key values from the provided context
        :param data: dictionary with the schema keys
        :return: new dictionary
        """

        for name, field in self.fields.items():
            if name in data:
                continue

            key = field.metadata.get("CTX_GET")
            val = self.context.get(key)

            if val is not None:
                data[name] = val

        return data

    def _set_ctx_values(self, data: dict) -> None:
        """
        Stores provided key values inside the context
        :param data: dictionary with the schema keys
        """

        for name, field in self.fields.items():
            key = field.metadata.get("CTX_SET")
            val = data.get(name)

            if key is not None and val is not None:
                self.context[key] = val


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
            raise ValidationError("The archival date cannot be prior the creation date")


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
