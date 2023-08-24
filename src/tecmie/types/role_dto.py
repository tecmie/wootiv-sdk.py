# File generated from our OpenAPI spec by Stainless.

from typing import List

from .shared import AuditDto, ReferenceIDDto
from .._models import BaseModel

__all__ = ["RoleDto"]


class RoleDto(BaseModel):
    id: str
    """Unique identifier"""

    assignees: List[ReferenceIDDto]
    """Assignee"""

    audit: AuditDto
    """Audit data"""

    description: str
    """Description of the role"""

    name: str
    """Name of the role"""
