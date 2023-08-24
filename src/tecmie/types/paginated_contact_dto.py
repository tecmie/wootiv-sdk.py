# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .read_contact_dto import ReadContactDto

__all__ = ["PaginatedContactDto"]


class PaginatedContactDto(BaseModel):
    count: float
    """Count of all records"""

    data: List[ReadContactDto]
    """Array of contact"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""
