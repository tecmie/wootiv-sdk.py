# File generated from our OpenAPI spec by Stainless.

from typing import List, Union

from .user_dto import UserDto
from .user_paginated_dto import UserPaginatedDto

__all__ = ["UserListResponse"]

UserListResponse = Union[UserPaginatedDto, List[UserDto]]
