# File generated from our OpenAPI spec by Stainless.

from typing import List

from ....._models import BaseModel
from ..stream_registry_query_dto import StreamRegistryQueryDto

__all__ = ["PaginatedStreamRegistry"]


class PaginatedStreamRegistry(BaseModel):
    data: List[StreamRegistryQueryDto]
    """The Stream registry entries."""

    limit: float

    offset: float

    page: float

    total: float
