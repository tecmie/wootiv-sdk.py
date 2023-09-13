# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .invitation_dto import InvitationDto

__all__ = ["InvitationPaginatedDto"]


class InvitationPaginatedDto(BaseModel):
    count: float
    """Count of all records"""

    data: List[InvitationDto]
    """Array of Invitations"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""
