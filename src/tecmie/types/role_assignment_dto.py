# File generated from our OpenAPI spec by Stainless.

from .shared import AuditDto, ReferenceIDDto
from .._models import BaseModel

__all__ = ["RoleAssignmentDto"]


class RoleAssignmentDto(BaseModel):
    id: str
    """Unique identifier"""

    assignee: ReferenceIDDto
    """Assignee"""

    audit: AuditDto
    """Audit data"""

    role: ReferenceIDDto
    """Role"""
