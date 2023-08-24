# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TokenRefreshParams"]


class TokenRefreshParams(TypedDict, total=False):
    refresh_token: Required[Annotated[str, PropertyInfo(alias="refreshToken")]]
    """JWT access token to use for request authorization."""
