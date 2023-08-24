# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactGroupUpdateParams"]


class ContactGroupUpdateParams(TypedDict, total=False):
    group_name: Required[Annotated[str, PropertyInfo(alias="groupName")]]
    """The name for the group"""

    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]
    """The ID of thw workspace the contact group belongs to"""
