# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PasswordUpdateParams"]


class PasswordUpdateParams(TypedDict, total=False):
    new_password: Required[Annotated[str, PropertyInfo(alias="newPassword")]]
    """New password account"""

    passcode: Required[str]
    """Passcode used to reset account password"""
