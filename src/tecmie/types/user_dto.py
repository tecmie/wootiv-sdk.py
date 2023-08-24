# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from pydantic import Field as FieldInfo

from .shared import AuditDto
from .._models import BaseModel

__all__ = ["UserDto"]


class UserDto(BaseModel):
    id: str
    """Unique identifier"""

    audit: AuditDto
    """Audit data"""

    email: str
    """Email"""

    username: str
    """Username"""

    avatar_url: Optional[str] = FieldInfo(alias="avatarURL", default=None)
    """Avatar URL"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """First Name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Last Name"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Phone Number"""

    role: Optional[str] = None
    """Role"""
