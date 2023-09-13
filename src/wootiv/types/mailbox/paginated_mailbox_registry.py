# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel
from .mailbox_registry_query_dto import MailboxRegistryQueryDto

__all__ = ["PaginatedMailboxRegistry"]


class PaginatedMailboxRegistry(BaseModel):
    data: List[MailboxRegistryQueryDto]
    """The mailbox registry entries."""

    limit: float

    offset: float

    page: float

    total: float
