# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import make_request_options
from ....types.mailbox import PaginatedMailboxRegistry
from ....types.mailbox.registry import (
    ResourceCreateResponse,
    resource_create_params,
    resource_retrieve_params,
)

__all__ = ["Resource", "AsyncResource"]


class Resource(SyncAPIResource):
    def create(
        self,
        id: str,
        *,
        enabled: bool,
        name: str,
        raw_content: Optional[str],
        raw_parsed: Optional[str],
        value: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreateResponse:
        """
        Create new registry vector resource

        Args:
          enabled: Whether the mailbox registry entry is enabled or disabled.

          name: The name of the mailbox registry.

          rawContent: The raw content of the mailbox registry.

          rawParsed: The parsed content of the mailbox registry.

          value: The required values needed to setup this registry entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/mailbox/{id}/registry/resource",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "raw_content": raw_content,
                    "raw_parsed": raw_parsed,
                    "value": value,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreateResponse,
        )

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
        List Registry resources and documents

        Args:
          limit: The maximum number of items to return.

          offset: The number of items to skip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/mailbox/{id}/registry/resource",
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
                    resource_retrieve_params.ResourceRetrieveParams,
                ),
            ),
            cast_to=PaginatedMailboxRegistry,
        )


class AsyncResource(AsyncAPIResource):
    async def create(
        self,
        id: str,
        *,
        enabled: bool,
        name: str,
        raw_content: Optional[str],
        raw_parsed: Optional[str],
        value: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreateResponse:
        """
        Create new registry vector resource

        Args:
          enabled: Whether the mailbox registry entry is enabled or disabled.

          name: The name of the mailbox registry.

          rawContent: The raw content of the mailbox registry.

          rawParsed: The parsed content of the mailbox registry.

          value: The required values needed to setup this registry entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/mailbox/{id}/registry/resource",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "raw_content": raw_content,
                    "raw_parsed": raw_parsed,
                    "value": value,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreateResponse,
        )

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
        List Registry resources and documents

        Args:
          limit: The maximum number of items to return.

          offset: The number of items to skip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/mailbox/{id}/registry/resource",
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
                    resource_retrieve_params.ResourceRetrieveParams,
                ),
            ),
            cast_to=PaginatedMailboxRegistry,
        )
