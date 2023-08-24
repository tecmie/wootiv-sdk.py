# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_dto import UserDto

__all__ = ["UserPaginatedDto"]


class UserPaginatedDto(BaseModel):
    count: float
    """Count of all records"""

    data: List[UserDto]
    """Array of Users"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""
