# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoginCreateParams"]


class LoginCreateParams(TypedDict, total=False):
    email: Required[str]
    """Recover email login by providing an email that will receive an username"""
