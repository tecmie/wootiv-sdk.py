# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from .shared import AuditDto
from .._models import BaseModel

__all__ = ["ReadContactGroupDto"]


class ReadContactGroupDto(BaseModel):
    id: str
    """Unique identifier"""

    audit: AuditDto
    """Audit data"""

    group_name: str = FieldInfo(alias="groupName")
    """Unique identifier"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Unique identifier"""
