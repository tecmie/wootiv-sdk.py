# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthSignupParams"]


class AuthSignupParams(TypedDict, total=False):
    email: Required[str]
    """Email"""

    password: Required[str]
    """Password"""

    plan: Required[str]
    """Trial plan"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
