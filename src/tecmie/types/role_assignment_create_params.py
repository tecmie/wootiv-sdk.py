# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..types import shared_params

__all__ = ["RoleAssignmentCreateParams"]


class RoleAssignmentCreateParams(TypedDict, total=False):
    assignee: Required[shared_params.ReferenceIDDto]
    """Assignee"""

    role: Required[shared_params.ReferenceIDDto]
    """Role"""
