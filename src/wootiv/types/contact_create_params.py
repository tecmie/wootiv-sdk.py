# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    contact_group_id: Required[Annotated[str, PropertyInfo(alias="contactGroupId")]]
    """The id for the contact group"""

    email: Required[str]
    """The email for the contact"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The name for the contact"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The lastname for the contact"""

    metadata: Required[object]
    """The metadata for the contact"""

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """The phone for the contact"""

    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]
    """The ID of thw workspace the contact contact belongs to"""
