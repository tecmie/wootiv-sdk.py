# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .shared import AuditDto
from .._models import BaseModel

__all__ = ["ReadContactDto"]


class ReadContactDto(BaseModel):
    id: str
    """Unique identifier"""

    audit: AuditDto
    """Audit data"""

    contact_group_id: str = FieldInfo(alias="contactGroupId")
    """The id for the contact group"""

    email: str
    """The email for the contact"""

    first_name: str = FieldInfo(alias="firstName")
    """The name for the contact"""

    last_name: str = FieldInfo(alias="lastName")
    """The lastname for the contact"""

    metadata: object
    """The metadata for the contact"""

    phone_number: str = FieldInfo(alias="phoneNumber")
    """The phone for the contact"""

    primary_contact: Literal["email", "phoneNumber"] = FieldInfo(alias="primaryContact")
    """the primary contact method for the contact"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """The ID of thw workspace the contact contact belongs to"""
