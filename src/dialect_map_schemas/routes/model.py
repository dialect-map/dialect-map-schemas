# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Type
from typing import Union

from ..schemas import StaticSchema
from ..schemas import ArchivalSchema
from ..schemas import EvolvingSchema
from ..schemas import BaseCombinedSchema


# Generic base schema type
Schema = Union[
    BaseCombinedSchema,
    ArchivalSchema,
    EvolvingSchema,
    StaticSchema,
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
