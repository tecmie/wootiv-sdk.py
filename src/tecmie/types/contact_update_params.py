# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    contact_group_id: Annotated[str, PropertyInfo(alias="contactGroupId")]
    """The id for the contact group"""

    email: str
    """The email for the contact"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The name for the contact"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The lastname for the contact"""

    metadata: object
    """The metadata for the contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone for the contact"""

    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]
    """The ID of thw workspace the contact contact belongs to"""
