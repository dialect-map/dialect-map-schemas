# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseStaticSchema


class CategoryMembership(BaseStaticSchema):
    """ArXiv paper - category membership record"""

    membership_id = fields.String(required=False)
    arxiv_id = fields.String(required=True)
    arxiv_rev = fields.Integer(required=True)
    category_id = fields.String(required=True)
    created_at = fields.DateTime(required=True)
