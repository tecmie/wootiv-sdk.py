# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .shared import AuditDto, ReferenceIDDto
from .._models import BaseModel

__all__ = ["InvitationDto"]


class InvitationDto(BaseModel):
    id: str
    """Unique identifier"""

    active: bool
    """True if Invitation is active"""

    audit: AuditDto
    """Audit data"""

    category: Literal["invitation", "invite"]
    """Category of invitation that refers the entity or event logic listeners"""

    code: str
    """Code claim invitation"""

    email: str
    """recipient email"""

    user: ReferenceIDDto
    """The owner of the org"""
