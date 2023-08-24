# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["BucketBulkUploadParams"]


class BucketBulkUploadParams(TypedDict, total=False):
    bulk: List[FileTypes]

    path: str
    """path to upload file"""
