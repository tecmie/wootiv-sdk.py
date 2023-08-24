# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from .read_contact_group_dto import ReadContactGroupDto
from .paginated_contact_group_dto import PaginatedContactGroupDto

__all__ = ["ContactGroupListResponse"]

ContactGroupListResponse = Union[PaginatedContactGroupDto, List[ReadContactGroupDto]]
