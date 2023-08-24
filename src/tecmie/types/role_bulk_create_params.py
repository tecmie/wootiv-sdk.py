# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RoleBulkCreateParams", "Bulk"]


class RoleBulkCreateParams(TypedDict, total=False):
    bulk: Required[List[Bulk]]
    """Array of Roles to create"""


class Bulk(TypedDict, total=False):
    description: Required[str]
    """Description of the role"""

    name: Required[str]
    """Name of the role"""
