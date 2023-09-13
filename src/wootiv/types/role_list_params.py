# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["RoleListParams"]


class RoleListParams(TypedDict, total=False):
    cache: int
    """Reset cache (if was enabled).

    <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>
    """

    fields: List[str]
    """Selects resource fields.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>
    """

    filter: List[str]
    """Adds filter condition.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#filter" target="_blank">Docs</a>
    """

    join: List[str]
    """Adds relational resources.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>
    """

    limit: int
    """Limit amount of resources.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#limit" target="_blank">Docs</a>
    """

    offset: int
    """Offset amount of resources.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#offset" target="_blank">Docs</a>
    """

    page: int
    """Page portion of resources.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#page" target="_blank">Docs</a>
    """

    s: str
    """Adds search condition.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#search" target="_blank">Docs</a>
    """

    sort: List[str]
    """Adds sort by field.

    <a href="https://github.com/nestjsx/crud/wiki/Requests#sort" target="_blank">Docs</a>
    """
