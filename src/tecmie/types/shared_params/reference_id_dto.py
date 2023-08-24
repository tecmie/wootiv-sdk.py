# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReferenceIDDto"]


class ReferenceIDDto(TypedDict, total=False):
    id: Required[str]
    """Unique identifier"""
