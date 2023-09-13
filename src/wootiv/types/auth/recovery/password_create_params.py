# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PasswordCreateParams"]


class PasswordCreateParams(TypedDict, total=False):
    email: Required[str]
    """
    Recover email password by providing an email that will receive a password reset
    link
    """
