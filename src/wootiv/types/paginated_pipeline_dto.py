# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .read_pipeline_dto import ReadPipelineDto

__all__ = ["PaginatedPipelineDto"]


class PaginatedPipelineDto(BaseModel):
    count: float
    """Count of all records"""

    data: List[ReadPipelineDto]
    """A list of agent pipelines"""

    page: float
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    total: float
    """Count of records on current page"""
