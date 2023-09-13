# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AwCreateSignedPutURLParams"]


class AwCreateSignedPutURLParams(TypedDict, total=False):
    filename: Required[str]
    """The name of the file we are creating namespace for"""
