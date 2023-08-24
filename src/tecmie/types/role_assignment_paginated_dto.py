# File generated from our OpenAPI spec by Stainless.

from .shared import AuditDto, ReferenceIDDto
from .._models import BaseModel

__all__ = ["RoleAssignmentPaginatedDto"]


class RoleAssignmentPaginatedDto(BaseModel):
    id: str
    """Unique identifier"""

    assignee: ReferenceIDDto
    """Assignee"""

    audit: AuditDto
    """Audit data"""

    role: ReferenceIDDto
    """Role"""
