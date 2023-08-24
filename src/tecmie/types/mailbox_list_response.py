# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from .read_pipeline_dto import ReadPipelineDto
from .paginated_pipeline_dto import PaginatedPipelineDto

__all__ = ["MailboxListResponse"]

MailboxListResponse = Union[PaginatedPipelineDto, List[ReadPipelineDto]]
