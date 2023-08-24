# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRetrieveParams"]


class ActionRetrieveParams(TypedDict, total=False):
    id: Required[str]

    limit: float
    """The maximum number of items to return."""

    offset: float
    """The number of items to skip."""
