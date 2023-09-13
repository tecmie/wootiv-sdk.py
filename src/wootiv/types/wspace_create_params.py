# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WspaceCreateParams"]


class WspaceCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the workspace"""

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """The unique identifier of the workspace owner"""
