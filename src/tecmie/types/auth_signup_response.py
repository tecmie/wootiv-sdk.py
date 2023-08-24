# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["AuthSignupResponse"]


class AuthSignupResponse(BaseModel):
    email: str
    """Email"""

    sub: str
    """user ID"""
