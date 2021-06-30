# -*- coding: utf-8 -*-

from marshmallow import ValidationError


def get_from_keys(data: dict, keys: list) -> object:
    """
    Gets the first existing value from a list of dictionary keys
    :param data: dictionary to check for the keys
    :param keys: list of keys to check
    :return: value
    """

    for key in keys:
        try:
            return data[key]
        except KeyError:
            pass

    raise ValidationError("None of the alternative data keys was found")
