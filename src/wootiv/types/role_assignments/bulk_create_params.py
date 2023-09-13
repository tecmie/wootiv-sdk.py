# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ...types import shared_params

__all__ = ["BulkCreateParams", "Bulk"]


class BulkCreateParams(TypedDict, total=False):
    bulk: Required[List[Bulk]]
    """Array of Roles Assignments to create"""


class Bulk(TypedDict, total=False):
    assignee: Required[shared_params.ReferenceIDDto]
    """Assignee"""

    role: Required[shared_params.ReferenceIDDto]
    """Role"""
