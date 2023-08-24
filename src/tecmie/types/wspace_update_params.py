# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WspaceUpdateParams"]


class WspaceUpdateParams(TypedDict, total=False):
    body_id: Annotated[str, PropertyInfo(alias="id")]
    """The unique identifier of the workspace"""

    audit: object
    """Audit information including createdAt and updatedAt timestamps"""

    name: str
    """The name of the workspace"""

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The unique identifier of the workspace owner"""

    slug: str
    """The URL Identifier for this workspace"""

    subscription: object
    """The subscription associated with the workspace"""

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """The subscription attached to this workspace"""

    workspace_members: Annotated[List[str], PropertyInfo(alias="workspaceMembers")]
    """The members associated with the workspace"""
