# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["AuthVerifyBillingResponse"]


class AuthVerifyBillingResponse(BaseModel):
    email: str
    """Email"""

    sub: str
    """user ID"""
