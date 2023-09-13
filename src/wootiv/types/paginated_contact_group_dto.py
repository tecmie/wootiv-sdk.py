# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .read_contact_group_dto import ReadContactGroupDto

__all__ = ["PaginatedContactGroupDto"]


class PaginatedContactGroupDto(BaseModel):
    count: float
    """Count of all records"""

    data: List[ReadContactGroupDto]
    """Array of contact groups"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""
