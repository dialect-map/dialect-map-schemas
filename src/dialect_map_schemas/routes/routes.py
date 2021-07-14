# -*- coding: utf-8 -*-

from .model import APIRoute

from ..schemas import *


# -------- Dialect Map: Category routes -------- #

DM_CATEGORY_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category",
    model_name="Category",
    model_schema=CategorySchema,
)
DM_CATEGORY_MEMBER_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category/membership",
    model_name="CategoryMembership",
    model_schema=CategoryMembershipSchema,
)
DM_CATEGORY_METRICS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/category-metrics",
    model_name="JargonCategoryMetrics",
    model_schema=JargonCategoryMetricsSchema,
)


# -------- Dialect Map: Jargon routes -------- #

DM_JARGON_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/jargon",
    model_name="Jargon",
    model_schema=JargonSchema,
)
DM_JARGON_GROUP_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/jargon-group",
    model_name="JargonGroup",
    model_schema=JargonGroupSchema,
)


# -------- Dialect Map: Paper routes -------- #

DM_PAPER_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper",
    model_name="Paper",
    model_schema=PaperSchema,
)
DM_PAPER_AUTHOR_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper/author",
    model_name="PaperAuthor",
    model_schema=PaperAuthorSchema,
)
DM_PAPER_METRICS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper-metrics",
    model_name="JargonPaperMetrics",
    model_schema=JargonPaperMetricsSchema,
)


# -------- Dialect Map: Reference routes -------- #

DM_REFERENCE_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/reference",
    model_name="PaperReference",
    model_schema=PaperReferenceSchema,
)
DM_REFERENCE_COUNTERS_ROUTE = APIRoute(
    api_name="dialect-map",
    api_path="/paper/reference/counters",
    model_name="PaperReferenceCounters",
    model_schema=PaperReferenceCountersSchema,
)
