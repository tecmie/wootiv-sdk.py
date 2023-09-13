# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .mail import Mail, AsyncMail
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Wootiv, AsyncWootiv

__all__ = ["Inbound", "AsyncInbound"]


class Inbound(SyncAPIResource):
    mail: Mail

    def __init__(self, client: Wootiv) -> None:
        super().__init__(client)
        self.mail = Mail(client)


class AsyncInbound(AsyncAPIResource):
    mail: AsyncMail

    def __init__(self, client: AsyncWootiv) -> None:
        super().__init__(client)
        self.mail = AsyncMail(client)
