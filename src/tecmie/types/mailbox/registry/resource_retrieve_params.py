# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResourceRetrieveParams"]


class ResourceRetrieveParams(TypedDict, total=False):
    limit: float
    """The maximum number of items to return."""

    offset: float
    """The number of items to skip."""
