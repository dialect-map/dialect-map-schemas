# -*- coding: utf-8 -*-

from .model import APIRoute

from ..schemas import *


# -------- Dialect Map: Category routes -------- #

DM_CATEGORY_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category",
    schema=CategorySchema,
)
DM_CATEGORY_MEMBER_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category/membership",
    schema=CategoryMembershipSchema,
)
DM_CATEGORY_METRICS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category-metrics",
    schema=JargonCategoryMetricsSchema,
)


# -------- Dialect Map: Jargon routes -------- #

DM_JARGON_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/jargon",
    schema=JargonSchema,
)
DM_JARGON_GROUP_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/jargon-group",
    schema=JargonGroupSchema,
)


# -------- Dialect Map: Paper routes -------- #

DM_PAPER_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper",
    schema=PaperSchema,
)
DM_PAPER_AUTHOR_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper/author",
    schema=PaperAuthorSchema,
)
DM_PAPER_METRICS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper-metrics",
    schema=JargonPaperMetricsSchema,
)
DM_PAPER_METADATA_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper-metadata",
    schema=PaperMetadataSchema,
)


# -------- Dialect Map: Reference routes -------- #

DM_REFERENCE_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/reference",
    schema=PaperReferenceSchema,
)
DM_REFERENCE_COUNTERS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper/reference/counters",
    schema=PaperReferenceCountersSchema,
)
