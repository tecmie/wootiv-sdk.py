# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

from .registry import Registry, AsyncRegistry
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import make_request_options
from ....types.mailbox import (
    StreamCreateResponse,
    StreamRetrieveResponse,
    stream_create_params,
)

if TYPE_CHECKING:
    from ...._client import Tecmie, AsyncTecmie

__all__ = ["Stream", "AsyncStream"]


class Stream(SyncAPIResource):
    registry: Registry

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.registry = Registry(client)

    def create(
        self,
        slug: str,
        *,
        id: str,
        attachments: List[List[object]],
        medium_integration_name: Literal["whatsapp", "postmark", "twilio", "core_api"],
        message_html: str,
        message_text: str,
        sender: Literal["system", "recipient", "manager", "agent"],
        status: Literal["sent", "received", "drafted", "flagged", "quarantined", "deleted", "enqueue"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> StreamCreateResponse:
        """
        Add a custom response to a conversation stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/mailbox/{id}/stream/{slug}",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "medium_integration_name": medium_integration_name,
                    "message_html": message_html,
                    "message_text": message_text,
                    "sender": sender,
                    "status": status,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamCreateResponse,
        )

    def retrieve(
        self,
        slug: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> StreamRetrieveResponse:
        """
        All the messages in a single thread within a conversation stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/mailbox/{id}/stream/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamRetrieveResponse,
        )


class AsyncStream(AsyncAPIResource):
    registry: AsyncRegistry

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.registry = AsyncRegistry(client)

    async def create(
        self,
        slug: str,
        *,
        id: str,
        attachments: List[List[object]],
        medium_integration_name: Literal["whatsapp", "postmark", "twilio", "core_api"],
        message_html: str,
        message_text: str,
        sender: Literal["system", "recipient", "manager", "agent"],
        status: Literal["sent", "received", "drafted", "flagged", "quarantined", "deleted", "enqueue"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> StreamCreateResponse:
        """
        Add a custom response to a conversation stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/mailbox/{id}/stream/{slug}",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "medium_integration_name": medium_integration_name,
                    "message_html": message_html,
                    "message_text": message_text,
                    "sender": sender,
                    "status": status,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamCreateResponse,
        )

    async def retrieve(
        self,
        slug: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> StreamRetrieveResponse:
        """
        All the messages in a single thread within a conversation stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/mailbox/{id}/stream/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamRetrieveResponse,
        )
