# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from .invitation_dto import InvitationDto
from .invitation_paginated_dto import InvitationPaginatedDto

__all__ = ["InvitationListResponse"]

InvitationListResponse = Union[InvitationPaginatedDto, List[InvitationDto]]
