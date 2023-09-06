# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from pydantic import Field as FieldInfo

from . import role_paginated_dto
from .._models import BaseModel
from .role_dto import RoleDto

__all__ = ["RoleListResponse", "RolePaginatedDto"]


class RolePaginatedDto(BaseModel):
    count: float
    """Count of all records"""

    data: role_paginated_dto.RolePaginatedDto
    """Array of Roles"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""


RoleListResponse = Union[RolePaginatedDto, List[RoleDto]]
