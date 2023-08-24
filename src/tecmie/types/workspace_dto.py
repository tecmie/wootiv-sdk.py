# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkspaceDto"]


class WorkspaceDto(BaseModel):
    id: str
    """The unique identifier of the workspace"""

    audit: object
    """Audit information including createdAt and updatedAt timestamps"""

    name: str
    """The name of the workspace"""

    owner_id: str = FieldInfo(alias="ownerId")
    """The unique identifier of the workspace owner"""

    slug: str
    """The URL Identifier for this workspace"""

    subscription: object
    """The subscription associated with the workspace"""

    subscription_id: str = FieldInfo(alias="subscriptionId")
    """The subscription attached to this workspace"""

    workspace_members: List[str] = FieldInfo(alias="workspaceMembers")
    """The members associated with the workspace"""
