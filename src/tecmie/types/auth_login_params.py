# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthLoginParams"]


class AuthLoginParams(TypedDict, total=False):
    password: Required[str]
    """Password"""

    username: Required[str]
    """Username"""
