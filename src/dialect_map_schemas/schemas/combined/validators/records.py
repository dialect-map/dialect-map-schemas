# -*- coding: utf-8 -*-

import functools

from marshmallow import ValidationError


def validate_records_field_equality(
    field_name: str,
    error_msg: str,
    origin_record: dict,
    target_record: dict,
) -> None:
    """
    Validates that a certain field is equal between two data records
    :param field_name: field to compare across data records
    :param error_msg: message to display in case of inequality
    :param origin_record: origin data record to compare against
    :param target_record: target data record to compare from
    """

    origin_val = origin_record[field_name]
    target_val = target_record[field_name]

    if origin_val != target_val:
        raise ValidationError(error_msg.format(origin_val=origin_val))


# -------- List of built validators -------- #

validate_arxiv_id = functools.partial(
    validate_records_field_equality,
    field_name="arxiv_id",
    error_msg="The Arxiv ID cannot be different than {origin_val}",
)

validate_arxiv_rev = functools.partial(
    validate_records_field_equality,
    field_name="arxiv_rev",
    error_msg="The Arxiv rev cannot be different than {origin_val}",
)

validate_created_at = functools.partial(
    validate_records_field_equality,
    field_name="created_at",
    error_msg="The creation date cannot be different than {origin_val}",
)
