# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Type
from typing import Union

from ..schemas import BaseStaticSchema
from ..schemas import BaseArchivalSchema
from ..schemas import BaseEvolvingSchema
from ..schemas import BaseCombinedSchema


# Generic base schema type
Schema = Union[
    BaseCombinedSchema,
    BaseArchivalSchema,
    BaseEvolvingSchema,
    BaseStaticSchema,
]


@dataclass
class APIRoute:
    """
    Object containing the basic information for a remote API route

    :attr api_name: informative name of the API
    :attr api_path: specific path within the API base URL
    :attr schema: specific data model schema associated to the route
    """

    api_name: str
    api_path: str
    schema: Type[Schema]
