# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from .read_contact_dto import ReadContactDto
from .paginated_contact_dto import PaginatedContactDto

__all__ = ["ContactListResponse"]

ContactListResponse = Union[PaginatedContactDto, List[ReadContactDto]]
