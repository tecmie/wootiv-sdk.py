# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeatureListParams"]


class FeatureListParams(TypedDict, total=False):
    plan_name: Required[Annotated[str, PropertyInfo(alias="planName")]]
