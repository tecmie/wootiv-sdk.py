# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["BucketUploadParams"]


class BucketUploadParams(TypedDict, total=False):
    file: FileTypes

    path: str
    """path to upload file"""
