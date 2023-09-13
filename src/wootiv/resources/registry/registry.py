# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .actions import Actions, AsyncActions
from .resources import Resources, AsyncResources
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Wootiv, AsyncWootiv

__all__ = ["Registry", "AsyncRegistry"]


class Registry(SyncAPIResource):
    resources: Resources
    actions: Actions

    def __init__(self, client: Wootiv) -> None:
        super().__init__(client)
        self.resources = Resources(client)
        self.actions = Actions(client)


class AsyncRegistry(AsyncAPIResource):
    resources: AsyncResources
    actions: AsyncActions

    def __init__(self, client: AsyncWootiv) -> None:
        super().__init__(client)
        self.resources = AsyncResources(client)
        self.actions = AsyncActions(client)
