# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TokenCreateParams"]


class TokenCreateParams(TypedDict, total=False):
    name: str
    """The human name of the workspace token"""
