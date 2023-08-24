# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .action import Action, AsyncAction
from .resource import Resource, AsyncResource
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import make_request_options
from ....types.mailbox import PaginatedMailboxRegistry, registry_retrieve_params

if TYPE_CHECKING:
    from ...._client import Tecmie, AsyncTecmie

__all__ = ["Registry", "AsyncRegistry"]


class Registry(SyncAPIResource):
    action: Action
    resource: Resource

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.action = Action(client)
        self.resource = Resource(client)

    def retrieve(
        self,
        id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedMailboxRegistry:
        """
        Get all Registry Items in this pipeline

        Args:
          limit: The maximum number of items to return.

          offset: The number of items to skip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/mailbox/{id}/registry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    registry_retrieve_params.RegistryRetrieveParams,
                ),
            ),
            cast_to=PaginatedMailboxRegistry,
        )


class AsyncRegistry(AsyncAPIResource):
    action: AsyncAction
    resource: AsyncResource

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.action = AsyncAction(client)
        self.resource = AsyncResource(client)

    async def retrieve(
        self,
        id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedMailboxRegistry:
        """
        Get all Registry Items in this pipeline

        Args:
          limit: The maximum number of items to return.

          offset: The number of items to skip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/mailbox/{id}/registry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    registry_retrieve_params.RegistryRetrieveParams,
                ),
            ),
            cast_to=PaginatedMailboxRegistry,
        )
