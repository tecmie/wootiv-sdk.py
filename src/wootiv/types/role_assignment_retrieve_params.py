# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RoleAssignmentRetrieveParams"]


class RoleAssignmentRetrieveParams(TypedDict, total=False):
    assignment: Required[str]

    cache: int
    """Reset cache (if was enabled).

    <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>
    """

    fields: List[str]
    """Selects resource fields.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>
    """

    join: List[str]
    """Adds relational resources.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>
    """
