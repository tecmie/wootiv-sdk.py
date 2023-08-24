# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthLoginResponse"]


class AuthLoginResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")
    """JWT access token to use for request authorization."""

    refresh_token: str = FieldInfo(alias="refreshToken")
    """JWT refresh token to use for obtaining a new access token."""

    sub: str
    """The user ID for subsequent GetByID request."""
