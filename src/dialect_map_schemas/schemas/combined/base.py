# -*- coding: utf-8 -*-

from marshmallow import Schema


class BaseCombinedSchema(Schema):
    """Base class for every combined schema"""

    @property
    def schema_id(self) -> None:
        """
        Raises an AttributeError as combined schemas do not have specific IDs
        :return: AttributeError
        """

        raise AttributeError()

    @property
    def name(self) -> str:
        """
        Gets the schema name
        :return: schema name
        """

        return self.__class__.__name__
