# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .tokens import Tokens, AsyncTokens
from .members import Members, AsyncMembers
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Wootiv, AsyncWootiv

__all__ = ["Space", "AsyncSpace"]


class Space(SyncAPIResource):
    members: Members
    tokens: Tokens

    def __init__(self, client: Wootiv) -> None:
        super().__init__(client)
        self.members = Members(client)
        self.tokens = Tokens(client)


class AsyncSpace(AsyncAPIResource):
    members: AsyncMembers
    tokens: AsyncTokens

    def __init__(self, client: AsyncWootiv) -> None:
        super().__init__(client)
        self.members = AsyncMembers(client)
        self.tokens = AsyncTokens(client)
